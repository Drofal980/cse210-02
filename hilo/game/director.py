from game.cards import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        deck (List[Card]): A list of Card() instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.deck = []
        self.is_playing = True
        self.score = 300
        self.total_score = 0

        #Creates a Card, sets value, and adds to a list
        for i in range(13):
            card = Card()
            card.set_number(i)
            self.deck.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if the next card will be higher or lower. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print("The card is: ")
        
        