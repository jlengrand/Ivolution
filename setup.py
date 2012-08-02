'''
Created on 19 avr. 2012

@author: jll
'''
# creating executable here
from distutils.core import setup
import os

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Ivolution",
    version = "1.0",
    author = "Julien Lengrand-Lambert",
    author_email = "julien@lengrand.fr",
    description = ("Timelapse creation using Face Recognition"),
    license = "BSD License",
    keywords = "image_processing computer_vision one_picture_a_day photography",
    url = "http://jlengrand.github.com/FaceMovie/",
    download_url = "http://jlengrand.github.com/FaceMovie/",
    packages=['ivolution', 'ivolution.util', 'ivolution.gui', 'ivolution.data'],
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
	#data_files = data_files,
    scripts=['Ivolution.py', 'Facemoviefier.py'],
    package_dir={'ivolution.data' : 'ivolution/data'},
    #package_data={'ivolution.data' : ['haarcascades/*'], 'ivolution.data' : ['samples/*'], 'ivolution.data' : ['ui/*'], 'ivolution.media' : ['media/*']}
    package_data={'ivolution.data' : ['haarcascades/*', 'samples/*', 'ui/*', 'media/*']}
)
