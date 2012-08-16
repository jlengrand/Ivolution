"""
.. module:: Facemovie
   :platform: Unix, Windows
   :synopsis: Main class of the application. Contains the core image processing functions.Plays the role of a controller for the application, as it supports the communication layer with the end user interface. 

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""
import os
import sys
import sys

import logging

import cv

from util import exif
import Guy

from util.Notifier import Observable
from util.Notifier import Observer

class FaceMovie(object, Observable, Observer):
    '''
    Main class of the whole application. 
    Contains the core image processing functions.
    Takes a bunch of parameters and a list of images and creates the ouput, depending what the user asked for. 
    Contains general methods, aimed at being used trough an interface.
    '''    
    def __init__(self, face_params):
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
        Observable.__init__(self) # used to send notifications to process
        Observer.__init__(self, "Library") # used to receive notification to stop

        self.console_logger = logging.getLogger('ConsoleLog') # Used to send messages to the console
        self.my_logger = logging.getLogger('FileLog') # Used to save events into a file

        self.source= face_params.input_folder # Source folder for pictures
        # Retrieving parameters for Face Detection
        self.face_params = face_params


        out_folder = self.face_params.output_folder
        self.out_path = "./data"
        self.out_name = "output" 
        self.out_format = "avi"
        # updating the out_folder if needed
        self.check_out_name(out_folder)

        self.face_params.output_folder
        self.out_path = "./data"
        self.out_name = "output" 
        self.out_format = "avi"
        # updating the out_folder if needed
        self.check_out_name(out_folder)

        self.sort_method = face_params.sort # sorting by name or using metadata (n or e)
        self.mode = face_params.mode # can be crop or conservative. 

        ###                
        self.guys = [] # List of pictures in source folder
        
        self.center = [0, 0] # Position of the center in output images (x, y)
        
        # Size of the final output image (x, y). Depends on selected mode
        self.dims = [0, 0]

        # number of channels of the set of images
        self.nChannels = 0
        # depth of the set of images
        self.depth = 0

        self.weight_steps = 5 # number of images to be inserted between each frame to reduce violent switch

        self.speed = [2, 5, 9]# this one should be internal. Number of fps for the video

        self.run = True # command used to stop the processing if needed

    def update(self, message):
        """
        Used to receive system commands, using the Observer pattern
        """
        if len(message) == 1: # system command
            self.run = False

    def list_guys(self):
        """
        Aims at populating the guys list, using the source folder as an input. 
        Guys list can be sorted either by name, or using metadata.
        In case source folder is not found; Exits without processing.
        Non Image files are autmatically skipped. 
        Source folder is searched recursively. All subfolders are also processed.
        .. note::In case no valid date is found for metadata mode, the images are taken in name order
        """
        try:
            os.path.exists(self.source)
            os.path.isdir(self.source) # checking if folder exists
        except : # find precise exception
            self.console_logger.critical("Source folder not found ! Exiting. . .")
            self.my_logger.critical("Source folder not found ! Exiting. . .")
            sys.exit(0)
                
        # loading images, create Guys and store it into guys
        ptr = 0
        for root, _, files in os.walk(self.source):
            for a_file in files:
                ptr += 1
                # notifying the Observers
                self.notify_progress("Processing file", ptr, len(files))

                if self.run : # as long as we want to continue
                    guy_source = os.path.join(root, a_file)
                    try:
                        image = cv.LoadImage(guy_source)
                        guy_name = os.path.splitext(a_file)[0]

                        # Tries to extract date from metadata
                        try:
                            guy_date = exif.parse(guy_source)['DateTime']
                        except Exception:
                            self.my_logger.warning("No metadata found for %s" %(guy_name))                        
                            if self.sort_method == "exif":
                                self.console_logger.warning(" No metadata found for %s" %(guy_name))

                            guy_date = ''

                        a_guy = Guy.Guy(guy_name, guy_date, guy_source)
                     
                        # populating guys
                        self.guys.append(a_guy)
                    except:
                        self.console_logger.info("Skipping %s. Not an image file" %(guy_source))
                        self.my_logger.info("Skipping %s. Not an image file" %(guy_source))

        self.sort_guys()
        self.console_logger.info("%d guys found in source folder." %(self.number_guys()))
        self.my_logger.info("%d guys found in source folder." %(self.number_guys()))

    def sort_guys(self):
        """
        Guys list has just been populated, but elements are not ordered yet.
        Sorts the elements of the list either by name or by date extracted from metadata,
        depending on the chosen mode.
        """
        # Sorting either by exif date or name
        if self.sort_method == "exif":
            self.guys.sort(key=lambda g: g.date)
        else: # default is sort by name
            self.guys.sort(key=lambda g: g.name)
    
    def search_faces(self):
        """
        Searches for all faces in the guys we have
        Results to be stored directly in guys

        Takes each image one after the other, and create a guy out of it. 
        The Face of each guy is searched.
        In case no face is found, a warning is returned and Guy is set to None
        """
        ptr = 0
        for a_guy in self.guys:
            ptr += 1
            if self.run:
                a_guy.search_face(self.face_params)

                # notifying the Observers
                self.notify_progress("Processing picture", ptr, self.number_guys())

                if a_guy.has_face(): # face(s) have been found
                    self.console_logger.info("Face found for %s" % (a_guy.name))
                    self.my_logger.info("Face found for %s" % (a_guy.name))                
                else:
                    self.console_logger.warning("No face found for %s. Skipped . . ." %(a_guy.name))
                    self.my_logger.warning("No face found for %s. Skipped . . ." %(a_guy.name))
        
    def percent(self, num, den):
        """
        Returns a float between 0 and 1, being the percentage given by num / den
        """
        if num > den :
            raise ArithmeticError
        if den <= 0 : 
            raise ZeroDivisionError

        return (num / float(den))

    def notify_progress(self, message_root, num, den):
        """
        A notification scheme to quickly notify most common messages
        """
        # notifying the Observers
        try:
            message = message_root + "  %d / %d" %(num, den)
            self.notify([message, self.percent(num, den)])
        except (ArithmeticError, ZeroDivisionError):
            #pass
            self.notify(["Error", 0])

    def clean_guys(self):
        """
        Removes all guys for who no face has been found.
        This avoids all has_face loops in the rest of the application       
        """
        return [a_guy for a_guy in self.guys if a_guy.has_face()] 

    def prepare_faces(self):
        """
        Searches for all faces and keep only the one that may be properly used.
        Images without face are discarded.
        The program is exited in case no face is found.
        Searches for the reference size. If will be used later for image resizing, so that
        all faces have the same size.
        """
        self.search_faces()
        # removes guys that have no faces
        self.guys = self.clean_guys()

        # check that everybody has the same number of channels
        self.check_channels()
        self.check_depth()

        if self.number_guys() == 0:
            self.console_logger.error("No face has been found in the whole repository! Exiting. . . ")
            self.my_logger.error("No face has been found in the whole repository! Exiting. . . ")            
            sys.exit(0) # FIXME : Find better way to do that

        # normalize faces to make them clean
        self.set_guys_ratio() # sets all faces to the same size, by calculating a ratio to a reference

    def check_depth(self):
        """
        Checks that the depth of all the images in guys is the same
        Sets the depth for the video
        """
        my_depth = []
        for a_guy in self.guys:
            my_depth.append(a_guy.depth)

        my_depth = list(set(my_depth))# remove duplicates
        if len(my_depth) != 1 :
            # We do not have a unique number of channels for all images
            self.console_logger.error("All images must have the same depth")
            self.my_logger.error("All images must have the same depth")                        
        else:
            self.depth = my_depth[0]

    def check_channels(self):
        """
        Checks that the number of channels of all the images in guys is the same
        Sets the number of channels for the video
        """
        my_chans = []
        for a_guy in self.guys:
            my_chans.append(a_guy.in_channels)

        my_chans = list(set(my_chans))# remove duplicates
        if len(my_chans) != 1 :
            # We do not have a unique number of channels for all images
            self.console_logger.error("All images must have the same number of channels")
            self.my_logger.error("All images must have the same number of channels")
        else:
            self.nChannels = my_chans[0]

    def set_guys_ratio(self):
        """
        For each Guy, calculates the factor by which the image is going to be resized so that all faces finally have the same size.
        """
        ref = self.find_reference()
        for a_guy in self.guys:
            a_guy.set_ratio(ref)

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

        return min(references)

    def find_final_dimensions(self, cropdims=(0, 0)):
        """
        Finds the final dimensions that will be needed to create the output.
        Depending on the desired output, it can be 
         - (default) the maximal size of the image, by overlapping all images and adding black borders.
         - (crop) the maximal size of the image by overlapping all the images, without adding any black borders
        - (custom crop) A chosen user size, defined as x * y times the head size.
        """
        if self.mode == "conservative":
            self.find_default_dims()
        elif self.mode == "crop":
            self.find_crop_dims()
        elif self.mode == "custom crop":
            # TODO : implement
            self.console_logger.critical("custom crop is not yet implemented")
            self.my_logger.critical("custom crop is not yet implemented")
            raise Exception
    
    def find_default_dims(self):
        """
        Calculates best output image size and position depending on
        faces found in guys.
        The system is simple. The output image should be as big as possible, 
        and faces are always placed in the same position. Depending on that, 
        the image input image is placed in the output at the correct position.
        Black borders are set everywhere else.
        """
        # TODO: badly done !
        x_af = 0
        y_af = 0

        ptr = 0
        for a_guy in self.guys:
            if self.run :
                ptr +=1
                # notifying the Observers
                self.notify_progress("Processing picture", ptr, self.number_guys())

                (xc, yc) = a_guy.resized_center()
                (inx, iny) = a_guy.resized_dims()
                        
                # update center
                if xc > self.center[0]:
                    self.center[0] = xc
                if yc > self.center[1]:
                    self.center[1] = yc
                # update right part
                if (inx - xc) > x_af:
                    x_af = inx - xc
                if (iny - yc) > y_af:
                    y_af = iny - yc
        
        self.dims = [x_af + self.center[0], y_af + self.center[1]]

    def find_crop_dims(self):
        """
        Calculates smallest output image that can be used to avoid adding black borders on image
        It will later be used to create the final image. 
        """
        # TODO: badly done !
        ht = 1000000 # space left above eyes
        hb = 1000000 # space left beneath eyes
        wl = 1000000 # space left left of eyes
        wr = 1000000 # space left right of eyes

        tr = 0

        ptr = 0
        for a_guy in self.guys:
            if self.run:
                ptr +=1
                # notifying the Observers
                self.notify_progress("Processing picture", ptr, self.number_guys())

                (xc, yc) = a_guy.resized_center()
                (inx, iny) = a_guy.resized_dims()            
                
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
                                     
        self.dims = [wl + wr, ht + hb]                 
        self.center = [wl, ht]

    def get_out_file(self):
        """
        Reconstructs the final output file for the movie creation
        :returns:  String --  The ouput file path to be saved
        """
        return os.path.join(self.out_path, (self.out_name + "." + self.out_format))

    def save_movie(self):
        """
        Creates a movie with all faces found in the inputs.
        Guy is skipped if no face is found.
        
        :param out_folder: the location where to save the output image.
        :type out_folder: string
        
        :param fps: the number of frames per second to be displayed in final video (3)
        :type fps: int       
        """
        speedrate = self.face_params.speed
        if "win" in sys.platform:
            fourcc = cv.CV_FOURCC('C', 'V', 'I', 'D')
        else: # some kind of Linux/Unix platform
            fourcc = cv.CV_FOURCC('F', 'M', 'P', '4')

        # Corrects frameSize to get a nice video output
        frameSize = self.resizes_for_video_codec() # Fixme : Put in global parameter
        # We have to resize the out_image to make them fit with the desired size
        corr_im = cv.CreateImage(frameSize, self.depth, self.nChannels)

        #frameSize = (652, 498)
        pace = ["slow", "normal", "fast"]
        self.console_logger.info("Speed is set to %s" %(pace[speedrate]))
        self.my_logger.info("Speed is set to %s" %(pace[speedrate]))        
        my_video = cv.CreateVideoWriter(self.get_out_file(),
                                      fourcc, 
                                      self.speed[speedrate], 
                                      frameSize,
                                      1)
        ii = 0 
        for a_guy in self.guys:
            if self.run:
                ii += 1 
                self.notify_progress("Saving frame", ii, self.number_guys())

                self.console_logger.info("Saving frame %d / %d" %(ii, self.number_guys()) )
                self.my_logger.info("Saving frame %d / %d" %(ii, self.number_guys()) )             
                out_im = self.prepare_image(a_guy)

                cv.Resize(out_im, corr_im, cv.CV_INTER_LINEAR)

                cv.WriteFrame(my_video, corr_im)

    def show_faces(self, mytime=1000):
        """
        Show all faces that have been found for the guys.
        The time for which each image will be displayed can be chosen.

        :param mytime: time for which the image should be displayed (in ms) (1000)
        :type mytime: int
        """
        win_name = " Face Results"
        cv.NamedWindow(win_name, cv.CV_WINDOW_NORMAL)
        cv.ResizeWindow(win_name, 640, 480) 

        for a_guy in self.guys:    
            if self.run:
                out_im = self.prepare_image(a_guy)
                cv.ShowImage(win_name, out_im)
                cv.WaitKey(mytime)

        cv.DestroyWindow(win_name)

    def save_faces(self, im_format="png"):
        """
        Save all faces into out_folder, in the given image format

        :param out_folder: the location where to save the output image.
        :type out_folder: string

        :param im_format: Format in which the image should be saved ("png")
        :type im_format: string        
        """
        for a_guy in self.guys: 
            if self.run:
                out_im = self.prepare_image(a_guy)
                self.save_guy(out_im, a_guy.name, im_format)    

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

    def check_out_name(self, out_folder):
        """
        Checks the desired output selected by the user. 
        It can be either a folder or a file itself.
        Checks whether the designated path ends with a extension name. 

        In case it is, the extension is checked and changed if needed

        :param out_folder: the path slected by the user as output location
        :type out_folder: String
        """

        if len(os.path.splitext(out_folder)[1]) > 0:# if ends up with an extension
            self.out_path, complete_name = os.path.split(out_folder)
            self.out_name, format = os.path.splitext(complete_name)
            if format != self.out_format:
                # the format is not compliant with what we can do. We refuse it
                self.my_logger.info("Changing format to avi")                         
        else:
            # no filename is given. We keep the default
            self.out_path = os.path.split(out_folder)[0]

    def save_guy(self, im, name, ext):
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
        out_name = os.path.join(self.out_path, file_name)
        self.my_logger.info("Saving %s" %(out_name))
        self.console_logger.info("Saving %s" %(out_name))
        
        cv.SaveImage(out_name, im)

    def prepare_image(self, a_guy):
        """
        Takes a Guy and processes its input image. Prepares the final output image for this
        Guy, so that it is ready to be saved in the desired output.

        :param a_guy: The Guy currently being processed. 
        :type a_guy: Guy 
        :returns:  IplImage --  The ouput image, created depending on the chosen mode, ready to be saved
        """        
        if self.mode == "conservative":
            out_im = a_guy.create_default_output(self.dims,
                                                self.center) 
        elif self.mode == "crop":
            out_im = a_guy.create_crop_output(self.dims,
                                            self.center)        
        return out_im

    def resizes_for_video_codec(self):
      """
      Searches for the closest couple of frameSize so that width*height is a multiple of 4 to avoid weird image encoding.

        :param frameSize: The desired video output size before correction. (in Pixels)
        :type frameSize: (int, int) 
        :returns:  corrected frameSize --  The desired output size after correction. In (x, y) form. 
      """
      frameSize = (self.dims[0], self.dims[1])   

      try:
        x, y = frameSize
      except ValueError:
        self.my_logger.error("unknown format for frameSize ")      
        return (0, 0)
      
      if not(isinstance(x, int)) or not(isinstance(x, int)):
        self.my_logger.error("method expects two integers")            
        return (0, 0)    

      while ((x * self.nChannels) % 4) != 0:
        x += 1  

      return (x, y)
