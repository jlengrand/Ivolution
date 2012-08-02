#!/usr/bin/env python

from gi.repository import Gtk, GObject
from ivolution.gui import IvolutionWindow


import os
print "Script"
print os.getcwd()
my_app = IvolutionWindow.IvolutionWindow("Ivolution")
GObject.threads_init()
Gtk.main()
