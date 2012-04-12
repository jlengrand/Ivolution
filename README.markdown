#Take on picture of yourself a day, simply get the results!

[FaceMovie](http://www.lengrand.fr) is a simple project that aims at helping you create videos of yourself over time, using photos as input.
I see a growing interest for this kind of projects, where people take one picture of themselves a day for several months (years ?) and compile it into a video. 
I started this project for a friend currently [travelling around the world](http://www.lengrand.fr). He wanted to create a video of its face changes along the trip.

The main idea is simple. The software takes a batch of images as input. The images are assumed to be named by date (so that an alphabetical order is also the chronological order).
The output is a video containing each image, where the face is centered and always placed in the same position. This way, people can actually see the face change over time.

**In progress: **

- The very central part of the code is finished. 
- I currently work on video quality enhancement (compression, speed, fade effects, ...)
- I plan to include a GUI to help people use the software, and later add support for a broader type of input images (profiles, eyes, glasses, . . .)
- I also think about a way for user to help the software in case it struggles with images (by manually pointing face on problematic images?). 
- Any other idea is welcome

## Getting started

## Libraries

The language I used to create this piece of software is Python, simply because I love it :P (and because it allows easy testing while developing IP applications).
I used Python 2.7 for development. 
The only library needed to run the code for now is Opencv (and by extension Numpy). See the documentation for more information. 

This project is developed on a windows platform, but there should be no compatibility problems with UNIX. 

## License

## Contact

I would enjoy having feedback if you like this idea, or even used it (even though you should change the source code to run it for now :) ). 
I would also like to know if you have heard about any other solution to make this kind of stuff ! (Couldn't find any on the internet!)
Feel free to mail me for any comment or request. 

You can contact me at julien at lengrand dot fr, or on my [current website](http://www.lengrand.fr)

Last update : 4/12/2012