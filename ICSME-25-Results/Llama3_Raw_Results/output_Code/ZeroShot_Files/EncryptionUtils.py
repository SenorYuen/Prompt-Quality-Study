# This is a class that provides methods for encryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.

class EncryptionUtils:
    def __init__(self, key):
        # Initializes the class with a key.
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        # Encrypts the plaintext using the Caesar cipher.
        # Convert the plaintext to lowercase and remove non-alphabetic characters.
        plaintext = ''.join(filter(str.isalpha, plaintext)).lower()
        
        # Initialize an empty string to store the ciphertext.
        ciphertext = ""
        
        # Iterate over each character in the plaintext.
        for char in plaintext:
            # Calculate the ASCII value of the character after shifting.
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            # Append the shifted character to the ciphertext.
            ciphertext += shifted_char
        
        # Return the ciphertext.
        return ciphertext

    def vigenere_cipher(self, plaintext):
        # Encrypts the plaintext using the Vigenere cipher.
        # Convert the plaintext and key to lowercase and remove non-alphabetic characters.
        plaintext = ''.join(filter(str.isalpha, plaintext)).lower()
        key = ''.join(filter(str.isalpha, self.key)).lower()
        
        # Initialize an empty string to store the ciphertext.
        ciphertext = ""
        
        # Initialize a counter to keep track of the current position in the key.
        key_index = 0
        
        # Iterate over each character in the plaintext.
        for char in plaintext:
            # Calculate the shift value based on the current character in the key.
            shift = ord(key[key_index]) - ord('a')
            
            # Calculate the ASCII value of the character after shifting.
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            # Append the shifted character to the ciphertext.
            ciphertext += shifted_char
            
            # Move to the next character in the key.
            key_index = (key_index + 1) % len(key)
        
        # Return the ciphertext.
        return ciphertext

    def rail_fence_cipher(self, plain_text, rails):
        # Encrypts the plaintext using the Rail Fence cipher.
        # Initialize a list of lists to represent the rails.
        rail = [''] * rails
        
        # Initialize variables to keep track of the current rail and direction.
        dir_down = False
        row, col = 0, 0
        
        # Iterate over each character in the plaintext.
        for char in plain_text:
            # Append the character to the current rail.
            rail[row] += char
            
            # If we are at the top or bottom rail, change direction.
            if row == 0:
                dir_down = True
            elif row == rails - 1:
                dir_down = False
            
            # Move to the next rail based on the current direction.
            row += 1 if dir_down else -1
        
        # Initialize an empty string to store the ciphertext.
        ciphertext = ""
        
        # Iterate over each rail and append its characters to the ciphertext.
        for i in range(rails):
            ciphertext += rail[i]
        
        # Return the ciphertext.
        return ciphertext

# Example usage:
utils = EncryptionUtils("key")
print(utils.caesar_cipher("Hello, World!", 3))
print(utils.vigenere_cipher("Attack at dawn"))
print(utils.rail_fence_cipher("WEAREDISCOVEREDSAVEYOURSELF", 3))