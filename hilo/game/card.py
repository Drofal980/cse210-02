class Card():
    """A paper card with a numerical value
   
    Attributes:
        value (int): The number on a card.
        suit (str): The suit of a card.
    """

    # 2) Create the class constructor. Use the following method comment.
    def __init__(self, value):
            """Constructs a new instance of Card with a value attribute.

            Args:
                self (Card): An instance of Card.
            """
            self.value = value
            self.suit = "Clubs"

    def __str__(self):
        return str(self.value) + " of "+ self.suit