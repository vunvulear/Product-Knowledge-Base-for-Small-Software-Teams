# 03 - Plan a change

Prepare a change for **[ISSUE / REQUEST]**. First read `docs/README.md` and only the business and technical docs relevant to the task. Read the linked GitLab issue and existing code/tests needed to understand current behavior.

Do not implement code in this step.

Summarize separately:

1. Confirmed business need and source.
2. Intended behavior and acceptance examples, quoting no more than needed and linking to the relevant docs.
3. Current implemented behavior and evidence from code/tests.
4. Difference between current and intended behavior.
5. Open questions that need a business decision.
6. Whether a durable `docs/changes/YYYY-MM-short-description/` record is useful. Use one for a material decision or cross-cutting change; do not create one for every small fix.
7. Technical approach and verification plan, only after intended behavior is clear.

Do not guess. If required intent is missing, stop at a reviewable list of questions rather than filling gaps.
