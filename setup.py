'''
Created on 19 avr. 2012

@author: jll
'''
# creating executable here
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'includes': ['numpy'] } },
    console=['facemovie.py'],
    zipfile = None,
)