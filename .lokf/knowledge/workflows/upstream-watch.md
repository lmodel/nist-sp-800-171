---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its sp800171-catalog job runs `scripts/check_upstream_release.py` against NIST's revisions and usnistgov/oscal-content, and on a finding opens or updates the issue titled Upstream watch: NIST's SP 800-171 has changed."
resource: .github/workflows/upstream-watch.yaml
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

`.github/workflows/upstream-watch.yaml` is the workflow named "Upstream watch". It runs every Monday at 07:00 UTC and by hand, since nothing in a pull request can change what it checks.[^upstream-watch.yaml] Its one job, `sp800171-catalog`, reads the checkout and holds `issues: write`. It runs `scripts/check_upstream_release.py` on the runner's Python, and on a finding `.github/scripts/report-issue.sh` opens the issue titled "Upstream watch: NIST's SP 800-171 has changed" or comments on the open one. [Update the upstream pins](../playbooks/update-upstream-pins.md) says what each finding asks for.

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml, the header comment, the on key and the jobs
