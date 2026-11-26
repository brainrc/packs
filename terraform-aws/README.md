# brainrc/terraform-aws

Terraform and Terragrunt (fmt, validate, tflint, plan review) and AWS (accounts, IAM, guardrails). Gatework 0.8's `brainrc-terraform` and `brainrc-aws`, moved here under the same names.

An official [brainrc](https://github.com/brainrc/brainrc) pack: one folder of
[brainrc/packs](https://github.com/brainrc/packs). brainrc installs its skills into every
AI coding tool it manages.

## Use it

Add it to brainrc's `packs.local.toml`, then run `brainrc apply`. Installing from a folder
of a repo (`subdir`) needs a brainrc release that includes
[#121](https://github.com/brainrc/brainrc/issues/121) (0.8.32 or later).

```toml
# packs.local.toml
[terraform-aws]
git = "https://github.com/brainrc/packs.git"
ref = "<a tag of brainrc/packs>"
subdir = "terraform-aws"
```

Gatework 0.8 still ships these skills under the same names (#318). Until it drops
them, exclude its copies so the two packs don't collide:

```toml
# brainrc.local.toml
exclude = [
  "gatework:skills/brainrc-terraform",
  "gatework:skills/brainrc-aws",
]
```

For every agent in one repository, put the same keys under `[packs.terraform-aws]` in that
repository's `brainrc.toml`.

## What's in it

| Skill | What it's for |
|---|---|
| [`brainrc-aws`](skills/brainrc-aws/SKILL.md) | AWS account safety, CLI usage, and review checklists for IAM, networking, S3, KMS, EKS, and cost. Use when a change or task involves AWS resources, IAM policies, the aws CLI, or AWS-specific Terraform. |
| [`brainrc-terraform`](skills/brainrc-terraform/SKILL.md) | Terraform/OpenTofu and Terragrunt conventions, offline validation, plan evidence, and review checklist. Use when writing, changing, or reviewing *.tf, *.tfvars, .terraform.lock.hcl, or terragrunt.hcl files. |

## Cost and permissions

Every session loads about 103 tokens from this pack: its rules and skill descriptions
(`brainrc tokens` shows the same count). A skill's body loads only when it's used.

It adds no hooks, MCP servers, tool grants or network domains
([permissions.toml](permissions.toml)).

## Evals

[evals/triggers.toml](evals/triggers.toml) has 3 requests: each skill gets one that
should load it and a near miss that shouldn't. brainrc merges them into
`python3 scripts/evals.py triggers` when the pack is enabled. That check needs a model, and
nothing here calls one in CI, so the delta with and without this pack is **unmeasured**.

Issue: [#316](https://github.com/brainrc/brainrc/issues/316).
