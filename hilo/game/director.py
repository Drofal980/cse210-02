from game.card import Card
import random


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
        self.deck_size = 13
        self.is_playing = True
        self.score = 300
        self.total_score = 0
        suits = ["Clubs", "Hearts", "Spades", "Diamonds"]

        #Creates a Card, sets value, and adds to a list
        
        for suit in suits:
            for i in range(self.deck_size):
                card = Card(i+1, suit)
                self.deck.append(card)
        
        #Shuffles deck
        random.shuffle(self.deck)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            print()
            self.do_outputs()
            input = self.get_inputs()
            self.do_updates(input)
            if self.check_score():
                self.play_again()
            else:
                self.is_playing = False

    def get_inputs(self):
        """Ask the user if next card is higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        prompt = True
        while prompt:
            decision = input("Higher or lower? [h/l] ").lower()
            if decision == 'h' or 'l':
                prompt == False
                return decision
        
    def do_updates(self, input):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        
        current_card = self.deck[0]
        next_card = self.deck[1]

        print("The next card is: " + str(next_card))
    
        #The player earns 100 points if they guessed correctly
        if input == "h":
            if  next_card.get_value() > current_card.get_value():
                self.score += 100
            #The player looses 75 points if they guessed incorrectly
            else:
                self.score -= 75
        elif input == "l":
            if next_card.get_value() < current_card.get_value():
                self.score += 100
            else:
                self.score -= 75
        
        print("Your score is: " + str(self.score))

        #Moves top card to bottom of deck
        self.move_top_card_to_bottom()

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if the next card will be higher or lower. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print("The card is: " + str(self.draw_card()))

        
    def draw_card(self):
        if not self.is_playing:
            return
        #Return first card
        return self.deck[0]

    def move_top_card_to_bottom(self):
        self.deck.append(self.deck[0])
        self.deck.remove(self.deck[0])
    
    def check_score(self):
        #if the player reaches 0 points the game is over
        if self.score <= 0:
            return False
        return True

    def play_again(self):
        if not self.is_playing:
            return
        correct_input = True
        while correct_input:
            decision = input("Play again? [y/n] ")
            if decision == 'n':
                correct_input = False
                self.is_playing = False
            elif decision == 'y':
                correct_input = False
                # self.is_playing = True
            else:
                print("Please use y or n")
                
            

        