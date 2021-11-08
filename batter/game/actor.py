from game import constants
from game.point import Point
import random

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _tag (string): The actor's tag.
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    """

    def __init__(self):
        """The class constructor."""
        self._description = ""
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

#     def get_description(self):
#         """Gets the artifact's description.
        
#         Returns:
#             string: The artifact's description.
#         """
#         return self._description 

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def set_description(self, description):
        """Updates the actor's description to the given one.
        
        Args:
            description (string): The given description.
        """
        self._description = description

    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_text(self, text):
        """Updates the actor's text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            position (Point): The given velocity.
        """
        self._velocity = velocity

class Ball(Actor):
    """A class of Actor that plays the Ball
    """
    def __init__(self):
        """
        The class constructor
        Args:
            self (Ball): an instance of Ball
        """
        super().__init__()

    def bounce_up(self):
        """Makes the ball bounce in a random direction direction
        Args:
            self (Ball): an instance of Ball
        """
        speed = 1
        speed_list = [-speed, speed]
        x = random.choice(speed_list)
        #y = random.randint(-speed, -1)
        y = random.choice(speed_list)
        velocity = Point(abs(x), abs(y))
        self.set_velocity(velocity)

    def bounce(self,direction=""):

        position = self.get_velocity()
        x = position.get_x()
        speed = 1
        x_list = [-speed, speed]
        y_list = [-speed, 0, speed]

        x = random.choice(x_list)
        if direction == "up":
            y = -1
        elif direction == "down":
            y = 1
        else:
            y = random.choice(y_list)
        velocity = Point(x, y)
        self.set_velocity(velocity)

class Message(Actor):
    """The game over message, win or lose
    """
    def __init__(self):
        """
        The class constructor
        Args:
            self (Ball): an instance of Ball
        """
        super().__init__()
        self._text = ""

    def win(self):
        self.set_text("\o/ YOU WIN! \o/")

    def lose(self):
        self.set_text("T_T YOU LOSE T_T")