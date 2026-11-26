---
name: brainrc-python
description: Python projects and libraries. Lint and format with Ruff, test with pytest or unittest, type-check when configured, and a review checklist. Use when writing, changing, or reviewing *.py files, pyproject.toml, or a Python package's tests.
---

# brainrc-python

## Validate (offline)
Run what the project configures; never add a tool it doesn't use.
```bash
ruff check .                  # lint, if Ruff is configured (pyproject [tool.ruff] or ruff.toml)
ruff format --check .         # formatting, without rewriting files
pytest -q                     # if pytest is configured or a dependency; else python3 -m unittest
mypy <package>  # or pyright  # only if the project configures one
```
Run through the project's environment manager (`uv run`, `poetry run`, `hatch run`, an
activated venv) so the pinned tool versions are used. `ruff check --fix` and `ruff format` rewrite
files: run them on the files you changed, then read the diff.

## Conventions
- Configuration lives in `pyproject.toml` (`[project]`, `[tool.ruff]`, `[tool.ruff.lint]`,
  `[tool.pytest.ini_options]`); don't add a second config file for a tool that already has one.
- Respect `requires-python`: no syntax or stdlib API newer than the oldest version it allows.
- Type hints on public functions; `dataclasses` or the project's model library for structured data.
- `pathlib` for paths, context managers for files, `subprocess.run([...], check=True)` with an
  argument list, never `shell=True` with input.
- Tests sit next to the project's existing tests and use its fixtures; one behaviour per test.
- Dependencies go in `pyproject.toml` with the project's lock tool (`uv lock`, `poetry lock`);
  never hand-edit a lock file.

## Review checklist
- [ ] Ruff and the type checker pass on the changed files; no new `# noqa` or `type: ignore`
      without a reason next to it.
- [ ] No mutable default arguments, bare `except:`, or swallowed exceptions.
- [ ] Imports at module top; no import-time side effects (network, file writes).
- [ ] New behaviour has a test that fails without the change.
- [ ] No secrets, tokens or absolute home paths in code, tests or fixtures.

## Never without approval
- Install packages or change the Python version (`pip install`, `uv add`, `poetry add`, a new
  interpreter): name what you'd install and ask.
- `ruff check --unsafe-fixes`, or reformatting files you didn't change.
- Publish a package (`uv publish`, `twine upload`, `poetry publish`).
