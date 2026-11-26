# brainrc/security-baseline

Safe defaults in one pack: Claude Code's sandbox on with auto-allow, and credential files kept out of reach of the Read tool and of sandboxed commands, so everyday work prompts less while core's guard still asks before anything outward-facing.

An official [brainrc](https://github.com/brainrc/brainrc) pack: one folder of
[brainrc/packs](https://github.com/brainrc/packs). brainrc installs its skills into every
AI coding tool it manages.

## Use it

Add it to brainrc's `packs.local.toml`, then run `brainrc apply`. Installing from a folder
of a repo (`subdir`) needs a brainrc release that includes
[#121](https://github.com/brainrc/brainrc/issues/121), the first after 0.8.31.

```toml
# packs.local.toml
[security-baseline]
git = "https://github.com/brainrc/packs.git"
ref = "<a tag of brainrc/packs>"
subdir = "security-baseline"
```

For every agent in one repository, put the same keys under `[packs.security-baseline]` in that
repository's `brainrc.toml`.

## What's in it

| Path | What it does |
|---|---|
| [`overrides/claude/settings.fragment.json`](overrides/claude/settings.fragment.json) | Turns on Claude Code's sandbox (`sandbox.enabled`) with `autoAllowBashIfSandboxed`, so a Bash command runs in the sandbox without a prompt unless a hook or rule says otherwise. Both are set only where your settings have no value. Denies the Read tool `.env` files (`.env`, `.env.local`, `.env.*.local`, `.env.production`) and credential files. It adds no allow rules. |
| `pack.toml` `[[guard.deny]]` | `path` rules that brainrc compiles into the sandbox's `denyRead` and `denyWrite`: `~/.aws/credentials`, `~/.gnupg`, `~/.pypirc` and Google Cloud's application default credentials, so a sandboxed command can't read them either. |
| [`evals/asks.toml`](evals/asks.toml), [`tests/test_baseline.py`](tests/test_baseline.py) | The eval below. |

Core's own guard (`guard_outward.py`, `guard_secrets.py`) still runs first on every call: it asks
before pushes, deletes, deploys and publishes, and before a command that names a secret file.
Inside the sandbox, a command core's guard doesn't flag runs without a prompt; the sandbox keeps
its writes to the project, and a host you haven't allowed needs your yes. A command that has to run
outside the sandbox, an `rm` of a critical path, and an ask rule's command still prompt
([Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing)). Read-only commands such
as `git status` never prompted. Other tools have no
sandbox brainrc can write, so there only the guard applies. Settings need brainrc's
`recommended` or `full` profile.

## Cost and permissions

Every session loads about 0 tokens from this pack: its rules and skill descriptions
(`brainrc tokens` shows the same count). A skill's body loads only when it's used.

It grants, as `brainrc.lock` records it ([permissions.toml](permissions.toml)):

- **tools:** `claude deny Read(**/.env)`, `claude deny Read(**/.env.*.local)`, `claude deny Read(**/.env.local)`, `claude deny Read(**/.env.production)`, `claude deny Read(~/.aws/credentials)`, `claude deny Read(~/.gnupg/**)`, `claude deny Read(~/.pypirc)`, `claude deny Read(~/.ssh/id_*)`, `claude sets sandbox = {"autoAllowBashIfSandboxed": true, "enabled": true}`

## Evals

[evals/asks.toml](evals/asks.toml) lists everyday actions and guarded ones.
[tests/test_baseline.py](tests/test_baseline.py) works out what each one does with brainrc core
alone and with this pack, from core's guard hooks and this pack's settings: 18 prompts with core alone and 9 with this pack, of 24 actions (4 refused outright). Every guarded
action still asks or is refused, so there are no new escapes. This is a static count under those
rules, assuming none of the commands is already in your allow list, not a recorded session.

## Sources

Conventions come from the tools' own docs:

- [Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing)
- [Claude Code permissions](https://code.claude.com/docs/en/permissions)

Issue: [#323](https://github.com/brainrc/brainrc/issues/323).
