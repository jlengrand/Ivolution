'''
Created on 25 avr. 2012

@author: jll
'''
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
                  'frontal face alt':"haarcascade_frontalface_alt",  
                  #profile face
                  'profile face':"haarcascade_profileface", 
                  #body
                  'full body':"haarcascade_fullbody", 
                  'lower body':"haarcascade_lowerbody", 
                  'upper body':"haarcascade_upperbody", 
                  }