class Card():
    """A paper card with a numerical value
   
    Attributes:
        value (int): The number on a card.
        suit (str): The suit of a card.
    """

    # 2) Create the class constructor. Use the following method comment.
    def __init__(self, value, suit):
            """Constructs a new instance of Card with a value attribute.

            Args:
                self (Card): An instance of Card.
            """
            self.suit = suit
            self.value = value
            
            face = self.value
            if self.value == 1:
                face = "Ace"
            elif self.value == 11:
                face == "Jack"
            elif self.value == 12:
                face == "Queen"
            elif self.value == 11:
                face == "King"
            self.face = face  

    #defined the get_value to return self. value
    def get_value(self):
        return self.value

    def __str__(self):
        return str(self.face) + " of " + str(self.suit)