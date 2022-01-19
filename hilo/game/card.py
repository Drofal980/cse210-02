class Card():
    """A paper card with a numerical value
   
    Attributes:
        value (int): The number on a card.
    """

    # 2) Create the class constructor. Use the following method comment.
    def __init__(self):
            """Constructs a new instance of Card with a value attribute.

            Args:
                self (Card): An instance of Card.
            """
            self.value = 0

    def get_number(self):
        """Returns value of card.

        Args:
            self (Card): An instance of Card.
        """
        return self.value

    def set_number(num):
        """Returns value of card.

            Args:
                num: integer value
        """
        self.value = num