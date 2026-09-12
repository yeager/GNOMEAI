#!/usr/bin/env python3
from pathlib import Path
import gi
gi.require_version('Adw', '1')
gi.require_version('Gtk', '4.0')
from gi.repository import Adw, Gio, Gtk
from installer import ArchiveError, inspect_archive, install_archive

class Window(Adw.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, title='Extension Pack Installer', default_width=560, default_height=360)
        self.extension = None
        self.status = Gtk.Label(label='Choose a GNOME Shell extension ZIP archive.', wrap=True, justify=Gtk.Justification.CENTER)
        self.install = Gtk.Button(label='Install locally', sensitive=False)
        self.install.connect('clicked', self.on_install)
        choose = Gtk.Button(label='Choose archive')
        choose.connect('clicked', self.on_choose)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=18, valign=Gtk.Align.CENTER, margin_top=36, margin_bottom=36, margin_start=36, margin_end=36)
        box.append(Gtk.Image.new_from_icon_name('package-x-generic-symbolic'))
        box.append(self.status); box.append(choose); box.append(self.install)
        self.set_content(box)
    def on_choose(self, button):
        dialog = Gtk.FileChooserNative.new('Choose Extension Archive', self, Gtk.FileChooserAction.OPEN, '_Open', '_Cancel')
        dialog.connect('response', self.on_selected); dialog.show()
    def on_selected(self, dialog, response):
        if response != Gtk.ResponseType.ACCEPT: return
        try:
            self.extension = inspect_archive(dialog.get_file().get_path())
            versions = ', '.join(self.extension.shell_versions) or 'unspecified Shell version'
            self.status.set_label(f'“{self.extension.name}”\n{self.extension.uuid}\nCompatible with: {versions}')
            self.install.set_sensitive(True)
        except ArchiveError as error:
            self.extension = None; self.install.set_sensitive(False); self.status.set_label(str(error))
    def on_install(self, button):
        try:
            target = install_archive(self.extension, Path.home() / '.local/share/gnome-shell/extensions')
            self.status.set_label(f'Installed to:\n{target}\nRestart GNOME Shell or log out to load it.')
            self.install.set_sensitive(False)
        except ArchiveError as error: self.status.set_label(str(error))
class App(Adw.Application):
    def __init__(self): super().__init__(application_id='io.github.yeager.ExtensionPackInstaller')
    def do_activate(self): Window(application=self).present()
if __name__ == '__main__': App().run()
