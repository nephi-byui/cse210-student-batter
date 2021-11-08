import random
from game import constants
from game import actor, constants
from game.point import Point
from game.move_actors_action import MoveActorsAction
from game.action import Action
import sys

# Update on the solo collisions class for week 8 - batter-collision

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
        
    Attributes:
    """

    def __init__(self):
        """HandleCollisionsAction class constructor        
        Args:
            self -  Instance of HandleCOllisionAction
        """



    #Execution
    def execute(self, cast):
        """Executes the action using the given actors.  
        * Collision or Bouncing on bricks , bat and wall
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        paddle = cast["paddle"][0] # only one instance
        #ball = cast["ball"][0] # only one instance
        
        balls = cast["ball"]
        
        score = cast["score"][0] # only one instance
        bricks = cast["brick"]
        message = cast["message"][0]

        for ball in balls:

            ball_position = ball.get_position()
            ball_x = ball_position.get_x()
            ball_y = ball_position.get_y()

            paddle_position = paddle.get_position()
            paddle_x_start = paddle_position.get_x()
            paddle_x_end = paddle_x_start + constants.PADDLE_LENGTH

            # IMMINENT BALL on PADDLE collision
            # for a more realistic bounce, it should bounce before collision and never overlap                     

            if ball_x in range (paddle_x_start,paddle_x_end) and ball_y == constants.PADDLE_Y_LEVEL - 1:
                ball.bounce("up")

            # make ball bounce off the edges
            elif ball_y in [0,1]:
                ball.bounce("down")

            #elif ball_x == 0 or ball_y == 1 or ball_y == 1:
            #    ball.bounce()

            # if ball
            elif ball_y >= constants.GAME_OVER_Y:
                
                if not constants.ZEN_MODE:
                    ball.set_velocity(Point(0,0))
                    ball.set_text("x")

                    message.lose()

                else:
                    ball.bounce("up")


            else:
                # BALL on BRICK collision
                for brick in bricks:
                    brick_position = brick.get_position()
                    if ball_position.equals(brick_position):
                            
                        # add points
                        score.add_points(1)
                        score.refresh()

                        # make ball bounce
                        ball.bounce()

                        # destroy brick
                        cast['brick'].remove(brick)
                        
                        current_score = score.get_score()
                        if current_score == 280:
                            message.win()
                        
                        break






 

 
