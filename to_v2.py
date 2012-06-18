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

facemovie.search_faces()


print "Exiting..."