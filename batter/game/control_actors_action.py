from game import constants
from game.action import Action
from game.point import Point

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        paddle = cast["paddle"][0]

        position = paddle.get_position()
        current_x = position.get_x()

        leftmost_edge = position.get_x() - 1
        rightmost_edge = int(position.get_x() + constants.PADDLE_LENGTH + 1)

        proposed_velocity = direction
        proposed_change_in_x = proposed_velocity.get_x()

        # stop at leftmost edge
        if leftmost_edge in [0,1] and proposed_change_in_x < 0:
            pass
        # stop at rightmost edge
        elif rightmost_edge in [(constants.MAX_X - 1), constants.MAX_X ]and proposed_change_in_x > 0:
            pass
        # move otherwise
        else:
            new_x = current_x + proposed_change_in_x
            new_y = constants.PADDLE_Y_LEVEL
            if new_x < 0:
                new_x = 0
            elif new_x + constants.PADDLE_LENGTH > constants.MAX_X:
                new_x = constants.MAX_X - constants.PADDLE_LENGTH
            new_position = Point(new_x,new_y)
            paddle.set_position(new_position)
        
