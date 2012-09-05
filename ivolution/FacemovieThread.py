"""
.. module:: Facemovie
   :platform: Unix, Windows
   :synopsis: Main class of the application. Contains the core image processing functions.Plays the role of a controller for the application, as it supports the communication layer.

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""
import threading

import logging

import Facemovie_lib

from util.Notifier import Observer
from util.Notifier import Observable


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
        Observer.__init__(self, "Application")

        self.stop_process = False

        self.face_params = face_params
        self.facemovie = Facemovie_lib.FaceMovie(self.face_params)
        self.facemovie.subscribe(self)  # Subscribing to facemovie reports
        self.subscribe(self.facemovie)  # Used to send request to stop

        self.my_logger = logging.getLogger('IvolutionFile.Thread')
        #self.console_logger = logging.getLogger('ConsoleLog')

    def update(self, message):
        """
        Trigerred by IvolutionWindow.
        Uses the Observer pattern to inform the user about the progress of the GUI.
        """
        if len(message) == 1:  # system commands
            if message[0] == "STOP":
                #self.console_logger.debug("Facemovie is going to stop")
                self.my_logger.debug("Facemovie is going to stop")

                self.stop_process = True
                self.notify(["Lib", ["STOP"]])
            else:
                #self.console_logger.debug("Unrecognized system command")
                self.my_logger.debug("Unrecognized system command")
                ##self.console_logger.debug(message)
                self.my_logger.debug(message)
        elif len(message) == 2:  # notifications

            ##self.console_logger.debug(message)
            self.my_logger.debug(message)
            if message[0] == "FILEADD":
                self.notify(["Interface", [message[0], message[1], 0]])
            else:
                # notify gui about small updates
                self.notify(["Interface", ["STATUS", message[0], message[1]]])

            # checking for fatal error
            if message[0] == "Error":
                #self.console_logger.debug("Fatal Error detected")
                self.my_logger.debug("Fatal Error detected")
                self.stop_process = True
                self.notify(["Lib", ["STOP"]])

        elif len(message) == 3:  # notifications
            if message[0] == "FILEDONE":
                self.notify(["Interface", message])

        else:
            #self.console_logger.debug("Unrecognized command")
            self.my_logger.debug("Unrecognized command")
            #self.console_logger.debug(message)
            self.my_logger.debug(message)

    def run(self):
        if not self.stop_process:

            self.my_logger.debug("Listing pictures")
            self.notify(["Interface", ["PROGRESS", "Listing pictures", 0.0]])
            num_guys = self.facemovie.list_guys()

            # FIXME: Later to be done in Lib
            if num_guys < 0:
                self.notify(["Interface", ["STATUS", "Source folder not found", 0.0]])
                self.stop_process = True
            elif num_guys == 0:
                self.notify(["Interface", ["STATUS", "No image found in source folder", 0.0]])
                self.stop_process = True

        if not self.stop_process:
            self.my_logger.debug("Detecting Faces")
            self.notify(["Interface", ["PROGRESS", "Detecting Faces", 0.2]])
            self.facemovie.prepare_faces()  # I want to search for the faces, and characteristics of the images

        if not self.stop_process:
            self.my_logger.debug("Calculating video requirements")
            self.notify(["Interface", ["PROGRESS", "Calculating video requirements", 0.6]])
            self.facemovie.find_final_dimensions()  # finds output size for desired mode.

        if not self.stop_process:
            self.my_logger.debug("Generating movie")
            self.notify(["Interface", ["PROGRESS", "Generating movie", 0.8]])
            self.facemovie.save_movie()
            self.my_logger.debug("Movie saved")
            self.notify(["Interface", ["PROGRESS", "Movie saved, Finished!", 1.0]])
            # updating status to avoid remanent messages
            self.notify(["Interface", ["STATUS", " ", 1.0]])

        if not self.stop_process:
            self.my_logger.debug("Thread terminated")

        if self.stop_process:
            self.notify(["Interface", ["PROGRESS", "Process cancelled!", 1.0]])
