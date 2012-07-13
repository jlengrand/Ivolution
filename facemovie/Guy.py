"""
.. module:: Guy
   :platform: Unix, Windows
   :synopsis: Class defining a Guy in the sense of the FaceMovie. Corresponds to one input image. An input folder is transformed in fact to a list of guys.

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""
import time
import logging

import cv

class Guy(object):
    """
        A new Guy is declared for each input image. 
        A Guy should have a face, and owns the input image.
    """
    def __init__(self, image_id, date, source):
        """All data linked to an input image

        :param image: the input image, formatted as an OpenCV Image
        :type image: IplImage

        :param image_id: the name of the image, formatted as a string
        :type image_id: string

        :param date: the date where the input image was taken.
        :type date: datetime
        """
        self.in_x = None
        self.in_y = None
        
        self.name = image_id # Name of the picture used as input
        self.date = self.find_date(date) # date where image was taken
        self.source = source
        
        self.faces = [] # List of faces detected for this input 
        
        # Some operations on variables
        #image = self.load_image() # used to get size
        image = self.load_image()
        #(self.or_x, self.or_y) = cv.GetSize(image) # image size in x, y
        (self.in_x, self.in_y) = cv.GetSize(image) # image size in x, y
        # FIXME : Time for me to find a better solution
        self.in_channels = image.nChannels
        self.depth = image.depth
        
        # Two variables used to define the new center of interest of the image
        # they are defined as the middle of input image at first
        self.x_center = 0
        self.y_center = 0

        self.ratio = 1.0

    def resized_dims(self):
        """
        Calculates the dimensions of the full image after having been resized using ratio.
        :returns list of int - list of two integers, being (resized_x, resized_y)
        """
        inx = int(self.ratio * self.in_x)
        iny = int(self.ratio * self.in_y)
        return (inx, iny)

    def resized_center(self):
        """
        Calculates the center position of the full image after having been resized using ratio.
        :returns list of int - list of two integers, being (new_center_x, new_center_y)
        """
        xc = int(self.ratio * self.x_center)
        yc = int(self.ratio * self.y_center)
        return (xc, yc)

    def load_image(self):
        """
        This function is used to load the image when needed. To reduce memory load, only its location is saved in real time
        Returns an iplImage.
        
        :returns IplImage - the input image, not modified; loaded using self.source
        """
        image = cv.LoadImage(self.source)
        
        return image
        
    def find_date(self, date):
        """This function takes a date as a string, and returns a date object.
        Used afterwards to sort images chronologically

        :param date: The date where the image was taken
        :type date: string

        :returns:  datetime -- Returns a date object according to time library.
        :raises: In case of error, set the date to be the current time.
        """
        try: 
            my_date = time.strptime(date, "%Y:%m:%d %H:%M:%S")
        except Exception:
            my_logger = logging.getLogger('FileLog')
            my_logger.error("Impossible to parse date for %s" %(self.name))
            my_date = time.time()
        return my_date

    def search_face(self, face_params):
        """
        Search on the picture for a face. 
        Populates faces list. 
        This function is the only one containing scaling information

        Set several Guy information, such as the face size, or the virtual center of the image

        :param face_params: The type of file to be used to train the classifier.
        :type face_params: string

        Once Faces have been found, they are listed and ordered
        """
        
        # Load the input image
        in_image = self.load_image()
        
        # Allocate the temporary images
        gray = cv.CreateImage((self.in_x, self.in_y), 
                              cv.IPL_DEPTH_8U, 
                              1)
        smallImage = cv.CreateImage((cv.Round(self.in_x / face_params.image_scale),
                                     cv.Round (self.in_y / face_params.image_scale)), 
                                    cv.IPL_DEPTH_8U ,
                                    1)        
        
        # Converts color input image to grayscale
        cv.CvtColor(in_image, gray, cv.CV_BGR2GRAY)
        # Scales input image for faster processing
        cv.Resize(gray, smallImage, cv.CV_INTER_LINEAR)
        # Equalizes the histogram
        cv.EqualizeHist(smallImage, smallImage)
        
        # Detect the faces
        small_faces = cv.HaarDetectObjects(smallImage, 
                                     face_params.face_cascade, 
                                     cv.CreateMemStorage(0),
                                     face_params.haar_scale, 
                                     face_params.min_neighbors, 
                                     face_params.haar_flags, 
                                     face_params.min_size)
        
        # Resizing faces to full_scale
        for face in small_faces:
            if len(face): # if faces have been found
                ((x, y, w, h), n) = face
                big_face = ((int(x * face_params.image_scale), 
                             int(y * face_params.image_scale), 
                             int(w * face_params.image_scale), 
                             int(h * face_params.image_scale)), n)
                self.faces.append(big_face)
        
        # sorting faces to keep only the most probable one
        self.sort_faces()
        self.update_center() # finds center of face in image
        
    def update_center(self):
        """
        Using sorted faces, defines the new center of interest of the output image

        Updates the center of the image, using the most probable face as reference. 
        If no face was found, the center is not updated.
        """
        if self.has_face():
            ((x, y, w, h), n) = self.faces[0]
            self.x_center = x + w / 2
            self.y_center = y + h / 2

    def sort_faces(self):
        """
        Sorts faces by number of neighbours found, most probable one first

        :param face_params: The type of file to be used to train the classifier.
        :type face_params: string

        :returns:   A list of faces, ordered by probability. If no faces is found, returns a void list.
        """
        if self.has_face() : # needed ?
            self.faces.sort(key= lambda prob : prob[1], reverse=True)
        else : 
            self.faces = []
    
    def set_ratio(self, reference):
        """
        """
        self.ratio = reference / float(self.faces[0][0][3])

    def create_default_output(self, size, point):
        """
        Creates image output, centering the face center with the required position
        If eq_ratio is set to something different than one, input image is scaled
        so that face/size = eq_ratio

        :param size: The size of the ouput image in [x, y] (in pixels)
        :type size: list of 2 ints
        :param point: The location of the Guy image center, after image has been cropped(in pixels)
        :type point: list of 2 ints

        :returns:  IplImage --  The ouput image, centered to fit with all other images

        """

        out_im = cv.CreateImage((size[0], size[1]),cv.IPL_DEPTH_8U, self.in_channels)
        cv.Zero(out_im)   

        # We want to place the input image so that the center of the face matches
        # x_center and y_center  
        (w, h) = self.resized_dims()
        (x_center, y_center) = self.resized_center()

        xtl = point[0] - x_center # position of top left corner in output image
        ytl = point[1] - y_center # position of top left corner in output image
            
        rect = (xtl, ytl, w, h) # creating the bounding rectangle on output image
        cv.SetImageROI(out_im, rect)
        
        # Load input image and resizes it to fit with what we want
        in_image = self.load_image()
        norm_im = cv.CreateImage((w, h),cv.IPL_DEPTH_8U, self.in_channels)
        cv.Resize(in_image, norm_im)

        # creating the final out image
        cv.Copy(norm_im, out_im)
        cv.ResetImageROI(out_im) 

        return out_im

    def create_crop_output(self, size, point):
        """
        Creates image output, centering the face center with the required position
        In this case, the image from which we have to select a ROI is the normalized image. 
        The output image shall be smaller than all other images.

        :param size: The size of the ouput image in [x, y] (in pixels)
        :type size: list of 2 ints
        :param point: The location of the Guy image center, after image has been cropped(in pixels)
        :type point: list of 2 ints

        :returns:  IplImage --  The ouput image, centered to fit with all other images

        """
        out_im = cv.CreateImage((size[0], size[1]),cv.IPL_DEPTH_8U, self.in_channels)
        cv.Zero(out_im)   
  
        (w, h) = self.resized_dims()
        (x_center, y_center) = self.resized_center()

        xtl = x_center - point[0] # position of top left corner in output image
        ytl = y_center - point[1] # position of top left corner in output image
        
        rect = (xtl, ytl, size[0], size[1]) # creating the bounding rectangle on output image

        # Load input image and resizes it to fit with what we want
        in_image = self.load_image()
        norm_im = cv.CreateImage((w, h),cv.IPL_DEPTH_8U, self.in_channels)
        cv.Resize(in_image, norm_im)
        
        cv.SetImageROI(norm_im, rect)

        # creating the final out image
        cv.Copy(norm_im, out_im)
        cv.ResetImageROI(out_im) 

        return out_im

    def num_faces(self):
        """
        Returns the number of faces found for this guy
        
        :returns:  int -- The number of faces found for the input image
        """             
        return len(self.faces)        

    def has_face(self):
        """
        Returns True of False whether images have been found for the current image or not.

        :returns:  boolean -- True if at least one face has been found
        """
        return (len(self.faces) > 0)
    