#!/usr/bin/env python3
import gi
gi.require_version('Adw','1');gi.require_version('Gtk','4.0')
from gi.repository import Adw,Gtk
from checker import check
class Window(Adw.ApplicationWindow):
 def __init__(self,**k):
  super().__init__(**k,title='Spell Lens',default_width=640,default_height=440)
  self.view=Gtk.TextView(wrap_mode=Gtk.WrapMode.WORD_CHAR); self.result=Gtk.Label(label='Text stays on this device.',wrap=True)
  button=Gtk.Button(label='Check spelling');button.connect('clicked',self.run)
  box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=12,margin_top=18,margin_bottom=18,margin_start=18,margin_end=18);box.append(Gtk.ScrolledWindow(child=self.view,vexpand=True));box.append(button);box.append(self.result);self.set_content(box)
 def run(self,b):
  text=self.view.get_buffer().get_text(self.view.get_buffer().get_start_iter(),self.view.get_buffer().get_end_iter(),True)
  try:
   words=check(text);self.result.set_label('No spelling issues found.' if not words else 'Possible spelling issues: '+', '.join(words))
  except RuntimeError as e:self.result.set_label(str(e))
class App(Adw.Application):
 def __init__(self):super().__init__(application_id='io.github.yeager.SpellLens')
 def do_activate(self):Window(application=self).present()
App().run()
