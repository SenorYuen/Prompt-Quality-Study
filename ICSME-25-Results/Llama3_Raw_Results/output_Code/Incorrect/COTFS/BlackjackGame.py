import random

class BlackjackGame:
    def __init__(self):
        # Initialize the Blackjack Game with the attribute deck, player_hand and dealer_hand
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        # Create a deck of 52 cards, which stores 52 random order poker with the Jokers removed
        suits = ['S', 'H', 'D', 'C']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck = [rank + suit for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def calculate_hand_value(self, hand):
        # Calculate the value of the poker cards stored in the hand list according to the rules of the Blackjack Game
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        total_value = sum([values[card[0]] for card in hand])
        num_aces = sum([1 for card in hand if card[0] == 'A'])
        
        # If the total hand value exceeds 21 and there are Aces present, one Ace is treated as having a value of 1 instead of 11
        while total_value > 21 and num_aces:
            total_value -= 10
            num_aces -= 1
        return total_value

    def check_winner(self, player_hand, dealer_hand):
        # Determine the winner of a game by comparing the hand values of the player and dealer
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)
        
        # If both players have hand values that are equal to or less than 21, the winner is the one whose hand value is closer to 21
        if player_value <= 21 and dealer_value <= 21:
            if player_value > dealer_value:
                return 'Player wins'
            elif player_value < dealer_value:
                return 'Dealer wins'
            else:
                return 'Dealer wins'  # In case of a tie, the dealer wins
        # Otherwise, the winner is the one with the lower hand value
        elif player_value <= 21:
            return 'Player wins'
        elif dealer_value <= 21:
            return 'Dealer wins'
        else:
            if player_value < dealer_value:
                return 'Player wins'
            else:
                return 'Dealer wins'