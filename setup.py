'''
Created on 19 avr. 2012

@author: jll
'''
# creating executable here
from distutils.core import setup
import py2exe, sys, os
import facemovie

sys.argv.append('py2exe')

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Facemovie",
    version = "0.4",
    author = "Julien Lengrand-Lambert",
    author_email = "jlengrand@gmail.com",
    description = ("An application aiming at creating a video of faces for people taking 'one picture a day' of themselves"),
    license = "BSD",
    keywords = "image_processing computer_vision one_picture_a_day photography",
    url = "https://github.com/jlengrand/FaceMovie",
    packages=['facemovie', 'facemovie.lib', 'facemovie.haarcascades'],
    long_description=read('README.markdown'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
    ],
    options = {'py2exe': {'bundle_files': 1, 'includes': ['numpy'] } },
    console=['facemovie/Facemoviefier.py'],
    zipfile = None,
)