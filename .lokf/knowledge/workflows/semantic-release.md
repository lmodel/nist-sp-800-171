---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: "The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request into main, its plan job checks that the commits, the changelog and the title would release and previews the release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub release and dispatches Knowledge Release."
resource: .github/workflows/semantic-release.yml
sources:
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:32:20Z"
---

# Semantic release (semantic-release.yml)

`.github/workflows/semantic-release.yml` is the workflow named "Semantic release".[^semantic-release.yml] On a pull request into `main`, its `plan` job reads whether the commits would release. When they would, it refuses to go on without a `v*` tag, with an empty `## [Unreleased]` section or with a title that has no releasing type, and then previews the release with `--dry-run`. On a push to `main`, its `release` job runs in the `release` Environment with `contents: write` and `actions: write`. It installs semantic-release 25.0.9 and its plugins at pinned versions with `--ignore-scripts`, and releases. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches Knowledge Release for the new tag. [Cut a release](../playbooks/release.md) gives the steps.

[^semantic-release.yml]: .github/workflows/semantic-release.yml, the header comment, the on key and the jobs
