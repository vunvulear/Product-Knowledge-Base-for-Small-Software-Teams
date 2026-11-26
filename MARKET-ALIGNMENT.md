# Market alignment and research notes

Reviewed 2026-11-26. This is a practical synthesis of official product and project documentation, not a claim that the market has one standard name or one required tool.

## What current practice supports

1. **Keep durable project knowledge structured and easy to navigate.** OpenAI describes a structured repository `docs/` as a knowledge system of record and a short `AGENTS.md` as its map, not as a giant encyclopedia. This starter uses that pattern with business and technical folders.
2. **Give agents a small entry point and task-relevant context.** Codex reads applicable `AGENTS.md` instructions. GitHub Copilot supports repository instructions in several clients, but support varies by client and feature. Instructions guide an agent; they do not guarantee compliance. This is why the template combines an index, short instructions, task links, and review checks.
3. **Keep current intent distinct from a change's working artifacts.** OpenSpec keeps current specifications separate from proposals and archived changes. Spec Kit supports existing projects and explicitly leaves retention and maintenance of artifacts to the team's chosen policy. Therefore, the knowledge base is independent of either framework.
4. **Link work items to code changes.** GitLab supports cross-links among issues, commits, and merge requests. A small MR checklist can request a documentation update when behavior changes.
5. **Use process in proportion to the change.** Direct Codex or Copilot work is fine for clear, small tasks. Structured methods such as OpenSpec, Spec Kit, and BMAD are optional aids for unclear or higher-impact work.

## Design choice in this kit

This kit uses **Product Knowledge Base** and **docs-as-code**. It assumes the Markdown documents live in the same repository as the code, in a folder accessible to business readers and developers. Business documents describe agreed intended behavior; technical documents describe the current solution. Git/GitLab keep versions and work history.

This is a lightweight design choice for small teams, not a requirement of Codex, Copilot, GitLab, or any spec framework. Markdown makes the content portable, but non-technical readers may prefer an editor or GitLab web interface.

## Sources

- OpenAI, Harness engineering: https://openai.com/index/harness-engineering/
- OpenAI, Codex prompting guide and `AGENTS.md`: https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide
- GitHub Copilot customization support matrix: https://docs.github.com/en/copilot/reference/custom-instructions-support
- GitHub Copilot customization overview: https://docs.github.com/en/copilot/concepts/customizations/comparing-customizations
- OpenSpec quickstart and archive model: https://openspec.dev/docs/quickstart
- Spec Kit: adopting in an existing project: https://github.github.com/spec-kit/how-to/existing-projects.html
- Spec Kit: evolving specifications: https://github.github.com/spec-kit/how-to/evolving-specs.html
- BMAD Method: https://bmadcode.com/method
- GitLab cross-linking issues: https://docs.gitlab.com/user/project/issues/crosslinking_issues/
- GitLab issue and merge request description templates: https://docs.gitlab.com/user/project/description_templates/
- GitLab documentation link checks: https://docs.gitlab.com/development/documentation/testing/

## Limitations

- An `AGENTS.md` or Copilot instruction file is a navigation aid, not a hard guarantee that every agent reads every document.
- A link checker can catch broken paths; it cannot confirm that business statements are true.
- AI-generated documentation must be reviewed by people who can confirm business intent.
- Product capabilities and framework commands change over time. Recheck official docs before adopting a tool or relying on a specific integration.
