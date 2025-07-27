import random

class BlackjackGame:
    """
    This is a class representing a game of blackjack, which includes creating a deck, calculating the value of a hand, and determine the winner based on the hand values of the player and dealer.
    """

    def __init__(self):
        """
        Initialize the Blackjack Game with the attribute deck, player_hand and dealer_hand.
        While initializing deck attribute, call the create_deck method to generate.
        The deck stores 52 rondom order poker with the Jokers removed, format is ['AS', '2S', ...].
        player_hand is a list which stores player's hand cards.
        dealer_hand is is a list which stores dealer's hand cards.
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        """
        Create a deck of 52 cards, which stores 52 rondom order poker with the Jokers removed.
        :return: a list of 52 rondom order poker with the Jokers removed, format is ['AS', '2S', ...].
        """
        # Define the suits and ranks of a deck of cards
        suits = ['S', 'H', 'D', 'C']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        # Generate the deck using list comprehension
        deck = [rank + suit for suit in suits for rank in ranks]
        
        # Shuffle the deck to randomize the order of the cards
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
        # Initialize the total hand value and the number of Aces
        total_value = 0
        num_aces = 0
        
        # Iterate over each card in the hand
        for card in hand:
            # Extract the rank of the card
            rank = card[0]
            
            # Check if the card is an Ace
            if rank == 'A':
                # Increment the number of Aces
                num_aces += 1
                # Add 11 to the total hand value (Ace is initially worth 11)
                total_value += 11
            # Check if the card is a face card (J, Q, K)
            elif rank in ['J', 'Q', 'K']:
                # Add 10 to the total hand value (face cards are worth 10)
                total_value += 10
            # If the card is not an Ace or a face card, it's a numbered card
            else:
                # Add the value of the numbered card to the total hand value
                total_value += int(rank)
        
        # If the total hand value exceeds 21 and there are Aces present, adjust the value of the Aces
        while total_value > 21 and num_aces:
            # Subtract 10 from the total hand value (one Ace is now worth 1 instead of 11)
            total_value -= 10
            # Decrement the number of Aces
            num_aces -= 1
        
        return total_value

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
        # Calculate the hand values of the player and dealer
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)
        
        # Check if both players have hand values that are equal to or less than 21
        if player_value <= 21 and dealer_value <= 21:
            # The winner is the one whose hand value is closer to 21
            if player_value > dealer_value:
                return 'Player wins'
            elif player_value < dealer_value:
                return 'Dealer wins'
            else:
                # If the hand values are equal, it's a tie
                return 'Tie'
        # If one or both players have hand values that exceed 21, the winner is the one with the lower hand value
        elif player_value <= 21:
            return 'Player wins'
        elif dealer_value <= 21:
            return 'Dealer wins'
        else:
            # If both players have hand values that exceed 21, the winner is the one with the lower hand value
            if player_value < dealer_value:
                return 'Player wins'
            else:
                return 'Dealer wins'