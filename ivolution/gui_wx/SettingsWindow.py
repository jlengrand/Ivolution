#!/usr/bin/env python
"""
.. module:: SettingsWindow
   :platform: Unix, Windows, Mac
   :synopsis: Settings Window of the Ivolution GUI designed to be supported by all platforms.

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""

import wx
import wx.lib.newevent

import sys
import os
import logging
import webbrowser

from .. import get_data # used to load images and files

from SettingsTemplate import SettingsTemplate


class SettingsWindow(SettingsTemplate):
    """
    Settings Window of the Ivolution application
    """
    def __init__(self, parent):
        """
        Overrides init frame SettingsTemplate
        """
        SettingsTemplate.__init__(self, parent)
        # TODO : Set icon
        #self.SetIcon(wx.Icon('ivolution/data/media/icons/spanner_48.ico', wx.BITMAP_TYPE_ICO))  # Sets icon


        # Defining settings value
        self.output_folder = parent.out_fo
        self.file_name = "Ivolution"





        self.outputLocationLabel.SetLabel(self.output_folder) # setting default value from main window

    # Virtual event handlers, overide them in your derived class
    def on_output( self, event ):
        pass
        # default_dir = "~/Pictures"
        # self.inputdialog = wx.DirDialog(self, "Please choose your input directory", style=1, defaultPath=default_dir)

        # if self.inputdialog.ShowModal() == wx.ID_OK:
        #     self.inputtextbox.SetLabel(self.inputdialog.GetPath())
        # self.inputdialog.Destroy()

    def on_cancel( self, event ):
        self.Close(True)  # Close the frame.

    def on_save( self, event ):
        event.Skip()