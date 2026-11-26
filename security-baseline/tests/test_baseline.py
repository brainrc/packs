"""The baseline's eval (#323): fewer ask prompts, no new escapes. For each action in
evals/asks.toml it works out what Claude Code does with brainrc core alone and with this pack:
core's guard hooks run first either way; Claude Code runs its built-in read-only commands (here
`git status`, `git diff`, `git log`) without a prompt; then the pack's permission deny rules and
its sandbox (`autoAllowBashIfSandboxed`), which runs other Bash commands without a prompt.

A static count under those rules, not a recorded session. README.md states the numbers."""
import json
import os
import tempfile
import tomllib
import unittest
from fnmatch import fnmatch
from pathlib import Path, PurePosixPath

import brainrc
from brainrc.testing import run_hook

PACK = Path(__file__).resolve().parent.parent
HOOKS = Path(brainrc.__file__).resolve().parent.parent / "overrides/claude/hooks"
SETTINGS = json.loads((PACK / "overrides/claude/settings.fragment.json").read_text(encoding="utf-8"))
ACTIONS = tomllib.loads((PACK / "evals/asks.toml").read_text(encoding="utf-8"))["action"]
STRICTNESS = {"allow": 0, "ask": 1, "deny": 2}
# The commands evals/asks.toml uses from Claude Code's built-in read-only set, which runs without a
# prompt in every mode (code.claude.com/docs/en/permissions, "Read-only commands").
READ_ONLY = ("git status", "git diff", "git log", "git show", "cat", "ls")


def setUpModule():
    # Core's guard reads the pack rules apply rendered; an empty home means none, as on a new machine.
    os.environ["BRAINRC_HOME"] = tempfile.mkdtemp()


def payload(action: dict) -> dict:
    if "bash" in action:
        return {"tool_name": "Bash", "tool_input": {"command": action["bash"]}}
    return {"tool_name": "Read", "tool_input": {"file_path": action["read"]}}


def hook_decision(action: dict) -> str | None:
    found = [run_hook(HOOKS / name, payload(action)) for name in ("guard_outward.py", "guard_secrets.py")]
    found = [d for d in found if d]
    return max(found, key=STRICTNESS.get) if found else None


def matches(rule: str, action: dict) -> bool:
    """A Claude Code `Read(<path pattern>)` rule: `**/` for any folder, `*` within a name."""
    tool, _, arg = rule.partition("(")
    arg = arg.rstrip(")")
    if tool == "Read" and "read" in action:
        path = action["read"]
        if arg.startswith("**/"):
            return PurePosixPath(path).match(arg[3:])
        if arg.endswith("/**"):
            return path.startswith(arg[:-2])
        return fnmatch(path, arg)
    return False


def read_only(action: dict) -> bool:
    command = action.get("bash", "").strip()
    return any(command == c or command.startswith(c + " ") for c in READ_ONLY)


def core_alone(action: dict) -> str:
    hook = hook_decision(action)
    if hook:
        return hook
    if "bash" in action and not read_only(action):
        return "ask"  # core sets no allow rules and no sandbox
    return "allow"


def with_pack(action: dict) -> str:
    perms = SETTINGS["permissions"]
    if any(matches(r, action) for r in perms.get("deny", [])):
        return "deny"  # a deny rule always holds, sandbox or not
    hook = hook_decision(action)
    if hook:
        return hook  # hooks run before the sandbox auto-allow
    if "bash" in action and not read_only(action):
        return "allow" if SETTINGS["sandbox"].get("autoAllowBashIfSandboxed") else "ask"
    return "allow"


def counts() -> dict[str, dict[str, int]]:
    out = {"core": {"allow": 0, "ask": 0, "deny": 0}, "pack": {"allow": 0, "ask": 0, "deny": 0}}
    for action in ACTIONS:
        out["core"][core_alone(action)] += 1
        out["pack"][with_pack(action)] += 1
    return out


class BaselineEvalTest(unittest.TestCase):
    def test_no_new_escapes(self):
        for action in ACTIONS:
            if action.get("guarded"):
                with self.subTest(action):
                    before, after = core_alone(action), with_pack(action)
                    self.assertIn(before, ("ask", "deny"), "a guarded action core's guard lets through")
                    self.assertGreaterEqual(STRICTNESS[after], STRICTNESS[before], "the pack loosened it")

    def test_fewer_ask_prompts(self):
        got = counts()
        self.assertLess(got["pack"]["ask"], got["core"]["ask"])

    def test_the_readme_states_the_counts(self):
        got = counts()
        line = (f"{got['core']['ask']} prompts with core alone and {got['pack']['ask']} with this pack, "
                f"of {len(ACTIONS)} actions")
        self.assertIn(line, (PACK / "README.md").read_text(encoding="utf-8").replace("\n", " "))

    def test_it_allows_nothing_outside_the_sandbox(self):
        # An allow rule would run a command without a prompt even where the sandbox can't hold it.
        self.assertNotIn("allow", SETTINGS["permissions"])
        self.assertTrue(SETTINGS["sandbox"]["enabled"])


if __name__ == "__main__":
    unittest.main()
