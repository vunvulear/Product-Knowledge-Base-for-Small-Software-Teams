# Product Knowledge Base

This folder is the project's human-readable product reference. It is kept with the code so changes can be reviewed and versioned together.

## Business

- [Overview](business/overview.md) - product purpose, users, and scope.
- [Requirements](business/requirements.md) - agreed needs and expected outcomes.
- [Flows](business/flows.md) - user and business workflows.
- [Rules](business/rules.md) - business rules and validations.
- [Domain](business/domain.md) - terms and concepts.
- [Open questions](business/open-questions.md) - unresolved facts needing confirmation.

## Technical

- [Overview](technical/overview.md) - current technical solution at a glance.
- [Architecture](technical/architecture.md) - components and interactions.
- [Data model](technical/data-model.md) - data entities and relationships.
- [Integrations](technical/integrations.md) - external boundaries and contracts.
- [Operations](technical/operations.md) - configuration, deployment, and support.

## Changes

- [Change records](changes/README.md) - durable context for selected important changes. GitLab Issues and Merge Requests remain the work-tracking record.

## Evidence and status

Every material statement should link to repository evidence or an approved business source. Use these labels where helpful:

- **Confirmed intent** - stated in an approved business source.
- **Implemented behavior** - observed in code or tests, with a source reference.
- **Open question** - not established by available sources.
- **Conflict** - sources disagree; describe both and leave unresolved until a responsible person decides.

Code behavior does not automatically prove business intent. See the separate `Ways of Working/` folder in this starter kit for the recommended maintenance loop.
