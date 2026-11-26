# brainrc/kubernetes

Kubernetes manifests, Helm and Kustomize (render and schema checks offline), GitOps with Argo CD or Flux, and Dockerfiles. Gatework 0.8's `brainrc-kubernetes`, `brainrc-gitops` and `brainrc-containers`, moved here under the same names.

An official [brainrc](https://github.com/brainrc/brainrc) pack: one folder of
[brainrc/packs](https://github.com/brainrc/packs). brainrc installs its skills into every
AI coding tool it manages.

## Use it

Add it to brainrc's `packs.local.toml`, then run `brainrc apply`. Installing from a folder
of a repo (`subdir`) needs a brainrc release that includes
[#121](https://github.com/brainrc/brainrc/issues/121) (0.8.32 or later).

```toml
# packs.local.toml
[kubernetes]
git = "https://github.com/brainrc/packs.git"
ref = "<a tag of brainrc/packs>"
subdir = "kubernetes"
```

Gatework 0.8 still ships these skills under the same names (#318). Until it drops
them, exclude its copies so the two packs don't collide:

```toml
# brainrc.local.toml
exclude = [
  "gatework:skills/brainrc-kubernetes",
  "gatework:skills/brainrc-gitops",
  "gatework:skills/brainrc-containers",
]
```

For every agent in one repository, put the same keys under `[packs.kubernetes]` in that
repository's `brainrc.toml`.

## What's in it

| Skill | What it's for |
|---|---|
| [`brainrc-containers`](skills/brainrc-containers/SKILL.md) | Dockerfiles and Compose files. Lint, build checks, image hardening, and caching conventions. Use when writing, changing, or reviewing Dockerfile*, Containerfile, .dockerignore, or compose*.yaml. |
| [`brainrc-gitops`](skills/brainrc-gitops/SKILL.md) | GitOps delivery with Argo CD and Flux. How changes flow through config repos, safe promotion across environments, sync ordering, and review of Application/Kustomization/HelmRelease resources. Use when changing GitOps config repos, Argo CD Applications/ApplicationSets, Flux Kustomizations/HelmReleases, or image promotion. |
| [`brainrc-kubernetes`](skills/brainrc-kubernetes/SKILL.md) | Kubernetes manifests, Helm charts, and Kustomize overlays. Offline rendering and schema validation, production-readiness conventions, and review checklist. Use when writing, changing, or reviewing Kubernetes YAML, Chart.yaml/values*.yaml/templates, or kustomization.yaml. |

## Cost and permissions

Every session loads about 198 tokens from this pack: its rules and skill descriptions
(`brainrc tokens` shows the same count). A skill's body loads only when it's used.

It adds no hooks, MCP servers, tool grants or network domains
([permissions.toml](permissions.toml)).

## Evals

[evals/triggers.toml](evals/triggers.toml) has 4 requests: each skill gets one that
should load it and a near miss that shouldn't. brainrc merges them into
`python3 scripts/evals.py triggers` when the pack is enabled. That check needs a model, and
nothing here calls one in CI, so the delta with and without this pack is **unmeasured**.

Issue: [#317](https://github.com/brainrc/brainrc/issues/317).
