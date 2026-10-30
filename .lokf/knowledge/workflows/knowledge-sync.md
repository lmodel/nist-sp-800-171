---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: "The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request, opened with the `KNOWLEDGE_SYNC_TOKEN` secret, and holds the workflow changes for a person to approve."
resource: .github/workflows/knowledge-sync.yaml
sources:
  - id: knowledge-sync.yaml
    resource: .github/workflows/knowledge-sync.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# Knowledge sync (knowledge-sync.yaml)

`.github/workflows/knowledge-sync.yaml` is the workflow named "Knowledge sync". It runs every Monday at 04:10 UTC and by hand, optionally for a named `tag`.[^knowledge-sync.yaml] Its `earlier` job reads the pin, the newest release of the Knowledge Trust Ladder and the last sync pull request. Its `sync` job runs the sync script read-only and passes its change on as a patch. Its `publish` job, in the `knowledge-sync` Environment, opens or refreshes one pull request with the `KNOWLEDGE_SYNC_TOKEN` secret. A change to a workflow file is held for the `review` job, in the Environment `KNOWLEDGE_SYNC_REVIEW_ENVIRONMENT` names, and the `push-workflows` job, which first checks that this Environment has required reviewers, then pushes it.

[^knowledge-sync.yaml]: .github/workflows/knowledge-sync.yaml, the header comment, the on key and the jobs
