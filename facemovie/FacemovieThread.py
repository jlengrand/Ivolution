"""
.. module:: Facemovie
   :platform: Unix, Windows
   :synopsis: Main class of the application. Contains the core image processing functions.Plays the role of a controller for the application, as it supports the communication layer with the end user interface. 

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""
import os
import sys
import threading

import logging

from facemovie import Facemovie_lib

class FacemovieThread(threading.Thread):
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

        self.face_params = face_params
        self.facemovie = Facemovie_lib.FaceMovie(self.face_params)

    def run(self):
        my_logger = logging.getLogger('FileLog')
        my_logger.debug("Thread started")

        self.facemovie.list_guys()
        my_logger.debug("Guys listed")
        self.facemovie.prepare_faces() # I want to search for the faces, and characteristics of the images   
        my_logger.debug("Faces prepared")
        self.facemovie.find_final_dimensions() # finds output size for desired mode.
        my_logger.debug("Final dimensions found")
        self.facemovie.save_movie()       
        my_logger.debug("Movie saved")

        my_logger.debug("Thread terminated")
