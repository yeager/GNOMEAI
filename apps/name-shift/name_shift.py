#!/usr/bin/env python3
"""A local GTK 4 batch rename utility with an explicit preview."""
from __future__ import annotations
import sys
from pathlib import Path
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gio, Gtk
sys.path.insert(0, str(Path(__file__).parent))
import renamer

class NameShift(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id='io.github.yeager.NameShift', flags=Gio.ApplicationFlags.HANDLES_OPEN)
        self.paths: list[Path] = []
        self.plans: list[renamer.Preview] = []

    def do_open(self, files: list[Gio.File], _count: int, _hint: str) -> None:
        self.paths = [Path(file.get_path()) for file in files if file.get_path()]
        self.activate()

    def do_activate(self) -> None:
        if self.props.active_window:
            self.props.active_window.present(); return
        self.window = Gtk.ApplicationWindow(application=self, title='Name Shift')
        self.window.set_default_size(760, 540)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12,
                      margin_top=18, margin_bottom=18, margin_start=18, margin_end=18)
        title = Gtk.Label(label='Preview file names before changing them', xalign=0,
                          css_classes=['title-2'])
        box.append(title)
        grid = Gtk.Grid(column_spacing=8, row_spacing=8)
        self.find = self._entry('Find in name')
        self.replace = self._entry('Replace with')
        self.prefix = self._entry('Prefix')
        self.suffix = self._entry('Suffix')
        for row, (label, entry) in enumerate((('Find', self.find), ('Replace', self.replace),
                                               ('Prefix', self.prefix), ('Suffix', self.suffix))):
            grid.attach(Gtk.Label(label=label, xalign=1), 0, row, 1, 1)
            grid.attach(entry, 1, row, 1, 1)
        choose = Gtk.Button(label='Choose files…')
        choose.connect('clicked', self._choose)
        grid.attach(choose, 2, 0, 1, 2)
        box.append(grid)
        self.status = Gtk.Label(label='Choose one or more files to begin.', xalign=0)
        box.append(self.status)
        self.list_box = Gtk.ListBox(selection_mode=Gtk.SelectionMode.NONE, vexpand=True)
        scroll = Gtk.ScrolledWindow(vexpand=True)
        scroll.set_child(self.list_box)
        box.append(scroll)
        controls = Gtk.Box(spacing=8, halign=Gtk.Align.END)
        clear = Gtk.Button(label='Clear')
        clear.connect('clicked', self._clear)
        self.apply_button = Gtk.Button(label='Rename files')
        self.apply_button.add_css_class('suggested-action')
        self.apply_button.connect('clicked', self._apply)
        controls.append(clear); controls.append(self.apply_button); box.append(controls)
        self.window.set_child(box); self._refresh(); self.window.present()

    def _entry(self, placeholder: str) -> Gtk.Entry:
        entry = Gtk.Entry(placeholder_text=placeholder)
        entry.connect('changed', lambda *_: self._refresh())
        return entry

    def _choose(self, *_args: object) -> None:
        dialog = Gtk.FileDialog(title='Choose files')
        dialog.open_multiple(self.window, None, self._chosen)

    def _chosen(self, dialog: Gtk.FileDialog, result: Gio.AsyncResult) -> None:
        try:
            files = dialog.open_multiple_finish(result)
        except Exception:
            return
        self.paths = [Path(file.get_path()) for file in files if file.get_path()]
        self._refresh()

    def _clear(self, *_args: object) -> None:
        self.paths = []; self._refresh()

    def _refresh(self) -> None:
        if hasattr(self, 'find'):
            self.plans = renamer.preview(self.paths, self.find.get_text(), self.replace.get_text(),
                                         self.prefix.get_text(), self.suffix.get_text())
        while child := self.list_box.get_first_child(): self.list_box.remove(child)
        for plan in self.plans:
            row = Gtk.Box(spacing=12, margin_top=6, margin_bottom=6, margin_start=8, margin_end=8)
            row.append(Gtk.Label(label=plan.source.name, xalign=0, hexpand=True, ellipsize=3))
            row.append(Gtk.Label(label='→'))
            target = Gtk.Label(label=plan.target.name, xalign=0, hexpand=True, ellipsize=3)
            if plan.error: target.add_css_class('error')
            row.append(target)
            if plan.error: row.append(Gtk.Label(label=plan.error, xalign=0, css_classes=['error']))
            self.list_box.append(row)
        valid = bool(self.plans) and not any(plan.error for plan in self.plans)
        self.apply_button.set_sensitive(valid)
        if not self.paths: self.status.set_text('Choose one or more files to begin.')
        elif valid: self.status.set_text(f'{len(self.plans)} file names are ready to change.')
        else: self.status.set_text('Resolve the highlighted name conflicts before renaming.')

    def _apply(self, *_args: object) -> None:
        try:
            self.paths = renamer.apply(self.plans)
        except (OSError, ValueError) as error:
            self.status.set_text(f'Rename failed: {error}')
            return
        self.status.set_text('Files renamed. The preview now shows their current names.')
        self._refresh()

if __name__ == '__main__':
    raise SystemExit(NameShift().run(sys.argv))
