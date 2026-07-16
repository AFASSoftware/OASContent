---
description: "Instructions for copilot on github.com"
applyTo: "**"
excludeAgent: "coding-agents"
---

## Reviewing a PR

- Write the summary in **Dutch**
- Be constructive and specific — state **what** is the problem and **why** it is a problem.
- Use your existing labeling system, so high, medium, low and nit.
- Give for `medium` and higher always a suggestion for improvement or fix.

### Review comment labels

Give a review comment one of the following labels:

- 🔴 high (`severity: high`)
- 🟠 medium (`severity: medium`)
- 🟡 low (`severity: low`)
- 🟢 nit (`severity: nitpick`)

### Summary and review

Make sure that the review summary **always** contains exactly one of the following lines as line, just above 'Changes:' or just below the title, for example 'PR Overview', of the review. It is very important that you do it this way, since everything above the title is ignored and everything below Changes: as well. The line should be precisely this, including double stars and spaces:

```
**review nodig: ja**
```

or

```
**review nodig: nee**
```

#### When `review nodig: ja`

- There is at least one **high** or **medium** comment
- There are more than 4 **low** comments
- The changes are too complex or sizeable to be able to give a trustworthy automatic review
- You doubt that the review you did covered everything

#### When `review nodig: nee`

- All comments are **low** or **nitpicks** (maximum 4 lows)
- The changes are trivial and safe
- You are confident that your review covered everything

**Important:** when in doubt, always choose `review nodig: ja`.

### PR labels

Add one or more of the following labels to the PR (in the summary, as a line below `review nodig`):

```
**labels: label1, label2**
```

Available labels:

- `📚 leerzaam` — PR demonstrates a pattern, technique, or solution other contributors can learn from. When applying this label, briefly explain in the summary **why** the PR is educational (e.g., which pattern or technique is noteworthy).
- `🧹 refactor` — Primarily restructuring without content changes
- `💥 breaking` — Contains breaking changes to OpenAPI specs or menu structures that affect published documentation
- `🏗️ infra` — Build, CI/CD, or tooling changes (scripts, workflows)
- `📐 large` — Very large PR; significantly more files or lines changed than typical
