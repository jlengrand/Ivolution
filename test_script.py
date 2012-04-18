'''
Created on 16 avr. 2012

@author: jll
'''
import os
import cv
from facemovie import *
from Guy import *

# quick and dirty tests
root_fo = "C:\Users\jll\perso\workspace\FaceMovie"
#in_fo = os.path.join(root_fo, "input\Axel_tsts")
in_fo = os.path.join(root_fo, "input\Axel")
out_fo = os.path.join(root_fo, "output")
par_fo = os.path.join(root_fo, "haarcascades")
    
my_movie = FaceMovie(in_fo, out_fo, par_fo)
my_movie.list_guys()
my_movie.search_faces()

# I want to change images so that all faces have the same size
my_movie.normalize_faces()

# I want to know the size of the output frame, knowing initial conditions
my_movie.find_out_dims()

#my_movie.show_faces(1000)
#my_movie.save_faces("output")
my_movie.save_movie("output")
    
print "Facemovie finished !"