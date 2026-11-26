---
name: brainrc-pr-description
description: Write a concise pull request title and description from a change's spec, plan, verification, and diff. Use when opening a PR, or when asked to write or improve a PR description.
---

# brainrc-pr-description

Use the repository's PR template (`.github/pull_request_template.md` or the like) when it has
one. Otherwise use the sections below, filled in from the spec (if any), the diff and commits.

- **Title:** imperative, 72 chars or fewer, describes the user-visible change ("Add CSV export to reports").
  If the project uses conventional commits, prefix it (`feat:`, `fix:`).
- **Why** comes first and comes from the problem, not the implementation.
- **What changed:** one bullet per meaningful change, user-visible first. No file-by-file tours.
- **Acceptance criteria:** checked boxes, each pointing at its evidence (a test, a command's output).
- **How to verify:** commands a reviewer can copy.
- **Follow-ups:** unaddressed MEDIUM/LOW findings, known limitations.
- **Link:** `Closes #N` (GitHub) or the tracker key. Link the spec path.

Keep it under ~40 lines. Reviewers skim.
