---
name: brainrc-rust
description: Rust crates and workspaces. Format with rustfmt, lint with Clippy, build and test with Cargo, and a review checklist. Use when writing, changing, or reviewing *.rs files, Cargo.toml, or Cargo.lock.
---

# brainrc-rust

## Validate (offline)
```bash
cargo fmt --all -- --check
cargo clippy --all-targets --all-features -- -D warnings
cargo test --all-features
cargo build --locked           # when Cargo.lock is committed
```
In a workspace, add `-p <crate>` to scope to the changed crates. If the project's CI names
features or a toolchain (`rust-toolchain.toml`), use those instead of `--all-features`. Use
`--offline` when the dependencies are already fetched.

## Conventions
- `Result` and `?` for recoverable errors; `unwrap`/`expect` only where failure is a bug, with an
  `expect` message that says why it can't happen.
- No `unsafe` without a `// SAFETY:` comment stating the invariant.
- Public items get doc comments; doc examples compile (`cargo test` runs them).
- Follow the crate's MSRV (`rust-version` in Cargo.toml): no newer language or std features.
- Dependencies through `cargo add`, which updates Cargo.lock; never hand-edit the lock file.

## Review checklist
- [ ] fmt, Clippy (warnings denied) and tests pass for the changed crates.
- [ ] No new `#[allow(clippy::...)]` without a reason next to it.
- [ ] No panics on input the caller controls; errors carry context.
- [ ] Public API or feature changes are intended and semver-appropriate.
- [ ] No secrets in code, tests or build scripts.

## Never without approval
- Add, upgrade or remove dependencies, or run `cargo update`: name the change and ask.
- Change the toolchain or MSRV.
- `cargo publish`, or `cargo install` of a tool the project doesn't list.
