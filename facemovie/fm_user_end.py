'''
Created on 29 mars 2012

@author: jll
'''

# This file should never be imported anywhere
import os
import sys
import argparse

import Facemovie
import FaceParams

class Facemoviefier():
    """
    Class defining the interactions with the end user.
    Should be used as point of entry for all end users.
    """
    
    def __init__(self):
        
        #inits Command Line Parser
        self.args = self.initCLParser()
        print self.args
        print self.args['equalize']
        
        # par folder should be known (contained somewhere in the installation)
        root_fo = "C:\Users\jll\perso\workspace\FaceMovie"
        par_fo = os.path.join(root_fo, "facemovie/haarcascades")
        self.face_params = FaceParams.FaceParams(par_fo, "frontal face alt")    
        
        self.facemovie = Facemovie.FaceMovie(self.args['input'], self.args['output'], self.face_params)

    def initCLParser(self):
        """
        Inits and Configures the command line parser designed to help the user configure the application 
        """
        parser = argparse.ArgumentParser(description="Creates a movie from a bunch of photos containing a Face.")
        
        # --- Arguments to be processed (for now) ---
        #input folder
        parser.add_argument('-i', '--input',  help='Input folder of the images', required=True)
        # output folder
        parser.add_argument('-o', '--output', help='Output folder to save the results', required=True)
        # equalize faces or not ? 
        parser.add_argument('-e', 
                            '--equalize', 
                            help='If this option is activated, images are resized so that all faces have the same size', 
                            action='store_true', 
                            default=True)
        
        
        args = vars(parser.parse_args())

        return args
        
    def run(self):
        """
        Runs all the steps needed to get the desired output
        """
        self.facemovie.list_guys() # find images in input folder
        self.facemovie.search_faces() # search for images with faces
        # I want to change images so that all faces have the same size
        if self.args['equalize']:
            self.facemovie.normalize_faces() # sets all faces to the same size
        # I want to know the size of the output frame, knowing initial conditions
        self.facemovie.find_out_dims() # finds output minimal size to get all eyes in the same place

        #choose your final step
        #self.facemovie.show_faces(1000)
        self.facemovie.save_faces(self.args['output'])
        #self.facemovie.save_movie(self.args['output'])        


if __name__ == '__main__':
    my_job = Facemoviefier()
    my_job.run()
    print "Facemovie finished !"