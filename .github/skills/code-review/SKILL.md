# Code Review Agent Skill

This skill configures Copilot to perform code reviews on pull requests for the OASContent repository, following established review guidelines and standards.

## Overview

This skill enables the Copilot code review agent to:
- Review changes in Dutch
- Apply consistent severity labels (high, medium, low, nit)
- Determine review necessity based on issue complexity
- Apply contextual PR labels
- Provide constructive, specific feedback

## Configuration

```yaml
displayName: "Code Review"
description: "Reviews pull requests with constructive feedback following OASContent standards"
guidelines:
  - name: "Language"
    value: "Write all reviews and comments in Dutch"
  - name: "Specificity"
    value: "Be constructive and specific — state what is the problem and why it is a problem"
  - name: "Severity Labels"
    value: "Use labels: 🔴 high (severity: high), 🟠 medium (severity: medium), 🟡 low (severity: low), 🟢 nit (severity: nitpick)"
  - name: "Suggestions for Medium+ Issues"
    value: "Always provide a suggestion for improvement or fix for medium and higher severity issues"
```

## Review Comment Severity Labels

Apply one of the following labels to each review comment:

- **🔴 high** (`severity: high`) — Critical issues that must be addressed
- **🟠 medium** (`severity: medium`) — Important issues that should be addressed
- **🟡 low** (`severity: low`) — Minor issues worth considering
- **🟢 nit** (`severity: nitpick`) — Style or preference suggestions

## Review Decision: "review nodig"

The summary must always contain exactly one of the following lines:

```
**review nodig: ja**
```

or

```
**review nodig: nee**
```

### Mark as "review nodig: ja" when:

- There is at least one **high** or **medium** comment
- There are more than 4 **low** comments
- The changes are too complex or sizeable for confident automatic review
- You doubt that the review covered everything

### Mark as "review nodig: nee" when:

- All comments are **low** or **nitpicks** (maximum 4 lows)
- The changes are trivial and safe
- You are confident the review covered everything

**Important:** When in doubt, always choose `review nodig: ja`.

## PR Labels

Add one or more of the following labels to the PR summary:

```
**labels: label1, label2**
```

### Available Labels

- **📚 leerzaam** — PR demonstrates a pattern, technique, or solution other contributors can learn from. Briefly explain why the PR is educational.
- **🧹 refactor** — Primarily restructuring without content changes
- **💥 breaking** — Contains breaking changes to OpenAPI specs or menu structures that affect published documentation
- **🏗️ infra** — Build, CI/CD, or tooling changes (scripts, workflows)
- **📐 large** — Very large PR; significantly more files or lines changed than typical

## Review Structure

1. **Summary** — High-level overview of changes and intent
2. **Review Decision** — Include the `review nodig: ja/nee` line
3. **Labels** — Apply relevant PR labels
4. **Reviewed Changes** — List which files were reviewed
5. **Feedback** — Provide specific comments with severity labels
6. **Suggestions** — Offer next steps or improvements

## Applied To

This skill applies to all pull requests in the AFASSoftware/OASContent repository by default.

## See Also

- [.github/instructions/codereview.instructions.md](../../instructions/codereview.instructions.md) — Full review guidelines
