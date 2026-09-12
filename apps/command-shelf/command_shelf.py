#!/usr/bin/env python3
"""A local GTK 4 shelf for named command snippets."""
from __future__ import annotations
import sys
from pathlib import Path
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gdk, Gtk
sys.path.insert(0, str(Path(__file__).parent))
import store


class CommandShelf(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id='io.github.yeager.CommandShelf')
        self.items = store.load()

    def do_activate(self) -> None:
        if self.props.active_window:
            self.props.active_window.present()
            return
        self.window = Gtk.ApplicationWindow(application=self, title='Command Shelf')
        self.window.set_default_size(680, 480)
        root = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12,
                       margin_top=12, margin_bottom=12, margin_start=12, margin_end=12)
        form = Gtk.Grid(column_spacing=8, row_spacing=8)
        self.name = Gtk.Entry(placeholder_text='Name')
        self.command = Gtk.Entry(placeholder_text='Command')
        add = Gtk.Button(label='Save command')
        add.connect('clicked', self._add)
        form.attach(self.name, 0, 0, 1, 1)
        form.attach(self.command, 1, 0, 1, 1)
        form.attach(add, 2, 0, 1, 1)
        self.list_box = Gtk.ListBox(selection_mode=Gtk.SelectionMode.SINGLE, vexpand=True)
        self.list_box.connect('row-selected', self._selection_changed)
        scroll = Gtk.ScrolledWindow(vexpand=True)
        scroll.set_child(self.list_box)
        controls = Gtk.Box(spacing=8, halign=Gtk.Align.END)
        self.copy = Gtk.Button(label='Copy selected')
        self.copy.connect('clicked', self._copy)
        self.delete = Gtk.Button(label='Delete selected')
        self.delete.connect('clicked', self._delete)
        controls.append(self.copy)
        controls.append(self.delete)
        root.append(form)
        root.append(scroll)
        root.append(controls)
        self.window.set_child(root)
        self._render()
        self._selection_changed()
        self.window.present()

    def _render(self) -> None:
        while child := self.list_box.get_first_child():
            self.list_box.remove(child)
        for item in self.items:
            row = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3,
                          margin_top=8, margin_bottom=8, margin_start=12, margin_end=12)
            row.append(Gtk.Label(label=item['name'], xalign=0, css_classes=['heading']))
            row.append(Gtk.Label(label=item['command'], xalign=0, selectable=True, ellipsize=3))
            self.list_box.append(row)

    def _selected(self) -> int | None:
        row = self.list_box.get_selected_row()
        return row.get_index() if row else None

    def _selection_changed(self, *_args: object) -> None:
        selected = self._selected() is not None
        self.copy.set_sensitive(selected)
        self.delete.set_sensitive(selected)

    def _add(self, *_args: object) -> None:
        item = {'name': self.name.get_text(), 'command': self.command.get_text()}
        self.items = store.save([item, *self.items])
        self.name.set_text('')
        self.command.set_text('')
        self._render()

    def _copy(self, *_args: object) -> None:
        index = self._selected()
        if index is not None:
            Gdk.Display.get_default().get_clipboard().set_text(self.items[index]['command'])

    def _delete(self, *_args: object) -> None:
        index = self._selected()
        if index is not None:
            self.items.pop(index)
            self.items = store.save(self.items)
            self._render()


if __name__ == '__main__':
    raise SystemExit(CommandShelf().run(sys.argv))
