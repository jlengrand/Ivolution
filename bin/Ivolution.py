#!/usr/bin/env python

import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 

from gi.repository import Gtk, GObject
from gui import IvolutionWindow


my_app = IvolutionWindow.IvolutionWindow()
GObject.threads_init()
Gtk.main()
