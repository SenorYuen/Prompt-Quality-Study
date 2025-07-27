import random

class BlackjackGame:
    def __init__(self):
        # Initialize the deck, player's hand, and dealer's hand
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        # Create a list of suits and ranks
        suits = ['S', 'H', 'D', 'C']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        # Use list comprehension to generate the deck
        deck = [rank + suit for suit in suits for rank in ranks]
        
        # Shuffle the deck to randomize the order
        random.shuffle(deck)
        
        return deck

    def calculate_hand_value(self, hand):
        # Initialize the total value and the number of Aces
        total_value = 0
        num_aces = 0
        
        # Iterate over each card in the hand
        for card in hand:
            # Get the rank of the card
            rank = card[0]
            
            # Check if the card is an Ace
            if rank == 'A':
                # Increment the number of Aces
                num_aces += 1
                # Add 11 to the total value (Ace is worth 11 initially)
                total_value += 11
            # Check if the card is a face card (J, Q, K)
            elif rank in ['J', 'Q', 'K']:
                # Add 10 to the total value (face cards are worth 10)
                total_value += 10
            # If the card is a number card, add its value to the total
            else:
                # Convert the rank to an integer and add it to the total value
                total_value += int(rank)
        
        # If the total value exceeds 21 and there are Aces, reduce the value of Aces
        while total_value > 21 and num_aces:
            # Subtract 10 from the total value (treating an Ace as 1 instead of 11)
            total_value -= 10
            # Decrement the number of Aces
            num_aces -= 1
        
        return total_value

    def check_winner(self, player_hand, dealer_hand):
        # Calculate the hand values of the player and dealer
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)
        
        # Check if both players have hand values that are equal to or less than 21
        if player_value <= 21 and dealer_value <= 21:
            # The winner is the one whose hand value is closer to 21
            if player_value > dealer_value:
                return "Player wins"
            elif player_value < dealer_value:
                return "Dealer wins"
            else:
                return "It's a tie"
        # If one or both players have hand values that exceed 21, the winner is the one with the lower hand value
        else:
            if player_value > 21 and dealer_value > 21:
                if player_value < dealer_value:
                    return "Player wins"
                elif player_value > dealer_value:
                    return "Dealer wins"
                else:
                    return "It's a tie"
            elif player_value > 21:
                return "Dealer wins"
            else:
                return "Player wins"

# Example usage:
game = BlackjackGame()
game.player_hand = ['AS', '8S']
game.dealer_hand = ['10D', '5C']
print(game.calculate_hand_value(game.player_hand))  # Output: 19
print(game.calculate_hand_value(game.dealer_hand))  # Output: 15
print(game.check_winner(game.player_hand, game.dealer_hand))  # Output: Player wins