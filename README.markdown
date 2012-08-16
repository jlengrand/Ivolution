#[Take one picture of yourself a day, automatically generate a movie!](http://jlengrand.github.com/FaceMovie/)


**Ivolution** is a simple project that aims at helping you create videos of yourself over time, using photos as input.
Simply take several pictures of yourself in the same position, and decide when to compile everything into a video. Just indicate the location of your pictures, Ivolution does everything else for you. 

Due to its general implementation, FaceMovie may be used for faces, but also profiles (for projects showing [women along pregnancy for example](http://www.youtube.com/watch?v=CG_KArKYTq4) or full body([for people workouting](http://www.youtube.com/watch?v=02Pzfv7JV48)). The only limitation comes from you ! 


## Installation

There are several ways you can choose from to run Ivolution, each being developed below.

### Ubuntu 12.04

First of all, install the dependencies :
 ```
 $ apt-get install python-opencv python-gi python-numpy
 ```

Retrieve the archive from [pypi](http://pypi.python.org/pypi/Ivolution/1.0)
 ```
 $ wget http://pypi.python.org/packages/source/I/Ivolution/Ivolution-0.5.1.tar.gz
 ``` 

Uncompress the archive and move into it
 ```
 $ tar xvf Ivolution-0.5.1.tar.gz; cd Ivolution-0.5.1
 ``` 

Finally, install the application (need administrators rights)
 ```
 $ python setup.py install --record files.txt 
 ``` 

**NOTE : ** __The --record option is used to ease later uninstallation. Keep the files.txt somewhere on your computer__


### Other linux distributions :

The steps should be the same as for Ubuntu, but for the dependencies. 
To run Ivolution, you need access to [Opencv](http://opencv.willowgarage.com/wiki/) and its python bindings and [GTK+](https://live.gnome.org/PyGObject).


### Windows (**Soon**)

### Github

You can also simply clone the project from Github and use it as you wish. 
```
git clone git://github.com/jlengrand/FaceMovie.git
```

## Getting Started

Now that Ivolution is installed on your system, let's start playing with it !
To run Ivolution, simply run it from any terminal :
 ```
 $ Ivolutioner
 ``` 

## Work in progress

Facemovie is still under development, and you should consider it as work in progress.
Lots of elements still have to be improved. 
You can **[have a look here](https://github.com/jlengrand/FaceMovie/issues?state=open)** to see my next objectives.

## License

This project is released under the new BSD license (3 clauses version). You can read more about the license in the LICENSE file or direclty on [GNU's website](http://www.gnu.org/licenses/license-list.html#ModifiedBSD). 

## Acknowledgment

The idea of this project comes from an idea of Axel Catoire, currently [travelling around the world](http://ungrandtour.blogspot.com/) with his girlfriend.
As a starter for my code, I used an excellent example from JAPSKUA, that you can find [here](http://japskua.wordpress.com/2010/08/04/detecting-eyes-with-python-opencv/)
And I used [Gene Cash's library](http://sourceforge.net/projects/exif-py/) to extract information from EXIF metadata in the images.

Finally, the logo of Ivolution comes from an image of [Luc Viatour](www.Lucnix.be).

## DISCLAIMER

Facemovie works with your images, so I feel like I need to write something about data usage. 
Facemovie is a work in progress, and I am not responsible for any corrpution it could cause to your data. 
I never experienced any problem using the software, but you should always back up your data before using it.

## Why this project 


I see a growing interest for projects where people take one picture of themselves a day for several months (years ?) and compile it into a [video](http://www.youtube.com/watch?v=6B26asyGKDo). 
When searching on the web, I realized that there was only one software allowing people to do this : the [everyday paid iphone app](http://www.everyday-app.com). I hope that Ivolution can help some of you!
The main difference with everyday is that Ivolution searches automatically for faces in the input images and compile them in the best possible way, so that your video look awesome. 

## Contact

I would enjoy having feedback if you like this idea, or even used it. Send me a link to your creations so that I can put them here !
**Feel free to [write some words here](https://github.com/jlengrand/FaceMovie/issues?state=open)** for any comment or request. 

You can contact me at julien at lengrand dot fr, or on my [current website](http://www.lengrand.fr).

Version : 0.5.1