---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/workflows/knowledge-registrar
genre: reference
title: Knowledge Registrar (knowledge-registrar.yaml)
description: "The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the gate on the knowledge bundle, run on pull requests that touch `.lokf/` or `knowledge_bundle/`, every Monday at 06:00 UTC and by hand; it validates the bundle and its relation targets against the domain schema, runs the conventions script, and checks that each new confirmation by a person is backed by an approval or a signed commit."
resource: .github/workflows/knowledge-registrar.yaml
sources:
  - id: knowledge-registrar.yaml
    resource: .github/workflows/knowledge-registrar.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# Knowledge Registrar (knowledge-registrar.yaml)

`.github/workflows/knowledge-registrar.yaml` is the workflow named "Knowledge Registrar". It runs on a pull request that touches `.lokf/`, `knowledge_bundle/` or the workflow itself, every Monday at 06:00 UTC and by hand.[^knowledge-registrar.yaml] Its `validate` job runs `just lokf-validate` and `just lokf-check-refs`, which pass the domain schema the justfile names, and the conventions script. Its `provenance` job, on a pull request only, checks that each new `human:` confirmation is backed by the named person's approval or signed commit. Its `attestation` job runs only for an unbacked confirmation, in the Environment that `KNOWLEDGE_CURATION_ENVIRONMENT` names.

[^knowledge-registrar.yaml]: .github/workflows/knowledge-registrar.yaml, the header comment, the on key and the jobs
