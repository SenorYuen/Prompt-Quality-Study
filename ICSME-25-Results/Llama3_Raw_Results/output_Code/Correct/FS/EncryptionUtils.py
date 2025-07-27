class EncryptionUtils:
    """
    This is a class that provides methods for encryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.
        """
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        """
        # Initialize an empty string to store the ciphertext
        ciphertext = ""
        
        # Iterate over each character in the plaintext
        for char in plaintext:
            # Check if the character is an uppercase letter
            if char.isupper():
                # Calculate the ASCII value of the encrypted character
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
                # Append the encrypted character to the ciphertext
                ciphertext += encrypted_char
            # Check if the character is a lowercase letter
            elif char.islower():
                # Calculate the ASCII value of the encrypted character
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
                # Append the encrypted character to the ciphertext
                ciphertext += encrypted_char
            # If the character is not a letter, append it to the ciphertext as is
            else:
                ciphertext += char
        
        # Return the ciphertext
        return ciphertext

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        # Initialize an empty string to store the ciphertext
        ciphertext = ""
        
        # Initialize a counter to keep track of the current position in the key
        key_index = 0
        
        # Iterate over each character in the plaintext
        for char in plaintext:
            # Check if the character is an uppercase letter
            if char.isupper():
                # Calculate the ASCII value of the encrypted character
                encrypted_char = chr((ord(char) - 65 + ord(self.key[key_index].upper()) - 65) % 26 + 65)
                # Append the encrypted character to the ciphertext
                ciphertext += encrypted_char
                # Move to the next character in the key
                key_index = (key_index + 1) % len(self.key)
            # Check if the character is a lowercase letter
            elif char.islower():
                # Calculate the ASCII value of the encrypted character
                encrypted_char = chr((ord(char) - 97 + ord(self.key[key_index].lower()) - 97) % 26 + 97)
                # Append the encrypted character to the ciphertext
                ciphertext += encrypted_char
                # Move to the next character in the key
                key_index = (key_index + 1) % len(self.key)
            # If the character is not a letter, append it to the ciphertext as is
            else:
                ciphertext += char
        
        # Return the ciphertext
        return ciphertext

    def rail_fence_cipher(self, plaintext, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The number of rails to use, int.
        :return: The ciphertext, str.
        """
        # Initialize a list to store the rails
        rail_list = [""] * rails
        
        # Initialize a counter to keep track of the current rail
        rail_index = 0
        
        # Initialize a flag to indicate the direction of the rail
        going_down = True
        
        # Iterate over each character in the plaintext
        for char in plaintext:
            # Append the character to the current rail
            rail_list[rail_index] += char
            
            # If we are going down and we are not at the last rail, move to the next rail
            if going_down and rail_index < rails - 1:
                rail_index += 1
            # If we are going down and we are at the last rail, start going up
            elif going_down and rail_index == rails - 1:
                going_down = False
                rail_index -= 1
            # If we are going up and we are not at the first rail, move to the previous rail
            elif not going_down and rail_index > 0:
                rail_index -= 1
            # If we are going up and we are at the first rail, start going down
            elif not going_down and rail_index == 0:
                going_down = True
                rail_index += 1
        
        # Initialize an empty string to store the ciphertext
        ciphertext = ""
        
        # Iterate over each rail and append its characters to the ciphertext
        for rail in rail_list:
            ciphertext += rail
        
        # Return the ciphertext
        return ciphertext