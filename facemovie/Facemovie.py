"""
.. module:: Facemovie
   :platform: Unix, Windows
   :synopsis: Main class of the application. Contains the core image processing
    functions.
   Plays the role of a controller for the application, as it supports the
    communication layer with the end user interface. 

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""
import os
import sys
import sys

import cv

from lib import exif
import Guy

class FaceMovie(object):
    '''
    Main class of the whole application. 
    Contains the core image processing functions.
    Takes a bunch of parameters and a list of images and tries to create a 
    video out of it.
    Contains general methods, aimed at being used trough an interface.
    '''    
    def __init__(self, in_folder, out_folder, face_params):
        """
        Initializes all parameters of the application. Input and output folders
         are defined, together with the classifier profile.

        :param in_folder: the location where input files will be searched
        :type in_folder: string
        :param out_folder: the location where the outputs will be saved
        :type out_folder: string
        :param face_param: the location of the profile file used to train the classifier
        :type face_param: string        
        """
        self.CV_MAX_PIXEL = 13000 * 13000 # experimental maximal size of an IplImage
        
        self.source= in_folder # Source folder for pictures
        self.out = out_folder # Folder to save outputs
        
        self.guys = [] # List of pictures in source folder
        
        # Retrieving parameters for Face Detection
        self.face_params = face_params
        
        # Position of the center in output images 
        self.x_center = 0
        self.y_center = 0

        # minimum size needed on right of center
        self.x_af = 0
        self.y_af = 0
        
        # Needed minimum size of output image
        self.dim_x = 0
        self.dim_y = 0
        
        self.normalize = False
        # thumbmails
        self.crop = False
        self.cropdims = [0, 0] # user defined desired dimensions for cropping
        self.width = [0, 0]
        self.height = [0, 0]
        
        self.face_mean = [0, 0]
        self.sort_method = "n" # sorting by name or using metadata (n or e)
        
    def set_crop_dims(self, crop_x, crop_y):
        """
        Sets the cropping dimension in case they have been provided by the end user

        :param crop_x: dimension of the desired cropping in x (in number of face size)
        :type crop_x: int
        :param crop_y: dimension of the desired cropping in y (in number of face size)
        :type crop_x: int        
        """
        self.cropdims = [crop_x, crop_y]
        
    def list_guys(self):
        """
        Aims at populating the guys list, using the source folder as an input. 
        Guys list shall be sorted chronologically.
        In case no valid date is found, it is set to ''.
        """
        try:
            os.path.exists(self.source)
            os.path.isdir(self.source) # checking if folder exists
        except : # find precise exception
            print "ERROR : Source folder not found ! Exiting. . ." 
            sys.exit(0)
            
        # just listing directory. Lets be more secure later
        files = os.listdir(self.source)
        
        # loading images, create Guys and store it into guys
        for token in files :
            guy_source = os.path.join(self.source, token)
            image = cv.LoadImage(guy_source)
            guy_name = os.path.splitext(token)[0]
            print guy_source
            try:
                guy_date = exif.parse(guy_source)['DateTime']
            except Exception:
                guy_date = ''

            a_guy = Guy.Guy(guy_name, guy_date, guy_source)
         
            # populating guys
            self.guys.append(a_guy)
       
        # Sorting either by exif date or name
        if self.sort_method == "e":
            print "Sorting files using EXIF metadata"
            self.guys.sort(key=lambda g: g.date)
        else: # default is sort by name
            print "Sorting files using file name"
            self.guys.sort(key=lambda g: g.name)
            
    def search_faces(self):
        """
        Searches for all faces in the guys we have
        Results to be stored directly in guys

        Takes each image one after the other, and create a guy out of it. 
        The Face of each guy is searched.
        In case no face is found, a warning is returned and Guy is set to None
        """
        for a_guy in self.guys:
            a_guy.search_face(self.face_params)
            if a_guy.has_face(): # face(s) have been found
                print "%d faces found for %s" % (a_guy.num_faces(), a_guy.name)
            else:
                print "Warning! No face found for %s" %(a_guy.name)
    
    def find_reference(self):
        """
        Searched for the best face size we want to have. 
        Defined (for now), as the smallest of all found faces.

        :returns int - the reference size of the bounding square for faces.
        """
        references = []
        for a_guy in self.guys:
            if a_guy.has_face():
                references.append(a_guy.faces[0][0][3]) # catch face size (width)

        if len(references) == 0:
            print "No face has been found in the whole repository! Exiting. . . "
            sys.exit(0)

        return min(references)

    def normalize_faces(self):
        """
        Creates new images, normalized by face size
        A reference is given in input. The idea is to get all images to have the
        same size in Guy.

        :param reference: the reference size of the face that we want to have (0)
        :type reference: int
        """
        self.normalize = True

        reference = self.find_reference()

        for a_guy in self.guys:
            if a_guy.has_face():
                a_guy.normalize_face(reference)
    
    def calc_mean_face(self):
        """
        Returns the mean size of all faces in input
        Used to correctly crop images

        .. note:: Designed for internal use only
        """
        tot_x = 0
        tot_y = 0
        nb_face = 0
        for a_guy in self.guys:
            if a_guy.has_face():
                ((x, y, w, h), n) = a_guy.faces[0]
                tot_x += w
                tot_y += h
                nb_face += 1
                
        self.face_mean = [float(tot_x) / nb_face, float(tot_y) / nb_face]
    
    def find_crop_dims(self):
        """
        Calculates smallest output image that can be used to avoid adding black borders on image
        It will later be used to create the final image. 
        The idea is the same as for :func:find_out_dims , but while avoiding black brders.
        """
        ht = 1000000 # space left above eyes
        hb = 1000000 # space left beneath eyes
        wl = 1000000 # space left left of eyes
        wr = 1000000 # space left right of eyes
        
        if self.cropdims != [0, 0]:
            w = int( (self.cropdims[0] * self.face_mean[0])  / 2)
            self.width = [w, w]
            h = int((self.cropdims[1] * self.face_mean[1]) / 2)
            self.height = [h, h]
        else:
            for a_guy in self.guys:
                if a_guy.has_face():
                    xc = a_guy.x_center
                    yc = a_guy.y_center
                    inx = a_guy.in_x
                    iny = a_guy.in_y
                    
                    # finding width    
                    if xc < wl:
                        wl = xc
                    if (inx - xc) < wr:
                        wr = inx - xc
                    # finding height
                    if yc < ht:
                        ht = yc
                    if (iny - yc) < hb:
                        hb = iny - yc
                                          
            self.width = [wl, wr]
            self.height = [ht, hb]
            
        if (sum(self.width) >= self.dim_x) or (sum(self.height) >= self.dim_y):
            print "Cropping inactive : Maximum dimensions reached"
            self.crop = False 
        else:
            self.crop = True
    
    def find_out_dims(self):
        """
        Calculates best output image size and position depending on
        faces found in guys.
        The system is simple. The output image should be as big as possible, 
        and faces are always placed in the same position. Depending on that, 
        the image input image is placed in the output at the correct position.
        Black borders are set everywhere else.
        """
        # FIXME: badly done !
        for a_guy in self.guys:
            if a_guy.has_face():
                xc = a_guy.x_center
                yc = a_guy.y_center
                inx = a_guy.in_x
                iny = a_guy.in_y
                    
                # update center
                if xc > self.x_center:
                    self.x_center = xc
                if yc > self.y_center:
                    self.y_center = yc
                # update right part
                if (inx - xc) > self.x_af:
                    self.x_af = inx - xc
                if (iny - yc) > self.y_af:
                    self.y_af = iny - yc
        
        self.dim_x = self.x_af + self.x_center
        self.dim_y = self.y_af + self.y_center
        
        if self.dim_x * self.dim_y > self.CV_MAX_PIXEL:
            print "Max size reached for large mode!"
            print "You may want to switch to crop mode or reduce image resolution !"
            sys.exit(0)
        
        # finishes by calculating average face size
        self.calc_mean_face()
    
    def crop_im_new(self, a_guy):
        """
        If needed, crops the image to avoid having black borders. 
        
        :param image: the image to be cropped
        :type image: IplImage
        """        
        if a_guy.normalize:
            image = a_guy.load_normalized_image()
        else :
            image = a_guy.load_image()
        
        
        width = self.width#[0, 0]
        height = self.height#[0, 0]
        out_im = cv.CreateImage((width[0] + width[1], height[0] + height[1]),cv.IPL_DEPTH_8U, image.nChannels)
        cv.Zero(out_im)        
        
        ((x, y, w, h), n) = a_guy.faces[0]
        # all should have the same w and h now ! What is different is the x and y !
        w = int(w * a_guy.ratio)
        h = int(h * a_guy.ratio)
        xtl = a_guy.x_center  - width[0]
        ytl = a_guy.y_center  - height[0]
        w = width[0] + width[1]
        h = height[0] + height[1]
            
        rect = (xtl, ytl, w, h)
        
        cv.SetImageROI(image, rect)
        print "###"
        print cv.GetSize(image), cv.GetSize(out_im)
        cv.Copy(image, out_im)
        cv.ResetImageROI(image)     
    
        return out_im
        
    def crop_im(self, image):
        """
        If needed, crops the image to avoid having black borders. 
        
        :param image: the image to be cropped
        :type image: IplImage
        """
        width = self.width#[0, 0]
        height = self.height#[0, 0]
        out_im = cv.CreateImage((width[0] + width[1], height[0] + height[1]),cv.IPL_DEPTH_8U, image.nChannels)
        cv.Zero(out_im)   
    
        xtl = self.x_center - width[0]
        ytl = self.y_center - height[0]
        w = width[0] + width[1]
        h = height[0] + height[1]
            
        rect = (xtl, ytl, w, h)
        
        cv.SetImageROI(image, rect)
        cv.Copy(image, out_im)
        cv.ResetImageROI(image)     
    
        return out_im
    
    def show_faces(self, mytime=1000):
        """
        Show all faces that have been found for the guys.
        The time for which each image will be displayed can be chosen.

        :param mytime: time for which the image should be displayed (in ms) (1000)
        :type mytime: int
        """
        for a_guy in self.guys:
            if a_guy.has_face():     
                out_im = a_guy.create_video_output(self.dim_x, 
                                          self.dim_y, 
                                          self.x_center, 
                                          self.y_center)
                if self.crop:
                    out_im = self.crop_im(out_im)
                self.out_display(out_im, a_guy.name, time=mytime)      

    def save_faces(self, out_folder, im_format="png"):
        """
        Save all faces into out_folder, in the given image format

        :param out_folder: the location where to save the output image.
        :type out_folder: string

        :param im_format: Format in which the image should be saved ("png")
        :type im_format: string        
        """
        for a_guy in self.guys: 
            if a_guy.has_face():
                out_im = a_guy.create_video_output(self.dim_x, 
                                          self.dim_y, 
                                          self.x_center, 
                                          self.y_center)
                if self.crop:
                    out_im = self.crop_im(out_im)
                self.save_result(out_im, a_guy.name, out_folder, im_format)    
                          
    def save_movie(self, out_folder, fps=3):
        """
        Creates a movie with all faces found in the inputs.
        Guy is skipped if no face is found.
        
        :param out_folder: the location where to save the output image.
        :type out_folder: string
        
        :param fps: the number of frames per second to be displayed in final video (3)
        :type fps: int       
        """
        filename = os.path.join(out_folder, "output.avi")
        # Codec is OS dependant.
        # FIXME : Find an unified version
        if "win" in sys.platform:
            fourcc = cv.CV_FOURCC('C', 'V', 'I', 'D')
        else: # some kind of Linux platform
        	#fourcc = cv.CV_FOURCC('I', '4', '2', '0')
        	print "Trying new codec for Ignacio"
        	fourcc = cv.CV_FOURCC('F', 'M', 'P', '4')

        if self.crop:
            width = self.width
            height = self.height
            frameSize = (width[0] + width[1], height[0] + height[1])
        else:
            frameSize = (self.dim_x, self.dim_y)   
        print "Speed is set to %d fps" %(fps)  
        my_video = cv.CreateVideoWriter(filename, 
                                      fourcc, 
                                      fps, 
                                      frameSize,
                                      1)
        ii = 0 
        for a_guy in self.guys:
            ii += 1 
            if a_guy.has_face():
                print "Saving frame %d / %d" %(ii, self.number_guys()) 
                out_im = a_guy.create_video_output(self.dim_x, 
                                          self.dim_y, 
                                          self.x_center, 
                                          self.y_center) 
                if self.crop:
                    #out_im = self.crop_im(out_im)   
                    out_im = self.crop_im_new(a_guy)                            
                cv.WriteFrame(my_video, out_im)

    def number_guys(self):
        """
        Simply returns the number of guys in the current to-be movie
        
        .. note:: 
            Designed for interface use only
        """  
        return len(self.guys)
    
    def out_display(self, im, name, time=1000, im_x=640, im_y=480):
        """
        Displays the output image, for time ms.
        Setting time to 0 causes the image to remains open.
        Window name slightly changed to match output

        :param im: the image to be saved, formatted as an OpenCV Image
        :type im: IplImage
        :param name: the name of the image to be saved
        :type name: string 

        :param time: time for which the image should be displayed (in ms) (1000)
        :type time: int 
        :param im_x: output size of the displayed image (in pixels) (640)
        :type im_x: int 
        :param im_y: output size of the displayed image (in pixels) (480)
        :type im_y: int 
        """
        win_name = name + " - out"
        cv.NamedWindow(win_name, cv.CV_WINDOW_NORMAL)
        cv.ResizeWindow(win_name, im_x, im_y) 
        cv.ShowImage(win_name, im)
        cv.WaitKey(time)
        cv.DestroyWindow(win_name)
        
    def save_result(self, im, name, out_folder, ext):
        """
        Saves output image to the given format (given in extension)
        
        :param im: the image to be saved, formatted as an OpenCV Image
        :type im: IplImage 
        :param name: the name of the image to be saved
        :type name: string 
        :param out_folder: the location where to save the image
        :type out_folder: string         
        :param ext: Format in which the image should be saved ("png")
        :type ext: string        
        """
        file_name = name + "." + ext
        out_name = os.path.join(out_folder, file_name)
        print "Saving %s" %(out_name)
        
        cv.SaveImage(out_name, im)
