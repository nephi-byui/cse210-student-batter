from game.actor import Actor
from game.point import Point
import random

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

    def bounce(self, direction=""):
        """Makes the ball bounce
        Args:
            self (Ball): an instance of Ball
            direction (STR): can be "up" or "down"
        """
        position = self.get_velocity()
        x = position.get_x()
        speed = 1
        x_list = [-speed, speed]
        y_list = [-speed, 0, speed]

        if direction == "up":
            x = random.choice(x_list)
            y = -1
        elif direction == "down":
            x = random.choice(x_list)
            y = 1
        elif direction == "left":
            x = -1
            y = random.choice(y_list)
        elif direction == "right":
            x = 1
            y = random.choice(y_list)
        elif direction == "down-left":
            x = 1
            y = -1
        elif direction == "down-right":
            x = 1
            y = 1
        else:
            x = random.choice(x_list)
            y = random.choice(y_list)

        velocity = Point(x, y)
        self.set_velocity(velocity)