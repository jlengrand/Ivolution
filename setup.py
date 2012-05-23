'''
Created on 19 avr. 2012

@author: jll
'''
# creating executable here
from distutils.core import setup
import sys
import os
import glob

import py2exe

import facemovie

sys.argv.append('py2exe')

def find_data_files(source,target,patterns):
    """Locates the specified data-files and returns the matches
    in a data_files compatible format.

    source is the root of the source data tree.
        Use '' or '.' for current directory.
    target is the root of the target data tree.
        Use '' or '.' for the distribution directory.
    patterns is a sequence of glob-patterns for the
        files you want to copy.
    """
    if glob.has_magic(source) or glob.has_magic(target):
        raise ValueError("Magic not allowed in src, target")
    ret = {}
    for pattern in patterns:
        pattern = os.path.join(source,pattern)
        for filename in glob.glob(pattern):
            if os.path.isfile(filename):
                targetpath = os.path.join(target,os.path.relpath(filename,source))
                path = os.path.dirname(targetpath)
                ret.setdefault(path,[]).append(filename)
    return sorted(ret.items())

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

haar_files = find_data_files('facemovie','',['haarcascades/*.xml'])   
print haar_files

setup(
    name = "Facemovie",
    version = "0.4",
    author = "Julien Lengrand-Lambert",
    author_email = "jlengrand@gmail.com",
    description = ("An application aiming at creating a video of faces for people taking 'one picture a day' of themselves"),
    license = "BSD License",
    keywords = "image_processing computer_vision one_picture_a_day photography",
    url = "https://github.com/jlengrand/FaceMovie",
    download_url = "https://github.com/jlengrand/FaceMovie", # FIXME : To be updated
    packages=['facemovie', 'facemovie.lib', 'facemovie.haarcascades'],
    #package_data={'facemovie': ['haarcascades/*.xml']}, # Adds xml files to the lib
    long_description=read('README.markdown'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Multimedia :: Graphics",
        "Intended Audience :: End Users/Desktop",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: Microsoft",
        "Programming Language :: Python :: 2 :: Only",
    ],
    platforms ={"Linux"},
	data_files = haar_files,
    options = {'py2exe': {'bundle_files': 1, 'includes': ['numpy'] } },
    console=['facemovie/Facemoviefier.py'],
    zipfile = None,
)