from game.actor import Actor

class Score(Actor):
    """ An Actor responsible for displaying the score
    args:
        Actor: the parent class
    """
    def __init__(self) -> None:
        """ The class constructor
        Args:
            self (Score):   an instance of Score
        """
        super().__init__()
        self._score = 0
        self._prefix = "Score: "
        self.refresh()

    def add_points(self,points):
        """
        Adds points to the score
        Args:
            self (Score):   an instance of Score
        Returns:
            none
        """
        self._score += points

    def refresh(self):
        """
        Updates the Actor._text based on self._score
        Args:
            self (Score):   an instance of Score
        Returns:
            none
        """
        self._text = f"{self._prefix}{self._score}"

    def get_score(self):
        """
        Returns the currenct score
        Args:
            self (Score):   an instance of Score
        Returns:
            score
        """
        return self._score
