# 01 - Initialize the Product Knowledge Base

Create or update a `docs/` folder for **[PROJECT ROOT]** using the starter structure in this package. Review the project code, tests, configuration, existing Markdown, and original Word documents before writing.

## Core rule

Use only facts supported by the repository's code, tests, configuration, or existing project documents. Do not use outside knowledge to fill gaps. Never invent business goals, actors, rules, flows, or expected outcomes.

## Keep intent and implementation distinct

- Business requirements, flows, and rules describe intended behavior only when an approved business document or explicit business decision supports them.
- Code and tests are evidence of implemented behavior. They do not, by themselves, prove business intent.
- If code shows a behavior but intent is not documented, label it **Implemented behavior** and add an open question about intended behavior when it matters.
- When sources conflict, cite both and label **Conflict**. Do not choose a winner without an explicit source of authority.

## Write

1. `docs/README.md` as the short navigation index.
2. Useful business docs: overview, requirements, flows, rules, domain, and open questions as needed.
3. Useful technical docs: overview, architecture, data model, integrations, and operations as needed.
4. Keep the business and technical sections separate and concise. Do not create empty or repetitive files.
5. Cite important statements with repository-relative paths and line numbers, or Word document section/page references where practical.
6. Do not change application code, tests, original Word documents, or existing docs outside `docs/`.

Before finishing, list files created/updated and the sources used. Call out any content that needs review by a business owner. Do not delete existing files unless separately requested.
