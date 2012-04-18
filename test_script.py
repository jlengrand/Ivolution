'''
Created on 16 avr. 2012

@author: jll
'''
import os
import cv
from facemovie import *
from Guy import *

# quick and dirty tests
root_fo = "C:\Users\jll\perso\FaceMovie"
#in_fo = os.path.join(root_fo, "input\Axel_tsts")
in_fo = os.path.join(root_fo, "input\plouf")
out_fo = os.path.join(root_fo, "output")
par_fo = os.path.join(root_fo, "haarcascades")
    
my_movie = FaceMovie(in_fo, out_fo, par_fo)
my_movie.list_guys()
my_movie.search_faces()

# I want to change images so that all faces have the same size
my_movie.normalize_faces()

print "ypolpa"
# I want to know the size of the output frame, knowing initial conditions
my_movie.find_out_dims()

# Here I want to modify in_im first
for a_guy in my_movie.guys:
    if a_guy.has_face():
        # some nice drawings
        ((x, y, w, h), n) = a_guy.faces[0]
        # the input to cv.HaarDetectObjects was resized, so scale the
        # bounding box of each face and convert it to two CvPoints
        pt1 = (x, y)
        pt2 = ((x + w), (y + h))
        cv.Rectangle(a_guy.norm_im, 
                    pt1, 
                    pt2, 
                    cv.RGB(255, 0, 0), 
                    3, 8, 0)# surrounds face   
        
        # Adds point in the center
        pt3 = (a_guy.x_center, a_guy.y_center)
        cv.Line(a_guy.norm_im, 
                pt3, 
                pt3, 
                cv.RGB(0, 255, 0), 
                3, 8, 0)

#for a_guy in my_movie.guys:
#    if a_guy.has_face:
#        try:
#            print a_guy.faces[0]
#        except IndexError:
#            print "Error"
#my_movie.show_faces(1000)
my_movie.save_faces("output")
#my_movie.save_movie("output")
    
print "Facemovie finished !"