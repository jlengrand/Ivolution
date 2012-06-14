"""
.. module:: weighted_images
   :platform: Unix, Windows
   :synopsis: Basic test script aiming at testing the possibility to use inter frames between images to enhance video output

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""
import sys

import cv

image1 = "../data/inputs/moi/DSC04858.jpg"
image2 = "../data/inputs/moi/DSC04882.jpg"

delay = 00

# input images
im1 = cv.LoadImage(image1)
im2 = cv.LoadImage(image2)

# cv.NamedWindow("im1", cv.CV_WINDOW_NORMAL)
# cv.NamedWindow("im2", cv.CV_WINDOW_NORMAL)

# cv.ResizeWindow("im1", 640, 480)
# cv.ResizeWindow("im2", 640, 480)

# cv.MoveWindow("im1", 0, 0)
# cv.MoveWindow("im2", 640, 0)

# cv.ShowImage("im1", im1)
# cv.ShowImage("im2", im2)

# weighted images

filename = "../data/output/weighted.avi"
# Codec is OS dependant.
# FIXME : Find an unified version
if "win" in sys.platform:
    fourcc = cv.CV_FOURCC('C', 'V', 'I', 'D')
else: # some kind of Linux/Unix platform
	fourcc = cv.CV_FOURCC('F', 'M', 'P', '4')

fps = 5
frameSize = cv.GetSize(im1)
my_video = cv.CreateVideoWriter(filename, 
                              fourcc, 
                              fps, 
                              frameSize,
                              1)

num_inter_im = 10
step = float(1)/10 

for i in range(num_inter_im + 1 ):
	print i
	im3 = cv.CreateImage(cv.GetSize(im1), im1.depth, im1.nChannels)
	alpha = step * i
	beta = 1 - alpha
	gamma = 0
	cv.AddWeighted(im1, alpha, im2, beta, gamma, im3) 
	cv.WriteFrame(my_video, im3)

# cv.NamedWindow("im3", cv.CV_WINDOW_NORMAL)
# cv.ResizeWindow("im3", 640, 480)
# cv.MoveWindow("im3", 640, 500)
# cv.ShowImage("im3", im3)

# cv.WaitKey(delay)