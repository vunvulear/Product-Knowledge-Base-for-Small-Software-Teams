# Change records

GitLab Issues, Merge Requests, commits, and CI results are the primary work history. This folder is optional and should contain only changes whose business rationale or cross-cutting decision would be hard to understand from those records alone.

## When to add a record

- A substantial change affects multiple business flows or important rules.
- A decision or trade-off needs durable context beyond the issue discussion.
- A major bug fix changes agreed product behavior or documents a significant known limitation.

## Suggested layout

`YYYY-MM-short-description/`

Copy the files from `../_change-template/` and link the GitLab issue and merge request. After delivery, update the current business or technical docs. The record explains the transition; it does not replace the current docs.

Do not create a folder for every small bug or code cleanup.
