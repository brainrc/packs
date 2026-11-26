"""This pack's own tests: `brainrc validate --pack <folder>` runs them (`test` in pack.toml), with
brainrc on the path. They keep the README's numbers and the permission manifest honest."""
import os
import re
import tomllib
import unittest
from pathlib import Path

from brainrc import permissions, tokens
from brainrc.sources import frontmatter, load_pack, skills

PACK = Path(__file__).resolve().parent.parent
TEXT = {".md", ".toml", ".json", ".yaml", ".yml", ".py", ".txt"}
SECRET = re.compile(r"(?i)\b(?:password|passwd|secret|token|api[_-]?key)\b\s*[:=]\s*[\"']?[\w/+.=-]{12,}")
SKIP = {"node_modules", "venv", "__pycache__"}


def text_files():
    for root, dirs, names in os.walk(PACK):
        dirs[:] = sorted(d for d in dirs if d not in SKIP and not d.startswith("."))
        for name in sorted(names):
            if Path(name).suffix in TEXT:
                yield Path(root, name)


def read_toml(name: str) -> dict:
    return tomllib.loads((PACK / name).read_text(encoding="utf-8"))


class RulesTest(unittest.TestCase):
    def test_rules_stay_short(self):
        # Rules load in every session on every machine with this pack: detail goes in a skill.
        for rule in sorted((PACK / "rules").glob("*.md")):
            lines = [line for line in rule.read_text(encoding="utf-8").splitlines() if line.strip()]
            self.assertLessEqual(len(lines), 30, f"{rule.name}: move the detail into a skill")


class SecretsTest(unittest.TestCase):
    def test_no_secret_values(self):
        for path in text_files():
            for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if SECRET.search(line):  # named, never printed
                    self.fail(f"{path.relative_to(PACK).as_posix()}:{n} looks like a secret")


class ManifestTest(unittest.TestCase):
    """permissions.toml is what installing this pack lets an agent do; brainrc.lock records the same
    from the files, so a change that widens it shows up here first."""

    def test_the_permission_manifest_matches_the_pack(self):
        src = load_pack(PACK)
        got = permissions.of_pack(src, permissions.user_items(src), hooks=True, mcp=True)
        want = {k: v for k, v in read_toml("permissions.toml").items() if v}
        self.assertEqual(want, got, "update permissions.toml to what the pack grants")

    def test_the_readme_states_the_token_cost(self):
        total, _ = tokens.always_tokens(load_pack(PACK))
        readme = (PACK / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"about {total} tokens", readme, "update the token cost in README.md")


class EvalsTest(unittest.TestCase):
    def test_every_skill_has_a_case_that_loads_it_and_one_that_must_not(self):
        # A skill only the user invokes (disable-model-invocation) is never loaded on its own.
        names = {p.name for p in skills(load_pack(PACK))
                 if frontmatter(p / "SKILL.md").get("disable-model-invocation") != "true"}
        if not names:
            return
        cases = read_toml("evals/triggers.toml")["case"]
        for name in sorted(names):
            with self.subTest(name):
                self.assertTrue(any(name in c.get("expect", []) for c in cases), "no case expects it")
                self.assertTrue(any(name in c.get("forbid", []) for c in cases), "no near miss forbids it")


if __name__ == "__main__":
    unittest.main()
