import sys
sys.path.append("../facemovie/lib")
import exif
import time

path = "../data/input/Axel/2012-01-15-06h13m41DSCN9849.JPG"

plop = exif.parse(path)['DateTime']
print plop

my_date = time.strptime(plop, "%Y:%m:%d %H:%M:%S")
print my_date
