#!/usr/bin/env python3
"""A local focus and break timer for GTK 4."""
from __future__ import annotations
import sys
from pathlib import Path
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import GLib, Gtk
sys.path.insert(0, str(Path(__file__).parent))
import store


class FocusBlock(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id='io.github.yeager.FocusBlock')
        self.settings = store.load()
        self.remaining = self.settings['focus_minutes'] * 60
        self.running = False
        self.break_mode = False
        self.timer_id: int | None = None

    def do_activate(self) -> None:
        if self.props.active_window:
            self.props.active_window.present()
            return
        self.window = Gtk.ApplicationWindow(application=self, title='Focus Block')
        self.window.set_default_size(360, 240)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12,
                      margin_top=24, margin_bottom=24, margin_start=24, margin_end=24)
        self.phase = Gtk.Label(label='Focus', css_classes=['title-2'])
        self.countdown = Gtk.Label(css_classes=['title-1'])
        self.focus = Gtk.SpinButton.new_with_range(1, 240, 1)
        self.focus.set_value(self.settings['focus_minutes'])
        self.break_length = Gtk.SpinButton.new_with_range(1, 240, 1)
        self.break_length.set_value(self.settings['break_minutes'])
        grid = Gtk.Grid(column_spacing=12, row_spacing=8)
        grid.attach(Gtk.Label(label='Focus minutes', xalign=0), 0, 0, 1, 1)
        grid.attach(self.focus, 1, 0, 1, 1)
        grid.attach(Gtk.Label(label='Break minutes', xalign=0), 0, 1, 1, 1)
        grid.attach(self.break_length, 1, 1, 1, 1)
        controls = Gtk.Box(spacing=8, halign=Gtk.Align.CENTER)
        self.start = Gtk.Button(label='Start')
        self.start.connect('clicked', self._toggle)
        reset = Gtk.Button(label='Reset')
        reset.connect('clicked', self._reset)
        controls.append(self.start)
        controls.append(reset)
        for child in (self.phase, self.countdown, grid, controls):
            box.append(child)
        self.window.set_child(box)
        self._render()
        self.window.present()

    def _duration(self) -> int:
        return int((self.break_length if self.break_mode else self.focus).get_value()) * 60

    def _render(self) -> None:
        self.phase.set_label('Break' if self.break_mode else 'Focus')
        minutes, seconds = divmod(max(self.remaining, 0), 60)
        self.countdown.set_label(f'{minutes:02d}:{seconds:02d}')
        self.start.set_label('Pause' if self.running else 'Start')

    def _toggle(self, *_args: object) -> None:
        self.running = not self.running
        if self.running and self.timer_id is None:
            self.timer_id = GLib.timeout_add_seconds(1, self._tick)
        self._render()

    def _tick(self) -> bool:
        if not self.running:
            self.timer_id = None
            return False
        self.remaining -= 1
        if self.remaining <= 0:
            self.break_mode = not self.break_mode
            self.remaining = self._duration()
            self.send_notification('focus-block-complete', GLib.Notification.new('Break started' if self.break_mode else 'Focus started'))
        self._render()
        return True

    def _reset(self, *_args: object) -> None:
        self.settings = store.save({'focus_minutes': int(self.focus.get_value()), 'break_minutes': int(self.break_length.get_value())})
        self.break_mode = False
        self.remaining = self.settings['focus_minutes'] * 60
        self._render()


if __name__ == '__main__':
    raise SystemExit(FocusBlock().run(sys.argv))
