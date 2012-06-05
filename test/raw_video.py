"""
.. script:: raw_video
   :platform: Unix, Windows
   :synopsis: Aims at taking the same images used to create the FaceMovie, but using doind any processing.
   This is used as an example to show the difference

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""
import sys 
import os 

import cv

root_folder = "../data/inputs/moi2"
out_name = "../data/output/raw.avi"

# fixed params
fourcc = cv.CV_FOURCC('C', 'V', 'I', 'D')
frameSize = (1280, 960)
fps = 3

# Processing
try:
    os.path.exists(root_folder)
    os.path.isdir(root_folder) # checking if folder exists
except : # find precise exception
    print "ERROR : Source folder not found ! Exiting. . ." 
    sys.exit(0)
            
# just listing directory. Lets be more secure later
files = os.listdir(root_folder)


my_video = cv.CreateVideoWriter(out_name, 
                              fourcc, 
                              fps, 
                              frameSize,
                              1)

# loading images, resizes image and populate the video
num_files = len(files)
inc = 0
for token in files :
	inc += 1
	guy_source = os.path.join(root_folder, token)
	image = cv.LoadImage(guy_source)
	out_image = cv.CreateImage(frameSize, image.depth, image.nChannels)# used in current bug solving. 
	cv.Resize(image, out_image)
	print "Saving frame %d / %d" %(inc, num_files) 
	cv.WriteFrame(my_video, out_image)

print "Finished raw movie!"