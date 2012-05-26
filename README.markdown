#Take one picture of yourself a day, automatically generate a movie!


**[FaceMovie](http://www.youtube.com/watch?v=JueOY7EtXrQ)** is a simple project that aims at helping you create videos of yourself over time, using photos as input.
I see a growing interest for this kind of projects, where people take one picture of themselves a day for several months (years ?) and compile it into a [video](http://www.youtube.com/watch?v=6B26asyGKDo). 
I started this project for a friend currently [travelling around the world](http://http://ungrandtour.blogspot.com/). He wanted to create a video of his face changes along the trip.

The main idea is simple. The software takes a batch of images as input. The images are assumed to be named by date (so that an alphabetical order is also the chronological order).
The output is a video containing each image, where the face is always placed in the same position. This way, people can actually see the face change over time.

**[You can check out the last results in video here !](http://www.youtube.com/watch?v=2pUHK7Sf23I)**

**In progress: **

- The very central part of the code is finished. 
- I currently work on video quality enhancement (compression, speed, fade effects, ...)
- I plan to include a GUI to help people use the software, and later add support for a broader type of input images (profiles, eyes, glasses, . . .)
- I also think about a way for user to help the software in case it struggles with images (by manually pointing face on problematic images?). 
- Any other idea is welcome

## Getting started


I have just started searching for a nice way to package the application in a single executable, which means if you want to test Facemovie you will have to directly run the code in the development branch.

In this part, I will thus consider that you have Python 2.7 and OpenCV (and of course its Python bindings) installed on your machine. 
To get the last version of Facemovie, simply clone the project from Github 
```
git clone git://github.com/jlengrand/FaceMovie.git
```

You will also need to have a bunch of photos of your face stored in a folder. Those images should contain only one person; and you should try to always keep the same angle with the camera.
If you dont, some samples are included in the project (placed in data/input/Axel)

Since version 0.4, Facemovie supports user interaction through the Facemovifier. That means that you should be able to run the application without modifying it.
If you are like me, you ight want to start by calling the helper : 
```
$ python Facemoviefier -h
```
 which will list the available parameters in the application. 

The simplest example you can run would be :
```
$ python Facemoviefier -i input_folder -o output_folder
```
, where input_folder and output_folder are strings.
If you place yourself in the facemovie folder and run the application from here, this line should work :
```
$ python Facemoviefier -i "../data/input/Axel" -o "../data/output"
```

If you decide to run the Facemovifier from another location, you should update the folders accordingly, and use the root_folder option:
```
$ python Facemoviefier -i input_folder -o output_folder -r facemovie_folder_location
```

You might want to save images instead of a movie as output:
```
$ python Facemoviefier -i "../data/input/Axel" -o "../data/output" -t i
```

And if you have profile images, you can (must) also decide to change the file used for training the classifier:
```
$ python Facemoviefier -i "../data/input/Axel" -o "../data/output" -p "profile face"
```
An extensive list of training files is available while calling the helper.

### Options available in the Facemoviefier

**Required :**

- -i, --input : 	Input folder of the images to be processed
- -o, --output : 	Output folder where the final results will be saved

**Optional :**

- -h, --help :	Shows help message and exits
- -r, --root : 	Location of the facemovie folder. Required if you run the Facemovifier from an external location
- -e, --equalize : If this option is activated, images will NOT be resized so that all faces have the same size.
- -p, --param:	Used to change the file used to train the classifier. Useful you want to detect something else than front faces.
- -t, --type :	The type of output to be created. Can be either images, video or simple display (nothing written on disc).


## Libraries

This piece of code is developed in [Python](http://www.python.org/), simply because I love it :P (and because it allows easy testing while developing Image Processing applications).
I used Python 2.7 for development. 
The only library needed to run the code for now is [Opencv](http://opencv.willowgarage.com/wiki/) (and by extension [Numpy](http://numpy.scipy.org/)). See [the documentation](http://opencv.willowgarage.com/wiki/InstallGuide) for more information. 

This project is developed on a Windows (7) platform, but there should (and, as a fanatic Linux User, will) be no compatibility problems with UNIX. 

## License

This project is released under the new BSD license (3 clauses version). You can read more about the license in the LICENSE file. 

## Acknowledgment

This project comes from an idea of Axel Catoire, currently [travelling around the world](http://ungrandtour.blogspot.com/)  with his girlfriend.
He also provides me with new pictures :).

As a starter for my code, I used an excellent example from JAPSKUA, that you can find [here](http://japskua.wordpress.com/2010/08/04/detecting-eyes-with-python-opencv/)


## Contact

I would enjoy having feedback if you like this idea, or even used it (even though you should change the source code to run it for now :) ). 
I would also like to know if you have heard about any other solution to make this kind of stuff ! (Couldn't find any but this Iphone [app](http://everyday-app.com/) on the internet !)
Feel free to mail me for any comment or request. 

You can contact me at julien at lengrand dot fr, or on my [current website](http://www.lengrand.fr).