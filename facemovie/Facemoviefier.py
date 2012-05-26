'''
Created on 29 mars 2012

@author: jll
'''

# This file should never be imported anywhere
import os
import sys
import argparse

from facemovie import Facemovie
from facemovie import FaceParams
from facemovie import training_types

class Facemoviefier():
    """
    Class defining the interactions with the end user.
    Should be used as point of entry for all end users.
    """
    def __init__(self):
        #inits Command Line Parser
        self.args = self.initCLParser()
        
    def init_facemovie(self):
        # FIXME : par folder should be known (contained somewhere in the installation)
        par_fo = os.path.join(self.args['root'], "haarcascades")
        self.face_params = FaceParams.FaceParams(par_fo, self.args['param'])    
        self.facemovie = Facemovie.FaceMovie(self.args['input'], self.args['output'], self.face_params)

    def initCLParser(self):
        """
        Inits and Configures the command line parser designed to help the user configure the application 
        """
        parser = argparse.ArgumentParser(description="Creates a movie from a bunch of photos containing a Face.")
        
        # TODO: Integrate face params file choice, with list of possibilities. (ncurses)
        # First to check if user asks for information 
        params = training_types.simple_set.keys()
        params.append('?')
        parser.add_argument('-p', 
                            '--param', 
                            choices=params,
                            help='Choose the desired file for training the recognition phaze. Should be chosen depending on the face presentation (profile, whole body, ...)', 
                            default='frontal_face')     
    
        # --- Arguments to be processed (for now) ---
        #input folder
        parser.add_argument('-i', '--input',  help='Input folder of the images', required=True)
        # output folder
        parser.add_argument('-o', '--output', help='Output folder to save the results', required=True)
        
        # root folder
        parser.add_argument('-r', '--root', help='Root folder where the application is placed', default=".")
        
        # equalize faces or not ? 
        parser.add_argument('-e', 
                            '--equalize', 
                            help='If this option is activated, images will NOT be resized so that all faces have the same size', 
                            action='store_false', 
                            default=True)

        # expand images or crop ? Default should be crop
        parser.add_argument('-c', 
                            '--crop', 
                            help='If this option is activated, images will be cropped and black borders will not be added' , 
                            action='store_true', 
                            default=False)

        # Crop to custom dims if desired
        parser.add_argument('-d', 
                            '--cropdims', 
                            help='Ignored if crop is not activated. Crops image to size x y' ,
                            nargs = 2)
        
        # type of output wanted (image, video, show)
        parser.add_argument('-t', 
                            '--type', 
                            choices='vis',
                            help='Selects the kind of output desired. Valid choices are v (video), i (images), s (show). Default is video', 
                            default='v')        
        
        # how to sort images. Default is file name
        parser.add_argument('-s', 
                            '--sort', 
                            choices='ne',
                            help='Choose which way images are sorted. Can be either using file name (n) or exif metadata (e). Default is n' , 
                            default='n')       
        
        args = vars(parser.parse_args())
        return args
        
    def run(self):
        """
        Runs all the steps needed to get the desired output
        """
        # selects xml used to train the classifier 
        if self.args['param'] == '?':
            print "Available param files are :"
            print "==="
            for item in training_types.simple_set:
                print item
            print "==="                
            print 'Please choose your param file (or let default value) and restart the application'
            sys.exit(0)      
        else:
            # creates Facemovie object, loads param file
            self.init_facemovie()
        
        #selects sorting method
        if self.args['sort'] == 'e':
            self.facemovie.sort_method = 'e';
        self.facemovie.list_guys()
        self.facemovie.search_faces()
        # I want to change images so that all faces have the same size
        if self.args['equalize']:
            self.facemovie.normalize_faces() # sets all faces to the same size
        # I want to know the size of the output frame, knowing initial conditions    
        self.facemovie.find_out_dims() # finds output minimal size to get all eyes in the same place
        if self.args['crop']:
            if self.args['cropdims']:
                self.facemovie.set_crop_dims(float(self.args['cropdims'][0]), float(self.args['cropdims'][1])) 
                # TODO : do we need something else than pixel here ? It stinks due to face normalization. Change to number of face size
            self.facemovie.find_crop_dims() # finds output minimal size to get all eyes in the same place

        #choose your final step
        if self.args['type'] == 's':
            self.facemovie.show_faces(1000)
        elif self.args['type'] == 'i':
            self.facemovie.save_faces(self.args['output'])
        elif self.args['type'] == 'v':
            self.facemovie.save_movie(self.args['output'])        

if __name__ == '__main__':
    my_job = Facemoviefier()
    my_job.run()
    print "Facemovie finished finally !"
