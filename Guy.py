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
        self.in_x = None
        self.in_y = None
        self.in_channels = image.nChannels
        self.name = image_id # Name of the picture used as input
        self.out_im = None
        self.in_image = None # input image

        
        self.faces = [] # List of faces detected for this input 
        # TODO: should eyes be tied to a precise face ?  
        self.eyes = []  # List of eyes detected for this input
        
        # Some operations on variables
        
        (self.in_x, self.in_y) = cv.GetSize(image) # image size in x, y
        
        # Creation of the images
        self.in_image = cv.CreateImage((self.in_x, self.in_y),cv.IPL_DEPTH_8U, self.in_channels)
        cv.Copy(image, self.in_image)
        self.out_im = cv.CreateImage((self.in_x, self.in_y),cv.IPL_DEPTH_8U, self.in_channels)
        cv.Zero(self.out_im) # put everything to 0
        

    def search_face(self, face_params):
        """
        Search on the picture for a face. 
        Populates faces
        """
        # Allocate the temporary images
        gray = cv.CreateImage((self.in_x, self.in_y), 
                              cv.IPL_DEPTH_8U, 
                              1)
        smallImage = cv.CreateImage((cv.Round(self.in_x / face_params.image_scale),
                                     cv.Round (self.in_y / face_params.image_scale)), 
                                    cv.IPL_DEPTH_8U ,
                                    1)        
        
        # Converts color input image to grayscale
        cv.CvtColor(self.in_image, gray, cv.CV_BGR2GRAY)
        # Scales input image for faster processing
        cv.Resize(gray, smallImage, cv.CV_INTER_LINEAR)
        # Equalizes the histogram
        cv.EqualizeHist(smallImage, smallImage)
        
        # Detect the faces
        self.faces = cv.HaarDetectObjects(smallImage, 
                                     face_params.face_cascade, 
                                     cv.CreateMemStorage(0),
                                     face_params.haar_scale, 
                                     face_params.min_neighbors, 
                                     face_params.haar_flags, 
                                     face_params.min_size)
        
    def in_display(self, time):
        """
        Displays the input image, for time ms.
        Setting time to 0 causes the image to remains open.
        """
        cv.NamedWindow(self.name)
        cv.ShowImage(self.name, self.in_image)
        cv.WaitKey(time)    
        cv.DestroyWindow(self.name)
        
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
        cv.DestroyWindow(win_name)

    def show_debug(self, face_params, time):
        """
        Function that may be used after having populated faces. 
        Displays each guy, with a red square around detected face, 
        for time ms.
        
        TODO: green square around most probable face? 
        See the doc !
        """
        debug_image = cv.CreateImage((self.in_x, self.in_y),cv.IPL_DEPTH_8U, self.in_channels)
        cv.Copy(self.in_image, debug_image)
        
        if self.has_face() : 
            for ((x, y, w, h), n) in faces:
                # the input to cv.HaarDetectObjects was resized, so scale the
                # bounding box of each face and convert it to two CvPoints
                pt1 = (int(x * face_params.image_scale), int(y * face_params.image_scale))
                pt2 = (int((x + w) * face_params.image_scale), int((y + h) * face_params.image_scale))
                cv.Rectangle(debug_image, 
                             pt1, 
                             pt2, 
                             cv.RGB(255, 0, 0), 
                             3, 8, 0)# If faces are found       
            
        win_name = self.name + " - debug"
        cv.NamedWindow(win_name)
        cv.ShowImage(win_name, debug_image)
        cv.WaitKey(time)
        cv.DestroyWindow(win_name)      
            
    def num_faces(self):
        """
        Returns the number of faces found for this guy
        """
        return len(self.faces)        

    def has_face(self):
        """
        Returns True if at least one face has been found
        """
        return (len(self.faces) > 0)

if __name__ == "__main__":
    # quick and dirty tests
    name = "input/search.jpg"
    im = cv.LoadImage(name)
    
    my_guy = Guy(im, os.path.basename(name))
    my_guy.in_display(100)
    my_guy.out_display(1000)
    