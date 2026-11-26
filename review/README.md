# brainrc/review

Review uncommitted changes, write PR descriptions and commit messages, and give prose a final plain-language pass. For a setup with Gatework off: Gatework ships these four skills itself.

An official [brainrc](https://github.com/brainrc/brainrc) pack: one folder of
[brainrc/packs](https://github.com/brainrc/packs). brainrc installs its skills into every
AI coding tool it manages.

## Use it

Add it to brainrc's `packs.local.toml`, then run `brainrc apply`. Installing from a folder
of a repo (`subdir`) needs a brainrc release that includes
[#121](https://github.com/brainrc/brainrc/issues/121), the first after 0.8.31.

```toml
# packs.local.toml
[review]
git = "https://github.com/brainrc/packs.git"
ref = "<a tag of brainrc/packs>"
subdir = "review"
```

Gatework, brainrc's default pack, ships these skills under the same names, so this pack is for a setup with Gatework off:

```toml
# packs.local.toml
[gatework]
enabled = false
```

To keep Gatework, leave this pack off; Gatework's copies do the same job.

For every agent in one repository, put the same keys under `[packs.review]` in that
repository's `brainrc.toml`.

## What's in it

| Skill | What it's for |
|---|---|
| [`brainrc-commit-message`](skills/brainrc-commit-message/SKILL.md) | Write a clear git commit message for staged changes. Use when the user asks to commit, or asks for a commit message. |
| [`brainrc-pr-description`](skills/brainrc-pr-description/SKILL.md) | Write a concise pull request title and description from a change's spec, plan, verification, and diff. Use when opening a PR, or when asked to write or improve a PR description. |
| [`brainrc-review`](skills/brainrc-review/SKILL.md) | Review uncommitted changes for bugs and security issues |
| [`brainrc-unslop`](skills/brainrc-unslop/SKILL.md) | Final editing pass that strips AI writing tells and makes prose plain and unambiguous before it ships (docs, ADRs, runbooks, READMEs, PR and commit bodies; not code or logs). Use for "unslop this", "final pass", "make this sound less AI". |

## Cost and permissions

Every session loads about 148 tokens from this pack: its rules and skill descriptions
(`brainrc tokens` shows the same count). A skill's body loads only when it's used.

It adds no hooks, MCP servers, tool grants or network domains
([permissions.toml](permissions.toml)).

## Evals

[evals/triggers.toml](evals/triggers.toml) has 4 requests: each skill gets one that
should load it and a near miss that shouldn't. brainrc merges them into
`python3 scripts/evals.py triggers` when the pack is enabled. That check needs a model, and
nothing here calls one in CI, so the delta with and without this pack is **unmeasured**.

`brainrc-review` is a slash command (`/brainrc-review`), not loaded on its own, so it has no trigger case that expects it.

Issue: [#314](https://github.com/brainrc/brainrc/issues/314).
