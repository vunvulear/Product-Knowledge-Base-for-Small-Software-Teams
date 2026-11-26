# Agent access to docs

The agent needs the docs committed in the branch/repository it is working from. Use a few layers so important context is discoverable:

1. `docs/README.md` is the index and links to business and technical docs.
2. Root `AGENTS.md` is a short map and instructs Codex to consult the index when the task touches product behavior or the solution design.
3. `.github/copilot-instructions.md` can point Copilot to the same index. Copilot support depends on its client and feature; keep the file short and check the official support matrix for the team's surface.
4. GitLab issue templates ask for links to the relevant requirement/flow. The MR template asks whether business or technical docs need an update.
5. The agent reports which docs it used; a reviewer checks that the relevant docs were considered.
6. Optional CI can validate Markdown syntax and internal links. It cannot certify business truth.

No prompt or instruction file can guarantee every model will follow every instruction. The goal is to make the right document easy to find and make omissions visible in review.
