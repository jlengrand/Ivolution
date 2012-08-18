#!/usr/bin/env python
"""
.. module:: AboutDialog
   :platform: Unix, Windows, Mac
   :synopsis: About window of the application. Used to display information

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""

import wx


class AboutDialog(wx.MessageDialog):
    """
    Custom About dialog frame for Ivolution
    """
    def __init__(self, parent, msg, caption="About Ivolution", style=wx.OK):
        """
        Overrides init dialog wx.MessageDialog
        """
        wx.MessageDialog.__init__(self, parent, msg, caption, style)
