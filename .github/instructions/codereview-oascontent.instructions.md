---
description: 'OASContent-specifieke review-instructies voor Copilot code review'
applyTo: '**'
excludeAgent: "cloud-agent"
---
## PR labels in this repository

This repository contains documentation content (OpenAPI specs, menu structures and
markdown pages) rather than application code. Interpret the PR labels from
`codereview.instructions.md` as follows:

- `🧹 refactor` — Primarily restructuring without content changes
- `💥 breaking` — Contains breaking changes to OpenAPI specs or menu structures that affect published documentation
- `🏗️ infra` — Build, CI/CD, or tooling changes (scripts, workflows)
