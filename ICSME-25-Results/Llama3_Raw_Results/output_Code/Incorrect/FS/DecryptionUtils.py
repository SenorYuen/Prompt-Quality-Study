class DecryptionUtils:
    """
    This is a class that provides methods for decryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption,str.
        """
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        """
        Deciphers the given ciphertext using the Caesar cipher
        :param ciphertext: The ciphertext to decipher,str.
        :param shift: The shift to use for decryption,int.
        :return: The deciphered plaintext,str.
        """
        # Initialize an empty string to store the deciphered text
        plaintext = ""
        
        # Iterate over each character in the ciphertext
        for char in ciphertext:
            # Check if the character is an uppercase letter
            if char.isupper():
                # Calculate the ASCII value of the deciphered character
                # and convert it back to a character
                plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
            # Check if the character is a lowercase letter
            elif char.islower():
                # Calculate the ASCII value of the deciphered character
                # and convert it back to a character
                plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
            # If the character is not a letter, add it to the plaintext as is
            else:
                plaintext += char
        
        # Return the deciphered plaintext
        return plaintext

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        """
        # Initialize an empty string to store the deciphered text
        plaintext = ""
        
        # Initialize a counter to keep track of the current position in the key
        key_index = 0
        
        # Iterate over each character in the ciphertext
        for char in ciphertext:
            # Check if the character is an uppercase letter
            if char.isupper():
                # Calculate the shift value based on the current character in the key
                shift = ord(self.key[key_index % len(self.key)].upper()) - 65
                
                # Calculate the ASCII value of the deciphered character
                # and convert it back to a character
                plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
                
                # Move to the next character in the key
                key_index += 1
            # Check if the character is a lowercase letter
            elif char.islower():
                # Calculate the shift value based on the current character in the key
                shift = ord(self.key[key_index % len(self.key)].lower()) - 97
                
                # Calculate the ASCII value of the deciphered character
                # and convert it back to a character
                plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
                
                # Move to the next character in the key
                key_index += 1
            # If the character is not a letter, add it to the plaintext as is
            else:
                plaintext += char
        
        # Return the deciphered plaintext
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        """
        # Initialize a list to store the rails
        rail_list = [''] * rails
        
        # Initialize a counter to keep track of the current rail
        rail_index = 0
        
        # Initialize a flag to indicate the direction of the rail
        going_down = True
        
        # Iterate over each character in the encrypted text
        for char in encrypted_text:
            # Add the character to the current rail
            rail_list[rail_index] += char
            
            # If we are going down and we are not at the last rail, move to the next rail
            if going_down and rail_index < rails - 1:
                rail_index += 1
            # If we are going up and we are not at the first rail, move to the previous rail
            elif not going_down and rail_index > 0:
                rail_index -= 1
            # If we are at the last rail and going down, change direction and move to the previous rail
            elif going_down and rail_index == rails - 1:
                going_down = False
                rail_index -= 1
            # If we are at the first rail and going up, change direction and move to the next rail
            elif not going_down and rail_index == 0:
                going_down = True
                rail_index += 1
        
        # Initialize an empty string to store the deciphered text
        plaintext = ""
        
        # Iterate over each rail
        for rail in rail_list:
            # Add the characters from the rail to the plaintext
            plaintext += rail
        
        # Return the deciphered plaintext
        return plaintext