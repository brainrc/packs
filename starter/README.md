# brainrc/starter

The smallest useful pack, for a setup with Gatework off: one skill that finds how to test, lint and build a project and checks the commands run.

An official [brainrc](https://github.com/brainrc/brainrc) pack: one folder of
[brainrc/packs](https://github.com/brainrc/packs). brainrc installs its skills into every
AI coding tool it manages.

## Use it

Add it to brainrc's `packs.local.toml`, then run `brainrc apply`. Installing from a folder
of a repo (`subdir`) needs a brainrc release that includes
[#121](https://github.com/brainrc/brainrc/issues/121), the first after 0.8.31.

```toml
# packs.local.toml
[starter]
git = "https://github.com/brainrc/packs.git"
ref = "<a tag of brainrc/packs>"
subdir = "starter"
```

Gatework, brainrc's default pack, ships this skill under the same name, so this pack is for a setup with Gatework off:

```toml
# packs.local.toml
[gatework]
enabled = false
```

To keep Gatework, leave this pack off; Gatework's copies do the same job.

For every agent in one repository, put the same keys under `[packs.starter]` in that
repository's `brainrc.toml`.

## What's in it

| Skill | What it's for |
|---|---|
| [`brainrc-project-commands`](skills/brainrc-project-commands/SKILL.md) | Discover a project's test, lint, typecheck, build, and format commands from its manifests and docs, and record a verified baseline. Use at the start of a task, or whenever you need to know how to test or build an unfamiliar project. |

It installs one file per AI tool brainrc manages: the skill's `SKILL.md`, so 5 with all five tools
present. Measured with Gatework off on clean homes: core alone installs 6 files for Claude Code
alone and 16 for all five tools; with this pack, 7 and 21.

## Cost and permissions

Every session loads about 58 tokens from this pack: its rules and skill descriptions
(`brainrc tokens` shows the same count). A skill's body loads only when it's used.

It adds no hooks, MCP servers, tool grants or network domains
([permissions.toml](permissions.toml)).

## Evals

[evals/triggers.toml](evals/triggers.toml) has 2 requests: each skill gets one that
should load it and a near miss that shouldn't. brainrc merges them into
`python3 scripts/evals.py triggers` when the pack is enabled. That check needs a model, and
nothing here calls one in CI, so the delta with and without this pack is **unmeasured**.

Issue: [#313](https://github.com/brainrc/brainrc/issues/313).
