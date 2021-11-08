# W08 Team Challenge: Batter

## Authors
* Alan Crisanto - alanvcrisanto@gmail.com
* Tianna DeSpain - des17015@byui.edu
* Nephi Malit - byui@nephi.malit.me
* Tatenda Felix Mukaro - muk21002@byui.edu

## The URL for your team's remote repository:
https://github.com/nephi-byui/cse210-student-batter.git

## The grading category that best describes your team's work:
* Exceeds requirements (5)

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

## Classes (13):
* Actor
* Action (abstract)
* Ball
* ControlActorsAction
* Director
* DrawActorsAction
* InputService
* HandleCollisionsAction
* Message
* MoveActorsAction
* OutputService
* Point
* Score