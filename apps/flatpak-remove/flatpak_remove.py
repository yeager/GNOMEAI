#!/usr/bin/env python3
import subprocess
import gi
gi.require_version('Adw','1'); gi.require_version('Gtk','4.0')
from gi.repository import Adw,Gio,Gtk
from model import parse_list
class Window(Adw.ApplicationWindow):
 def __init__(self,**k):
  super().__init__(**k,title='Flatpak Remove',default_width=600,default_height=480)
  self.list=Gtk.ListBox(selection_mode=Gtk.SelectionMode.SINGLE); self.status=Gtk.Label(label='Select a user-installed Flatpak app.',margin_top=12,margin_bottom=12)
  remove=Gtk.Button(label='Remove selected app');remove.connect('clicked',self.remove)
  box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL); box.append(Gtk.ScrolledWindow(child=self.list,vexpand=True));box.append(self.status);box.append(remove);self.set_content(box);self.reload()
 def reload(self):
  try: apps=parse_list(subprocess.check_output(['flatpak','list','--user','--app','--columns=application,name'],text=True,stderr=subprocess.STDOUT))
  except (OSError,subprocess.CalledProcessError) as e: self.status.set_label(f'Cannot list user Flatpak apps: {e}');return
  for app in apps:
   row=Adw.ActionRow(title=app.name,subtitle=app.app_id);row.app=app;self.list.append(row)
  if not apps:self.status.set_label('No user-installed Flatpak apps found.')
 def remove(self,b):
  row=self.list.get_selected_row()
  if not row:return
  dialog=Adw.AlertDialog(heading=f'Remove “{row.app.name}”?',body='This removes the selected user-installed Flatpak app.')
  dialog.add_response('cancel','Cancel');dialog.add_response('remove','Remove');dialog.set_response_appearance('remove',Adw.ResponseAppearance.DESTRUCTIVE)
  dialog.choose(self,None,lambda d,r: self.confirm(row.app) if d.choose_finish(r)=='remove' else None)
 def confirm(self,app):
  try: subprocess.run(['flatpak','uninstall','--user','--noninteractive',app.app_id],check=True);self.status.set_label(f'Removed {app.name}.')
  except subprocess.CalledProcessError as e:self.status.set_label(f'Could not remove {app.name}: {e}')
class App(Adw.Application):
 def __init__(self):super().__init__(application_id='io.github.yeager.FlatpakRemove')
 def do_activate(self):Window(application=self).present()
App().run()
