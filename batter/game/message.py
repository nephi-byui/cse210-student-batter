from game.actor import Actor

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
        """ Displays text for a victorious game
        Args:
            self (Ball): an instance of Ball
        """
        self.set_text("\o/ YOU WIN! \o/")

    def lose(self):
        """ Displays text for a losing game
        Args:
            self (Ball): an instance of Ball
        """
        self.set_text("T_T YOU LOSE T_T")