# brainrc/node-ts

Node.js and TypeScript: the project's package manager and scripts, `tsc --noEmit`, ESLint with typescript-eslint, conventions and a review checklist.

An official [brainrc](https://github.com/brainrc/brainrc) pack: one folder of
[brainrc/packs](https://github.com/brainrc/packs). brainrc installs its skills into every
AI coding tool it manages.

## Use it

Add it to brainrc's `packs.local.toml`, then run `brainrc apply`. Installing from a folder
of a repo (`subdir`) needs a brainrc release that includes
[#121](https://github.com/brainrc/brainrc/issues/121), the first after 0.8.31.

```toml
# packs.local.toml
[node-ts]
git = "https://github.com/brainrc/packs.git"
ref = "<a tag of brainrc/packs>"
subdir = "node-ts"
```

Gatework 0.8 still ships these skills under the same names (#318). Until it drops
them, exclude its copies so the two packs don't collide:

```toml
# brainrc.local.toml
exclude = [
  "gatework:skills/brainrc-node-ts",
]
```

For every agent in one repository, put the same keys under `[packs.node-ts]` in that
repository's `brainrc.toml`.

## What's in it

| Skill | What it's for |
|---|---|
| [`brainrc-node-ts`](skills/brainrc-node-ts/SKILL.md) | Node.js and TypeScript projects. Type-check with tsc, lint with ESLint and typescript-eslint, run the package's tests, and a review checklist. Use when writing, changing, or reviewing *.ts, *.tsx, *.js, *.mjs files, package.json, or tsconfig*.json. |

## Cost and permissions

Every session loads about 62 tokens from this pack: its rules and skill descriptions
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

- [typescript-eslint, Getting Started](https://typescript-eslint.io/getting-started/)

Issue: [#184](https://github.com/brainrc/brainrc/issues/184).
