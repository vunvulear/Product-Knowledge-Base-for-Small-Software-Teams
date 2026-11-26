# Changes and bugs

## Feature or business behavior change

1. Create a GitLab issue describing the need and expected outcome. Link the relevant business docs.
2. If the behavior is unclear or material, get business confirmation before implementation.
3. For a clear, low-risk task, work directly with Codex or Copilot. For a complex or high-impact change, optionally use OpenSpec, Spec Kit, BMAD, or another agreed workflow.
4. Implement and test against the agreed acceptance examples.
5. In the Merge Request, update current business docs if intent changed and technical docs if the solution changed. Link the issue and docs.
6. Add a `docs/changes/` record only when the decision/rationale needs more durable explanation than the issue and MR provide.

## Bug

1. Record observed and expected behavior, reproduction steps, environment/version, and impact in a GitLab issue.
2. Link the relevant business flow or rule. If expected behavior is not established, mark it as an open question.
3. Add or update a regression test when the bug can be reliably reproduced and automated.
4. Update current docs only if the fix changes or clarifies agreed behavior or the technical solution.
5. Link the issue, MR, and verification result. Do not create a separate Markdown bug log that duplicates GitLab.

## Keep history in the right place

- GitLab Issues: requests, bug discussion, owner, and status.
- Merge Requests: proposed change, review, and links to implementation.
- Git and CI: document/code versions and observed test results (pipeline retention depends on GitLab settings).
- `docs/changes/`: optional context for substantial decisions, not every work item.
