#!/usr/bin/env python
"""
.. module:: IvolutionWindow
   :platform: Unix, Windows, Mac
   :synopsis: Main Window of the Ivolution GUI designed to be supported by all platforms.

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""

import wx
import wx.lib.newevent

import os
import logging
import webbrowser

from .. import get_data # used to load images and files

from .. import FaceParams
from .. import FacemovieThread

from ..util.Notifier import Observer
from ..util.Notifier import Observable

from AboutDialog import AboutDialog


class IvolutionWindow(wx.Frame, Observer, Observable):
    """
    Main Window of the Ivolution application
    """
    def __init__(self, parent, title):
        """
        Overrides init frame wx.Frame
        """
        wx.Frame.__init__(self, parent, title=title, size=(500, 700))
        Observer.__init__(self, title)
        Observable.__init__(self)

        self.gaugerange = 100 # max value of progress bar

        # Sets icon
        # ib = wx.IconBundle()
        # ib.AddIconFromFile("ivolution/data/media/vitruve_64.png", wx.BITMAP_TYPE_ANY)
        # self.SetIcons(ib)

        # image = wx.Image("ivolution/data/media/vitruve_64.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        # icon = wx.EmptyIcon()
        # icon.CopyFromBitmap(image)
        # self.SetIcon(icon)

        # Sets up logging capability
        self.my_logger = None
        self.console_logger = None
        self.setup_logger()

        ####
        ## Setting up interface
        # Creating the menubar
        self.menubar = self.setup_menubar()
        self.panel = wx.Panel(self)
        # Creating the title layout
        title = self.setup_titlelayout()
        # Creating the settings layout
        settings = self.setup_settingslayout()
        # Creating the buttons layout
        buttons = self.setup_buttonslayout()
        # Creating the status bar
        self.statusbar = self.setup_statusbar()

        # Creating the main grid
        maingrid = self.setup_maingrid(title, settings, buttons)
        self.panel.SetSizer(maingrid)
        self.panel.Layout()
        self.Show(True)
        ####

        # Defines all our parameters neededfor the facemovie
        self.root_fo = ""
        self.in_fo = ""  # Input folder, where images are located
        self.out_fo = ""  # Input folder, where the video will be saved
        self.mode = "crop"  # type of video to be created
        self.sort = "name"  # how image files will be chronologically sorted
        self.speed = 1  # Speed of the movie
        self.param = "frontal_face"  # type of face profile to be searched for

        self.in_fo = ""  # Input folder, where images are located

        self.process_running = False
        self.facemovie = None

    # GUI set up
    def setup_buttonslayout(self):
        """
        Creates the box containing Start/Stop buttons
        """
        commandbox = wx.FlexGridSizer(2, 1, 0, 0)

        buttonsbox = wx.FlexGridSizer(1, 2, 0, 0)

        startbutton = wx.Button(self.panel, label='Create Movie!')
        startbutton.Bind(wx.EVT_BUTTON, self.on_start)
        stopbutton = wx.Button(self.panel, label='Stop processing')
        stopbutton.Bind(wx.EVT_BUTTON, self.on_stop)

        buttonsbox.AddMany([startbutton, stopbutton])

        # progress bar
        self.progressgauge = wx.Gauge(self.panel, range=self.gaugerange) # range is max value of gauge

        commandbox.AddMany([buttonsbox, self.progressgauge])

        return commandbox

    def setup_requiredsettings(self):
        """
        Creates the box containing all required settings
        """
        requiredbox = wx.FlexGridSizer(3, 1, 0, 0)

        title = wx.StaticText(self.panel, label="Required parameters:")

        # Creates input box, allowing to choose the input folder
        inputbox = wx.FlexGridSizer(2, 1, 0, 0)
        inputtext = wx.StaticText(self.panel, label="Choose your input folder:")

        inputchooserbox = wx.FlexGridSizer(1, 2, 0, 0)
        self.inputchoosertext = wx.StaticText(self.panel, label="/home/jll/Documents/Ivolution/ivolution/data/samples/")
        inputchooserbutton = wx.Button(self.panel, label="..")
        inputchooserbutton.Bind(wx.EVT_BUTTON, self.on_input)
        #inputchooser = wx.DirDialog(self.panel, "Please choose your project directory:", style=1 ,defaultPath=os.getcwd())
        inputchooserbox.AddMany([self.inputchoosertext, inputchooserbutton])

        inputbox.AddMany([inputtext, inputchooserbox])

        # Creates output box, allowing to choose the output folder
        outputbox = wx.FlexGridSizer(2, 1, 0, 0)
        outputtext = wx.StaticText(self.panel, label="Choose your output folder:")

        outputchooserbox = wx.FlexGridSizer(1, 2, 0, 0)
        self.outputchoosertext = wx.StaticText(self.panel, label="~/Videos")
        outputchooserbutton = wx.Button(self.panel, label="..")
        outputchooserbutton.Bind(wx.EVT_BUTTON, self.on_output)

        #inputchooser = wx.DirDialog(self.panel, "Please choose your project directory:", style=1 ,defaultPath=os.getcwd())
        outputchooserbox.AddMany([self.outputchoosertext, outputchooserbutton])
        #outputchooser = wx.DirDialog(self.panel, "Choose a directory:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

        outputbox.AddMany([outputtext, outputchooserbox])

        requiredbox.AddMany([title, inputbox, outputbox])

        return requiredbox

    def setup_optionalsettings(self):
        """
        Creates the box containing all optional settings
        """
        optionalbox = wx.FlexGridSizer(5, 1, 0, 0)

        title = wx.StaticText(self.panel, label="Optional parameters:")

        # Creates typeface box, allowing to choose face or profile
        typefacebox = wx.FlexGridSizer(2, 1, 0, 0)
        typefacetext = wx.StaticText(self.panel, label="Type of face:")
        types = ['frontal_face', 'profile_face']
        self.typefacelist = wx.ComboBox(self.panel, choices=types, style=wx.CB_READONLY)
        self.typefacelist.SetValue(types[0])

        typefacebox.AddMany([typefacetext, self.typefacelist])

        # Creates the video speed box
        videospeedbox = wx.FlexGridSizer(2, 1, 0, 0)
        videospeedtext = wx.StaticText(self.panel, label="Video Speed:")
        self.speedvals = ['slow', 'medium', 'fast']
        self.videospeedlist = wx.ComboBox(self.panel, choices=self.speedvals, style=wx.CB_READONLY)
        self.videospeedlist.SetValue(self.speedvals[1])

        videospeedbox.AddMany([videospeedtext, self.videospeedlist])

        # Creates the video mode box
        videomodebox = wx.FlexGridSizer(2, 1, 0, 0)
        videomodetext = wx.StaticText(self.panel, label="Choose your prefered mode:")
        videomodechoices = wx.FlexGridSizer(1, 2, 0, 0)

        self.cropmode = wx.RadioButton(self.panel, label='Crop Mode', style=wx.RB_GROUP)
        self.conservativemode = wx.RadioButton(self.panel, label='Conservative Mode')
        videomodechoices.AddMany([self.cropmode, self.conservativemode])
        videomodebox.AddMany([videomodetext, videomodechoices])

        # Creates the file method box
        filemethodbox = wx.FlexGridSizer(2, 1, 0, 0)
        filemethodtext = wx.StaticText(self.panel, label="Choose your prefered mode:")
        filemethodchoices = wx.FlexGridSizer(1, 2, 0, 0)
        self.namemode = wx.RadioButton(self.panel, label="File name", style=wx.RB_GROUP)
        self.exifmode = wx.RadioButton(self.panel, label="EXIF metadata")
        filemethodchoices.AddMany([self.namemode, self.exifmode])
        filemethodbox.AddMany([filemethodtext, filemethodchoices])

        optionalbox.AddMany([title, typefacebox, videospeedbox, videomodebox, filemethodbox])

        return optionalbox

    def setup_settingslayout(self):
        """
        Defines the second part of the GUI, containing all parameters
        that can be changed
        """
        settingsbox = wx.FlexGridSizer(2, 1, 9, 15)  # main box

        # contains a box with required parameters
        requiredbox = self.setup_requiredsettings()
        # and another with optional parameters
        optionalbox = self.setup_optionalsettings()

        settingsbox.AddMany([(requiredbox), (optionalbox)])

        return settingsbox

    def setup_titlelayout(self):
        """
        Defines the first part of the GUI, showing the title and logo
        """
        hbox = wx.BoxSizer(wx.HORIZONTAL)  # used to contain logo part and text part
        vbox = wx.BoxSizer(wx.VERTICAL)  # used to separate title and one-liner
        logobox = wx.BoxSizer(wx.HORIZONTAL)

        wx_logo = wx.EmptyBitmap(1, 1)  # Create a bitmap container object.
        wx_logo.LoadFile("ivolution/data/media/vitruve_50.jpg", wx.BITMAP_TYPE_ANY)  # Load it with a file image.

        logo = wx.StaticBitmap(self.panel, 1, wx_logo)
        #logo = wx.StaticText(self.panel, label="Logo Here")  # Change for proper logo
        title = wx.StaticText(self.panel, label="Ivolution")
        one_liner = wx.StaticText(self.panel, label="Take one picture of yourself a day,\
 automatically generate a movie!")

        logobox.Add(logo)
        vbox.Add(title, flag=wx.RIGHT, border=8)
        vbox.Add(one_liner, flag=wx.RIGHT, border=8)

        hbox.Add(logobox, flag=wx.RIGHT, border=8)
        hbox.Add(vbox, flag=wx.RIGHT, border=8)

        return hbox

    def setup_maingrid(self, title, settings, buttons):
        """
        Defines the main grid that will be used as layout in the window.
        """
        maingrid = wx.FlexGridSizer(4, 1, vgap=0, hgap=0)
        maingrid.AddMany([title, settings, buttons])
        return maingrid

    def setup_statusbar(self):
        """
        Sets up all elements of the status bar
        """
        self.sb = self.CreateStatusBar()

    def setup_filemenu(self):
        """
        Sets up all elements of the file menu
        """
        file_menu = wx.Menu()

        #Sets up the Help menu item
        menuHelp = file_menu.Append(wx.ID_HELP, "Help", "Help online")
        self.Bind(wx.EVT_MENU, self.on_help, menuHelp)

        # Sets up the About menu item
        menuAbout = file_menu.Append(wx.ID_ABOUT, "About", " Information about this program")
        self.Bind(wx.EVT_MENU, self.on_about, menuAbout)

        file_menu.AppendSeparator()

        # Sets up the Exit menu item
        menuExit = file_menu.Append(wx.ID_EXIT, "Exit", " Terminate the program")
        self.Bind(wx.EVT_MENU, self.on_exit, menuExit)

        return file_menu

    def setup_menubar(self):
        """
        """
        # Creating the menubar.
        menuBar = wx.MenuBar()

        filemenu = self.setup_filemenu()

        menuBar.Append(filemenu, "File")  # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        return menuBar

    # Events Handling
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
        self.notify(["STOP"])  # Asking the Facemovie to stop
        self.process_running = False

        #self.on_exit(event) # Finally shuts down the interface

    def on_input(self, event):
        """
        Activated when a user clicks to choose its input location
        """
        default_dir = "~/Pictures"
        self.inputdialog = wx.DirDialog(self, "Please choose your input directory", style=1, defaultPath=default_dir)

        if self.inputdialog.ShowModal() == wx.ID_OK:
            self.inputchoosertext.SetLabel(self.inputdialog.GetPath())
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
        about = AboutDialog(self, "Ivolution")
        about.ShowModal()  # Show it
        about.Destroy()  # finally destroy it when finished.

    def on_exit(self, event):
        """
        Called when the IvolutionWindow is closed, or File/Exit is called.
        """
        # Clean up code for saving application state should be added here.
        self.notify(["STOP"])  # Asking the Facemovie to stop
        self.process_running = False
        self.Close(True)  # Close the frame.

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
        self.in_fo = self.inputchoosertext.GetLabel() + "/"
        self.out_fo = self.outputchoosertext.GetLabel() + "/"
        self.param = self.typefacelist.GetValue()
        self.speed = self.speedvals.index(self.videospeedlist.GetValue())  # We need and integer between 0 and 2

        self.mode = self.get_current_mode()
        self.sort = self.get_current_sort()

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
                wx.MutexGuiLeave()
                # TODO : status bar here
                # Uses GLib to run Thread safe operations on GUI
                #GLib.idle_add(self.progressbar.set_fraction, float(message[2]))
                #GLib.idle_add(self.progressbar.set_text, message[1])

                if float(message[2]) >= 1.0:  # 100% of process
                    self.my_logger.debug("Reached end of facemovie process")
                    #self.console_logger.debug("Reached end of facemovie process")
                    self.process_running = False

            elif message[0] == "STATUS":  # status label
                wx.MutexGuiEnter()  # to avoid thread problems
                self.sb.SetStatusText(message[1])
                wx.MutexGuiLeave()

        elif len(message) > 1:  # system commands shall be ignored
            self.console_logger.debug("Unrecognized command")
            self.my_logger.debug("Unrecognized command")
            self.console_logger.debug(message)
            self.my_logger.debug(message)

if __name__ == "__main__":
    app = wx.App(False)
    frame = IvolutionWindow(None, "Ivolution Window")
    app.MainLoop()  # Runs application
