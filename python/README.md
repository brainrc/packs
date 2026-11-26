# brainrc/python

Python projects and libraries: Ruff for lint and format, pytest or unittest, the type checker the project configures, conventions and a review checklist.

An official [brainrc](https://github.com/brainrc/brainrc) pack: one folder of
[brainrc/packs](https://github.com/brainrc/packs). brainrc installs its skills into every
AI coding tool it manages.

## Use it

Add it to brainrc's `packs.local.toml`, then run `brainrc apply`. Installing from a folder
of a repo (`subdir`) needs a brainrc release that includes
[#121](https://github.com/brainrc/brainrc/issues/121) (0.8.32 or later).

```toml
# packs.local.toml
[python]
git = "https://github.com/brainrc/packs.git"
ref = "<a tag of brainrc/packs>"
subdir = "python"
```

It works beside Gatework, brainrc's default pack: none of its skills share a name with Gatework's.

For every agent in one repository, put the same keys under `[packs.python]` in that
repository's `brainrc.toml`.

## What's in it

| Skill | What it's for |
|---|---|
| [`brainrc-python`](skills/brainrc-python/SKILL.md) | Python projects and libraries. Lint and format with Ruff, test with pytest or unittest, type-check when configured, and a review checklist. Use when writing, changing, or reviewing *.py files, pyproject.toml, or a Python package's tests. |

## Cost and permissions

Every session loads about 60 tokens from this pack: its rules and skill descriptions
(`brainrc tokens` shows the same count). A skill's body loads only when it's used.

It adds no hooks, MCP servers, tool grants or network domains
([permissions.toml](permissions.toml)).

## Evals

[evals/triggers.toml](evals/triggers.toml) has 2 requests: each skill gets one that
should load it and a near miss that shouldn't. brainrc merges them into
`python3 scripts/evals.py triggers` when the pack is enabled. That check needs a model, and
nothing here calls one in CI, so the delta with and without this pack is **unmeasured**.

## Sources

Conventions come from the tools' own docs:

- [Ruff tutorial](https://docs.astral.sh/ruff/tutorial/)

Issue: [#183](https://github.com/brainrc/brainrc/issues/183).
