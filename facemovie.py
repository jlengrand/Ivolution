'''
Created on 27 mars 2012

@author: jll
'''
import cv
import os
import Guy

class FaceMovie(object):
    '''
    Main class of the whole application. 
    Contains the core image processing functions.
    Supports the communication layer with the end user interface.
    '''


    def __init__(self, in_folder, out_folder, param_folder):
        '''
        Constructor
        '''
        self.source= in_folder # Source folder for pictures
        self.out = out_folder # Folder to save outputs
        self.params_source = param_folder # Folder in which xml files can be found
        
        self.guys = [] # List of pictures in source folder
        
        # Setting up some default parameters for Face Detection
        self.face_cascade = cv.Load(os.path.join(param_folder, "haarcascade_frontalface_alt.xml"))
        self.eye_cascade = cv.Load(os.path.join(param_folder, "haarcascade_eye.xml"))

        # To be defined more precisely
        self.min_size = (20,20)
        self.image_scale = 2
        self.haar_scale = 1.2
        self.min_neighbors = 2
        self.haar_flags = 0
        
    def list_guys(self):
        """
        Aims at populating the guys list, using the source folder as an input. 
        Guys list shall be sorted by file name alphabetical order
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
            image = cv.LoadImage(os.path.join(self.source, token))
            a_guy = Guy.Guy(image, token)
         
            # populating guys
            self.guys.append(a_guy)
        
if __name__ == "__main__":
    # quick and dirty tests
    root_fo = "C:\Users\jll\perso\FaceMovie"
    in_fo = os.path.join(root_fo, "input\Axel")
    out_fo = os.path.join(root_fo, "output")
    par_fo = os.path.join(root_fo, "haarcascades")
    
    my_movie = FaceMovie(in_fo, out_fo, par_fo)
    my_movie.list_guys()
    print "Done !"