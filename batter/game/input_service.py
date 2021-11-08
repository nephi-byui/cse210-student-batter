import sys
from game.point import Point
from game import constants
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self, screen):
        """The class constructor."""
        self._screen = screen
        self._keys = {}

        speed_factor = constants.PADDLE_SPEED
        self._keys[-1] = "exit" # Esc
        self._keys[27] = "exit" # Esc
        self._keys[97] = Point( -speed_factor, 0) # a
        self._keys[100] = Point( speed_factor, 0) # d
        
    def get_direction(self):
        """Gets the selected direction for the given player, or exits when Esc is pressed

        Returns:
            Point: The selected direction.
        """
        direction = Point(0, 0)
        event = self._screen.get_event()
            
        if isinstance(event, KeyboardEvent):            
            direction = self._keys.get(event.key_code, Point(0, 0))
        if direction == "exit":
            sys.exit()
        else:
            return direction
