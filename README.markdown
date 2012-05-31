#Take one picture of yourself a day, automatically generate a movie!


**[FaceMovie](http://www.youtube.com/watch?v=JueOY7EtXrQ)** is a simple project that aims at helping you create videos of yourself over time, using photos as input.
Simply take several pictures of yourself in the same position, and decide when to compile everything into a video. Just indicate the location of your pictures, Facemovie does everything else for you. 

I see a growing interest for projects where people take one picture of themselves a day for several months (years ?) and compile it into a [video](http://www.youtube.com/watch?v=6B26asyGKDo). 
When searching on the web, I realized that there was only one software allowing people to do this, the [everyday paid iphone app](everyday url). I hope that Facemovie could help some of you!
The main difference with everyday is that Facemovie searches automatically for faces in the input images and compile them in the best possible way, so that your video lok awesome. 

Due to its general implementation, FaceMovie may be used for faces, but also profiles (for projects showing [women along pregnancy for example](http://www.youtube.com/watch?v=CG_KArKYTq4) or full body([for people workouting](http://www.youtube.com/watch?v=02Pzfv7JV48)). The only limitation comes from you ! 

**[You can check out an example of video here.](http://www.youtube.com/watch?v=2pUHK7Sf23I)**.


## Getting started


There are several ways you can choose from to run Facemovie, each being developed below.
Please not that you best pick as this stage would be to choose the executable. 

### Windows executable (Default)

This is the current safest and easiest solution for you. 

Download the archive available [here](). By default, choose the full archive.
The light archive is intended for users having Python2.7 already installed on their system. In this case, a python.dll is given with the executable.

Uncompress the archive. It contains three elements :
 - The executable itself, called Facemovifier.exe.
 - A folder called haar_cascades. It contains files used by the executable. Leave it in the same location as the executable by default.
 - This README

 In order to check that everything is ready, open a command line in at the executable location and run the Facemovie helper : 
 ```
 $ cd my\installation\folder
 $ Facemoviefier.exe -h
 ``` 

 You are now ready to use the Facemovie !

### Github

You can also simply clone the project from Github and use it as you wish. 
```
git clone git://github.com/jlengrand/FaceMovie.git
```

This is a very good solution if you already have Python2.7 and OpenCV installed on your system (see requirements chapter).

To check the code, simply open a command line and try to run the Facemovifier : 
 ```
 $ cd my\cloned\folder
 $ python facemovie\Facemoviefier.py -h
 ``` 

Scripts are available for Windows and Linux (called __run.sh__ and __run_windows.sh__) in order to help you run Facemovie. 



- Download a single executable [here](). Choose the file corresponding to your architecture, unzip the archive and you're done !
  - Depending on your setup, you can choose installers including the Python interpreter or not. 
  - The executable ships with a folder called haar__cascades and containing elements needed for the recognition phaze of the algorithm. 
  Leave them in the same location as the executable by default.
- Install the Python package via pip. (see command here).
  - setup install
  - You'll need some libraries installed to run the code, but the Facemovifier command will be available in your Python interpreter. 
- Clone the project from Github and use the code. For this, you will have to install all the tool needed to run the Python code(see requirements chapter below).
```
git clone git://github.com/jlengrand/FaceMovie.git
```
  - I created scripts for Windows and Linux in the repo, so that the code can be used easily.
  - This way, you'll get the last version of the code

For each of the following commands, __Facemovifier__ should be replaced by __FaceMovifier.exe__ or __python Facemovifier__ depending on your installation method (executable or Python egg).


Once installed, let's start by calling the helper of Facemovie. It can be done by
```
$ Facemoviefier -h
```
depending whether you used the installer or the Python egg. 
This command will list all the available parameters that can be used.

The next step is to try to create you first video. It is no more complex than running the following in command line :
```
$ Facemoviefier -i input_folder -o output_folder
```
Where input_folder is the repository where all your images are stored, and output_folder where you want the results to be saved. 
If you don't have images, you can still test the application by downloading some samples [here](lien vers samples).

Here is a concrete example : 
```
$ Facemoviefier.exe -i "../data/input/samples" -o "../data/output"
```

**NOTE : ** In order to get good results, your  images should contain only one person; and you should try to always keep the same angle with the camera for each of them.


Facemovie needs the list of haar_cascades to correctly detect faces. This means that if you decide to run the Facemovie from another location, you should update the folders accordingly and use the root_folder option:
``` 
$ Facemoviefier -i input_folder -o output_folder -r haar_cascades_folder_location
```


Facemovie allows you to choose the type of output you want once the processing is done. This can be done by using the --type (-t) option. Here is the case where I save images instead of a movie in output.
```
$ Facemoviefier -i "../data/input/Axel" -o "../data/output" -t i
```

By default, Facemovie is searching for frontal faces. You can change this by setting up which profile to use using the --profile (-p) option:  
```
$ Facemoviefier -i "../data/input/Axel" -o "../data/output" -p "profile face"
```
An extensive list of training files is available while calling the helper, or by running the following command.
```
$ Facemoviefier -p ?
```

### Options available in the Facemoviefier

**Required :**

- -i, --input : 	Input folder of the images to be processed
- -o, --output : 	Output folder where the final results will be saved

**Optional :**

- -h, --help :	Shows help message and exits
- -r, --root : 	Location of the facemovie folder. Required if you run the Facemovifier from an external location
- -e, --equalize : If this option is activated, images will NOT be resized so that all faces have the same size.
- -p, --param :	Used to change the file used to train the classifier. Useful you want to detect something else than front faces.
    Available parameters : 
        - upper body.
        - profile face.
        - lower body.
        - frontal face (default).
        - full body.
- -t, --type :	The type of output to be created. Can be either images, video or simple display (nothing written on disc).
    Available types :
        - video
        - images
        - simple graphical display
- -e, --equalize : When this option is activated, Facemovie will **NOT** resize images so that faces always keep the same size. This may result in lower quality results but avoid resizing images. 
- -s, --sort : The way used to sort images chronologically. Can be done either by using file names or EXIF metadata.
    Available modes :
        - name (default)
        - EXIF 
- -c, --crop : In this mode, final images are cropped so that only the desired part of the body is kept. This will remove parts of the input images, but will avoid addition of black borders in the output.
- -d, --cropdims : Expects two floats here. Ignored if crop mode is not selected. This allows to choose the window to be cropped. The values are defined in "number of face size".
This means that for example -d 2 2 will output square images, of size 2 x the size of the subject face.  


## Libraries

The whole aplication is developed using [Python2.7.3](http://www.python.org/download/). Any Python2.7 should be enough though.
To run the application, you'll also need to install [Opencv](http://opencv.willowgarage.com/wiki/).See [the documentation](http://opencv.willowgarage.com/wiki/InstallGuide) for more information. 

I also used the excellent [exif library](http://sourceforge.net/projects/exif-py/) to enhance sorting capabilities. It is embedded in the code, and you will not need to install it.

This project is developed on a Windows (7) platform, but there should (and, as a fanatic Linux User, will) be no compatibility problems with UNIX. 
The Linux application will be made available through a Python egg, available on [Pypi](http://pypi.python.org/pypi).

## Work in progress

Facemovie is still under development, and you should consider it as work in progress.
Lots of elements still have to be improved. 

Here is a list of my next objectives : 

 - Implement a simple GUI to avoid this ugly command line interface
 - Allow manual interaction to help the algorithm. When no face is found, the software currently discard the image. I would allow the user to point the face himself.
 - Implement a feature that detects and corrects roations (for when the face is not always straight)
 - Enhance documentation and tests
 - **Any idea is welcome !**

## License

This project is released under the new BSD license (3 clauses version). You can read more about the license in the LICENSE file or direclty on [GNU's website](http://www.gnu.org/licenses/license-list.html#ModifiedBSD). 

## Acknowledgment

The idea of this project comes from an idea of Axel Catoire, currently [travelling around the world](http://ungrandtour.blogspot.com/) with his girlfriend.
As a starter for my code, I used an excellent example from JAPSKUA, that you can find [here](http://japskua.wordpress.com/2010/08/04/detecting-eyes-with-python-opencv/)
And I used Gene Cash's library to extract information from EXIF metadata in the images.

## DISCLAIMER

Facemovie works with your images, so I feel like I need to write something about data usage. 
Facemovie is a work in progress, and I am not responsible for any corrpution it could cause to your data. 
I never experienced any problem using the software, but you should always back up your data before using it.

## Contact

I would enjoy having feedback if you like this idea, or even used it. Send me a link to your creations so that I can put them here !
Feel free to mail me for any comment or request. 

You can contact me at julien at lengrand dot fr, or on my [current website](http://www.lengrand.fr).

Version : 0.8.1