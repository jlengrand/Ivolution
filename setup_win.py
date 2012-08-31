'''
Created on 31 aug. 2012

@author: jll
'''
# creating executable here
from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')
sys.path.append("C:\\Program Files\\Microsoft Visual Studio 9.0\\VC\\redist\\x86\\Microsoft.VC90.CRT")

setup(
    options = {'py2exe': {'bundle_files': 1, 'includes': ['numpy', 'wx'] } },
    console=['Ivolutioner'],
    zipfile = None,
)