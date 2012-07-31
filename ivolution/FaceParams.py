"""
.. module:: FaceParams
   :platform: Unix, Windows
   :synopsis: Simple class used to store parameters used for Face detection.

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""
import cv
import os

import logging

import training_types

class FaceParams(object):
    '''
    Simple class used to store parameters used for Face detection
    '''
    def __init__(self, xml_folder, input_folder, output_folder, training_type="frontal_face", sort="name", mode="conservative",speed=1):
        """
        Creates dictionary for all types of training files
        some of them shall never be used. Perhaps would it be good to lower the dict size, or hide some of them
        postpend .xml

        :param xml_folder: the location where xml files are located
        :type xml_folder: string
        :param training_type: the type of profile we are going to use
        :type training_type: string
                                
        :param input_folder: the location where images are located
        :type input_folder: string
        :param output_folder: the location where the video will be saved
        :type output_folder: string
        :param speed: the time delay between frames in the video
        :type speed: int                                             
        :param mode: the creation mode of the video. Defines whether images are cropped, or black borders are added.
        :type mode: string
        :param sort: the method used to sort images chronologically
        :type sort: string                       
        """

        self.input_folder = input_folder
        self.output_folder = output_folder
        self.speed = 1 # between 0 and 2
        self.mode = mode # conservative or crop
        self.sort = sort # name or exif

        cascade_name = training_types.simple_set[training_type] + ".xml"
        # Setting up some default parameters for Face Detection
        self.face_cascade = cv.Load(os.path.join(xml_folder, cascade_name))

        # To be defined more precisely
        self.min_size = (20,20)
        self.image_scale = 2 # Image scaling chosen for classification (2) 
        self.haar_scale = 1.2 # Haar scaling chosen for classification (1.2) 
        self.min_neighbors = 2 # the Minimum number of neighbors to be defined (2) 
        self.haar_flags = 0 # the chosen number of haar flags (0)

        self.log()

    def __str__(self):
        """
        More convenient print method
        """
        print "---------"
        print "Selected parameters for your Facemovie:"
        print "Input Folder: %s" % (self.input_folder)
        print "Output Folder: %s" % (self.output_folder)
        print "Speed for movie:  %s" % (["slow", "medium", "fast"][self.speed])
        print "Video Mode: %s" % (self.mode)
        print "Files sorting method: %s" % (self.sort)
        print "-----"
        print "Selected parameters for Face Detection:"
        print "Selected cascade for Face detection : %s" % ("haarcascade_frontalface_alt")
        print "Minimum Size (x, y): %d, %d" % (self.min_size[0], self.min_size[1])
        print "Image scaling: %d)" % (self.image_scale)
        print "Haar scaling: %f" % (self.haar_scale)
        print "Number of Haar flags: %d" % (self.haar_flags)
        print "Minimum number of neighbors: %d" % (self.min_neighbors)
        print "---------"

    def log(self):
        """
        Log configuration 
        """
        my_logger = logging.getLogger('FileLog')
        params_str =  "---------"
        params_str += "Selected parameters for your Facemovie:"
        params_str += "Input Folder: %s" % (self.input_folder)
        params_str += "Output Folder: %s" % (self.output_folder)
        params_str += "Speed for movie:  %s" % (["slow", "medium", "fast"][self.speed])
        params_str += "Video Mode: %s" % (self.mode)
        params_str += "Files sorting method: %s" % (self.sort)
        params_str += "-----"
        params_str += "Selected parameters for Face Detection:"
        params_str += "Selected cascade for Face detection : %s" % ("haarcascade_frontalface_alt")
        params_str += "Minimum Size (x, y): %d, %d" % (self.min_size[0], self.min_size[1])
        params_str += "Image scaling: %d)" % (self.image_scale)
        params_str += "Haar scaling: %f" % (self.haar_scale)
        params_str += "Number of Haar flags: %d" % (self.haar_flags)
        params_str += "Minimum number of neighbors: %d" % (self.min_neighbors)
        params_str += "---------"  
        my_logger.debug(params_str)
      