# Principles and ownership

## Principles

1. Business first: keep requirements, business rules, and flows readable for non-technical people.
2. Grounded documentation: cite project sources; label implementation observations, open questions, and conflicts.
3. Current docs describe current agreed intent and current technical solution. Git history and GitLab work items preserve the change trail.
4. Avoid duplication. Keep a fact in one main document and link to it elsewhere.
5. Use Markdown and normal Git reviews. Do not require OpenSpec, Spec Kit, BMAD, or a particular coding assistant.
6. Match ceremony to risk and ambiguity.

## Ownership

- A business owner confirms requirements, business rules, and user-facing flows.
- A technical owner confirms architecture, data, integrations, and operations.
- For a small team, one person can hold both roles, but business intent should still be explicitly confirmed.
- The person changing behavior proposes doc updates in the same review as the code change.

## Status vocabulary

- **Confirmed intent** - approved business source or decision supports it.
- **Implemented behavior** - observed in code/tests/configuration.
- **Open question** - not established by available sources.
- **Conflict** - sources do not agree.
