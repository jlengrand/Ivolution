#!/usr/bin/env python
"""
.. module:: IvolutionWindow
   :platform: Unix, Windows, Mac
   :synopsis: Main Window of the Ivolution GUI designed to be supported by all platforms.

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""

import wx
import wx.lib.newevent

import sys
import os
import logging
import webbrowser

from .. import get_data # used to load images and files

from .. import FaceParams
from .. import FacemovieThread

from ..util.Notifier import Observer
from ..util.Notifier import Observable

from IvolutionTemplate import IvolutionTemplate


class IvolutionWindow(IvolutionTemplate, Observer, Observable):
    """
    Main Window of the Ivolution application
    """
    def __init__(self, parent, title):
        """
        Overrides init frame IvolutionTemplate
        """
        IvolutionTemplate.__init__(self, parent)
        Observer.__init__(self, "Interface")
        Observable.__init__(self)

        # Sets up logging capability
        self.my_logger = None
        self.console_logger = None
        self.setup_logger()

        # Defines all our parameters neededfor the facemovie
        self.get_default_parameters()

        self.process_running = False
        self.facemovie = None

        self.inputtextbox.SetLabel(self.in_fo)  # sets label to default input folder
        self.SetIcon(wx.Icon('ivolution/data/media/vitruve.ico', wx.BITMAP_TYPE_ICO))  # Sets icon

        self.Show(True)  # Finally show the frame

    def get_default_parameters(self):
        """
        """
        # FIXME: You gotta try on a Mac
        self.videospeedlistChoices = [u"slow", u"medium", u"fast"]
        self.gaugerange = 100

        self.root_fo = ""
        self.mode = "crop"  # type of video to be created
        self.sort = "name"  # how image files will be chronologically sorted
        self.speed = 1  # Speed of the movie
        self.param = "frontal_face"  # type of face profile to be searched for

        if "win" in sys.platform:
            self.out_fo = "C:/Users/jll/Videos/"  # Default folder for Windows
            self.in_fo = "C:\Users\jll\Pictures/"
        else:
            self.out_fo = "C:/Users/jll/Videos/"  # Default folder for Linux
            self.in_fo = "/home/jll/Pictures/"

    # Overriding event handling methods
    def on_settings(self, event):
        print "settings"

    def on_start(self, event):
        """
        User asks for starting the algorithm
        Sets all parameters and start processing
        """
        self.my_logger.debug("start pressed")
        if not self.process_running:  # start only if not already running
            self.set_parameters()
            self.print_parameters()
            # Instantiating the facemovie
            self.facemovie = FacemovieThread.FacemovieThread(self.face_params)
            self.facemovie.subscribe(self)  # I want new information ! Subscribes to facemovie reports
            self.subscribe(self.facemovie)  # Subscribing facemovie to our messages

            self.facemovie.start()

            self.process_running = True
        else:
            self.console_logger.error("Cannot start, process already running !")
            self.my_logger.error("Cannot start, process already running !")

    def on_stop(self, event):
        """
        User asks for stopping the algorithm
        Asks the FacemovieThread to terminate
        """
        self.my_logger.debug("Stop pressed")
        self.console_logger.debug("Stop pressed")
        self.notify(["Application", ["STOP"]])  # Asking the Facemovie to stop
        self.process_running = False

        #self.on_exit(event) # Finally shuts down the interface

    def on_input(self, event):
        """
        Activated when a user clicks to choose its input location
        """
        default_dir = "~/Pictures"
        self.inputdialog = wx.DirDialog(self, "Please choose your input directory", style=1, defaultPath=default_dir)

        if self.inputdialog.ShowModal() == wx.ID_OK:
            self.inputtextbox.SetLabel(self.inputdialog.GetPath())
        self.inputdialog.Destroy()

    def on_output(self, event):
        """
        Activated when a user clicks to choose its output location
        """
        default_dir = "~/Videos"
        self.outputdialog = wx.DirDialog(self, "Please choose your output directory", style=1, defaultPath=default_dir)

        if self.outputdialog.ShowModal() == wx.ID_OK:
            self.outputchoosertext.SetLabel(self.outputdialog.GetPath())
        self.outputdialog.Destroy()

    def on_help(self, event):
        """
        Opens a browser and points to online help.
        """
        url = "http://jlengrand.github.com/FaceMovie/"
        webbrowser.open(url, new=2)  # in new tab if possible

    def on_about(self, event):
        """
        Displays the about box for Ivolution
        """
        description = """FaceMovie is a project aiming at helping you
 create videos of yourself over time. Simply take pictures of yourself, Facemovie does everything else for you.
FaceMovie may be used for faces, but also profiles (to show women along pregnancy for example) or full body (for people workouting). The only limitation comes from you !
"""

        licence = """Ivolution is free software; you can redistribute
it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the License,
or (at your option) any later version.

