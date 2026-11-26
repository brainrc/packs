# brainrc packs

The official packs for [brainrc](https://github.com/brainrc/brainrc), one per folder. Gatework,
brainrc's default pack, has [a repo of its own](https://github.com/brainrc/gatework).

| Folder | ID | What | Tokens every session | With Gatework |
|---|---|---|---|---|
| [`starter`](starter/) | `brainrc/starter` | a small base for a setup without Gatework: find a project's commands | 58 | off |
| [`review`](review/) | `brainrc/review` | review, PR description, commit message and unslop | 148 | off |
| [`go`](go/) | `brainrc/go` | Go services and database migrations | 119 | exclude its copies |
| [`terraform-aws`](terraform-aws/) | `brainrc/terraform-aws` | Terraform and AWS | 103 | exclude its copies |
| [`kubernetes`](kubernetes/) | `brainrc/kubernetes` | Kubernetes, GitOps and containers | 198 | exclude its copies |
| [`python`](python/) | `brainrc/python` | Python: Ruff and pytest | 60 | on |
| [`node-ts`](node-ts/) | `brainrc/node-ts` | Node and TypeScript: tsc and ESLint | 62 | on |
| [`rust`](rust/) | `brainrc/rust` | Rust: rustfmt, Clippy and cargo test | 50 | on |
| [`security-baseline`](security-baseline/) | `brainrc/security-baseline` | guard rules for credential files, secret protection and a sandbox profile | 0 | on |

"Tokens every session" is what the pack's skill descriptions and rules add to every session; a
skill's body loads only when it's used. "With Gatework" says how the pack sits beside Gatework:
`on` works alongside it, `exclude its copies` takes over skills Gatework 0.8 still ships (the
pack's README lists the `exclude` lines), and `off` is for a setup with Gatework turned off.

## Use one

Add it to brainrc's `packs.local.toml` with the folder as `subdir`, then run `brainrc apply`:

```toml
[python]
git = "https://github.com/brainrc/packs.git"
ref = "<a tag of this repo>"
subdir = "python"
```

`subdir` needs a brainrc release that includes
[brainrc/brainrc#121](https://github.com/brainrc/brainrc/issues/121), the first after 0.8.31. For
every agent in one repository, put the same keys under `[packs.python]` in its `brainrc.toml`.
brainrc's lock records the folder and commit, so `brainrc install --frozen` gives every machine
the same files.

## Each pack ships

- `pack.toml`: its ID, prefix (`brainrc-`), the brainrc versions it works with and a token budget.
- `skills/`: Validate / Conventions / Review checklist / Never without approval.
- `evals/triggers.toml`: a request that should load each skill and a near miss that shouldn't,
  merged into `scripts/evals.py triggers` when the pack is enabled. That check needs a model, and
  nothing here calls one, so each pack's delta is unmeasured until someone runs it.
- `permissions.toml`: the hooks, MCP servers, tool grants and network domains it adds, as
  `brainrc.lock` records them.
- `tests/`: run by `brainrc validate --pack <folder>`; they keep the README's token cost and the
  permission manifest true.

CI runs brainrc's `validate-pack` action on every folder.

## License

MIT, as brainrc.
