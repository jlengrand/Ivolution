"""
.. module:: ivolution
   :platform: Unix, Windows
   :synopsis: Aims at helping you create videos of yourself over time, using photos as input. Take great pictures, FaceMovie will do the rest !

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""
import os
import sys

if hasattr(sys, 'frozen'):
    _ROOT = os.path.split(sys.executable)[0]
else:
    _ROOT = os.path.abspath(os.path.dirname(__file__))

def get_data(path):
    print os.path.join(_ROOT, 'data', path)
    return os.path.join(_ROOT, 'data', path)
