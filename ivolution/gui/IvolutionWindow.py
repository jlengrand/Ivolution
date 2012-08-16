#!/usr/bin/env python

import os

import webbrowser

import logging

from gi.repository import Gtk, GLib

from AboutDialog import AboutDialog

from .. import get_data

# import os
# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# os.sys.path.insert(0,parentdir) # import parent folder

from .. import Facemovie_lib
from .. import FaceParams
from .. import FacemovieThread

from ..util.Notifier import Observer 
from ..util.Notifier import Observable

import time

class IvolutionWindow(Observer, Observable):       
    def __init__(self, name):
        FacemovieThread.Observer.__init__(self, name)
        FacemovieThread.Observable.__init__(self)

        self.my_logger = None
        self.console_logger = None

        self.builder = Gtk.Builder()
        self.builder.add_from_file(get_data('ui/IvolutionWindow.glade'))
        #self.builder.add_from_file("ivolution/data/ui/IvolutionWindow.glade")
        #self.builder.connect_signals({ "on_ivolutionwindow_destroy" : Gtk.main_quit })
        self.window = self.builder.get_object("ivolution_window")
        self.window.show()
        self.builder.connect_signals(self)       

        ## Defines parameters needed to run the FaceMovie
        self.root_fo = ""
        self.in_fo = "" # Input folder, where images are located
        self.out_fo = "" # Input folder, where the video will be saved
        self.mode = "crop" # type of video to be created
        self.sort = "name" # how image files will be chronologically sorted
        self.speed = 1 # Speed of the movie
        self.param = "frontal_face" # type of face profile to be searched for

        self.in_fo = "" # Input folder, where images are located

        self.process_running = False

        self.facemovie = None

        self.AboutDialog = None # class

        self.setup()
        self.setup_logger()

    def setup(self):
        """
        Sets up all the default paramters and retrieve the element of the GUI we want to follow
        """
        self.AboutDialog = AboutDialog  # FIXME : Still not working

        self.startbutton = self.builder.get_object("startbutton")

        self.filechooserinput = self.builder.get_object("filechooserinput")
        self.filechooseroutput = self.builder.get_object("filechooseroutput")
        
        self.typecombobox = self.builder.get_object("typecombobox")
        self.typecombobox.set_active(0)

        self.speedcombobox = self.builder.get_object("speedcombobox")
        self.speedcombobox.set_active(0)

        self.cropradiobutton = self.builder.get_object("cropradiobutton")
        self.namesortradiobutton = self.builder.get_object("namesortradiobutton")

        self.progressbar = self.builder.get_object("progressbar")
        self.statuslabel = self.builder.get_object("statuslabel")


    # Signal handling related stuff

    def on_cropradiobutton_toggled(self,widget):
        """
        We need to take care only of this one as both are grouped
        """
        if widget.get_active(): # means crop is activated
            self.mode = "crop"
        else:
            self.mode = "conservative"

    def on_namesortradiobutton_toggled(self,widget):
        """
        We need to take care only of this one as both are grouped
        """
        if widget.get_active(): # means name is activated
            self.sort = "name"
        else:
            self.sort = "exif"

    def on_startbutton_pressed(self, widget):
        """
        Sets all parameters and start processing
        """
        self.my_logger.debug("start pressed")
        if not self.process_running: # start only if not already running
            self.set_parameters()
            self.print_parameters()
            # Instantiating the facemovie
            self.facemovie = FacemovieThread.FacemovieThread(self.face_params)
            self.facemovie.subscribe(self) # I want new information ! Subscribes to facemovie reports
            self.subscribe(self.facemovie) # Subscribing facemovie to our messages

            self.facemovie.start()

            self.process_running = True
        else:
            self.console_logger.error("Cannot start, process already running !")
            self.my_logger.error("Cannot start, process already running !")            

    def on_stopbutton_pressed(self, widget):
        """
        Asks the Facemovie thread to terminate
        """
        self.my_logger.debug("Stop pressed")
        self.console_logger.debug("Stop pressed") 
        self.notify(["STOP"]) # Asking the Facemovie to stop
        self.process_running = False

    def on_destroy(self, widget, data=None):
        """Called when the IvolutionWindow is closed."""
        # Clean up code for saving application state should be added here.
        self.notify(["STOP"]) # Asking the Facemovie to stop
        self.process_running = False

        Gtk.main_quit()
        print "Gtk Exited"

    def on_menu_about_activate(self, widget, data=None):
        """
        Displays the about box for Ivolution
        # FIXME : Can start several about Dialogs at the same time
        """
        if self.AboutDialog is not None:
            about = self.AboutDialog()

    def on_menu_help_activate(self, widget, data=None):
        """
        Opens a browser and points to online help.
        """
        url = "http://jlengrand.github.com/FaceMovie/"
        webbrowser.open(url,new=2) # in new tab if possible
        #print "Should open help"

    #Methods processing data
    def set_parameters(self):
        """
        Sets all needed parameters for create the movie.
        """
        self.in_fo = self.filechooserinput.get_current_folder() + "/" # TODO : Find correct fix
        self.out_fo = self.filechooseroutput.get_current_folder() + "/" # TODO : Find correct fix
        self.param = self.typecombobox.get_active_text()
        self.speed = self.speedcombobox.get_active() # We need and integer between 0 and 2

        # Instantiating the face_params object that will be needed by the facemovie
        par_fo = os.path.join(self.root_fo, get_data("haarcascades"))
        self.face_params = FaceParams.FaceParams(par_fo,
                                                self.in_fo,
                                                self.out_fo,
                                                self.param,
                                                self.sort,
                                                self.mode,
                                                self.speed)

    def print_parameters(self):
        print "#########"
        print "Settings:"
        print "input folder :   %s" %( self.in_fo)
        print "output folder :   %s" %( self.out_fo)

        print "Face Type :   %s" %( self.param)
        print "Speed chosen :   %s" %( self.speed)
        print "Mode chosen :   %s" %( self.mode)
        print "Sort method :   %s" %( self.sort)

        print "#########"   


    def setup_logger(self):
        """
        Configures our logger to save error messages
        Start logging in file here
        """
        personal_dir = "~/.ivolution"
        log_root = 'fm.log'
        log_file = os.path.join(os.path.expanduser(personal_dir),log_root) 

        # create logger for  'facemovie'
        self.my_logger = logging.getLogger('FileLog')
        
        self.my_logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        
        #fh = logging.StreamHandler()
        fh = logging.FileHandler(log_file)

        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        self.console_logger = logging.getLogger('ConsoleLog')
        self.console_logger.setLevel(logging.DEBUG) # not needed

        ch = logging.StreamHandler()
        #ch.setLevel(logging.DEBUG) # not needed

        # add the handlers to the logger
        self.my_logger.addHandler(fh)
        
        self.my_logger.info("######") # Separating different sessions

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

            if message[0] == "PROGRESS": # progress bar
                # big steps performed

                # Uses GLib to run Thread safe operations on GUI
                GLib.idle_add(self.progressbar.set_fraction, float(message[2]))
                GLib.idle_add(self.progressbar.set_text, message[1])

                if float(message[2]) >= 1.0: # 100% of process
                    self.my_logger.debug("Reached end of facemovie process")
                    #self.console_logger.debug("Reached end of facemovie process") 
                    self.process_running = False  

            elif message[0] == "STATUS": # status label
                # intermediate results
                GLib.idle_add(self.statuslabel.set_text, message[1])
                #pass

        elif len(message) > 1: #system commands shall be ignored
            self.console_logger.debug("Unrecognized command")
            self.my_logger.debug("Unrecognized command")
            self.console_logger.debug(message)
            self.my_logger.debug(message)   

if __name__ == "__main__":
    app = IvolutionWindow()
    Gtk.main()        