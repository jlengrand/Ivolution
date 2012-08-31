'''
Created on 19 avr. 2012

@author: julien Lengrand-Lambert
'''

# creating executable here
from distutils.core import setup
import os

personal_dir = "~/.ivolution"

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def create_personal():
    # creating personal folder
    if not os.path.exists(os.path.expanduser(personal_dir)):
        os.makedirs(os.path.expanduser(personal_dir))

    # creating personal file
    log_root = 'ivolution.log'
    log_file = os.path.join(os.path.expanduser(personal_dir), log_root)
    if not os.path.exists(log_file):
        print log_file
        open(log_file, 'w').close()

    os.chmod(log_file, 02777)  # allow read write access

setup(
    name="Ivolution",
    version="0.6",
    author="Julien Lengrand-Lambert",
    author_email="julien@lengrand.fr",
    description=("Timelapse creation using Face Recognition"),
    license="BSD License",
    keywords="image_processing computer_vision one_picture_a_day photography timelapse face_recognition",
    url="http://jlengrand.github.com/FaceMovie/",
    download_url="http://jlengrand.github.com/FaceMovie/",
    packages=['ivolution', 'ivolution.util', 'ivolution.gui', 'ivolution.data'],
    long_description=read('README.markdown'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Video :: Conversion",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Intended Audience :: End Users/Desktop",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 2 :: Only",
    ],
    #data_files = data_files,
    scripts=['Ivolutioner'],
    package_dir={'ivolution.data': 'ivolution/data'},
    package_data={'ivolution.data': ['haarcascades/*', 'samples/*', 'media/*']},
)

create_personal()
