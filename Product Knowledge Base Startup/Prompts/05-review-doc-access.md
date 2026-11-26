# 05 - Check agent access to project docs

Check whether a coding agent working from **[REPOSITORY ROOT]** can find the Product Knowledge Base.

Verify, without changing files:

1. `docs/README.md` exists, is linked from repository guidance, and links to existing docs.
2. `AGENTS.md` points to the index and explains when to read business vs technical docs.
3. If GitHub Copilot is used, inspect the relevant supported instruction file(s), such as `.github/copilot-instructions.md`; note that support varies by client and feature.
4. The active issue or request links to the specific business/technical docs needed for the task.
5. Documentation files are tracked in the branch the agent is using.

Do not claim instructions guarantee model compliance. Report what is automatically supplied, what is merely linked, and what a human must provide. Recommend the smallest fix for any missing path. Do not edit files in this review.
