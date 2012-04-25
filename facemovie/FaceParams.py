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
    def __init__(self, xml_folder, training_type, i_scale=2, h_scale=1.2, h_flags=0, mn=2):
        '''
        Constructor
        '''
        # Creates dictionary for all types of training files
        # some of them shall never be used. Perhaps would it be good to lower the dict size, or hide some of them
        self.training_types = {#eyes
                          'eyes':"haarcascade_eye", 
                          'glasses':"haarcascade_eye_tree_eyeglasses",
                          'left eye splits':"haarcascade_lefteye_2splits",
                          'eye pair big':"haarcascade_mcs_eyepair_big",
                          'eye pair small':"haarcascade_mcs_eyepair_small",
                          'left eye':"haarcascade_mcs_lefteye",
                          'right eye':"haarcascade_mcs_righteye",
                          'right eye splits':"haarcascade_righteye_2splits",
                          # frontal faces
                          'frontal face alt':"haarcascade_frontalface_alt", 
                          'frontal face alt2':"haarcascade_frontalface_alt2", 
                          'frontal face':"haarcascade_frontalface_default", 
                          #profile face
                          'profile face':"haarcascade_profileface", 
                          #body
                          'full body':"haarcascade_fullbody", 
                          'lower body':"haarcascade_lowerbody", 
                          'upper body mcs':"haarcascade_mcs_upperbody", 
                          'upper body':"haarcascade_upperbody", 
                          #ear
                          'left ear':"haarcascade_mcs_leftear", 
                          'right ear':"haarcascade_mcs_rightear", 
                          #mouth
                          'mouth':"haarcascade_mcs_mouth",
                          #nose
                          'nose':"haarcascade_mcs_nose"
                          }
        # postpend .xml
        cascade_name = self.training_types[training_type] + ".xml"
        # Setting up some default parameters for Face Detection
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
        
    def get_types(self):
        """
        Lists all possible types for training files
        Returns list of string
        """
        types = []
        for key, val in self.training_types.iteritems():
            types.append(key)
        return types