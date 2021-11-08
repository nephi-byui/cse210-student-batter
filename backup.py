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
        self._verify = True



    #Execution
    def execute(self, cast):
        """Executes the action using the given actors.  
        * Collision or Bouncing on bricks , bat and wall
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        if self._verify:
            paddle = cast["paddle"][0] # only one instance
            ball = cast["ball"][0] # only one instance
            bricks = cast["brick"]
            score = cast["score"][0] # only one instance
            speed = 1
            speed_list = [-speed, speed]

            # BALL on BRICK collision
            for brick in bricks:
                if ball.get_position().equals(brick.get_position()):
                        
                        # add points
                        score.add_points(1)
                        score.refresh()

                        ball.bounce()
                        # ball_velocity = ball.get_velocity()
                        #new_velocity = ball_velocity.reverse()
                        #ball.set_velocity(new_velocity)
                        #
                        cast['brick'].remove(brick)
                        self._verify  = False

            # IMMINENT BALL on PADDLE collision
            # for a more realistic bounce, it should bounce before collision and never overlap

            ball_position = ball.get_position()
            ball_x = ball_position.get_x()

            paddle_position = paddle.get_position()
            paddle_x = paddle_position.get_x()

            if ball.get_position().equals(above_pad):
                x = random.choice(speed_list)
                y = random.randint(-speed, -1)
                velocity = Point(x, y)
                ball.set_velocity(velocity)
                #ball.bounce()
                self._verify = False
                #return            



            # BALL collide with y-axis-GAME_OVER_Y
            ball_position = ball.get_position()
            ball_y = ball_position.get_y()
            if ball_y == constants.GAME_OVER_Y:
                # GAME OVER
                sys.exit()

        else:
            self._verify = True


 



        
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
