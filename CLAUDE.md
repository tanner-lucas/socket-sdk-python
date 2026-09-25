# Fork workflow

This is a personal fork of `SocketDev/socket-sdk-python`. This file and
`.claude/` live only on the fork's `claude-config` branch and must never
reach upstream.

## Branches

- `main` mirrors `upstream/main` exactly. Never commit to it; only
  fast-forward it to `upstream/main`.
- `claude-config` is `main` plus a single commit holding this file and
  `.claude/settings.json`. When `upstream/main` has moved, rebase
  `claude-config` onto it and force-push it (it is the only branch that
  may be force-pushed).
- Do all work on a new branch created from `upstream/main`, not from
  `claude-config`, named for the change: `fix/<topic>`, `feat/<topic>`,
  `chore/<topic>`, `docs/<topic>`, e.g. `fix/fullscans-stdout-logging`.
  Push that branch instead of the session's auto-named `claude/...` branch.
- Never include `CLAUDE.md` or `.claude/` in a work branch or a PR.

## Remotes

`origin` is the fork. If `upstream` is missing, add it:
`git remote add upstream https://github.com/SocketDev/socket-sdk-python.git`

## Commits and PRs

Commits must be authored by the fork owner, not Claude. The container's
global git identity is Claude's, so before the first commit of every
session run:

```
git config user.name tanner-lucas
git config user.email tannerlucasdev@gmail.com
git config commit.gpgsign false
```

Do not add `Co-Authored-By`, `Claude-Session`, or "Generated with Claude
Code" lines to commit messages or PR descriptions.

## Checks

Install dependencies with `uv sync`, then run
`uv run --with pytest pytest tests/unit -q` before pushing.
