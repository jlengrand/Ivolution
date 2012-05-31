"""
.. module:: Face
   :platform: Unix, Windows
   :synopsis: Class defining a Face in the sense of the FaceMovie

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""

class Face(object):
    """
        Face-like blob used in the Face Detection algorithm.

        .. note::

            This class is the very root of our detection part for now; as Eye is not yet used.
            We use Faces to store data while processing images
    """
    def __init__(self):
        """A facemovie redifinition of the human face.

           x_pos    (int)   : x position of the face in the image (in pixels)
           y_pos    (int)   : y position of the face in the image (in pixels)
           x_size   (int)   : x size of the blob (in pixels)
           y_size   (int)   : y size of the blob (in pixels)
           conf     (float)   : confidence indice, indicating the probability of the target to actually be an face
        """
        x_center = None # x position of the face in the image
        y_center = None # y position of the face in the image
        x_size = None # x size of the blob in pixel
        y_size = None # y size of the blob in pixel
        conf = None # confidence indice, indicating the probability of the target to actually be an eye