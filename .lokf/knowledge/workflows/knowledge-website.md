---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: "The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true."
resource: .github/workflows/knowledge-website.yaml
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

`.github/workflows/knowledge-website.yaml` is the workflow named "Knowledge website". It runs on a push or a pull request that touches the site's sources, such as `website/`, `.lokf/`, `README.md`, `docs/` or `CHANGELOG.md`, every Monday at 05:23 UTC and by hand.[^knowledge-website.yaml] Its `build` job builds the site with a read-only token and checks every link. Its `deploy` job holds `pages: write` and `id-token: write`, runs in the `github-pages` Environment for the default branch only, and does nothing until `KNOWLEDGE_WEBSITE_ENABLED` is `true`. The header says that Pages must first be set to build from Actions, and that a repository with another Pages publisher keeps the variable unset until that publisher is retired.

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the header comment, the on key and the jobs
