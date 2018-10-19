#!/usr/bin/env python3
import os,sys

# Find local IP.
ip_local = os.popen("ip address show scope 0").read()
ip_local = ip_local.split('inet ', 1)[1]
ip_local = ip_local.split('/', 1)[0]
print("Local IP: "+ip_local) # For CLI usage.

# Find global IP.
import urllib.request
ip_global = urllib.request.urlopen('https://api.ipify.org').read().decode("utf-8").strip()
print("Global IP: "+ip_global) # For CLI usage.

# Build the GUI.
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gio, Gtk

# Basic event handling.
class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

builder = Gtk.Builder()

# Load GUI data files.
try:
	# Installed version.
	file = "/usr/share/lanpack/lan.glade"
	builder.add_from_file(file)
except:
	try:
		# Local version.
		file = "./lan.glade"
		builder.add_from_file(file)
	except:
		print ("Could not load GTK GUI at: "+file)
		sys.exit(1)

builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

label = builder.get_object("entry1")
label.set_text(ip_local)

label = builder.get_object("entry2")
label.set_text(ip_global)

Gtk.main()
