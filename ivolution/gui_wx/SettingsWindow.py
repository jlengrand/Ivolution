#!/usr/bin/env python
"""
.. module:: SettingsWindow
   :platform: Unix, Windows, Mac
   :synopsis: Settings Window of the Ivolution GUI.

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""

import wx
import wx.lib.newevent

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
        # Sets icon
        #self.SetIcon(wx.Icon('ivolution/data/media/icons/spanner_48.ico',
        #            wx.BITMAP_TYPE_ICO))

        # Defining settings value
        self.output_folder = parent.out_fo
        self.video_name = "Ivolution"
        self.type = ""
        self.mode = ""
        self.speed = ""
        self.sort = ""

        # setting default value from main window
        self.outputLocationLabel.SetLabel(self.output_folder)

    # Virtual event handlers, overide them in your derived class
    def on_output(self, event):
        self.outputdialog = wx.DirDialog(self,
                                        "Please choose your output directory",
                                        style=1,
                                        defaultPath=self.output_folder)

        if self.outputdialog.ShowModal() == wx.ID_OK:
            self.output_folder = self.outputdialog.GetPath()
            self.outputLocationLabel.SetLabel(self.output_folder)
        self.outputdialog.Destroy()

    def on_cancel(self, event):
        self.Close(True)  # Close the frame.

    def on_save(self, event):
        event.Skip()