File Hunter is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details. You should have
received a copy of the GNU General Public License along with File Hunter;
if not, write to the Free Software Foundation, Inc., 59 Temple Place,
Suite 330, Boston, MA  02111-1307  USA"""

        info = wx.AboutDialogInfo()

        info.SetIcon(wx.Icon('ivolution/data/media/vitruve.png', wx.BITMAP_TYPE_PNG))
        info.SetName('Ivolution')
        info.SetVersion('0.8')
        info.SetDescription(description)
        info.SetCopyright('(C) 2012 Julien Lengrand-Lambert')
        info.SetWebSite('http://www.lengrand.fr')
        info.SetLicence(licence)
        info.AddDeveloper('Julien Lengrand-Lambert')
        info.AddDocWriter('Julien Lengrand-Lambert')
        info.AddArtist('Luc Viatour')
        info.AddTranslator('Julien Lengrand-Lambert')

        wx.AboutBox(info)

    def on_exit(self, event):
        """
        Called when the IvolutionWindow is closed, or File/Exit is called.
        """
        # Clean up code for saving application state should be added here.
        self.notify(["Application", ["STOP"]])  # Asking the Facemovie to stop
        self.process_running = False
        self.Close(True)  # Close the frame.

    # system methods
    def get_current_mode(self):
        """
        """
        if self.cropmode.GetValue():
            mode = "crop"
        else:
            mode = "conservative"

        return mode

    def get_current_sort(self):
        """
        """
        if self.namemode.GetValue():
            sort = "name"
        else:
            sort = "exif"

        return sort

    def set_parameters(self):
        """
        Retrieves all parameters needed for the algorithm to run
        """
        #self.in_fo = self.inputtextbox.GetLabel() + "/"
        self.in_fo = "C:\Users\jll\perso\Ivolution\ivolution\data\samples" + "/"
        self.out_fo = "C:\Users\jll\Videos" + "/"
        #self.out_fo = self.outputchoosertext.GetLabel() + "/"
        self.param = "frontal_face"
        #self.param = self.typefacelist.GetValue()
        #self.speed = self.videospeedlistChoices.index(self.videospeedlist.GetValue())  # We need and integer between 0 and 2
        self.speed = self.videospeedlistChoices[1]

        self.mode = "crop"
        self.sort = "name"
        #self.mode = self.get_current_mode()
        #self.sort = self.get_current_sort()

        # Instantiating the face_params object that will be needed by the facemovie
        par_fo = os.path.join(self.root_fo, get_data("haarcascades"))
        self.face_params = FaceParams.FaceParams(par_fo,
                                                 self.in_fo,
                                                 self.out_fo,
                                                 self.param,
                                                 self.sort,
                                                 self.mode,
                                                 self.speed)

        self.print_parameters()

    def print_parameters(self):
        print "#########"
        print "Settings:"
        print "input folder :   %s" % (self.in_fo)
        print "output folder :   %s" % (self.out_fo)

        print "Face Type :   %s" % (self.param)
        print "Speed chosen :   %s" % (self.speed)
        print "Mode chosen :   %s" % (self.mode)
        print "Sort method :   %s" % (self.sort)

        print "#########"

    def setup_logger(self):
        """
        Configures our logger to save error messages
        Start logging in file here
        """
        personal_dir = "~/.ivolution"
        log_root = 'fm.log'
        log_file = os.path.join(os.path.expanduser(personal_dir), log_root)

        # create logger for  'facemovie'
        self.my_logger = logging.getLogger('FileLog')

        self.my_logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages

        #fh = logging.StreamHandler()
        fh = logging.FileHandler(log_file)

        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        self.console_logger = logging.getLogger('ConsoleLog')
        self.console_logger.setLevel(logging.DEBUG)  # not needed

        ch = logging.StreamHandler()
        #ch.setLevel(logging.DEBUG) # not needed

        # add the handlers to the logger
        self.my_logger.addHandler(fh)

        self.my_logger.info("######")  # Separating different sessions

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # create formatter and add it to the handlers
        fh.setFormatter(formatter)
        #ch.setFormatter(formatter)

        self.console_logger.addHandler(ch)

    def update(self, message):
        """
        Trigerred by FacemovieThread.
        Uses the Observer pattern to inform the user about the progress of the current job.
        """
        if len(message) == 3:
            # notifications
            #self.console_logger.debug(message)
            self.my_logger.debug(message)

            if message[0] == "PROGRESS":  # progress bar
                # big steps performed
                wx.MutexGuiEnter()  # to avoid thread problems
                self.progressgauge.SetValue(self.gaugerange * float(message[2]))
                self.statusbar.SetStatusText(message[1], 0)
                wx.MutexGuiLeave()

                if float(message[2]) >= 1.0:  # 100% of process
                    self.my_logger.debug("Reached end of facemovie process")
                    #self.console_logger.debug("Reached end of facemovie process")
                    self.process_running = False

            elif message[0] == "STATUS":  # status label
                if message[1] == "Error":
                    wx.MutexGuiEnter()  # to avoid thread problems
                    self.statusbar.SetStatusText("Error detected", 0)
                    self.progressgauge.SetValue(0)
                    wx.MutexGuiLeave()
                    self.process_running = False

                wx.MutexGuiEnter()  # to avoid thread problems
                self.statusbar.SetStatusText(message[1], 1)
                wx.MutexGuiLeave()
            elif message[0] == "FILEADD":
                item = wx.ListItem()
                item.SetText(message[1])
                wx.MutexGuiEnter()  # to avoid thread problems
                self.filelist.InsertItem(item)
                wx.MutexGuiLeave()
            elif message[0] == "FILEDONE":
                for i in range(self.filelist.GetItemCount()):
                    if message[1] == self.filelist.GetItemText(i):
                        if message[2] == 1:
                            color = "green"
                        else:
                            color = "red"
                        wx.MutexGuiEnter()  # to avoid thread problems
                        self.filelist.SetItemTextColour(i, color)
                        wx.MutexGuiLeave()

        elif len(message) > 1:  # system commands shall be ignored
            self.console_logger.debug("Unrecognized command")
            self.my_logger.debug("Unrecognized command")
            self.console_logger.debug(message)
            self.my_logger.debug(message)
