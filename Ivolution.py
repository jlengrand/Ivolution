#!/usr/bin/env python

from gi.repository import Gtk

class Ivolution(object):       
	def __init__(self):
	    builder = Gtk.Builder()
	    builder.add_from_file("data/ui/IvolutionWindow.glade")
	    #builder.connect_signals({ "on_window_destroy" : gtk.main_quit })
	    self.window = builder.get_object("ivolution_window")
	    self.window.show()

	def on_destroy(self, widget, data=None):
		"""Called when the IvolutionWindow is closed."""
		# Clean up code for saving application state should be added here.
		Gtk.main_quit()

if __name__ == "__main__":
	app = Ivolution()
	Gtk.main()