# GNOMEAI

A public archive of GNOME contribution work prepared with AI assistance.

This repository explicitly accepts AI-assisted submissions. Every contribution must still be reviewable, buildable, tested where practical, and licensed compatibly with its destination project. Do not submit credentials, generated binaries, vendored build directories, or changes that have not been inspected by a person.

## Contents

- [`patches/`](patches): one directory per local contribution branch. Each contains an ordered `git format-patch` series and `METADATA.json` with its source project, upstream base, commit IDs and archive-directory name.
- [`PATCHES.json`](PATCHES.json): machine-readable index of all patch series.
- [`PLAN.md`](PLAN.md): the live review and implementation plan for the 250 GNOME issues examined so far.
- [`issues-250.csv`](issues-250.csv): issue inventory used by that plan.

## Applying a patch series

Clone the source project listed in `METADATA.json`, check out a compatible upstream revision, then apply the series:

```sh
git am /path/to/GNOMEAI/patches/PROJECT/BRANCH/*.patch
```

Some series deliberately depend on another series. `PLAN.md` records those relationships and the original merge-request context.
