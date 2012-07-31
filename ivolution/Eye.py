"""
.. module:: Eye
   :platform: Unix, Windows
   :synopsis: Class defining an Eye in the sense of the FaceMovie

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""

class Eye(object):
    """
        Eye-like blob used in the Face Detection algorithm.

        .. note::

            This class **is not used for now**, but should get useful when implementing
             the use interaction feature
    """
    def __init__(self):
        """A facemovie redefinition of the human eye

        :param x_pos: x position of the eye in the image (in pixels)
        :type x_pos: int
        :param y_pos: y position of the eye in the image (in pixels)
        :type y_pos: int        
        :param x_size: x size of the blob (in pixels)
        :type x_size: int
        :param y_size: y size of the blob (in pixels)
        :type y_size: int
        :param conf: confidence indice, indicating the probability of the target to actually be an eye
        :type conf: float
        """
        x_pos = None # x position of the eye in the image
        y_pos = None # y position of the eye in the image
        x_size = None # x size of the blob in pixel
        y_size = None # y size of the blob in pixel
        conf = None # confidence indice, indicating the probability of the target to actually be an eye