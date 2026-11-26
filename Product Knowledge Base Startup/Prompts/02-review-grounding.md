# 02 - Review documentation grounding

Review every Markdown file under `docs/`. Check each factual statement against the cited repository code, tests, configuration, or original project documents. Do not use general knowledge or external sources to fill gaps.

For each claim, verify:

- Does the cited source exist and support the statement?
- Is a statement about intended business behavior supported by an approved business source, rather than code alone?
- Is code behavior labeled as implementation evidence?
- Are conflicts and unknowns explicit?
- Do links, paths, and line/section/page references resolve?

Correct or remove unsupported statements. Move meaningful unknowns to `docs/business/open-questions.md` or the relevant technical doc. Do not invent replacements. Do not change application code or original source documents. End with a short list of reviewed files, corrections, conflicts, and open questions.
