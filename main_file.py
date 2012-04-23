'''
Created on 29 mars 2012

@author: jll
'''
import os
import facemovie

import sys
if __name__ == '__main__':
    print sys.argv
    #We need input_folder, output_folder, param_folder for now
    if len(sys.argv) == 1:
        print "Setting up the parameters!"
        in_fo = raw_input("indicate input folder:")
        out_fo = raw_input("indicate output folder:")
        par_fo = raw_input("indicate parameters folder:")
    elif len(sys.argv) == 2:
        print "I trust your inputs!"
        [in_fo, out_fo, par_fo] = sys.argv[1, :]
    else :
        print "Chosen automatic way!"
        root_fo = "C:\Users\jll\perso\workspace\FaceMovie"
        in_fo = os.path.join(root_fo, "input\Axel")
        out_fo = os.path.join(root_fo, "output")
        par_fo = os.path.join(root_fo, "haarcascades")
    
    my_movie = facemovie.FaceMovie(in_fo, out_fo, par_fo)
    my_movie.list_guys() # find images in input folder
    my_movie.search_faces() # search for images with faces
    # I want to change images so that all faces have the same size
    my_movie.normalize_faces() # sets all faces to the same size
    # I want to know the size of the output frame, knowing initial conditions
    my_movie.find_out_dims() # finds output minimal size to get all eyes in the same place

    #choose your final step
    #my_movie.show_faces(1000)
    #my_movie.save_faces("output")
    my_movie.save_movie("output")
    
    print "Facemovie finished !"