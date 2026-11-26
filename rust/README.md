# brainrc/rust

Rust crates and workspaces: rustfmt, Clippy with warnings denied, cargo test, conventions and a review checklist.

An official [brainrc](https://github.com/brainrc/brainrc) pack: one folder of
[brainrc/packs](https://github.com/brainrc/packs). brainrc installs its skills into every
AI coding tool it manages.

## Use it

Add it to brainrc's `packs.local.toml`, then run `brainrc apply`. Installing from a folder
of a repo (`subdir`) needs a brainrc release that includes
[#121](https://github.com/brainrc/brainrc/issues/121), the first after 0.8.31.

```toml
# packs.local.toml
[rust]
git = "https://github.com/brainrc/packs.git"
ref = "<a tag of brainrc/packs>"
subdir = "rust"
```

It works beside Gatework, brainrc's default pack: none of its skills share a name with Gatework's.

For every agent in one repository, put the same keys under `[packs.rust]` in that
repository's `brainrc.toml`.

## What's in it

| Skill | What it's for |
|---|---|
| [`brainrc-rust`](skills/brainrc-rust/SKILL.md) | Rust crates and workspaces. Format with rustfmt, lint with Clippy, build and test with Cargo, and a review checklist. Use when writing, changing, or reviewing *.rs files, Cargo.toml, or Cargo.lock. |

## Cost and permissions

Every session loads about 50 tokens from this pack: its rules and skill descriptions
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

- [Clippy in GitHub Actions](https://doc.rust-lang.org/clippy/continuous_integration/github_actions.html)

Issue: [#185](https://github.com/brainrc/brainrc/issues/185).
