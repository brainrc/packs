# brainrc/go

Go services (vet, tests, golangci-lint, conventions and a review checklist) and database migrations. Gatework 0.8's `brainrc-go-service` and `brainrc-db-migrations`, moved here under the same names.

An official [brainrc](https://github.com/brainrc/brainrc) pack: one folder of
[brainrc/packs](https://github.com/brainrc/packs). brainrc installs its skills into every
AI coding tool it manages.

## Use it

Add it to brainrc's `packs.local.toml`, then run `brainrc apply`. Installing from a folder
of a repo (`subdir`) needs a brainrc release that includes
[#121](https://github.com/brainrc/brainrc/issues/121) (0.8.32 or later).

```toml
# packs.local.toml
[go]
git = "https://github.com/brainrc/packs.git"
ref = "<a tag of brainrc/packs>"
subdir = "go"
```

Gatework 0.8 still ships these skills under the same names (#318). Until it drops
them, exclude its copies so the two packs don't collide:

```toml
# brainrc.local.toml
exclude = [
  "gatework:skills/brainrc-go-service",
  "gatework:skills/brainrc-db-migrations",
]
```

For every agent in one repository, put the same keys under `[packs.go]` in that
repository's `brainrc.toml`.

## What's in it

| Skill | What it's for |
|---|---|
| [`brainrc-db-migrations`](skills/brainrc-db-migrations/SKILL.md) | Safe database schema and data migrations (Postgres-first; golang-migrate, goose, Atlas, Alembic, Flyway), expand/contract changes, locking risks, and backfills. Use when adding or reviewing migration files, changing schemas, or writing data backfills. |
| [`brainrc-go-service`](skills/brainrc-go-service/SKILL.md) | Go services and CLIs. Build/test/lint commands, idioms for errors, context, concurrency, HTTP servers, and testing, plus a review checklist for common Go bugs. Use when writing, changing, or reviewing *.go files or go.mod. |

## Cost and permissions

Every session loads about 119 tokens from this pack: its rules and skill descriptions
(`brainrc tokens` shows the same count). A skill's body loads only when it's used.

It adds no hooks, MCP servers, tool grants or network domains
([permissions.toml](permissions.toml)).

## Evals

[evals/triggers.toml](evals/triggers.toml) has 3 requests: each skill gets one that
should load it and a near miss that shouldn't. brainrc merges them into
`python3 scripts/evals.py triggers` when the pack is enabled. That check needs a model, and
nothing here calls one in CI, so the delta with and without this pack is **unmeasured**.

Issue: [#315](https://github.com/brainrc/brainrc/issues/315).
