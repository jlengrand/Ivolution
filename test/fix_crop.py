
import os
import cv



def resizes_for_video_codec(frameSize):
  """
  Searches for the closest couple of frameSize so that width*height is a multiple of 4 to avoid weird image encoding.
  """
  try:
    x,y = frameSize
  except ValueError:
    print "ERROR: unknown format for frameSize "
    return (0, 0)
  
  if not(isinstance(x, int)) or not(isinstance(x, int)):
    print "ERROR: method expects two integers"
    return (0, 0)    

  while ((x * 3) % 4) != 0:
    x += 1  

  print frameSize
  print x, y

  return (x, y)

in_dir = "../data/inputs/sample-test"
out = "output.avi"


# loading images, create Guys and store it into guys
frameSize = (1257, 499)


frameSize = resizes_for_video_codec(frameSize)


#frameSize = (453, 325)
fourcc = cv.CV_FOURCC('F', 'M', 'P', '4')
my_video = cv.CreateVideoWriter(out, 
                              fourcc, 
                              15, 
                              frameSize,
                              1)

for root, _, files in os.walk(in_dir):
    for a_file in files:
        guy_source = os.path.join(in_dir, a_file)
        print guy_source
        image = cv.LoadImage(guy_source)

        small_im = cv.CreateImage(frameSize, 
                                  image.depth ,
                                  image.nChannels)        
        cv.Resize(image, small_im, cv.CV_INTER_LINEAR)
        cv.WriteFrame(my_video, small_im)

print "Finished !"