#!/usr/bin/env python3
"""A manual, local clipboard shelf for GNOME."""

from __future__ import annotations

import sys
from pathlib import Path

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gdk, Gio, Gtk

sys.path.insert(0, str(Path(__file__).parent))
import store


class ClipShelf(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id="io.github.yeager.ClipShelf")
        self.items = store.load()
        self.list_box = Gtk.ListBox()
        self.list_box.set_selection_mode(Gtk.SelectionMode.SINGLE)
        self.list_box.connect("row-selected", self._selection_changed)
        self.copy_button = Gtk.Button(label="Copy selected")
        self.copy_button.set_sensitive(False)
        self.copy_button.connect("clicked", self._copy_selected)
        self.delete_button = Gtk.Button(label="Delete selected")
        self.delete_button.set_sensitive(False)
        self.delete_button.connect("clicked", self._delete_selected)

    def do_activate(self) -> None:
        window = self.props.active_window
        if window:
            window.present()
            return
        window = Gtk.ApplicationWindow(application=self, title="Clip Shelf")
        window.set_default_size(620, 480)
        header = Gtk.HeaderBar()
        capture = Gtk.Button(label="Capture clipboard")
        capture.connect("clicked", self._capture)
        header.pack_start(capture)
        header.pack_end(self.copy_button)
        header.pack_end(self.delete_button)
        window.set_titlebar(header)
        scroll = Gtk.ScrolledWindow(vexpand=True)
        scroll.set_child(self.list_box)
        window.set_child(scroll)
        self._render()
        window.present()

    def _render(self) -> None:
        while row := self.list_box.get_first_child():
            self.list_box.remove(row)
        for item in self.items:
            label = Gtk.Label(label=item, wrap=True, wrap_mode=2, xalign=0)
            label.set_margin_top(9)
            label.set_margin_bottom(9)
            label.set_margin_start(12)
            label.set_margin_end(12)
            self.list_box.append(label)

    def _selected_index(self) -> int | None:
        row = self.list_box.get_selected_row()
        return row.get_index() if row else None

    def _selection_changed(self, *_args: object) -> None:
        has_selection = self._selected_index() is not None
        self.copy_button.set_sensitive(has_selection)
        self.delete_button.set_sensitive(has_selection)

    def _capture(self, *_args: object) -> None:
        clipboard = Gdk.Display.get_default().get_clipboard()
        clipboard.read_text_async(None, self._captured)

    def _captured(self, clipboard: Gdk.Clipboard, result: Gio.AsyncResult) -> None:
        try:
            text = clipboard.read_text_finish(result)
        except Exception:
            return
        if not text:
            return
        self.items = store.prepend(text, self.items)
        self._render()

    def _copy_selected(self, *_args: object) -> None:
        index = self._selected_index()
        if index is not None:
            Gdk.Display.get_default().get_clipboard().set_text(self.items[index])

    def _delete_selected(self, *_args: object) -> None:
        index = self._selected_index()
        if index is None:
            return
        self.items.pop(index)
        self.items = store.save(self.items)
        self._render()


if __name__ == "__main__":
    raise SystemExit(ClipShelf().run(sys.argv))
