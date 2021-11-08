

class ControlActorsAction():

    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):

        self._input_service = input_service


    def execute(self, cast):

        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        direction = self._input_service.get_direction()

        paddle = cast["paddle"][0]
        paddle.set_velicity(direction) 