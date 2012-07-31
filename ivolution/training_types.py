"""
.. module:: training_types
   :platform: Unix, Windows
   :synopsis: Dumb class aiming at regrouping all information concerning the trainers for classification. Each entry is linked to a label, corresponding to a different type of recognition (frontal, profile, . . . )

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""
# File used only to store a dictionary off all xml files used to train the classifier
complete_set = {#eyes
                  'eyes':"haarcascade_eye", 
                  'glasses':"haarcascade_eye_tree_eyeglasses",
                  'left eye splits':"haarcascade_lefteye_2splits",
                  'eye pair big':"haarcascade_mcs_eyepair_big",
                  'eye pair small':"haarcascade_mcs_eyepair_small",
                  'left eye':"haarcascade_mcs_lefteye",
                  'right eye':"haarcascade_mcs_righteye",
                  'right eye splits':"haarcascade_righteye_2splits",
                  # frontal faces
                  'frontal face alt':"haarcascade_frontalface_alt", 
                  'frontal face alt2':"haarcascade_frontalface_alt2", 
                  'frontal face':"haarcascade_frontalface_default", 
                  #profile face
                  'profile face':"haarcascade_profileface", 
                  #body
                  'full body':"haarcascade_fullbody", 
                  'lower body':"haarcascade_lowerbody", 
                  'upper body mcs':"haarcascade_mcs_upperbody", 
                  'upper body':"haarcascade_upperbody", 
                  #ear
                  'left ear':"haarcascade_mcs_leftear", 
                  'right ear':"haarcascade_mcs_rightear", 
                  #mouth
                  'mouth':"haarcascade_mcs_mouth",
                  #nose
                  'nose':"haarcascade_mcs_nose"
                  }

simple_set = {# frontal faces
                  'frontal_face':"haarcascade_frontalface_alt",  
                  #profile face
                  'profile_face':"haarcascade_profileface", 
                  #body
                  'full_body':"haarcascade_fullbody", 
                  'lower_body':"haarcascade_lowerbody", 
                  'upper_body':"haarcascade_upperbody", 
                  }