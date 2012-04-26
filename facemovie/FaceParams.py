'''
Created on 30 mars 2012

@author: jll
'''
import cv
import os

import training_types

class FaceParams(object):
    '''
    Simple class used to store parameters used for Face detection
    '''
    def __init__(self, xml_folder, training_type, i_scale=2, h_scale=1.2, h_flags=0, mn=2):
        '''
        Constructor
        '''
        # Creates dictionary for all types of training files
        # some of them shall never be used. Perhaps would it be good to lower the dict size, or hide some of them
        # postpend .xml
        cascade_name = training_types.simple_set[training_type] + ".xml"
        # Setting up some default parameters for Face Detection
        print os.path.join(xml_folder, cascade_name)
        self.face_cascade = cv.Load(os.path.join(xml_folder, cascade_name))

        # To be defined more precisely
        self.min_size = (20,20)
        self.image_scale = i_scale
        self.haar_scale = h_scale
        self.min_neighbors = mn
        self.haar_flags = h_flags
        
    def __str__(self):
        """
        More convenient print method
        """
        print "---------"
        print "Selected parameters for Face Detection:"
        print "Selected cascade for Face detection : %s" % ("haarcascade_frontalface_alt")
        print "Minimum Size (x, y): %d" % (self.min_size[0], self.min_size[1])
        print "Image scaling: %d, %d)" % (self.image_scale)
        print "Haar scaling: %f" % (self.haar_scale)
        print "Number of Haar flags: %d" % (self.haar_flags)
        print "Minimum number of neighbors: %d" % (self.min_neighbors)
        print "---------"