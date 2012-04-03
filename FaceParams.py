'''
Created on 30 mars 2012

@author: jll
'''
import cv
import os

class FaceParams(object):
    '''
    Simple class used to store parameters used for Face detection
    '''
    def __init__(self, xml_folder, i_scale=2, h_scale=1.2, h_flags=0, mn=2):
        '''
        Constructor
        '''
        # Setting up some default parameters for Face Detection
        self.face_cascade = cv.Load(os.path.join(xml_folder, "haarcascade_frontalface_alt.xml"))
        self.eye_cascade = cv.Load(os.path.join(xml_folder, "haarcascade_eye.xml"))

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