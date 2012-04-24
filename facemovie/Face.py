'''
Created on 29 mars 2012

@author: jll
'''

class Face(object):
    '''
    Created is an Face-like blob is found using the Face Detection algorithm.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        x_center = None # x position of the face in the image
        y_center = None # y position of the face in the image
        x_size = None # x size of the blob in pixel
        y_size = None # y size of the blob in pixel
        conf = None # confidence indice, indicating the probability of the target to actually be an eye