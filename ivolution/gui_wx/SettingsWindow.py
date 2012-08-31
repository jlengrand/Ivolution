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

        self.parent = parent

        # Defining settings value
        self.output_folder = parent.out_fo
        self.video_name = "Ivolution"
        self.type = ""
        self.mode = ""
        self.speed = ""
        self.sort = ""

        # setting default value from main window
        self.outputLocationLabel.SetLabel(self.output_folder)
        self.typeCombo.SetSelection(0)
        self.speedCombo.SetSelection(1)

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
        # output_folder is already set
        self.video_name = self.outputText.GetValue()
        self.type = self.typeCombo.GetSelection()
        self.mode = self.modeRadioBox.GetSelection()
        self.speed = self.speedCombo.GetSelection()
        self.sort = self.sortRadioBox.GetSelection()

        #self.print_parameters()
        self.setParentParams()
        self.Close(True)  # Close the frame.

    def setParentParams(self):
        modeChoices = [u"conservative", u"crop"]
        paramChoices = [u"frontal_face", u"profile_face"]
        sortChoices = [u"name", u"exif"]

        #self.video_name
        self.parent.out_fo = self.output_folder
        self.parent.param = paramChoices[self.type]
        self.parent.mode = modeChoices[self.mode]
        self.parent.speed = self.speed
        self.parent.sort = sortChoices[self.sort]

    def print_parameters(self):
        print "#########"
        print "Settings:"
        print "file name :   %s" % (self.video_name)
        print "output folder :   %s" % (self.output_folder)

        print "Face Type :   %s" % (self.type)
        print "Speed chosen :   %s" % (self.speed)
        print "Mode chosen :   %s" % (self.mode)
        print "Sort method :   %s" % (self.sort)

        print "#########"
