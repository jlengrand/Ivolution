'''
Created on 29 mars 2012

@author: jll
'''
import cv
import os

import facemovie

if __name__ == '__main__':
    # Main test file to test current application  
    root_fo = "C:\Users\jll\perso\FaceMovie"
    #in_fo = os.path.join(root_fo, "input\Axel_tsts")
    in_fo = os.path.join(root_fo, "input\Axel")
    out_fo = os.path.join(root_fo, "output")
    par_fo = os.path.join(root_fo, "haarcascades")
    
    my_movie = FaceMovie(in_fo, out_fo, par_fo)
    my_movie.list_guys()
    my_movie.search_faces()
    # I want to know the size of the output frame, knowing initial conditions
    my_movie.find_out_dims()

    #my_movie.show_faces(1000)
    #my_movie.save_faces("output", debug=False)
    my_movie.save_movie("output", debug=False)
    
    print "Facemovie finished !"