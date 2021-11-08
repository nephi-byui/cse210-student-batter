from game.actor import Actor

class Score(Actor):
    def __init__(self) -> None:
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
