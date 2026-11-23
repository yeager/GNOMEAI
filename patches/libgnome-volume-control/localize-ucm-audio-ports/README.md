# Localize generic UCM audio ports

The UCM port descriptions `Speaker` and `Headphones` are exposed verbatim by PipeWire. Localize these two descriptions only when the UCM port name and the PulseAudio port type also match. Preserve custom descriptions, unknown ports, numbered devices and microphone labels.

The three companion patches add Swedish translations to GNOME Shell, Settings Daemon and Control Center. Settings Daemon also needs the GVC source in its gettext input list. Each consumer must update its GVC subproject to the patched revision when integrating these changes; updating translations alone does not change the display.

Validation: built the GVC subproject with its Meson CI harness and ran its new port-label test, including exact matches and custom/mismatched/null cases. All three Swedish catalogs pass `msgfmt --check`, and gettext resolves both labels to `Högtalare` and `Hörlurar`. The installed GNOME session has not been rebuilt or tested with this patch.

Related existing GNOME issue: https://gitlab.gnome.org/GNOME/libgnome-volume-control/-/issues/29
