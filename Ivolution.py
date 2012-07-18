#!/usr/bin/env python

import os

from gi.repository import Gtk

from AboutDialog import AboutDialog

from facemovie import Facemovie_lib
from facemovie import FaceParams

class Ivolution():       
    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("data/ui/IvolutionWindow.glade")
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

        self.in_fo = "" # Input folder, where imaes are located

        self.facemovie = None

        self.AboutDialog = None # class

        self.setup()

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
        self.set_parameters()
        self.print_parameters()

    def on_stopbutton_pressed(self, widget):
        """
        Asks the Facemovie thread to terminate
        """
        print "Stop"    

    def on_destroy(self, widget, data=None):
        """Called when the IvolutionWindow is closed."""
        # Clean up code for saving application state should be added here.
        Gtk.main_quit()
        print "Gtk Exited"

    def on_menu_about_activate(self, widget, data=None):
        """
        Displays the about box for Ivolution
        # FIXME : Can start several contents Windows at the same time
        """
        if self.AboutDialog is not None:
            about = self.AboutDialog()
            #response = about.run()
            #about.destroy()



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
        par_fo = os.path.join(self.root_fo, "haarcascades")
        self.face_params = FaceParams.FaceParams(par_fo,
                                                self.in_fo,
                                                self.out_fo,
                                                self.param,
                                                self.sort,
                                                self.mode,
                                                self.speed)

    def print_parameters(self):
        print self.in_fo
        print self.out_fo
        print self.param
        print self.speed
        print self.mode
        print self.sort

if __name__ == "__main__":
    app = Ivolution()
    Gtk.main()