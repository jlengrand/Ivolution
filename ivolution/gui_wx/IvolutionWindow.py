#!/usr/bin/env python
"""
.. module:: IvolutionWindow
   :platform: Unix, Windows, Mac
   :synopsis: Main Window of the Ivolution GUI designed to be supported by all platforms.

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""

import wx
import os
import logging

from .. import get_data # used to load images and files

from AboutDialog import AboutDialog


class IvolutionWindow(wx.Frame):
    """
    Main Window of the Ivolution application
    """
    def __init__(self, parent, title):
        """
        Overrides init frame wx.Frame
        """
        wx.Frame.__init__(self, parent, title=title, size=(500, 700))

        # Sets up logging capability
        self.my_logger = None
        self.console_logger = None
        self.setup_logger()

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
        # self.statusbar = self.setup_statusbar()

        # Creating the main grid
        maingrid = self.setup_maingrid(title, settings, buttons)
        self.panel.SetSizer(maingrid)
        self.panel.Layout()
        self.Show(True)

    # GUI set up
    def setup_buttonslayout(self):
        """
        Creates the box containing Start/Stop buttons
        """
        buttonsbox = wx.FlexGridSizer(1, 2, 0, 0)

        startbutton = wx.Button(self.panel, label='Create Movie!')
        stopbutton = wx.Button(self.panel, label='Stop processing')
        #stopbutton.Bind(wx.EVT_BUTTON, self.on_exit)  # Example of event

        buttonsbox.AddMany([startbutton, stopbutton])

        return buttonsbox

    def setup_requiredsettings(self):
        """
        Creates the box containing all required settings
        """
        requiredbox = wx.FlexGridSizer(3, 1, 0, 0)

        title = wx.StaticText(self.panel, label="Required parameters:")

        # Creates input box, allowing to choose the input folder
        inputbox = wx.FlexGridSizer(2, 1, 0, 0)
        inputtext = wx.StaticText(self.panel, label="Choose your input folder:")
        inputchooser = wx.Button(self.panel, label="~/Pictures")
        #inputchooser = wx.StaticText(self.panel, label="input folder")
        #inputchooser = wx.FileDialog(self.panel, message="Open an Image...", defaultDir=os.getcwd(), defaultFile="", style=wx.OPEN)
        #inputchooser = wx.DirDialog(self.panel, "Please choose your project directory:", style=1 ,defaultPath=os.getcwd())

        inputbox.AddMany([inputtext, inputchooser])

        # Creates output box, allowing to choose the output folder
        outputbox = wx.FlexGridSizer(2, 1, 0, 0)
        outputtext = wx.StaticText(self.panel, label="Choose your output folder:")
        outputchooser = wx.Button(self.panel, label="~/Videos")
        #outputchooser = wx.StaticText(self.panel, label="output folder")
        #outputchooser = wx.DirDialog(self.panel, "Choose a directory:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

        outputbox.AddMany([outputtext, outputchooser])

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
        typefacelist = wx.ComboBox(self.panel, choices=types, style=wx.CB_READONLY)
        typefacelist.SetValue(types[0])

        typefacebox.AddMany([typefacetext, typefacelist])

        # Creates the video speed box
        videospeedbox = wx.FlexGridSizer(2, 1, 0, 0)
        videospeedtext = wx.StaticText(self.panel, label="Video Speed:")
        speeds = ['slow', 'medium', 'fast']
        videospeedlist = wx.ComboBox(self.panel, choices=speeds, style=wx.CB_READONLY)
        videospeedlist.SetValue(speeds[1])

        videospeedbox.AddMany([videospeedtext, videospeedlist])

        # Creates the video mode box
        videomodebox = wx.FlexGridSizer(2, 1, 0, 0)
        videomodetext = wx.StaticText(self.panel, label="Choose your prefered mode:")
        videomodechoices = wx.FlexGridSizer(1, 2, 0, 0)

        cropmode = wx.RadioButton(self.panel, label='Crop Mode', style=wx.RB_GROUP)
        conservativemode = wx.RadioButton(self.panel, label='Conservative Mode')
        videomodechoices.AddMany([cropmode, conservativemode])
        videomodebox.AddMany([videomodetext, videomodechoices])

        # Creates the file method box
        filemethodbox = wx.FlexGridSizer(2, 1, 0, 0)
        filemethodtext = wx.StaticText(self.panel, label="Choose your prefered mode:")
        filemethodchoices = wx.FlexGridSizer(1, 2, 0, 0)
        namemode = wx.RadioButton(self.panel, label="File name", style=wx.RB_GROUP)
        exifmode = wx.RadioButton(self.panel, label="EXIF metadata")
        filemethodchoices.AddMany([namemode, exifmode])
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

    # def setup_statusbar(self):
    #     """
    #     Sets up all elements of the status bar
    #     """
    def setup_filemenu(self):
        """
        Sets up all elements of the file menu
        """
        file_menu = wx.Menu()

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
    def on_about(self, event):
        """
        Displays the about box for Ivolution
        TODO : Create the About Window
        """
        about = AboutDialog(self, "Ivolution")
        about.ShowModal()  # Show it
        about.Destroy()  # finally destroy it when finished.
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        # dlg = wx.MessageDialog(self, "Ivolution", "About Ivolution", wx.OK)
        # dlg.ShowModal()  # Show it
        # dlg.Destroy()  # finally destroy it when finished.
        print "About !"

    def on_exit(self, event):
        """
        Called when the IvolutionWindow is closed, or File/Exit is called.
        """
        self.Close(True)  # Close the frame.

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

if __name__ == "__main__":
    app = wx.App(False)
    frame = IvolutionWindow(None, "Ivolution Window")
    app.MainLoop()  # Runs application
