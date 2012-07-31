"""
.. module:: Facemovie
   :platform: Unix, Windows
   :synopsis: Main class of the application. Contains the core image processing functions.Plays the role of a controller for the application, as it supports the communication layer with the end user interface. 

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""
import sys
import threading
import time

import logging

import Facemovie_lib

class Observer():
    """
    Implements a simple Observer from the Observer pattern
    """

    def __init__(self, name="bob"):
        """
        """
        self.name = name


    def update(self, message):
        """
        """
        if message is not None:
            #print "%s received %s" %(self.name, message)
            pass

    def __str__(self):
        return self.name


class Observable():
    """
    Implements a simple Observable from the Observer pattern
    """

    def __init__(self):
        """
        """
        self.val = 1
        self.obs_collection = []


    def subscribe(self, observer):
        """
        """
        try:
            if not(observer in self.obs_collection):
                self.obs_collection.append(observer)
                #print "%s added to collection" %(str(observer))
            else:
                #print "%s already in collection" %(str(observer))
                pass

        except TypeError:
            #print "Failed to add %s" %(str(observer))
            pass

    def unsubscribe(self, observer):
        """
        """
        try:
            if observer in self.obs_collection:
                self.obs_collection.remove(observer)
                #print "%s removed from collection" %(str(observer))
            else:
                #print "%s not in collection" %(str(observer))
                pass

        except TypeError:
            #print "Failed to remove %s" %(str(observer))
            pass

    def notify(self, message):
        """
        """
        for observer in self.obs_collection:
            #print "sent %s to %s" %(message, str(observer))
            observer.update(message)


    def set_val(self, val=1):
        """
        """
        self.val += val
        self.notify(str(self.val))


class FacemovieThread(threading.Thread, Observable, Observer):
    '''
    Creates a Thread version of Facemovie using the facemovie_lib.
    This class can then be run anywhere, from a GUI, script, ...
    '''    
    def __init__(self, face_params):
        """
        Initializes all parameters of the application. Input and output folders
         are defined, together with the classifier profile.

        :param face_params: A faceparams object that contains all needed information to run the Facemovie.
        :type face_params: FaceParams      
        """
        threading.Thread.__init__(self)
        Observable.__init__(self)
        Observer.__init__(self, "Facemovie")

        self.stop_process = False

        self.face_params = face_params
        self.facemovie = Facemovie_lib.FaceMovie(self.face_params)

        self.my_logger = logging.getLogger('FileLog')
        self.console_logger = logging.getLogger('ConsoleLog')

    def update(self, message):
        """
        Trigerred by IvolutionWindow. 
        Uses the Observer pattern to inform the user about the progress of the GUI.
        """
        if message[0] == "STOP":
            self.console_logger.debug("Facemovie is going to stop")
            self.my_logger.debug("Facemovie is going to stop")

            self.stop_process = True
        elif message[0] == "START":
            self.console_logger.debug("Facemovie is asked to stop")
            self.my_logger.debug("Facemovie is asked to stop")

            self.stop_process = False
        else:
            self.console_logger.debug(message[0])
            self.my_logger.debug(message[0])
    def run(self):

        # FIXME : Quite ugly way of doing. Find better!
        if not self.stop_process:
            self.facemovie.list_guys()
            self.my_logger.debug("Guys listed")
            self.notify(["Pictures listed", 0.2])

        if not self.stop_process:
            self.facemovie.prepare_faces() # I want to search for the faces, and characteristics of the images   
            self.my_logger.debug("Faces prepared")
            self.notify(["Faces detected", 0.6])

        if not self.stop_process:
            self.facemovie.find_final_dimensions() # finds output size for desired mode.
            self.my_logger.debug("Final dimensions found")
            self.notify(["Video dimensions found", 0.8])

        if not self.stop_process:
            self.facemovie.save_movie()       
            self.my_logger.debug("Movie saved")
            self.notify(["Movie saved, Finished!", 1.0])

        if not self.stop_process:
            self.my_logger.debug("Thread terminated")

        if self.stop_process:
            self.notify(["Process cancelled!", 1.0])            