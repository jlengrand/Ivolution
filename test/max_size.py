"""
.. module:: max_size
   :platform: Unix, Windows
   :synopsis: Test class aiming at finding the maximum image size that can be generated to create a FaceMovie using OpenCV

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""

import cv



#x = 1000
#y = 169000
x = 13000
y = 13000

max_pix = x * y

bb = cv.LoadImage("../data/inputs/moi/DSC04862.JPG")

aa = cv.CreateImage((x, y), cv.IPL_DEPTH_8U, 3)

#cv.Resize(bb, aa)
cv.Zero(aa)

cv.NamedWindow("a", 1)
cv.ShowImage("a", aa)
cv.WaitKey(1000)


print "Done!"
print max_pix
print 13000 * 13000