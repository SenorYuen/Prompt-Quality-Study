import random

class BlackjackGame:
    """
    This is a class representing a game of blackjack, which includes creating a deck, calculating the value of a hand, and determine the winner based on the hand values of the player and dealer.
    """

    def __init__(self):
        """
        Initialize the Blackjack Game with the attribute deck, player_hand and dealer_hand.
        While initializing deck attribute, call the create_deck method to generate.
        The deck stores 52 random order poker with the Jokers removed, format is ['AS', '2S', ...].
        player_hand is a list which stores player's hand cards.
        dealer_hand is a list which stores dealer's hand cards.
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        """
        Create a deck of 52 cards, which stores 52 random order poker with the Jokers removed.
        :return: a list of 52 random order poker with the Jokers removed, format is ['AS', '2S', ...].
        """
        # Suits and ranks for a standard deck of cards
        suits = ['S', 'H', 'D', 'C']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        # Create the deck by combining each rank with each suit
        deck = [rank + suit for suit in suits for rank in ranks]
        
        # Shuffle the deck to randomize the order
        random.shuffle(deck)
        
        return deck

    def calculate_hand_value(self, hand):
        """
        Calculate the value of the poker cards stored in hand list according to the rules of the Blackjack Game.
        If the card is a digit, its value is added to the total hand value.
        Value of J, Q, or K is 10, while Aces are worth 11.
        If the total hand value exceeds 21 and there are Aces present, one Ace is treated as having a value of 1 instead of 11,
        until the hand value is less than or equal to 21, or all Aces have been counted as value of 1.
        :param hand: list
        :return: the value of the poker cards stored in hand list, a number.
        """
        value = 0
        ace_count = 0
        
        # Calculate initial hand value and count aces
        for card in hand:
            rank = card[:-1]  # Get the rank part of the card
            if rank.isdigit():  # If the rank is a number
                value += int(rank)
            elif rank in ['J', 'Q', 'K']:  # Face cards are worth 10
                value += 10
            elif rank == 'A':  # Count Aces as 11 initially
                value += 11
                ace_count += 1
        
        # Adjust for Aces if value exceeds 21
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        
        return value

    def check_winner(self, player_hand, dealer_hand):
        """
        Determines the winner of a game by comparing the hand values of the player and dealer.
        rule:
        If both players have hand values that are equal to or less than 21, the winner is the one whose hand value is closer to 21.
        Otherwise, the winner is the one with the lower hand value.
        :param player_hand: list
        :param dealer_hand: list
        :return: the result of the game, only two certain str: 'Dealer wins' or 'Player wins'
        """
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)

        # Determine the winner based on the calculated hand values
        if player_value > 21:
            return 'Dealer wins'
        elif dealer_value > 21:
            return 'Player wins'
        elif player_value > dealer_value:
            return 'Player wins'
        else:
            return 'Dealer wins'