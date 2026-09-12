# Top-50 Triage

This file records checks that prevent duplicate patches and separates a small, testable change from work that needs a larger design or backend change. Source repositories are used only for local investigation. Nothing here is submitted to GNOME or GitLab.

| Rank | Request | Status | Evidence and next step |
| ---: | --- | --- | --- |
| 4 | GNOME Shell: clipboard-only screenshots | Archived | `patches/gnome-shell/work-screenshot-save-to-disk/` adds the persisted `save-to-disk` preference. Disabling it keeps the PNG in the clipboard and does not create a screenshot file. |
| 11 | File Roller: drag an archive to a Nautilus folder to extract | Needs integration design | Current File Roller implements drops *into* its window (`fr_window_on_drop()`), but no outgoing archive-content drag source. A correct implementation needs a temporary extraction contract and lifecycle agreement with the file manager. |
| 12 | GNOME Software: quit when inactive | Already implemented | At local source revision `3e657d1`, `gs_application_new()` sets GApplication's `inactivity-timeout` to 12,000 milliseconds. No duplicate patch is published. |
| 15 | Geary: mark every message read | Needs backend operation | The existing UI actions cover loaded conversations. A complete solution must enumerate and update the backing mailbox, including pagination, cancellation, and IMAP error handling. |
| 17 | GTK: keep the Save filename field focused while choosing a folder | Reproduction needed | Folder navigation is asynchronous in `gtkfilechooserwidget.c`. A regression test must first establish the precise input path and focus owner before changing focus restoration. |
| 28 | GNOME Extensions: local extension installation | Built as a GNOMEAI app | [`Extension Pack Installer`](apps/extension-pack-installer/) validates ZIP paths and `metadata.json`, refuses overwrite, and installs only after an explicit local action. |
| 26 | Scheduled light/dark appearance | Needs daemon and settings design | A panel-only switch would not schedule changes. This requires a persistent service, daylight or user schedule policy, and a stable settings API. |
| 39 | GTK: spellchecking | Needs provider API | GTK renders `spelling-error` styling supplied by Wayland IME, but has no general dictionary provider, word-range API, or replacement-menu contract for applications. |
| 43 | VTE: OSC 52 | Needs explicit clipboard authorization | The terminal parser recognizes OSC 52, but a safe implementation requires a visible authorization policy before a remote program can write the local clipboard. |
| 48 | GNOME Calendar: flexible recurrence intervals | Archived | `patches/gnome-calendar/recurrence-interval/` adds the numeric interval control and preserves iCalendar `INTERVAL`. |
| 65 | Control Center: Applications list does not populate | No source defect reproduced | The panel rebuilds from `g_app_info_get_all()` and refreshes on `GAppInfoMonitor::changed`. The reported symptom needs a reproducer with its desktop-file and session context. |
| 69 | GTK: repeated Wayland `text_input.enable` | Needs protocol test | GTK enables on text-input focus entry and on legacy on-screen-keyboard activation. The tree has no text-input-v3 protocol mock, so a state guard cannot be validated without risking legacy keyboard activation. |
| 49 | GNOME Software: screenshot zoom | Archived | `patches/gnome-software/screenshot-zoom/` opens the selected screenshot at its original size in an Adwaita dialog. |
