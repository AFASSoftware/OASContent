---
description: "Markdown review skill for documentation changes"
applyTo: "**/*.md"
---

# Markdown review

Use this skill when reviewing Markdown documentation changes. Focus on clarity, correctness, consistency, and reader impact.

## Review goals

- Confirm the content is accurate, complete, and not misleading.
- Check that the structure helps readers scan and understand the page.
- Verify links, references, and code fences are valid.
- Ensure translated pages stay aligned across locales when applicable.
- Prefer actionable feedback over style-only remarks.

## What to check

### Frontmatter and metadata

- Required frontmatter fields are present and valid.
- Title, date, tags, and author are consistent with the page’s purpose.
- Metadata matches any sibling locale version.
- New or changed metadata does not break indexing or publishing rules.

### Structure and readability

- Heading hierarchy is logical and sequential.
- Sections are in a sensible order for the reader’s task.
- Paragraphs are concise and scannable.
- Lists and tables are easy to read and internally consistent.
- Code blocks, callouts, and quotes are used intentionally.

### Links and references

- Internal links resolve to the correct page, anchor, or file.
- Relative links are correct from the file’s location.
- Cross-references still make sense after renames or restructuring.
- External links are not stale or obviously incorrect.
- Anchors match the rendered heading text, not just the source text.

### Terminology and consistency

- Use the same terms consistently throughout the document.
- Keep product names, feature names, and button labels aligned with existing docs.
- Avoid introducing new jargon without explanation.
- If a term changes across locales, confirm it is intentional and clear.

### Locale parity for translations

- NL and EN versions cover the same intent and scope.
- Important steps, warnings, and requirements exist in both locales.
- The translation does not drift in meaning, omissions, or emphasis.
- Examples, filenames, and references are localized only when needed.

### Formatting and Markdown hygiene

- Headings use the correct Markdown level.
- Bullet lists are formatted consistently.
- Tables render cleanly and are not overly wide or ambiguous.
- Code fences use the correct language where helpful.
- Line breaks, spacing, and emphasis do not reduce readability.
- Avoid trailing whitespace unless it is intentionally required.

### Completeness and doc quality

- The document answers the reader’s likely next question.
- Steps are actionable and do not skip required prerequisites.
- Warnings and limitations are clear where the content could be misread.
- Examples are present when they improve understanding.
- The text does not imply guarantees that are not actually supported.

## Common warning signs

- A new term is introduced without definition.
- A link label changes but the destination does not match.
- NL and EN pages diverge in meaning.
- A date or instruction is updated in one locale but not the other.
- The document says “always” or “never” without enough context.
- A section sounds correct but is vague enough to be interpreted incorrectly.

## Suggested review workflow

1. Read the frontmatter first.
2. Scan headings to understand the document’s structure.
3. Check whether the change is clear in context, not just line-by-line.
4. Verify links, anchors, examples, and file references.
5. Compare sibling locale pages when the document is translated.
6. Leave comments only on issues that affect clarity, correctness, consistency, or maintainability.
7. For medium and high findings, explain the user impact and suggest a fix.

## Review comment style

- Be constructive and specific.
- Explain what is wrong and why it matters.
- Prefer one clear suggestion over multiple vague remarks.
- Use severity labels consistently.
- For documentation, call out user confusion, broken navigation, missing context, and locale drift.

## When to approve

Approve when the Markdown change is:

- accurate,
- readable,
- structurally sound,
- consistent with related docs,
- and free of broken references or misleading wording.

## When to block

Block or request changes when the Markdown change:

- breaks links or anchors,
- creates inconsistent locale content,
- introduces unclear or misleading instructions,
- weakens the document’s structure,
- or omits essential context for the reader.
