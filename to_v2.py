"""
.. module:: weighted_images
   :platform: Unix, Windows
   :synopsis: Script used to help refactoring the Facemovie. Should not be used

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""
import sys

import cv

from facemovie import Facemovie
from facemovie import FaceParams

in_fo = "data/inputs/samples"
out_fo = "data"

xml_fo = "haarcascades"

face_params = FaceParams.FaceParams(xml_fo, 'frontal_face')

facemovie = Facemovie.FaceMovie(in_fo, out_fo, face_params)
facemovie.list_guys()

facemovie.prepare_faces()

# default mode
facemovie.find_final_dimensions(cropdims=(0, 0))
print "###"
print facemovie.dim_x, facemovie.dim_y
print facemovie.x_center, facemovie.y_center
print "###"
facemovie.save_out_movie(out_fo, 3)
facemovie.save_faces(out_fo)

# crop mode
facemovie.mode = "crop"
facemovie.find_final_dimensions(cropdims=(0, 0))
print "###"
print facemovie.dim_x, facemovie.dim_y
print facemovie.x_center, facemovie.y_center
print "###"
facemovie.save_out_movie(out_fo, 2)  
#facemovie.show_faces()
facemovie.save_faces(out_fo)

print "Exiting..."