import random
from game import actor, constants
from game.point import Point
from game.move_actors_action import MoveActorsAction
from game.action import Action

# Update on the solo collisions class for week 8 - batter-collision

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
        
    Attributes:
        _verify - checks collisions  on movement frames against boolean  value
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
            paddle = cast["paddle"] # there's only one
            ball = cast["ball"][0] # there's only one
            bricks = cast["brick"] # Define result of impact on bricks
            speed = 1
            speed_list = [-speed, speed]

        # Collision on bricks

        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                    ball.set_floor()
                    cast['brick'].remove(brick)
                    self._verify  = False
                    return
        

            # Padle implementation
        for pad in paddle:
            if ball.get_position().equals(pad.get_position()):
                x = random.choice(speed_list)
                y = random.randint(-speed, -1)
                velocity = Point(x, y)
                ball.set_velocity(velocity)

                self._verify = False
                return

            
            self._verify = False


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
