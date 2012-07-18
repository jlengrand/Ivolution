#!/usr/bin/env python

from gi.repository import Gtk, GObject
from gui import IvolutionWindow


my_app = IvolutionWindow.IvolutionWindow()
GObject.threads_init()
Gtk.main()
