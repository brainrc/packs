# Instructions for AI assistants editing this repo

This repo is public: brainrc's official packs, one per folder. Their skills load into other
people's agents.

- Each folder is a pack: `pack.toml`, `README.md`, `skills/`, `evals/triggers.toml`,
  `permissions.toml`, `tests/` and `tripwires.toml`. Every skill starts with `brainrc-` and has
  frontmatter `name` (its folder's name) and `description` (what it does and when to use it).
- Domain skills keep brainrc's shape: Validate (offline commands) / Conventions / Review checklist /
  Never without approval. Take tool conventions from the tool's own current docs, and cite them in
  the pack's README.
- No secrets, tokens, personal emails, employer or client names, or home folder paths: write `~` and
  environment variable names. Examples use "acme".
- A pack's README states its always-loaded token cost and its permissions; its tests fail when
  either drifts. Each skill needs a trigger case that loads it and a near miss in
  `evals/triggers.toml`.
- CI finds every folder with a `pack.toml`. List a pack in `.github/core-only` while it reuses
  names Gatework ships. A new pack also gets a row in brainrc's official table
  (brainrc/brainrc `docs/packs.md`, `OFFICIAL_PACK_IDS` in `brainrc/naming.py`).
- After a change, run `brainrc validate --pack <folder>` for each pack you touched; it runs the
  pack's tests too. Nothing here calls a model, in CI or in tests.
