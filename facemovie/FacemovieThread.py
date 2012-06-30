"""
.. module:: Facemovie
   :platform: Unix, Windows
   :synopsis: Main class of the application. Contains the core image processing functions.Plays the role of a controller for the application, as it supports the communication layer with the end user interface. 

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""
import os
import sys
import threading

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
        print "In thread !"

        self.facemovie.list_guys()
        self.facemovie.prepare_faces() # I want to search for the faces, and characteristics of the images   
        self.facemovie.find_final_dimensions() # finds output size for desired mode.
        self.facemovie.save_movie()       

        print "Finished!"
