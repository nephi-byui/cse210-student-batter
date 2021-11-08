# Batter
What's your batting average? Find out with this terminal version of the arcade 
classic. The goal is simple. Just bat the ball at the blricks until there are 
none left. If you miss the ball the game is over.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and asciimatics 1.12.0 or new installed 
and running on your machine. You can install Asciimatics by opening a terminal 
and running the following command.
```
python3 -m pip install asciimatics
```
After you've installed the required libraries, open a terminal and browse to the 
project's root folder. Start the program by running the following command.
```
python3 batter 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the hunter folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- batter              (source code for game)
  +-- game              (specific game classes)
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Asciimatics 1.12.0

## Authors
* Alan Crisanto - alanvcrisanto@gmail.com
* Tianna DeSpain - des17015@byui.edu
* Nephi Malit - byui@nephi.malit.me
* Tatenda Felix Mukaro - muk21002@byui.edu

## Batter Game Rules:
* The bricks are arranged in 4 rows and 70 columns at the top of the screen.
* The bat (or paddle) is positioned near the bottom of the screen.
* The player can move the bat left or right within the boundaries of the screen.
* The ball moves of its own accord, bouncing off the bat, bricks and walls.
* If the bat misses the ball the game is over.

## Basic Requirements met:
* The program must use the Batter template: https://github.com/byui-cse/cse210-student-batter
* The program must have a README file with assignment and author names.
* The program must have at least ten classes.
* Each module, class and method must have a corresponding comment using the style demonstrated in the solo checkpoint.
* The game must remain generally true to the order of play described in the rules.

## Extra Features implemented (options in constants.py):
* Enhanced feedback (score)
* Enhanced appearance (longer bat, more balls)
* Enhanced screens (vicotry, game over, messages)
* Options (configurable in constants.py)

## Options
* ZEN_MODE (True or False) : ball bounces off the bottom of screen
* BALL_COUNT (INT) : have more than one ball on screen
* PADDLE_SPEED (INT) : set the user-controlled paddle speed movement
* PADDLE_LENGTH (INT) : set the length of the paddle 
