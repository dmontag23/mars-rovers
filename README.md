# Mars Rovers - Solution

# Setup

## Run with Docker
To run this code with Docker, first ensure Docker is installed on your machine (you can download and install
Docker by following the instructions at https://docs.docker.com/get-docker/).

Clone the repo. In the base directory, run ``docker build -t mars-rovers . && docker run -it mars-rovers``.
## Run with Python
In order to run this code with python, you need to have python version 3.7.9 or later installed on your local machine.
You can install python at https://www.python.org/downloads/.

### Running the application
Clone the repo. In the base directory, run ``python3 main.py`` to run the application.

### Running the unit tests
In the base directory, run ``python3 -m unittest -v`` to run the unit tests.

# Overview of the Solution

The idea behind the solution is to have a primary class, called ``Rover``, which stores a ``Terrain`` (grid)
on which the rover can move. The ``Terrain`` class checks whether a new coordinate point is on the current plane, 
while the rest of the logic is implement as methods in the ``Rover`` class. The ``CreateRovers`` class
provides a way for users to interface with the ``Rover`` class using the command line input.

# Improvement and Extensions
## Improvements
- Type-checking: There are many places in the code (such as the Rover class) where the type of the class
  members should be checked. Since the user input should catch all errors now this isn't
  a big deal, but it could become one should other input methods be added/extensions to the code are made.
- Implementation of the CreateRovers class: Right now, the CreateRovers class is a utility class (it contains all static methods).
  It may be better to redesign the class in a way that fits better with other input classes, should those be created
  in the future (see the extensions section below). Perhaps the class should also be named differently to reflect
  the fact that it primarily deals with user input.
- Implementation of directions: Right now, the actual character of the direction the rover is facing is stored 
  in the Rover class. It might be better to implement this value as an index to the appropriate value in the DIRECTIONS
  tuple so that the index does not need to be looked up every time the rover turns.
- Exceptions: The way exceptions are handled right now is a bit messy, which could lead to an inconsistent user experience.
  I try to raise exceptions as close to the user input as possible so that the user is informed as soon as possible 
  as to whether or not their input is valid. However, there are other exceptions within the code that try and account 
  for bad input should another input method be utilized. I also catch some exceptions only to throw a more specific 
  exception message, which may not be the best approach to handling those types of situations.
- Program flow: Right now, the program runs on an infinite loop unless an exception is thrown, in which case the program
  crashes. This does not provide a nice experience for the user. It would be better to have the user terminate the program
  whenever they want and, when an error is thrown, the user should be notified and have a chance to re-input a correct value.
## Extensions
- Input: Different input classes could be created that allow reading the input from a file, via an API, etc.
- UI: It would be fun to create a UI where the user could input the values for the terrain grid and various starting points/commands for the rover(s) and watch the rover(s) move on the plateau.
