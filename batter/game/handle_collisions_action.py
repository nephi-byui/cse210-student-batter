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
        _verify - checks collisions on movement frames against boolean  value
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
        ball = cast["ball"][0] # only one instance
        bricks = cast["brick"]
        score = cast["score"][0] # only one instance
        #speed = 1
        #speed_list = [-speed, speed]

        ball_position = ball.get_position()
        ball_x = ball_position.get_x()
        ball_y = ball_position.get_y()

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
                    break



        # IMMINENT BALL on PADDLE collision
        # for a more realistic bounce, it should bounce before collision and never overlap                       


        paddle_position = paddle.get_position()
        paddle_x_start = paddle_position.get_x() - 1
        paddle_x_end = paddle_x_start + constants.PADDLE_LENGTH + 1

        if ball_x in range (paddle_x_start,paddle_x_end) and ball_y == constants.PADDLE_Y_LEVEL - 1:
            ball.bounce()
            #ball.bounce()
            #x = random.choice(speed_list)
            #y = random.randint(-speed, -1)
            #velocity = Point(x, y)
            #ball.set_velocity(velocity)

        # make ball bounce off the edges
        elif ball_x == 0 or ball_y == 1 or ball_y == constants.MAX_Y-1 or ball_y == constants.GAME_OVER_Y:
            ball.bounce()

        elif ball_y == constants.GAME_OVER_Y:
            # GAME OVER
            #sys.exit()

            """
            if ball.x .equals(above_pad):
                x = random.choice(speed_list)
                y = random.randint(-speed, -1)
                velocity = Point(x, y)
                ball.set_velocity(velocity)
                #ball.bounce()
                self._verify = False
                #return            
                # 
            """



        # BALL collide with y-axis-GAME_OVER_Y
        #ball_position = ball.get_position()
        #ball_y = ball_position.get_y()
        #if ball_y == constants.GAME_OVER_Y:
        #    # GAME OVER
        #    sys.exit()

 



        
        #...................................................................
        #Commented code from solo project code
        # marquee = cast["marquee"][0] # there's only one
        # robot = cast["robot"][0] # there's only one
        # artifacts = cast["artifact"]
        # marquee.set_text("")
        # for artifact in artifacts:
        #     if robot.get_position().equals(artifact.get_position()):
        #         description = artifact.get_description()
        #         marquee.set_text(description) 
