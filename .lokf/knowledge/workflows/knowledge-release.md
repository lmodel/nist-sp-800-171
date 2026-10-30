---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/workflows/knowledge-release
genre: reference
title: Knowledge Release (knowledge-release.yaml)
description: "The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: dispatched with a release's tag, or started by a published release once `KNOWLEDGE_RELEASE_ENABLED` is true, it attaches the bundle zip, the domain schema as `schema-<tag>-nist-sp-800-171.yaml` with its checksum, and the Copilot skills to the release, when the bundle or the schema changed or `force` is set."
resource: .github/workflows/knowledge-release.yaml
sources:
  - id: knowledge-release.yaml
    resource: .github/workflows/knowledge-release.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# Knowledge Release (knowledge-release.yaml)

`.github/workflows/knowledge-release.yaml` is the workflow named "Knowledge Release". It runs when it is dispatched with a `tag`, and on a published release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.[^knowledge-release.yaml] Its `pack` job validates and packs the bundle, the domain schema and the Copilot skills read-only, and names them from `KNOWLEDGE_RELEASE_NAME`, or else from the repository's name. Its `attach` job, which holds `contents: write`, `id-token: write` and `attestations: write`, checks each file against its checksum, attests its build provenance, and uploads it. The domain schema goes up as `schema-<tag>-<name>.yaml` with its own `.sha256`. The header says that a release whose bundle and domain schema are unchanged gets no zip, and that the workflow runs no agent and never commits or pushes.

[^knowledge-release.yaml]: .github/workflows/knowledge-release.yaml, the header comment, the on key and the jobs
