'''
Created on 16 avr. 2012

@author: jll
'''

import os
from context import facemovie
from facemovie.Facemovie import FaceMovie

if __name__ == '__main__':
    root_fo = "C:\Users\jll\perso\workspace\FaceMovie"
    in_fo = os.path.join(root_fo, "data/input\Axel")
    out_fo = os.path.join(root_fo, "data/output")
    par_fo = os.path.join(root_fo, "facemovie/haarcascades")
    
    my_movie = FaceMovie(in_fo, out_fo, par_fo)
    my_movie.list_guys() # find images in input folder
    
    # listing training files
    print my_movie.face_params.get_types()
    
    #my_movie.search_faces() # search for images with faces
    # I want to change images so that all faces have the same size
    #my_movie.normalize_faces() # sets all faces to the same size
    # I want to know the size of the output frame, knowing initial conditions
    #my_movie.find_out_dims() # finds output minimal size to get all eyes in the same place

    #choose your final step
    #my_movie.show_faces(1000)
    #my_movie.save_faces("output")
    #my_movie.save_movie("output")
    
    print "Facemovie finished !"