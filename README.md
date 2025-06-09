### Yvonne Richardson
### STEM 103
### Level 3: final Project

# Wheel of Fortune, the Final Round
# Team: Yvonne Richardson
# Objective
What does the project do? Why is it useful or relevant?

There are two levels to this project.

### Develop a product that is useful, recognizable, and fun.
* The recognizability is in the title of the project and in the project description.
* As for being useful, there are a number of schools of thought on the meaning and usefulness of games. However, exploring that perspective is a non-goal for the project.
* Fun - most games are fun.  Exploration is fun. Games may make the user think that debugging is fun.

### Demonstrate all of the competencies acquired as a result of being a student in this class (and then some).
See the Competencies section.

## PROJECT DESCRIPTION
The project is similar to the bonus round of the famous game show.  Contestants will select a category and then "spin" the wheel for a random and secret prize.

The blanks that represent the puzzle are displayed on the screen, and then the letters "NSTLRE" are filled in, if present.

The contestant guesses 3 consonants and a vowel, and then is given the opportunity to solve the puzzle. Instead of being given 10 seconds to solve, however, the contestant is given 5 tries to type in the correct answer. If they guess correctly, the game will reward them with congratulatory images and messages.  If they do not guess the puzzle in the expected number of tries, the game will display non-congratulatory images and messages, along with the answer to the puzzle.

The user is given the opportunity to play the bonus round again, whereupon the game re-sets itself with another prize and another puzzle.

## COMPETENCIES
The competencies acquired are from every homework assignment from this class.
I am also including the random number generator and some basic string manipulation as described in w3schools.org/python.
This list of competencies is inherently pseudocode, and will be copied into the actual code as appropriate.  Note that the order in which the competencies are in this list may not be the order in which they are demonstrated in the code.
They are as follows:

DataCamp - Python Basics
Input - input the user's choice of categories and letters
Math -  add special items to the list, like money based on length of puzzle.
Output - Display fun things on the screen to increase the feel of the game show experience
Variable - Store user guesses 
DataCamp - Python Logic, Control Flow and Filtering
Elif - work through the user's puzzle guesses
For Loop - fill in the blanks on the screen
Functions -  random number generator, file handling, screen displays
If Else - select consonants or select vowels
Lists - store the choices for the puzzle categories
While - while the user has not completed guessing the puzzle answer and has not run out of guesses
CSV Files - read in the choices for each puzzle category and store them in lists

The plan that guides the implementation is to follow the above specification until the code is complete and fully debugged.  


### RESULTS
The project description is pretty close to the code that I actually wanted to write. It's really easy to plop the human-readable comments into a file and then translate them one line at a time. However, I did have to look up a lot of Python syntax. This style of coding is somewhere between relying on Tooltips with the right-mouse click and looking up the code in a pre-Tooltip paper manual.

Many of these answers might have been found if I had used a debugger that displays the syntax or a link to the correct syntax.  However, locating really good ideas as to how to make my code work is usually beyond the debugger.

I suppose if I had looked long enough, I would have found some examples in the manuals located at w3schools, but sometimes it is useful to see the code in action by studying the snippets that are available online previous to writing your own code. 

#### TESTING
Here are some details on how I tested my project.  For the most part it is string handling, so there are range checks and numeric checks that ensure that
inputs are valid.  For example, if a response is required, it cannot have a length of zero. On the other hand, if you have seen the game directions before,
you can just hit "enter" and the game will continue wihtout displaying the instructions.

There are lists of vowels and consonants to ensure that reqponses are one or the other as required. These are simple loops, so they don't cause a lot of frustration when you get it wrong and cannot get out of the loop. Note that the ampersand ("&") is neither a vowel nor a consonant, even if it is a character within a puzzle answer.

There are similar checks for integers vs. strings. This was useful when working with a list that contains both of them and has to treat them different ways.

### WHAT I LEARNED

There is a worldwide community of Python developers that post code all over the Internet. Not all of them are right, and even the right answers are not always compatible. I explored several ideas for code constructs before I found some that I liked that worked. 

Due to the design constraints, there was nothing that was required that had to be removed from the project.  However, in terms of dressing up a working project, I was able to verify that the sound libraries are incompatible with github.com and the terminal as it was used.

#### CREDITS

My general guideline when surfing the Internet for the syntax that will realize my code is to bookmark every site that I think will help.  This is important because not every piece of code you want works, or is usable, or is compatible with Python and its libraries. For example, there is a Python library that can be used to display emojis.  However, there are a lot of emojis that are not in the Python library, and many Internet sites do not spell them correctly - "blue circle" is not "blue_circle". 

So, without further ado, the following is a list of sites that I used to develop this project.
https://www.w3schools.com/python

https://www.boattrader.com/boat/2025-tahoe-t16-9788171/

https://blog.enterprisedna.co/python-print-without-newline-easy-step-by-step-guide/#:~:text=To%20print%20without%20a%20new,%22)

https://www.digitalocean.com/community/tutorials/python-string-substring

https://en.wikipedia.org/wiki/ANSI_escape_code#Colors

https://www.wheeloffortunelive.com/rules

### NEW PYTHON FEATURES - INSTALLS

There are a number of Python libraries that were used in the development of this project, many of which are not a part of the original language.  We are familiar with imports like datetime or random, but when using code that is outside of the Python libraries, you must use an install in addition to the imports.
Many of the installs can be accomplished using the following syntax.
pip install python-colored-print

When in doubt, the full syntax is as follows:
$ pip install git+https://github.com/ChrisBuilds/terminaltexteffects.git


