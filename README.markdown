#[Take one picture of yourself a day, automatically generate a movie!](http://jlengrand.github.com/FaceMovie/)


**FaceMovie** is a simple project that aims at helping you create videos of yourself over time, using photos as input.
Simply take several pictures of yourself in the same position, and decide when to compile everything into a video. Just indicate the location of your pictures, Facemovie does everything else for you. 

I see a growing interest for projects where people take one picture of themselves a day for several months (years ?) and compile it into a [video](http://www.youtube.com/watch?v=6B26asyGKDo). 
When searching on the web, I realized that there was only one software allowing people to do this : the [everyday paid iphone app](http://www.everyday-app.com). I hope that Facemovie can help some of you!
The main difference with everyday is that Facemovie searches automatically for faces in the input images and compile them in the best possible way, so that your video look awesome. 

Due to its general implementation, FaceMovie may be used for faces, but also profiles (for projects showing [women along pregnancy for example](http://www.youtube.com/watch?v=CG_KArKYTq4) or full body([for people workouting](http://www.youtube.com/watch?v=02Pzfv7JV48)). The only limitation comes from you ! 


## Installation

There are several ways you can choose from to run Facemovie, each being developed below.

### Windows executable (Default)

This is the current easiest solution, as it runs out of the box. 

Download the archive available **[here](https://dl.dropbox.com/u/4286043/GH/FaceMovie/Facemovie-0.8.2-exe.zip)**. 

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

To check the code, simply open a command line and try to run the Facemovifier : 
 ```
 $ cd my\cloned\folder
 $ python Facemoviefier.py -h
 ``` 

### Pipy

The Linux application is also available through a Python egg, available on [Pypi](http://pypi.python.org/pypi/Facemovie/0.8).
You can then simply install Facemovie using [pip] (http://pypi.python.org/pypi/pip): 
```
$ pip install Facemovie
```



## Getting Started

Now that FaceMovie is installed on your system, let's start playing with it !
If you do not have images to play with, note that an [archive including samples](https://dl.dropbox.com/u/4286043/GH/FaceMovie/samples.zip) is available.

For each of the following commands, __Facemovifier__ should be replaced by __FaceMovifier.exe__ or __python Facemovifier__ depending on your installation method.


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

Here is a concrete example : 
```
$ Facemoviefier.exe -i "../data/input/samples" -o "../data/output"
```

**NOTE : ** In order to get good results, your images should contain only one person; and you should try to always keep the same angle with the camera for each of them.

Facemovie needs the list of haar_cascades to correctly detect faces. This means that if you decide to run the Facemovie from another location, you should update the folders accordingly and use the root_folder option:
``` 
$ Facemoviefier -i input_folder -o output_folder -r haar_cascades_folder_location
```

Facemovie also allows you to choose the type of output you want once the processing is done. This can be done by using the --type (-t) option. Here is the case where I save images instead of a movie in output.
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

```
- -i, --input :   Input folder of the images to be processed
- -o, --output :  Output folder where the final results will be saved
```

**Optional :**

```
- -h, --help :  Shows help message and exits
- -r, --root :  Location of the facemovie folder. Required if you run the Facemovifier from an external location
- -p, --param : Used to change the file used to train the classifier. Useful you want to detect something else than front faces.
    Available parameters : 
        - upper body.
        - profile face.
        - lower body.
        - frontal face (default).
        - full body.
- -t, --type :  The type of output to be created. Can be either images, video or simple display (nothing written on disc).
    Available types :
        - video
        - images
        - simple graphical display 
- -s, --sort : The way used to sort images chronologically. Can be done either by using file names or EXIF metadata.
    Available modes :
        - name (default)
        - EXIF 
- -c, --crop : In this mode, final images are cropped so that only the desired part of the body is kept. This will remove parts of the input images, but will avoid addition of black borders in the output.
- -d, --cropdims : Expects two floats here. Ignored if crop mode is not selected. This allows to choose the window to be cropped. The values are defined in "number of face size".
This means that for example -d 2 2 will output square images, of size 2 x the size of the subject face.  
```

## Libraries

The whole aplication is developed using [Python2.7.3](http://www.python.org/download/). Any Python2.7 should be enough though.
To run the application, you'll also need to install [Opencv](http://opencv.willowgarage.com/wiki/).

**NOTE : ** If you are using Ubuntu 12.04, best of luck ! The opencv package is available in the main repo. Simply run :
```
$ sudo aptitude install python-opencv libcv2.3 libcvaux2.3 libhighgui2.3 libopencv-contrib2.3 libopencv-gpu2.3 python-numpy
```

I also used the excellent [exif library](http://sourceforge.net/projects/exif-py/) to enhance sorting capabilities. It is embedded in the code, and you will not need to install it.

This project has been successfully tested on Windows 7 and Ubuntu 12.04 platforms.

## Work in progress

Facemovie is still under development, and you should consider it as work in progress.
Lots of elements still have to be improved. 
You can **[have a look here](https://github.com/jlengrand/FaceMovie/issues?state=open)** to see my next objectives.

## Other ressources

The complete documentation for the code is **[available here](https://dl.dropbox.com/u/4286043/GH/FaceMovie/Facemovie-0.8.2_doc/index.html)**.

But you might also want to download :
- [Complete documentation for the code.](https://dl.dropbox.com/u/4286043/GH/FaceMovie/doc.zip)
- [Samples available to test the code.](https://dl.dropbox.com/u/4286043/GH/FaceMovie/samples.zip)
- [List of available haar cascades.](https://dl.dropbox.com/u/4286043/GH/FaceMovie/haarcascades.zip)

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
**Feel free to [write some words here](https://github.com/jlengrand/FaceMovie/issues?state=open)** for any comment or request. 

You can contact me at julien at lengrand dot fr, or on my [current website](http://www.lengrand.fr).

Version : 0.8.2