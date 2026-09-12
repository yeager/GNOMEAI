# GNOME Work Plan

This plan tracks 250 GNOME issues selected by community demand and current relevance. It is an engineering queue, not a promise that every request is suitable for an isolated patch. Each item is first checked for a current reproduction, existing upstream work, ownership boundaries, design requirements, and a testable implementation path.

## Working Rules

- Prefer a small, reviewable fix with a regression test.
- Keep the archive independent; do not submit patches to GNOME or GitLab.
- Do not replace a required design or security decision with a superficial UI change.
- Archive every prepared contribution as an ordered patch series with its upstream base.
- AI assistance is allowed; each archived patch still requires technical review and accountable ownership.

## Issue Inventory

The first 50 entries were globally vote-sorted when collected. Entries 51–250 are verified current issues, but are not globally vote-sorted because the source query was rate-limited. Full machine-readable data is in [`issues-250.csv`](issues-250.csv).

| Rank | Selection | Project | Issue | Votes |
| ---: | --- | --- | --- | ---: |
| 1 | globally vote-sorted | mutter | [Separate workspaces on multiple monitors](https://gitlab.gnome.org/GNOME/mutter/-/work_items/37) | 207 |
| 2 | globally vote-sorted | nautilus | [Implement "Jump to file" feature (type ahead / type to seek)](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/1157) | 135 |
| 3 | globally vote-sorted | geary | [Unified inbox](https://gitlab.gnome.org/GNOME/geary/-/work_items/53) | 92 |
| 4 | globally vote-sorted | gnome-shell | [Ability to save screenshots to clipboard only (without saving to disk)](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/5208) | 84 |
| 5 | globally vote-sorted | geary | [Tracking: Transparent encryption and signing with GPG](https://gitlab.gnome.org/GNOME/geary/-/work_items/6) | 75 |
| 6 | globally vote-sorted | gnome-shell | [Top bar on all monitors](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/4603) | 71 |
| 7 | globally vote-sorted | gnome-control-center | [Ability to set scroll speed in system settings](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/379) | 71 |
| 8 | globally vote-sorted | geary | [Port to GTK4](https://gitlab.gnome.org/GNOME/geary/-/work_items/1212) | 70 |
| 9 | globally vote-sorted | gnome-shell | [Login controls not displayed on all screens](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/3867) | 67 |
| 10 | globally vote-sorted | gnome-shell | [Rework GNOME Shell's architecture to allow restarting under Wayland without crashing / taking down the spawned apps with it](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/5634) | 54 |
| 11 | globally vote-sorted | file-roller | [File Roller drag'n'drop extraction to Nautilus folder is broken](https://gitlab.gnome.org/GNOME/file-roller/-/work_items/4) | 53 |
| 12 | globally vote-sorted | gnome-software | [Quit when inactive](https://gitlab.gnome.org/GNOME/gnome-software/-/work_items/942) | 50 |
| 13 | globally vote-sorted | gnome-shell | [Wrong keyboard layout in lock screen](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/225) | 49 |
| 14 | globally vote-sorted | mutter | [Update for the Wayland tearing protocol](https://gitlab.gnome.org/GNOME/mutter/-/work_items/2517) | 48 |
| 15 | globally vote-sorted | geary | [Ability to "mark all emails as read"](https://gitlab.gnome.org/GNOME/geary/-/work_items/101) | 47 |
| 16 | globally vote-sorted | mutter | [Disable focus stealing prevention](https://gitlab.gnome.org/GNOME/mutter/-/work_items/673) | 46 |
| 17 | globally vote-sorted | gtk | [Selecting a folder to save to loses focus on file name](https://gitlab.gnome.org/GNOME/gtk/-/work_items/326) | 44 |
| 18 | globally vote-sorted | gnome-shell | [Blur semi-transparent backgrounds in some of GNOME Shell's UI components](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/1590) | 43 |
| 19 | globally vote-sorted | mutter | [Snap to top and bottom (edges) too](https://gitlab.gnome.org/GNOME/mutter/-/work_items/579) | 43 |
| 20 | globally vote-sorted | gnome-remote-desktop | [Remote desktop with locked local screen](https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/work_items/16) | 40 |
| 21 | globally vote-sorted | geary | [Allow sorting/grouping conversations in the list](https://gitlab.gnome.org/GNOME/geary/-/work_items/85) | 39 |
| 22 | globally vote-sorted | gnome-shell | [OSK needs (at least the option of) modifiers (Ctrl/Alt/Super)](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/181) | 39 |
| 23 | globally vote-sorted | Initiatives | [Port to GTK4](https://gitlab.gnome.org/GNOME/Initiatives/-/work_items/26) | 38 |
| 24 | globally vote-sorted | mutter | [Better Window Tiling](https://gitlab.gnome.org/GNOME/mutter/-/work_items/704) | 38 |
| 25 | globally vote-sorted | mutter | [color management: support scRGB](https://gitlab.gnome.org/GNOME/mutter/-/work_items/4083) | 36 |
| 26 | globally vote-sorted | gnome-control-center | [Add automatic and manual scheduling for light and dark theme switching](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/2060) | 36 |
| 27 | globally vote-sorted | gnome-control-center | [Add per-monitor min/max brightness settings](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/1209) | 36 |
| 28 | globally vote-sorted | gnome-extensions-app | [Extension installation?](https://gitlab.gnome.org/GNOME/gnome-extensions-app/-/work_items/6) | 35 |
| 29 | globally vote-sorted | gnome-shell | [An easy way to return the Application Grid positions to its default? (Gnome 3.38)](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/3180) | 35 |
| 30 | globally vote-sorted | gnome-online-accounts | [Cannot login to microsoft office365 "exchange" account with 2fa enabled](https://gitlab.gnome.org/GNOME/gnome-online-accounts/-/work_items/102) | 35 |
| 31 | globally vote-sorted | mutter | [Fractional Scaling Known issues and TODO](https://gitlab.gnome.org/GNOME/mutter/-/work_items/478) | 35 |
| 32 | globally vote-sorted | glib | ["Open with other application" will set selected application as default](https://gitlab.gnome.org/GNOME/glib/-/work_items/1026) | 35 |
| 33 | globally vote-sorted | libadwaita | [Recoloring API](https://gitlab.gnome.org/GNOME/libadwaita/-/work_items/53) | 34 |
| 34 | globally vote-sorted | seahorse | [Import of certificate with seahorse does not work; Import button stays disabled](https://gitlab.gnome.org/GNOME/seahorse/-/work_items/205) | 34 |
| 35 | globally vote-sorted | gnome-clocks | [Allow that alarms also beep when gnome-clocks is not running](https://gitlab.gnome.org/GNOME/gnome-clocks/-/work_items/1) | 34 |
| 36 | globally vote-sorted | gtk | [ListView scrolling sometimes jumps up and down when doing high-resolution scrolling](https://gitlab.gnome.org/GNOME/gtk/-/work_items/6344) | 33 |
| 37 | globally vote-sorted | console | [provide the option to change the default window size](https://gitlab.gnome.org/GNOME/console/-/work_items/140) | 32 |
| 38 | globally vote-sorted | gnome-shell | [App grid: Allow uninstalling apps](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/4752) | 32 |
| 39 | globally vote-sorted | gtk | [GTK 4 Spellcheck Support](https://gitlab.gnome.org/GNOME/gtk/-/work_items/3814) | 32 |
| 40 | globally vote-sorted | gnome-system-monitor | [Provide GPU and vRAM usage in the Resources tab's graphs and counters](https://gitlab.gnome.org/GNOME/gnome-system-monitor/-/work_items/62) | 32 |
| 41 | globally vote-sorted | nautilus | [Improve running binaries experience](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/443) | 32 |
| 42 | globally vote-sorted | mutter | [Mouse not being recorded when screencasting (Even when enabled)](https://gitlab.gnome.org/GNOME/mutter/-/work_items/3182) | 31 |
| 43 | globally vote-sorted | vte | [Add support for OSC 52](https://gitlab.gnome.org/GNOME/vte/-/work_items/2495) | 31 |
| 44 | globally vote-sorted | adwaita-icon-theme | [Include additional mimetype icons?](https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/work_items/24) | 31 |
| 45 | globally vote-sorted | gnome-shell | [[Feature] Blurred wallpaper as overview background](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/4307) | 30 |
| 46 | globally vote-sorted | nautilus | [Prompt rename automatically when a new file is created from template](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/524) | 30 |
| 47 | globally vote-sorted | gnome-shell | [Ability to record system audio in video screencasts](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/5524) | 29 |
| 48 | globally vote-sorted | gnome-calendar | [More flexible event recurrence UI (repeat every X number of days/weeks/months/years, specific days of the week or month, etc.)](https://gitlab.gnome.org/GNOME/gnome-calendar/-/work_items/272) | 29 |
| 49 | globally vote-sorted | gnome-software | [Can't zoom in on screenshots](https://gitlab.gnome.org/GNOME/gnome-software/-/work_items/313) | 29 |
| 50 | globally vote-sorted | gnome-control-center | [New design for fractional scaling setting](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/2516) | 28 |
| 51 | verified current selection; not globally vote-sorted | nautilus | ["Open in Console": choose which terminal application to open](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/2978) | 22 |
| 52 | verified current selection; not globally vote-sorted | gnome-control-center | [Default Apps: Add Terminal](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/3374) | 16 |
| 53 | verified current selection; not globally vote-sorted | vte | [Implementing the Kitty keyboard protocol](https://gitlab.gnome.org/GNOME/vte/-/work_items/2601) | 15 |
| 54 | verified current selection; not globally vote-sorted | gtk | [Cannot use keyboard shortcut Ctrl+Shift+N to create new folder on non-Latin keyboard layouts](https://gitlab.gnome.org/GNOME/gtk/-/work_items/5384) | 15 |
| 55 | verified current selection; not globally vote-sorted | gnome-bluetooth | [Allow editing device name for display](https://gitlab.gnome.org/GNOME/gnome-bluetooth/-/work_items/13) | 11 |
| 56 | verified current selection; not globally vote-sorted | gnome-calendar | [Ability to set / configure (or auto-remember) per-calendar default reminder alarm time delays, for newly created or imported ical events](https://gitlab.gnome.org/GNOME/gnome-calendar/-/work_items/98) | 10 |
| 57 | verified current selection; not globally vote-sorted | nautilus | [Use zst compression instead of xz](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/1936) | 9 |
| 58 | verified current selection; not globally vote-sorted | gnome-autoar | [Multiple threads support for (de)compression](https://gitlab.gnome.org/GNOME/gnome-autoar/-/work_items/29) | 7 |
| 59 | verified current selection; not globally vote-sorted | gnome-control-center | [Support image-based system updates](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/3773) | 7 |
| 60 | verified current selection; not globally vote-sorted | gnome-shell | [Keyboard layout changes when typing password on lock screen](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/8617) | 5 |
| 61 | verified current selection; not globally vote-sorted | papers | [Implement tile-based rendering (faster, multithreaded, lower memory usage, etc.)](https://gitlab.gnome.org/GNOME/papers/-/work_items/210) | 4 |
| 62 | verified current selection; not globally vote-sorted | mutter | [temporary low frame rate after wake from suspend](https://gitlab.gnome.org/GNOME/mutter/-/work_items/4022) | 4 |
| 63 | verified current selection; not globally vote-sorted | gnome-build-meta | [Move to dbus-broker](https://gitlab.gnome.org/GNOME/gnome-build-meta/-/work_items/709) | 3 |
| 64 | verified current selection; not globally vote-sorted | mutter | [Mutter on Wayland makes incorrect assumption about StartupNotify key in desktop entries](https://gitlab.gnome.org/GNOME/mutter/-/work_items/1330) | 3 |
| 65 | verified current selection; not globally vote-sorted | gnome-control-center | [gnome-control-center applications panel does not appear to be populating correctly.](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/3721) | 3 |
| 66 | verified current selection; not globally vote-sorted | gnome-shell | [notify-send with --app-name doesn't work, notifications are silenced](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9413) | 2 |
| 67 | verified current selection; not globally vote-sorted | gnome-software | [Update software repository settings UI](https://gitlab.gnome.org/GNOME/gnome-software/-/work_items/3000) | 2 |
| 68 | verified current selection; not globally vote-sorted | gnome-system-monitor | [Display swap usage per process](https://gitlab.gnome.org/GNOME/gnome-system-monitor/-/work_items/352) | 2 |
| 69 | verified current selection; not globally vote-sorted | gtk | [Sends too many text_input.enable() events](https://gitlab.gnome.org/GNOME/gtk/-/work_items/8349) | 2 |
| 70 | verified current selection; not globally vote-sorted | NetworkManager-openvpn | [nm-openvpn-service-openvpn-helper does not support new dns and resolve domain environment entry format (OpenVPN client 2.6+)](https://gitlab.gnome.org/GNOME/NetworkManager-openvpn/-/work_items/152) | 2 |
| 71 | verified current selection; not globally vote-sorted | gnome-calendar | [Adaptive event details dialog](https://gitlab.gnome.org/GNOME/gnome-calendar/-/work_items/1205) | 2 |
| 72 | verified current selection; not globally vote-sorted | gnome-keyring | [DBus race between gcr-prompter and gnome-shell internal prompter for unlocking keyring](https://gitlab.gnome.org/GNOME/gnome-keyring/-/work_items/176) | 2 |
| 73 | verified current selection; not globally vote-sorted | gnome-shell | [Bluetooth Quick Settings UX: too easy to accidentally disable bluetooth](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/8595) | 2 |
| 74 | verified current selection; not globally vote-sorted | gtk | [API to override the max number of items in a ListView](https://gitlab.gnome.org/GNOME/gtk/-/work_items/7824) | 2 |
| 75 | verified current selection; not globally vote-sorted | mutter | [VRR not applying uniformly to Wayland Native applications (Proton games)](https://gitlab.gnome.org/GNOME/mutter/-/work_items/4559) | 2 |
| 76 | verified current selection; not globally vote-sorted | gnome-build-meta | [no man pages in the base image](https://gitlab.gnome.org/GNOME/gnome-build-meta/-/work_items/1052) | 2 |
| 77 | verified current selection; not globally vote-sorted | gimp | [Fill and Stroke tools write alpha=0 instead of color on new layers (3.2.4)](https://gitlab.gnome.org/GNOME/gimp/-/work_items/16750) | 1 |
| 78 | verified current selection; not globally vote-sorted | gnome-control-center | [No way to map a touchpad to a single monitor](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/3517) | 1 |
| 79 | verified current selection; not globally vote-sorted | gimp | [Scanner doesn't remember export path](https://gitlab.gnome.org/GNOME/gimp/-/work_items/16273) | 1 |
| 80 | verified current selection; not globally vote-sorted | mutter | [Secondary GPU hot-add with already-connected monitors never triggers monitor reconfiguration](https://gitlab.gnome.org/GNOME/mutter/-/work_items/4617) | 1 |
| 81 | verified current selection; not globally vote-sorted | NetworkManager-openvpn | [nm-openvpn fails to clean up orphaned tun device and process on unclean VPN disconnect](https://gitlab.gnome.org/GNOME/NetworkManager-openvpn/-/work_items/168) | 1 |
| 82 | verified current selection; not globally vote-sorted | gnome-software | [Missing icons with gtk 4.23.4](https://gitlab.gnome.org/GNOME/gnome-software/-/work_items/3021) | 1 |
| 83 | verified current selection; not globally vote-sorted | citemplates | [opendir(/var/lib/flatpak/repo): No such file or directory](https://gitlab.gnome.org/GNOME/citemplates/-/work_items/49) | 1 |
| 84 | verified current selection; not globally vote-sorted | nautilus | [Nautilus not opening my terminal when clicking `Open in console`](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/3221) | 1 |
| 85 | verified current selection; not globally vote-sorted | nautilus | ["Open in Terminal" menu item has a different position from "Open in Console"](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/2446) | 1 |
| 86 | verified current selection; not globally vote-sorted | gdm | [RFE: Separate login and screen unlock PAM stacks](https://gitlab.gnome.org/GNOME/gdm/-/work_items/1098) | 1 |
| 87 | verified current selection; not globally vote-sorted | gnome-calendar | [Allow setting recurring events to occur on the "last day of the month" (28th, 29th, 30th, 31st day) automatically](https://gitlab.gnome.org/GNOME/gnome-calendar/-/work_items/938) | 1 |
| 88 | verified current selection; not globally vote-sorted | epiphany | [Empty OpenSearch XML crashes epiphany](https://gitlab.gnome.org/GNOME/epiphany/-/work_items/2954) | 1 |
| 89 | verified current selection; not globally vote-sorted | gimp | [Null pointer crash when painting in 3.0.2](https://gitlab.gnome.org/GNOME/gimp/-/work_items/13501) | 1 |
| 90 | verified current selection; not globally vote-sorted | calls | [Dial Pad tab fails to enable use of the SIP provider for a SIP test number](https://gitlab.gnome.org/GNOME/calls/-/work_items/705) | 1 |
| 91 | verified current selection; not globally vote-sorted | gnome-shell | [Optimize the GPU impact of accessibility zoom](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9398) | 1 |
| 92 | verified current selection; not globally vote-sorted | gnome-tweaks | [allow to use default systemd action for power button press, or add hybrid sleep to the drop-down list](https://gitlab.gnome.org/GNOME/gnome-tweaks/-/work_items/78) | 1 |
| 93 | verified current selection; not globally vote-sorted | xdg-desktop-portal-gnome | [Remote Desktop permission is not persisted for Steam Controller on Wayland](https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome/-/work_items/220) | 1 |
| 94 | verified current selection; not globally vote-sorted | gnome-shell | [My screencast gets fried when background blur is enabled](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9310) | 1 |
| 95 | verified current selection; not globally vote-sorted | gnome-build-meta | [Can't login because GDM tries to use fingerprint reader](https://gitlab.gnome.org/GNOME/gnome-build-meta/-/work_items/734) | 1 |
| 96 | verified current selection; not globally vote-sorted | mobile-broadband-provider-info | [Add support for 901 mcc](https://gitlab.gnome.org/GNOME/mobile-broadband-provider-info/-/work_items/34) | 1 |
| 97 | verified current selection; not globally vote-sorted | gnome-shell | [[Bug] Cursor themes not working in 51.beta](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9341) | 1 |
| 98 | verified current selection; not globally vote-sorted | mutter | [intermittent test failure in stacking tests: trying to create a negative-sized region](https://gitlab.gnome.org/GNOME/mutter/-/work_items/3633) | 1 |
| 99 | verified current selection; not globally vote-sorted | gimp | [file_save saves without EXIF](https://gitlab.gnome.org/GNOME/gimp/-/work_items/14166) | 1 |
| 100 | verified current selection; not globally vote-sorted | gimp | [Increase HEIF maximum image size limit on load](https://gitlab.gnome.org/GNOME/gimp/-/work_items/3867) | 1 |
| 101 | verified current selection; not globally vote-sorted | epiphany | [Autofill Fills CSS-Hidden Fields](https://gitlab.gnome.org/GNOME/epiphany/-/work_items/2951) | 1 |
| 102 | verified current selection; not globally vote-sorted | gnome-build-meta | [docs: improve the chapter-to-chapter flow of our book](https://gitlab.gnome.org/GNOME/gnome-build-meta/-/work_items/1300) | 1 |
| 103 | verified current selection; not globally vote-sorted | gnome-calendar | [Figure out what to display/expose to screen reader users](https://gitlab.gnome.org/GNOME/gnome-calendar/-/work_items/1634) | 1 |
| 104 | verified current selection; not globally vote-sorted | gtk | [Win32: cursor scale is truncated to an integer, doesn't match Windows' own 150%/175% cursor-size tier](https://gitlab.gnome.org/GNOME/gtk/-/work_items/8398) | 1 |
| 105 | verified current selection; not globally vote-sorted | gtk | [selecting an item immediately after scrolling to the top causes the view to jump back and forth](https://gitlab.gnome.org/GNOME/gtk/-/work_items/8391) | 1 |
| 106 | verified current selection; not globally vote-sorted | gnome-autoar | [Return value from signal handlers is lost in case of async API](https://gitlab.gnome.org/GNOME/gnome-autoar/-/work_items/42) | 0 |
| 107 | verified current selection; not globally vote-sorted | gnome-shell | [Run command dialog terminal discoverability and compatibility](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9412) | 0 |
| 108 | verified current selection; not globally vote-sorted | glycin | [glycin-svg spins at 100 % CPU forever when the loader's RLIMIT_AS is exhausted](https://gitlab.gnome.org/GNOME/glycin/-/work_items/322) | 0 |
| 109 | verified current selection; not globally vote-sorted | gtk | [this SVG file is not rendered](https://gitlab.gnome.org/GNOME/gtk/-/work_items/8410) | 0 |
| 110 | verified current selection; not globally vote-sorted | gweather-locations | [Missing city: Bardstown, KY](https://gitlab.gnome.org/GNOME/gweather-locations/-/work_items/63) | 0 |
| 111 | verified current selection; not globally vote-sorted | gnome-system-monitor | [Provide a "Copy process ID" action (in properties dialog, and right-click menu?)](https://gitlab.gnome.org/GNOME/gnome-system-monitor/-/work_items/377) | 0 |
| 112 | verified current selection; not globally vote-sorted | glib | [Unable to include glib.h inside an extern "C" block from C++ code](https://gitlab.gnome.org/GNOME/glib/-/work_items/4046) | 0 |
| 113 | verified current selection; not globally vote-sorted | gnome-shell | [Unable to extract shell extension](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/8567) | 0 |
| 114 | verified current selection; not globally vote-sorted | gimp | [Filters > Decor > Addborder  opacity is influenced by setting of brush opacity](https://gitlab.gnome.org/GNOME/gimp/-/work_items/16719) | 0 |
| 115 | verified current selection; not globally vote-sorted | epiphany | [Pango Markup Injection in Passwords dialog](https://gitlab.gnome.org/GNOME/epiphany/-/work_items/2956) | 0 |
| 116 | verified current selection; not globally vote-sorted | gimp | [TIFF with Position offset loaded incorrectly with "Open as Layers"](https://gitlab.gnome.org/GNOME/gimp/-/work_items/16756) | 0 |
| 117 | verified current selection; not globally vote-sorted | gnome-shell | [Ghost/duplicate window in overview after external monitor disconnect](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9382) | 0 |
| 118 | verified current selection; not globally vote-sorted | gimp | [Move to snapcraft9/core26 (with Chisel)](https://gitlab.gnome.org/GNOME/gimp/-/work_items/15744) | 0 |
| 119 | verified current selection; not globally vote-sorted | glycin | [Memory allocation fails on Buildservers with "Operation not permitted (os error 1)"](https://gitlab.gnome.org/GNOME/glycin/-/work_items/324) | 0 |
| 120 | verified current selection; not globally vote-sorted | papers | [Sidebar content hard to read due to the low contrast between the black (thin) text and the gray background](https://gitlab.gnome.org/GNOME/papers/-/work_items/749) | 0 |
| 121 | verified current selection; not globally vote-sorted | papers | [feature request: option to disable all link preview popups](https://gitlab.gnome.org/GNOME/papers/-/work_items/744) | 0 |
| 122 | verified current selection; not globally vote-sorted | gimp | [Spectral Blending Implementation Issues](https://gitlab.gnome.org/GNOME/gimp/-/work_items/16727) | 0 |
| 123 | verified current selection; not globally vote-sorted | papers | [Unlike Evince, Papers can't open from links auxiliary files in presentation mode](https://gitlab.gnome.org/GNOME/papers/-/work_items/745) | 0 |
| 124 | verified current selection; not globally vote-sorted | gimp | [Select by Colour doesn't work with some un-merged Colours filters.](https://gitlab.gnome.org/GNOME/gimp/-/work_items/16723) | 0 |
| 125 | verified current selection; not globally vote-sorted | gimp | [Image > Canvas Size does not work right when there are vector layers and groups involved](https://gitlab.gnome.org/GNOME/gimp/-/work_items/16736) | 0 |
| 126 | verified current selection; not globally vote-sorted | gnome-control-center | [text size settings panel and "Seeing" settings are inconsistent](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/3725) | 0 |
| 127 | verified current selection; not globally vote-sorted | gtk | [search-entry: Needs extra touch to show OSK although it has focus](https://gitlab.gnome.org/GNOME/gtk/-/work_items/8409) | 0 |
| 128 | verified current selection; not globally vote-sorted | libgtop | [procmap incorrectly reads shared_clean, shared_dirty, private_clean and private_dirty under latest Linux kernel's procfs](https://gitlab.gnome.org/GNOME/libgtop/-/work_items/70) | 0 |
| 129 | verified current selection; not globally vote-sorted | gimp | [Blank UI when launching on macOS](https://gitlab.gnome.org/GNOME/gimp/-/work_items/13203) | 0 |
| 130 | verified current selection; not globally vote-sorted | mutter | [SIGSEGV when resuming from s2idle on 51.rc](https://gitlab.gnome.org/GNOME/mutter/-/work_items/5042) | 0 |
| 131 | verified current selection; not globally vote-sorted | libsecret | [secret-tool: Couldn't create item: The secret was transferred or encrypted in an invalid way.](https://gitlab.gnome.org/GNOME/libsecret/-/work_items/115) | 0 |
| 132 | verified current selection; not globally vote-sorted | snapshot | [No top buttons on Pop OS 24.04 Cosmic](https://gitlab.gnome.org/GNOME/snapshot/-/work_items/371) | 0 |
| 133 | verified current selection; not globally vote-sorted | mutter | [Crash in `meta_wayland_tablet_update_sprite()` due to NULL `tablet`](https://gitlab.gnome.org/GNOME/mutter/-/work_items/5043) | 0 |
| 134 | verified current selection; not globally vote-sorted | gtk | [SVG animation yet playing within CSS background](https://gitlab.gnome.org/GNOME/gtk/-/work_items/8408) | 0 |
| 135 | verified current selection; not globally vote-sorted | gnome-control-center | ["Dim Screen" doesn't work in "Power Saver" mode](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/3812) | 0 |
| 136 | verified current selection; not globally vote-sorted | mutter | [Black screen on AMD Strix Halo (gfx1150 / DCN 3.5.1) — shadow buffer blit produces no output with atomic modesetting](https://gitlab.gnome.org/GNOME/mutter/-/work_items/4722) | 0 |
| 137 | verified current selection; not globally vote-sorted | gnome-boxes | [USB redirection gets stuck in an endless reset loop when the device is connected to a USB 3.0 (SuperSpeed) host port](https://gitlab.gnome.org/GNOME/gnome-boxes/-/work_items/1179) | 0 |
| 138 | verified current selection; not globally vote-sorted | epiphany | [WebExtension API crashes web process: strcmp(NULL) in on_send_message_finish](https://gitlab.gnome.org/GNOME/epiphany/-/work_items/2908) | 0 |
| 139 | verified current selection; not globally vote-sorted | gnome-remote-desktop | [Failed NLA reconnect leaves orphaned GDM greeter holding screen lock, blocking all subsequent logins](https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/work_items/318) | 0 |
| 140 | verified current selection; not globally vote-sorted | gnome-network-displays | [Crashes with LG webOS builtin chromecast receiver](https://gitlab.gnome.org/GNOME/gnome-network-displays/-/work_items/500) | 0 |
| 141 | verified current selection; not globally vote-sorted | geary | [`to_preview_text()` hangs at 100% CPU on very large email bodies due to unbounded `reduce_whitespace` input](https://gitlab.gnome.org/GNOME/geary/-/work_items/1712) | 0 |
| 142 | verified current selection; not globally vote-sorted | gnumeric | [Embedded images (JPEG/PNG) not displayed in Flatpak build (1.12.60/1.12.61, GNOME 49/50 runtime)](https://gitlab.gnome.org/GNOME/gnumeric/-/work_items/892) | 0 |
| 143 | verified current selection; not globally vote-sorted | mutter | [renderer/native: rebuild_views drops queued KMS updates without listener feedback, leaking the onscreen via a posted_frame ref cycle](https://gitlab.gnome.org/GNOME/mutter/-/work_items/4982) | 0 |
| 144 | verified current selection; not globally vote-sorted | meld | [macOS CI builds broken](https://gitlab.gnome.org/GNOME/meld/-/work_items/994) | 0 |
| 145 | verified current selection; not globally vote-sorted | mutter | [High GPU usage in 51.rc while the monitor is sleeping](https://gitlab.gnome.org/GNOME/mutter/-/work_items/5041) | 0 |
| 146 | verified current selection; not globally vote-sorted | gnome-maps | [contact info about iD presets](https://gitlab.gnome.org/GNOME/gnome-maps/-/work_items/1000) | 0 |
| 147 | verified current selection; not globally vote-sorted | gnote | [Plugin to remove broken links?](https://gitlab.gnome.org/GNOME/gnote/-/work_items/225) | 0 |
| 148 | verified current selection; not globally vote-sorted | libadwaita | [AdwSidebarItems only wraps when in `page` mode](https://gitlab.gnome.org/GNOME/libadwaita/-/work_items/1164) | 0 |
| 149 | verified current selection; not globally vote-sorted | gnome-settings-daemon | ["Performance mode temporarily disabled" appears mistakenly](https://gitlab.gnome.org/GNOME/gnome-settings-daemon/-/work_items/960) | 0 |
| 150 | verified current selection; not globally vote-sorted | gnome-settings-daemon | [Screen dims when Power Saver profile is enabled and "Dim Screen" is disabled](https://gitlab.gnome.org/GNOME/gnome-settings-daemon/-/work_items/888) | 0 |
| 151 | verified current selection; not globally vote-sorted | citemplates | [Add support for rust-nightly](https://gitlab.gnome.org/GNOME/citemplates/-/work_items/50) | 0 |
| 152 | verified current selection; not globally vote-sorted | gnome-keyring | [gdbusconnection.c:invoke_get_property_in_idle_cb assertion failure: error != NULL](https://gitlab.gnome.org/GNOME/gnome-keyring/-/work_items/195) | 0 |
| 153 | verified current selection; not globally vote-sorted | epiphany | [Mouse gestures are broken](https://gitlab.gnome.org/GNOME/epiphany/-/work_items/2955) | 0 |
| 154 | verified current selection; not globally vote-sorted | gtk | [gdk_surface_handle_event: SIGSEGV dereferencing surface in nautilus (GDK_SURFACE_IS_MAPPED, gdksurface.c:2993)](https://gitlab.gnome.org/GNOME/gtk/-/work_items/8368) | 0 |
| 155 | verified current selection; not globally vote-sorted | tinysparql | [Segfault in sqlite3VdbeExec (null VdbeCursor) during file-notifier cursor iteration](https://gitlab.gnome.org/GNOME/tinysparql/-/work_items/501) | 0 |
| 156 | verified current selection; not globally vote-sorted | mutter | [Clicking in Fedora installer (anaconda) sometimes doesn't work since 3f17e68 "clutter/frame-clock: Restrict ASAP dispatch in maybe_reschedule_update"](https://gitlab.gnome.org/GNOME/mutter/-/work_items/5033) | 0 |
| 157 | verified current selection; not globally vote-sorted | gnome-shell | [MprisSource/MprisPlayer SignalTracker leak on lock screen](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9410) | 0 |
| 158 | verified current selection; not globally vote-sorted | gtk | [GtkLabel: set_attributes() does not invalidate the rendered PangoLayout for labels set with set_markup(), once painted](https://gitlab.gnome.org/GNOME/gtk/-/work_items/8407) | 0 |
| 159 | verified current selection; not globally vote-sorted | nautilus | [Add fallback for "Open in Console"](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/3667) | 0 |
| 160 | verified current selection; not globally vote-sorted | gnome-control-center | [Fingerprint Enrollment UI Papercuts](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/3798) | 0 |
| 161 | verified current selection; not globally vote-sorted | shotwell | [Importing (to network drive) results in too many reads](https://gitlab.gnome.org/GNOME/shotwell/-/work_items/5195) | 0 |
| 162 | verified current selection; not globally vote-sorted | mutter | [Intermittent desktop stutter/lagginess for about 10 seconds after (re)boot or resume on Intel i915](https://gitlab.gnome.org/GNOME/mutter/-/work_items/5023) | 0 |
| 163 | verified current selection; not globally vote-sorted | epiphany | [Invalid OpenSearch url crashes epiphany](https://gitlab.gnome.org/GNOME/epiphany/-/work_items/2953) | 0 |
| 164 | verified current selection; not globally vote-sorted | nautilus | [Primary suggested "Replace" action button is not focused when the overwrite confirmation dialog appears](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/4321) | 0 |
| 165 | verified current selection; not globally vote-sorted | gdk-pixbuf | [(CVE-2026-18090) Heap out-of-bounds read in `uncompress()` in `gdk-pixbuf/io-icns.c`](https://gitlab.gnome.org/GNOME/gdk-pixbuf/-/issues/308) | 0 |
| 166 | verified current selection; not globally vote-sorted | libgnome-games-support | [Only create score dialog row widgets on setup](https://gitlab.gnome.org/GNOME/libgnome-games-support/-/work_items/41) | 0 |
| 167 | verified current selection; not globally vote-sorted | chronojump | [forceSensor capture from terminal (autonomous program)](https://gitlab.gnome.org/GNOME/chronojump/-/work_items/1274) | 0 |
| 168 | verified current selection; not globally vote-sorted | evolution | [MS 365 login using Intune fails](https://gitlab.gnome.org/GNOME/evolution/-/work_items/3389) | 0 |
| 169 | verified current selection; not globally vote-sorted | gnome-control-center | [Sound panel behaves incorrectly when selecting Bluetooth Handsfree device](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/3710) | 0 |
| 170 | verified current selection; not globally vote-sorted | libgnome-volume-control | [Drop workaround for pipewire/wireplumber creating additional, unselectable devices](https://gitlab.gnome.org/GNOME/libgnome-volume-control/-/work_items/36) | 0 |
| 171 | verified current selection; not globally vote-sorted | libgnome-volume-control | [Sound panel stays on "No Input Devices" when the default source is WirePlumber's port-less Bluetooth loopback (A2DP)](https://gitlab.gnome.org/GNOME/libgnome-volume-control/-/work_items/48) | 0 |
| 172 | verified current selection; not globally vote-sorted | libadwaita | [AdwPasswordEntryRow: the apply button sits before the suffix widgets](https://gitlab.gnome.org/GNOME/libadwaita/-/work_items/1159) | 0 |
| 173 | verified current selection; not globally vote-sorted | glycin | [(Non-root podman)-containerized native file dialog crashes when container is started with: --cap-add=PERFMON](https://gitlab.gnome.org/GNOME/glycin/-/work_items/325) | 0 |
| 174 | verified current selection; not globally vote-sorted | console | [Support the org.freedesktop.Terminal1 intent specification](https://gitlab.gnome.org/GNOME/console/-/work_items/461) | 0 |
| 175 | verified current selection; not globally vote-sorted | console | [xdg-terminal-exec support](https://gitlab.gnome.org/GNOME/console/-/work_items/384) | 0 |
| 176 | verified current selection; not globally vote-sorted | libmanette | [Global main context (GMainContext) dependency](https://gitlab.gnome.org/GNOME/libmanette/-/work_items/53) | 0 |
| 177 | verified current selection; not globally vote-sorted | gnome-settings-daemon | [Donation notification for particular campaigns](https://gitlab.gnome.org/GNOME/gnome-settings-daemon/-/work_items/953) | 0 |
| 178 | verified current selection; not globally vote-sorted | gnome-remote-desktop | [RDP remote login: mouse works in GDM, but sometimes stops working after login](https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/work_items/363) | 0 |
| 179 | verified current selection; not globally vote-sorted | gdm | [Unlocking logged-in sessions stuck at password prompt since 50.1](https://gitlab.gnome.org/GNOME/gdm/-/work_items/1093) | 0 |
| 180 | verified current selection; not globally vote-sorted | mutter | [After Microsoft Edge starts, the mouse cursor stays busy for about 15 seconds, then returns to normal.](https://gitlab.gnome.org/GNOME/mutter/-/work_items/4826) | 0 |
| 181 | verified current selection; not globally vote-sorted | epiphany | [Web app launched from GNOME Software crashes Epiphany](https://gitlab.gnome.org/GNOME/epiphany/-/work_items/1859) | 0 |
| 182 | verified current selection; not globally vote-sorted | gnome-connections | [F10 is intercepted by Connections and exits the active RDP display](https://gitlab.gnome.org/GNOME/gnome-connections/-/work_items/209) | 0 |
| 183 | verified current selection; not globally vote-sorted | gnome-connections | [Potential security issue: local clipboard content should not be indiscriminately sent to the server without the user's consent](https://gitlab.gnome.org/GNOME/gnome-connections/-/work_items/200) | 0 |
| 184 | verified current selection; not globally vote-sorted | gnome-connections | [High CPU usage when the remote host becomes unresponsive](https://gitlab.gnome.org/GNOME/gnome-connections/-/work_items/203) | 0 |
| 185 | verified current selection; not globally vote-sorted | gnome-connections | [RDP Session Terminates Instantly When Using Flatpak Connections](https://gitlab.gnome.org/GNOME/gnome-connections/-/work_items/206) | 0 |
| 186 | verified current selection; not globally vote-sorted | gnome-terminal | [Hamburger menu popover stuck when entering fullscreen on Wayland](https://gitlab.gnome.org/GNOME/gnome-terminal/-/work_items/8155) | 0 |
| 187 | verified current selection; not globally vote-sorted | mutter | [Mutter fails to adjust calibration of touchpanel upon resolution aspect ratio change](https://gitlab.gnome.org/GNOME/mutter/-/work_items/5040) | 0 |
| 188 | verified current selection; not globally vote-sorted | pygobject | [GLib.log_set_default_handler is not ported in the Python binding](https://gitlab.gnome.org/GNOME/pygobject/-/work_items/772) | 0 |
| 189 | verified current selection; not globally vote-sorted | pygobject | [GLib.LogField is serialized with values referenced as raw memory addresses instead of byte strings, hence it can not used from the Python code](https://gitlab.gnome.org/GNOME/pygobject/-/work_items/771) | 0 |
| 190 | verified current selection; not globally vote-sorted | librsvg | [Crash in downstream Cairo when rendering <text>](https://gitlab.gnome.org/GNOME/librsvg/-/work_items/1239) | 0 |
| 191 | verified current selection; not globally vote-sorted | gnome-shell | [Scrolling on quick settings volume slider with Bluetooth headphones connected sometimes results in volume jumping to completely different level](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9406) | 0 |
| 192 | verified current selection; not globally vote-sorted | glib | [(CVE-2026-86469) (#YWH-PGM9867-289) TOCTOU on GLib through g_file_replace() in gio/glocalfileoutputstream.c via G_FILE_CREATE_REPLACE_DESTINATION leads to Arbitrary File Overwrite](https://gitlab.gnome.org/GNOME/glib/-/work_items/4044) | 0 |
| 193 | verified current selection; not globally vote-sorted | nautilus | [Pressing ctrl+x (cut) on a file in Recents view should raise an error toast/notification](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/4273) | 0 |
| 194 | verified current selection; not globally vote-sorted | gnome-shell | [Padding is inconsistent](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9405) | 0 |
| 195 | verified current selection; not globally vote-sorted | meld | [slowdown while merging a change into another buffer in 3 way comparison](https://gitlab.gnome.org/GNOME/meld/-/work_items/993) | 0 |
| 196 | verified current selection; not globally vote-sorted | gnome-disk-utility | [Disk page looks awkward when no information is present](https://gitlab.gnome.org/GNOME/gnome-disk-utility/-/work_items/503) | 0 |
| 197 | verified current selection; not globally vote-sorted | gthumb | [Videos "Respect orientation" option is misleading](https://gitlab.gnome.org/GNOME/gthumb/-/work_items/410) | 0 |
| 198 | verified current selection; not globally vote-sorted | gnome-shell | [Shm leak during lock screen](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9403) | 0 |
| 199 | verified current selection; not globally vote-sorted | evolution-data-server | [PROCEDURE alarm argument injection bypassing the ATTACH allow-list](https://gitlab.gnome.org/GNOME/evolution-data-server/-/work_items/656) | 0 |
| 200 | verified current selection; not globally vote-sorted | gnome-shell | [App Grid icons loading delay](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9327) | 0 |
| 201 | verified current selection; not globally vote-sorted | gnome-shell | [AppFolderDialog leaks a changed::name GSettings handler → use-after-free crash on app install](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9384) | 0 |
| 202 | verified current selection; not globally vote-sorted | gnome-shell | [mpris.js: _updateState() is O(N²) in metadata size, stalling the compositor on large MPRIS Metadata](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9394) | 0 |
| 203 | verified current selection; not globally vote-sorted | gimp | [Actions path on Search popup (/) are not localized](https://gitlab.gnome.org/GNOME/gimp/-/work_items/16751) | 0 |
| 204 | verified current selection; not globally vote-sorted | gtk | [Nautilus "Open With" crashes with SIGSEGV in `cairo_font_options_copy`/`pango_fc_font_map_add` — PangoFcFontMap accessed from a GTask thread pool worker while rendering a symbolic icon](https://gitlab.gnome.org/GNOME/gtk/-/work_items/8295) | 0 |
| 205 | verified current selection; not globally vote-sorted | mutter | [Clipping of top bar when mouse pointer is on bottom of screen](https://gitlab.gnome.org/GNOME/mutter/-/work_items/4681) | 0 |
| 206 | verified current selection; not globally vote-sorted | pango | [Build fails with clang 23: -Werror=unused-but-set-variable now includes -Wunused-but-set-global](https://gitlab.gnome.org/GNOME/pango/-/work_items/900) | 0 |
| 207 | verified current selection; not globally vote-sorted | citemplates | [Update default-rules](https://gitlab.gnome.org/GNOME/citemplates/-/work_items/48) | 0 |
| 208 | verified current selection; not globally vote-sorted | gimp | [View->Shrink Wrap: erratic behavior with vertical images](https://gitlab.gnome.org/GNOME/gimp/-/work_items/16717) | 0 |
| 209 | verified current selection; not globally vote-sorted | mutter | [Crash when disabling external monitor in Settings](https://gitlab.gnome.org/GNOME/mutter/-/work_items/2718) | 0 |
| 210 | verified current selection; not globally vote-sorted | mutter | [[44, 45] fullscreen-maximize test case intermittently fails on ARM: Expected size 800x600 didn't match actual size 500x400](https://gitlab.gnome.org/GNOME/mutter/-/work_items/3050) | 0 |
| 211 | verified current selection; not globally vote-sorted | mutter | [Intermittent test failure: stacking/restore-size.metatest: 27: Expected size 300x200 didn't match actual size 500x400](https://gitlab.gnome.org/GNOME/mutter/-/work_items/2509) | 0 |
| 212 | verified current selection; not globally vote-sorted | mutter | [[44, 45] unfullscreen-strut-change test case intermittently fails on ARM: Expected size 800x600 didn't match actual size 500x400](https://gitlab.gnome.org/GNOME/mutter/-/work_items/3051) | 0 |
| 213 | verified current selection; not globally vote-sorted | mutter | [Clutter /grab/input-only test intermittently failing: assertion failed (expected[i].type == elem->type): (6 == 3)](https://gitlab.gnome.org/GNOME/mutter/-/work_items/3205) | 0 |
| 214 | verified current selection; not globally vote-sorted | gnome-shell-extensions | [Window List: Sometimes draws on top of fullscreen windows in an auto-hide way.](https://gitlab.gnome.org/GNOME/gnome-shell-extensions/-/work_items/598) | 0 |
| 215 | verified current selection; not globally vote-sorted | nautilus | [GTK4 Deprecations](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/2722) | 0 |
| 216 | verified current selection; not globally vote-sorted | libsoup | [(CVE-2026-85197) (#YWH-PGM9867-298) Heap UAF on SoupSession through on_data_read() in libsoup/http2/soup-client-message-io-http2.c via g_input_stream_read_async() in glib/gio/ginputstream.c with GOAWAY frame](https://gitlab.gnome.org/GNOME/libsoup/-/work_items/552) | 0 |
| 217 | verified current selection; not globally vote-sorted | gjs | [Free `GObject`s declared with the `using` keyword after end of scope](https://gitlab.gnome.org/GNOME/gjs/-/work_items/749) | 0 |
| 218 | verified current selection; not globally vote-sorted | gnome-settings-daemon | [Automatic Time Zone incorrectly changes America/Cancun to America/Mexico_City after every reboot in Cancun, Mexico](https://gitlab.gnome.org/GNOME/gnome-settings-daemon/-/work_items/952) | 0 |
| 219 | verified current selection; not globally vote-sorted | xdg-desktop-portal-gnome | [InputCapture reports version 0 on GNOME 50.0, despite full v1 backend support](https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome/-/work_items/225) | 0 |
| 220 | verified current selection; not globally vote-sorted | pygobject | [ASAN g_* reports leaks on pygobject info objects](https://gitlab.gnome.org/GNOME/pygobject/-/work_items/770) | 0 |
| 221 | verified current selection; not globally vote-sorted | libmks | [MksDisplay requests guest resolution in logical pixels, so the guest is upscaled and blurry under fractional scaling](https://gitlab.gnome.org/GNOME/libmks/-/work_items/22) | 0 |
| 222 | verified current selection; not globally vote-sorted | librsvg | [panic: Data storage buffer dimension mismatch](https://gitlab.gnome.org/GNOME/librsvg/-/work_items/1215) | 0 |
| 223 | verified current selection; not globally vote-sorted | librsvg | [Don't process data: URIs for images when fuzzing](https://gitlab.gnome.org/GNOME/librsvg/-/work_items/1238) | 0 |
| 224 | verified current selection; not globally vote-sorted | gtk | [GtkMenuButton not rendering SVG properly](https://gitlab.gnome.org/GNOME/gtk/-/work_items/8399) | 0 |
| 225 | verified current selection; not globally vote-sorted | baobab | [Is a non-GIO (e.g. POSIX) fast path acceptable for this utility? Is there an AI usage policy?](https://gitlab.gnome.org/GNOME/baobab/-/work_items/242) | 0 |
| 226 | verified current selection; not globally vote-sorted | mutter | [non-deterministic test failures](https://gitlab.gnome.org/GNOME/mutter/-/work_items/4035) | 0 |
| 227 | verified current selection; not globally vote-sorted | gnome-calendar | ["Event deleted" GtkOverlay message is announced by Orca only as it is about to disappear, as focus defaults to the sidebar togglebutton which gets read first](https://gitlab.gnome.org/GNOME/gnome-calendar/-/work_items/1454) | 0 |
| 228 | verified current selection; not globally vote-sorted | mutter | [wayland-unit test is flaky](https://gitlab.gnome.org/GNOME/mutter/-/work_items/4711) | 0 |
| 229 | verified current selection; not globally vote-sorted | gimp | [Color picker reports old value on same location across layers with alpha enabled](https://gitlab.gnome.org/GNOME/gimp/-/work_items/15742) | 0 |
| 230 | verified current selection; not globally vote-sorted | gimp | [The clipboard pattern and brush are the image size and not the copied layer size.](https://gitlab.gnome.org/GNOME/gimp/-/work_items/16104) | 0 |
| 231 | verified current selection; not globally vote-sorted | gimp | [Separator hover state gets stuck after click away from popup/context menu](https://gitlab.gnome.org/GNOME/gimp/-/work_items/15867) | 0 |
| 232 | verified current selection; not globally vote-sorted | gimp | [Incorrect Histogram Arithmetic Mean Values](https://gitlab.gnome.org/GNOME/gimp/-/work_items/4332) | 0 |
| 233 | verified current selection; not globally vote-sorted | gimp | [Raw float image loader ignores endian](https://gitlab.gnome.org/GNOME/gimp/-/work_items/15595) | 0 |
| 234 | verified current selection; not globally vote-sorted | mutter | [map-after-headless test fails randomly](https://gitlab.gnome.org/GNOME/mutter/-/work_items/5030) | 0 |
| 235 | verified current selection; not globally vote-sorted | gimp | [Text tool: Non-zero (negative) kerning is broken](https://gitlab.gnome.org/GNOME/gimp/-/work_items/5673) | 0 |
| 236 | verified current selection; not globally vote-sorted | gnome-shell | [Sound and window management bugs.](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9402) | 0 |
| 237 | verified current selection; not globally vote-sorted | libsoup | [Cannot load goodhousekeeping.com: Unexpected state changed READ_DATA -> READ_DATA_START, expected to be from READ_HEADERS](https://gitlab.gnome.org/GNOME/libsoup/-/work_items/555) | 0 |
| 238 | verified current selection; not globally vote-sorted | gnome-control-center | [Previewing a custom keyboard layout from Settings doesn't work](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/3756) | 0 |
| 239 | verified current selection; not globally vote-sorted | gtk | [build: reenable macos-arm64 when the runner is fixed](https://gitlab.gnome.org/GNOME/gtk/-/work_items/8401) | 0 |
| 240 | verified current selection; not globally vote-sorted | mutter | [Per-user/per-session selection of primary GPU](https://gitlab.gnome.org/GNOME/mutter/-/work_items/5037) | 0 |
| 241 | verified current selection; not globally vote-sorted | gnome-characters | [Wrong number of result metas returned by search provider](https://gitlab.gnome.org/GNOME/gnome-characters/-/work_items/187) | 0 |
| 242 | verified current selection; not globally vote-sorted | gimp | [Changing the visibility of an un-merged filter is omitted from the undo history.](https://gitlab.gnome.org/GNOME/gimp/-/work_items/16163) | 0 |
| 243 | verified current selection; not globally vote-sorted | vte | [Long IME preedit text is clipped instead of wrapped](https://gitlab.gnome.org/GNOME/vte/-/work_items/2962) | 0 |
| 244 | verified current selection; not globally vote-sorted | gnome-disk-utility | [[Bug] Drives on sidebar do not always refresh for loop devices](https://gitlab.gnome.org/GNOME/gnome-disk-utility/-/work_items/496) | 0 |
| 245 | verified current selection; not globally vote-sorted | libxml2 | [regexp: Remaining issues with character ranges and escapes](https://gitlab.gnome.org/GNOME/libxml2/-/work_items/1103) | 0 |
| 246 | verified current selection; not globally vote-sorted | gdk-pixbuf | [Four memory bugs found in gdk-pixbuf with PoCs](https://gitlab.gnome.org/GNOME/gdk-pixbuf/-/work_items/314) | 0 |
| 247 | verified current selection; not globally vote-sorted | gnome-control-center | [graphics tablets: Tablet rotation no longer affecting touch](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/3804) | 0 |
| 248 | verified current selection; not globally vote-sorted | gimp | [GIMP should support SpaceNavigator / 3D Xinput devices](https://gitlab.gnome.org/GNOME/gimp/-/work_items/1050) | 0 |
| 249 | verified current selection; not globally vote-sorted | gimp | [GeoTiff file opens only in b/w and not in grayscale (due to tags not being read)](https://gitlab.gnome.org/GNOME/gimp/-/work_items/9691) | 0 |
| 250 | verified current selection; not globally vote-sorted | evince | [Unimplemented annotation: POPPLER_ANNOT_SCREEN](https://gitlab.gnome.org/GNOME/evince/-/work_items/35) | 0 |

## Archived Contribution Series

Each series is stored below `patches/` and can be applied locally with `git am`. The exact source repository, base revision, tip commit, and patch filenames are in [`PATCHES.json`](PATCHES.json) and in the series-local `METADATA.json`.

| Project | Branch | Commits | Archive |
| --- | --- | ---: | --- |
| console | `xdg-terminal-exec` | 1 | [`default-window-size`](patches/console/default-window-size) |
| console | `xdg-terminal-exec` | 2 | [`xdg-terminal-exec`](patches/console/xdg-terminal-exec) |
| epiphany | `webextension-null-message` | 1 | [`webextension-null-message`](patches/epiphany/webextension-null-message) |
| gdk-pixbuf | `icns-rle-bounds` | 1 | [`icns-rle-bounds`](patches/gdk-pixbuf/icns-rle-bounds) |
| geary | `preview-text-input-limit` | 6 | [`preview-text-input-limit`](patches/geary/preview-text-input-limit) |
| gimp | `addborder-opacity` | 1 | [`addborder-opacity`](patches/gimp/addborder-opacity) |
| gimp | `fix-action-search-localized-menu-path` | 1 | [`fix-action-search-localized-menu-path`](patches/gimp/fix-action-search-localized-menu-path) |
| gimp | `fix-color-picker-exact-samples` | 3 | [`fix-color-picker-exact-samples`](patches/gimp/fix-color-picker-exact-samples) |
| gimp | `fix-raw-float-endianness` | 1 | [`fix-raw-float-endianness`](patches/gimp/fix-raw-float-endianness) |
| gnome-autoar | `async-signal-return` | 1 | [`async-signal-return`](patches/gnome-autoar/async-signal-return) |
| gnome-bluetooth | `master` | 1 | [`device-alias`](patches/gnome-bluetooth/device-alias) |
| gnome-calendar | `main` | 1 | [`default-reminders`](patches/gnome-calendar/default-reminders) |
| gnome-calendar | `main` | 1 | [`recurrence-interval`](patches/gnome-calendar/recurrence-interval) |
| gnome-characters | `fix-search-result-metas` | 1 | [`fix-search-result-metas`](patches/gnome-characters/fix-search-result-metas) |
| gnome-clocks | `master` | 1 | [`background-alarms`](patches/gnome-clocks/background-alarms) |
| gnome-connections | `rdp-pass-f10` | 1 | [`rdp-pass-f10`](patches/gnome-connections/rdp-pass-f10) |
| gnome-control-center | `feature-default-terminal` | 2 | [`feature-default-terminal`](patches/gnome-control-center/feature-default-terminal) |
| gnome-control-center | `fix-about-arm-cpu-info` | 2 | [`fix-about-arm-cpu-info`](patches/gnome-control-center/fix-about-arm-cpu-info) |
| gnome-control-center | `fix-global-shortcuts-wayland-shutdown` | 1 | [`fix-global-shortcuts-wayland-shutdown`](patches/gnome-control-center/fix-global-shortcuts-wayland-shutdown) |
| gnome-control-center | `fix-input-level-source` | 1 | [`fix-input-level-source`](patches/gnome-control-center/fix-input-level-source) |
| gnome-control-center | `fix-sound-preserve-configured-sink` | 1 | [`fix-sound-preserve-configured-sink`](patches/gnome-control-center/fix-sound-preserve-configured-sink) |
| gnome-control-center | `fix-wwan-unspecified-sim` | 1 | [`fix-wwan-unspecified-sim`](patches/gnome-control-center/fix-wwan-unspecified-sim) |
| gnome-network-displays | `ctrl-close-reentrancy` | 2 | [`ctrl-close-reentrancy`](patches/gnome-network-displays/ctrl-close-reentrancy) |
| gnome-settings-daemon | `fix-power-saver-idle-dim` | 2 | [`fix-power-saver-idle-dim`](patches/gnome-settings-daemon/fix-power-saver-idle-dim) |
| gnome-shell | `app-folder-dialog-signal-cleanup` | 1 | [`app-folder-dialog-signal-cleanup`](patches/gnome-shell/app-folder-dialog-signal-cleanup) |
| gnome-shell | `mpris-cleanup-isolated` | 1 | [`mpris-cleanup-isolated`](patches/gnome-shell/mpris-cleanup-isolated) |
| gnome-shell | `mpris-metadata-unpack` | 1 | [`mpris-metadata-unpack`](patches/gnome-shell/mpris-metadata-unpack) |
| gnome-shell | `notification-sender-grace` | 1 | [`notification-sender-grace`](patches/gnome-shell/notification-sender-grace) |
| gnome-shell | `work/screenshot-recent-files-fix` | 1 | [`work-screenshot-recent-files-fix`](patches/gnome-shell/work-screenshot-recent-files-fix) |
| gnome-shell | `work/screenshot-save-to-disk` | 1 | [`work-screenshot-save-to-disk`](patches/gnome-shell/work-screenshot-save-to-disk) |
| gnome-software | `main` | 1 | [`screenshot-zoom`](patches/gnome-software/screenshot-zoom) |
| gnome-terminal | `fix-fullscreen-menu-popover` | 1 | [`fix-fullscreen-menu-popover`](patches/gnome-terminal/fix-fullscreen-menu-popover) |
| gthumb | `clarify-video-orientation` | 1 | [`clarify-video-orientation`](patches/gthumb/clarify-video-orientation) |
| gtk | `avoid-svg-preload` | 1 | [`avoid-svg-preload`](patches/gtk/avoid-svg-preload) |
| gtk-frdp | `close-on-event-check-failure` | 1 | [`close-on-event-check-failure`](patches/gtk-frdp/close-on-event-check-failure) |
| libadwaita | `entry-row-apply-after-suffix` | 1 | [`entry-row-apply-after-suffix`](patches/libadwaita/entry-row-apply-after-suffix) |
| libgnome-games-support | `fix-score-dialog-row-factory` | 1 | [`fix-score-dialog-row-factory`](patches/libgnome-games-support/fix-score-dialog-row-factory) |
| libgnome-volume-control | `fix-recording-level-source` | 1 | [`fix-recording-level-source`](patches/libgnome-volume-control/fix-recording-level-source) |
| gnome-system-monitor | `main` | 1 | [`process-swap`](patches/gnome-system-monitor/process-swap) |
| libgtop | `procmap-smaps-values` | 2 | [`procmap-smaps-values`](patches/libgtop/procmap-smaps-values) |
| libgtop | `work/gpu-metrics-port` | 2 | [`work-gpu-metrics-port`](patches/libgtop/work-gpu-metrics-port) |
| libmanette | `thread-main-context` | 1 | [`thread-main-context`](patches/libmanette/thread-main-context) |
| nautilus | `compression-tar-zstd` | 1 | [`compression-tar-zstd`](patches/nautilus/compression-tar-zstd) |
| nautilus | `cut-recent-feedback` | 1 | [`cut-recent-feedback`](patches/nautilus/cut-recent-feedback) |
| nautilus | `focus-conflict-replace` | 1 | [`focus-conflict-replace`](patches/nautilus/focus-conflict-replace) |
| nautilus | `compression-tar-zstd` | 1 | [`rename-template-file`](patches/nautilus/rename-template-file) |
| NetworkManager-openvpn | `ci-const-correctness` | 1 | [`ci-const-correctness`](patches/NetworkManager-openvpn/ci-const-correctness) |
| NetworkManager-openvpn | `openvpn-2-6-dns-options` | 1 | [`openvpn-2-6-dns-options`](patches/NetworkManager-openvpn/openvpn-2-6-dns-options) |
| pango | `ci-windows-fontconfig` | 1 | [`ci-windows-fontconfig`](patches/pango/ci-windows-fontconfig) |
| pango | `clang23-unused-global` | 3 | [`clang23-unused-global`](patches/pango/clang23-unused-global) |
| seahorse | `main` | 1 | [`importable-items`](patches/seahorse/importable-items) |
| shotwell | `prepare-before-copy` | 1 | [`prepare-before-copy`](patches/shotwell/prepare-before-copy) |
| xdg-desktop-portal-gnome | `fix-input-capture-version-50` | 1 | [`fix-input-capture-version-50`](patches/xdg-desktop-portal-gnome/fix-input-capture-version-50) |

## Known Dependencies and Follow-up

- The GNOME Control Center recording-level patch depends on the accompanying libgnome-volume-control API patch.
- The Power Saver patch includes a regression test that fails against the previous behaviour and passes with the fix.
- The source repositories are referenced only for compatible local bases and investigation. GNOMEAI does not make GNOME or GitLab submissions.
