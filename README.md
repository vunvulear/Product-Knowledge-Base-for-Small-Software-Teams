# Product Knowledge Base Startup

A small, tool-independent starter kit for keeping product knowledge in Markdown beside the code.

## What is included

- `Template/` - a reusable folder structure and blank document templates for one software project.
- `Example/` - a small, fictional booking product with example source material and populated documents.
- `Prompts/` - reusable prompts to inspect a project, initialize docs from source evidence, review grounding, and maintain docs as work changes.
- `Ways of Working/` - lightweight guidance for owners, agent access, changes, bugs, reviews, and history.
- `MARKET-ALIGNMENT.md` - the market research behind this starter kit, with primary-source links.

## Suggested start

1. Copy the contents of `Template/repository/` into the root of one project repository.
2. Replace the placeholders with confirmed project information. Keep unknowns as open questions.
3. Run `Prompts/00-discover-project.md` first, then use `Prompts/01-initialize-from-sources.md` to draft the documents from the project code and existing documents.
4. Have a business owner review business intent and a technical owner review the technical description.
5. Keep the knowledge base in the normal Git review flow. Add OpenSpec, Spec Kit, BMAD, or another method only when a change benefits from more structure.

## Important source-of-truth distinction

The reviewed business documents describe agreed, intended behavior. Code and tests are evidence of implemented behavior. If these disagree, record the discrepancy and ask the responsible person to decide; do not silently change one to match the other.

The example is fictional and only demonstrates format. It is not a real product or a recommended business policy.
