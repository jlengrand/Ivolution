#Take on picture of yourself a day, simply get the results!


**[FaceMovie](http://www.youtube.com/watch?v=JueOY7EtXrQ)** is a simple project that aims at helping you create videos of yourself over time, using photos as input.
I see a growing interest for this kind of projects, where people take one picture of themselves a day for several months (years ?) and compile it into a [video](http://www.youtube.com/watch?v=6B26asyGKDo). 
I started this project for a friend currently [travelling around the world](http://http://ungrandtour.blogspot.com/). He wanted to create a video of his face changes along the trip.

The main idea is simple. The software takes a batch of images as input. The images are assumed to be named by date (so that an alphabetical order is also the chronological order).
The output is a video containing each image, where the face is always placed in the same position. This way, people can actually see the face change over time.

**[You can check out the last results in video here !](http://www.youtube.com/watch?v=JueOY7EtXrQ)**

**In progress: **

- The very central part of the code is finished. 
- I currently work on video quality enhancement (compression, speed, fade effects, ...)
- I plan to include a GUI to help people use the software, and later add support for a broader type of input images (profiles, eyes, glasses, . . .)
- I also think about a way for user to help the software in case it struggles with images (by manually pointing face on problematic images?). 
- Any other idea is welcome

## Getting started

## Libraries

This piece of code is developed in [Python](http://www.python.org/), simply because I love it :P (and because it allows easy testing while developing Image Processing applications).
I used Python 2.7 for development. 
The only library needed to run the code for now is [Opencv](http://opencv.willowgarage.com/wiki/) (and by extension [Numpy](http://numpy.scipy.org/)). See [the documentation](http://opencv.willowgarage.com/wiki/InstallGuide) for more information. 

This project is developed on a Windows (7) platform, but there should (and, as a fanatic Linux User, will) be no compatibility problems with UNIX. 

## License

Not defined yet. Let's say that the code is public and that you can use it and modify it as you want. 
I would simply love is a short message (like "Thank you !" or "You rock !" :p) if you find the project useful. 

## Contact

I would enjoy having feedback if you like this idea, or even used it (even though you should change the source code to run it for now :) ). 
I would also like to know if you have heard about any other solution to make this kind of stuff ! (Couldn't find any but this Iphone [app](http://everyday-app.com/) on the internet !)
Feel free to mail me for any comment or request. 

You can contact me at julien at lengrand dot fr, or on my [current website](http://www.lengrand.fr).