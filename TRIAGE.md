# Top-50 Triage

This file records checks that prevent duplicate patches and separates a small, testable change from work that needs a larger design or backend change. Source repositories are used only for local investigation. Nothing here is submitted to GNOME or GitLab.

| Rank | Request | Status | Evidence and next step |
| ---: | --- | --- | --- |
| 4 | GNOME Shell: clipboard-only screenshots | Archived | `patches/gnome-shell/work-screenshot-save-to-disk/` adds the persisted `save-to-disk` preference. Disabling it keeps the PNG in the clipboard and does not create a screenshot file. |
| 11 | File Roller: drag an archive to a Nautilus folder to extract | Needs integration design | Current File Roller implements drops *into* its window (`fr_window_on_drop()`), but no outgoing archive-content drag source. A correct implementation needs a temporary extraction contract and lifecycle agreement with the file manager. |
| 12 | GNOME Software: quit when inactive | Already implemented | At local source revision `3e657d1`, `gs_application_new()` sets GApplication's `inactivity-timeout` to 12,000 milliseconds. No duplicate patch is published. |
| 15 | Geary: mark every message read | Needs backend operation | The existing UI actions cover loaded conversations. A complete solution must enumerate and update the backing mailbox, including pagination, cancellation, and IMAP error handling. |
| 17 | GTK: keep the Save filename field focused while choosing a folder | Reproduction needed | Folder navigation is asynchronous in `gtkfilechooserwidget.c`. A regression test must first establish the precise input path and focus owner before changing focus restoration. |
| 26 | Scheduled light/dark appearance | Needs daemon and settings design | A panel-only switch would not schedule changes. This requires a persistent service, daylight or user schedule policy, and a stable settings API. |
| 43 | VTE: OSC 52 | Needs explicit clipboard authorization | The terminal parser recognizes OSC 52, but a safe implementation requires a visible authorization policy before a remote program can write the local clipboard. |
| 48 | GNOME Calendar: flexible recurrence intervals | Archived | `patches/gnome-calendar/recurrence-interval/` adds the numeric interval control and preserves iCalendar `INTERVAL`. |
| 49 | GNOME Software: screenshot zoom | Archived | `patches/gnome-software/screenshot-zoom/` opens the selected screenshot at its original size in an Adwaita dialog. |
