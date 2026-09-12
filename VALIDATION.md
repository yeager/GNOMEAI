## GNOME System Monitor: per-process swap usage

Patch archive: `patches/gnome-system-monitor/process-swap/`

- `git diff --check` passed.
- `meson setup build --wipe` stopped before compilation because the local development environment lacks `giomm-2.68`.
- The Processes table gains a sortable **Swap Memory** column and summary. It reads each process’s `VmSwap` value from `/proc/<pid>/status`; inaccessible or unsupported process entries display zero.

## Seahorse: retain import action for importable data

Patch archive: `patches/seahorse/importable-items/`

- `git diff --check` passed.
- `meson setup build --wipe` reached dependency validation and stopped because the local development environment lacks `pwquality`.
- The dialog now keeps **Import All** enabled after an importable parsed item even if a later parsed item has no importer, and skips the latter instead of aborting the full import action.

## GNOME Software: full-size screenshots

Patch archive: `patches/gnome-software/screenshot-zoom/`

- `git diff --check` passed.
- `meson setup build --wipe` reached dependency validation and stopped because the local development environment lacks `packagekit-glib2`.
- No runtime screenshot is claimed: the patch opens a clicked carousel image in a fixed-size Adwaita dialog and asks the existing image loader for its original dimensions.

## Nautilus: rename files created from templates

Patch archive: `patches/nautilus/rename-template-file/`

- `git diff --check` passed.
- Meson configuration reached dependency validation but stopped because this Nautilus 51 source requires `gio-2.0 >= 2.89.0`; the local system has 2.88.0.
- The patch reuses Nautilus’s existing rename popover after the newly created template file has been selected. It does not change empty-file or folder creation.

## GNOME Clocks: active alarms after closing the window

Patch archive: `patches/gnome-clocks/background-alarms/`

- `meson setup build --wipe`, `meson compile -C build`, and `meson test -C build --print-errorlogs` passed.
- The project completed all three supplied checks: desktop entry, GSettings schema, and metainfo validation.
- An isolated Xvfb and D-Bus session loaded an active alarm, sent `Ctrl+W`, and confirmed that the process remained alive.
- The behavior has no new visible control: an active alarm keeps the application alive after the last window closes, and the hold is released when the final alarm becomes inactive.

## GNOME Calendar: per-calendar default reminders

Patch archive: `patches/gnome-calendar/default-reminders/`

- `meson setup build --wipe` configured successfully.
- The two modified C files compiled with Meson's generated compiler commands.
- The generated calendar-management UI includes the nine reminder choices.
- An isolated `glib-compile-schemas --strict` run and a keyfile-backed GSettings round trip stored `{'work': 15}`.
- A complete build remains blocked by three pre-existing Blueprint 0.19 compatibility errors in unrelated Calendar views.

# Validation

## GNOME Shell: persistent screenshot save-to-disk option

Patch archive: `patches/gnome-shell/work-screenshot-save-to-disk/`

- `node --check js/ui/screenshot.js` passed.
- The GSettings schema XML parsed successfully with Python's XML parser.
- `git diff --check 8b21ff4^ 8b21ff4` passed.
- Meson configured with `--wrap-mode=nodownload -Dtests=false`.
- A full compile reached GNOME Shell C sources and stopped on an API mismatch between the archived GNOME Shell 49.1 source and the locally installed Mutter 50.1 headers. The errors are in unchanged `src/shell-global.c` and `src/shell-screenshot.c`; the patch changes only `js/ui/screenshot.js` and `data/org.gnome.shell.gschema.xml.in`.

The upstream JavaScript test suite was disabled only because its `jasmine-gjs` wrap was unavailable in the offline configuration. It has not been represented as passing.

## Console: configurable default window size

Patch archive: `patches/console/default-window-size/`

- `meson setup build --wipe` passed.
- `meson compile -C build` passed.
- `meson test -C build --print-errorlogs` passed: 44 of 44 tests.
- The settings regression test covers both the default 800×600 size and a user-configured 1024×768 size when previous-window restoration is disabled.

## GNOME Bluetooth: editable device name

Patch archive: `patches/gnome-bluetooth/device-alias/`

- `meson setup build --wipe` passed.
- `meson compile -C build` passed.
- `LANGUAGE=C LC_ALL=C LANG=C meson test -C build --print-errorlogs` passed: 18 of 18 tests.
- A dbusmock regression test changes `Alias` and confirms the client receives the update.
- The UI writes the user-selected BlueZ `org.bluez.Device1.Alias` property with an asynchronous system-DBus call; it does not maintain a separate name store.
