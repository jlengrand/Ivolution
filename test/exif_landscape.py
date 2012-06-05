"""
.. module:: max_size
   :platform: Unix, Windows
   :synopsis: Test class aiming at finding the maximum image size that can be generated to create a FaceMovie using OpenCV

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""

from facemovie.lib import exif
import cv


guy_source = "C:\Users\jll\perso\workspace\FaceMovie\data\inputs\moi\DSC04869.JPG"
aa = cv.LoadImage(guy_source)
cv.NamedWindow("a")
cv.ShowImage("a", aa)
cv.WaitKey(100)

data = exif.parse(guy_source)
print data.keys()
print data["Orientation"] # portrait/ paysage? ? ? 