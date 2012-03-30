'''
Created on 29 mars 2012

@author: jll
'''

class Eye(object):
    '''
    Created is an Eye-like blob is found using the Face Detection algorithm.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        x_pos = None # x position of the eye in the image
        y_pos = None # y position of the eye in the image
        x_size = None # x size of the blob in pixel
        y_size = None # y size of the blob in pixel
        conf = None # confidence indice, indicating the probability of the target to actually be an eye