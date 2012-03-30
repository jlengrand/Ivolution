'''
Created on 29 mars 2012

@author: jll
'''
import cv

import os # needed only for main. Shall be removed

class Guy(object):
    '''
    Represents the user on the people at a fixed time. 
    All datas found for this time may be found here.
    '''
    def __init__(self, image, image_id):
        '''
        Constructor
        '''
        self.in_image = image # input image
        self.in_x = None
        self.in_y = None
        self.in_channels = self.in_image.nChannels
        self.name = image_id # Name of the picture used as input
        self.out_im = None
        
        self.faces = [] # List of faces detected for this input 
        # TODO: should eyes be tied to a precise face ?  
        self.eyes = []  # List of eyes detected for this input
        
        # Some operations on variables
        
        (self.in_x, self.in_y) = cv.GetSize(self.in_image) # image size in x, y
        
        # Creation of the output image
        self.out_im = cv.CreateImage((self.in_x, self.in_y),cv.IPL_DEPTH_8U, self.in_channels)
        cv.Zero(self.out_im) # put everything to 0
        
        
    def in_display(self, time):
        """
        Displays the input image, for time ms.
        Setting time to 0 causes the image to remains open.
        """
        cv.NamedWindow(self.name)
        cv.ShowImage(self.name, self.in_image)
        cv.WaitKey(time)      
        
    def out_display(self, time):
        """
        Displays the output image, for time ms.
        Setting time to 0 causes the image to remains open.
        Window name slightly changed to match output
        """
        win_name = self.name + " - out"
        cv.NamedWindow(win_name)
        cv.ShowImage(win_name, self.in_image)
        cv.WaitKey(time)
    
if __name__ == "__main__":
    # quick and dirty tests
    name = "input/search.jpg"
    im = cv.LoadImage(name)
    
    my_guy = Guy(im, os.path.basename(name))
    my_guy.in_display(100)
    my_guy.out_display(1000)
    