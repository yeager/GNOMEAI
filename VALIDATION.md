# Validation

## GNOME Shell: persistent screenshot save-to-disk option

Patch archive: `patches/gnome-shell/work-screenshot-save-to-disk/`

- `node --check js/ui/screenshot.js` passed.
- The GSettings schema XML parsed successfully with Python's XML parser.
- `git diff --check 8b21ff4^ 8b21ff4` passed.
- Meson configured with `--wrap-mode=nodownload -Dtests=false`.
- A full compile reached GNOME Shell C sources and stopped on an API mismatch between the archived GNOME Shell 49.1 source and the locally installed Mutter 50.1 headers. The errors are in unchanged `src/shell-global.c` and `src/shell-screenshot.c`; the patch changes only `js/ui/screenshot.js` and `data/org.gnome.shell.gschema.xml.in`.

The upstream JavaScript test suite was disabled only because its `jasmine-gjs` wrap was unavailable in the offline configuration. It has not been represented as passing.
