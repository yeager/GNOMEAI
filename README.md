# GNOMEAI

GNOMEAI is an independent GitHub archive for GNOME-related patch series, debugging notes, and implementation plans where AI may be used as a productive development tool. It does not submit work to GNOME or GitLab.

AI is not a threat to software development. Used well, it shortens the path from a bug report to a clear reproduction, helps people navigate large codebases, suggests focused changes, and finds tests that might otherwise be missed. It leaves more time for work that still needs judgment: understanding user needs, choosing architecture, reviewing risk, and taking responsibility for the result.

A contribution is judged by the same standards regardless of the tools used to create it:

- Does it solve a real problem?
- Is the change small enough to understand and review?
- Is there a reproduction or relevant test?
- Does it fit the project's design, APIs, and maintenance needs?
- Are authorship, licensing, and limitations clear?

AI-assisted contributions are welcome here. They must be factual, tested where practical, and reviewable line by line. Do not add secrets, build directories, or generated changes that have not been inspected.

## Contents

- [`patches/`](patches) contains one directory per work branch. Each directory has an ordered `git format-patch` series and `METADATA.json` with the source project, upstream base, commit IDs, and archive directory.
- [`PATCHES.json`](PATCHES.json) is a machine-readable index of every patch series.
- [`PLAN.md`](PLAN.md) contains the working review and implementation plan for 250 GNOME issues.
- [`issues-250.csv`](issues-250.csv) is the issue inventory used by the plan.

## Apply a patch series

Clone the source project listed in `METADATA.json`, check out a compatible upstream revision, and apply the series:

```sh
git am /path/to/GNOMEAI/patches/PROJECT/ARCHIVE-DIRECTORY/*.patch
```

Some series depend on other series. Read `PLAN.md` and the relevant metadata before applying a series locally.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). Always state the target project, base revision, problem addressed, validation performed, and known limitations. The contributor is responsible for the final diff in this archive.

## Apps

- [Clip Shelf](apps/clip-shelf/): a manual, local clipboard-text shelf for GTK 4.
- [Focus Block](apps/focus-block/): a local focus and break timer.
- [Command Shelf](apps/command-shelf/): a local library of copyable command snippets.
- [Name Shift](apps/name-shift/): local batch renaming with a validated file-name preview.
