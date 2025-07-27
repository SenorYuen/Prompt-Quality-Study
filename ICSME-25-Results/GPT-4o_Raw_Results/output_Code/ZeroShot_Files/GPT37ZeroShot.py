class EncryptionUtils:
    def __init__(self, key):
        """
        Initializes the class with a key.
        """
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The text to be encrypted, str.
        :param shift: The number of positions to shift each character, int.
        :return: The ciphertext, str.
        """
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():  # Only encrypt alphabetic characters
                shift_amount = shift % 26
                base = ord('A') if char.isupper() else ord('a')
                # Shift character and wrap around the alphabet
                cipher_char = chr((ord(char) - base + shift_amount) % 26 + base)
                ciphertext += cipher_char
            else:
                ciphertext += char  # Non-alphabetic characters are added unchanged
        return ciphertext

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The text to be encrypted, str.
        :return: The ciphertext, str.
        """
        ciphertext = []
        key_index = 0
        key_length = len(self.key)
        
        for char in plaintext:
            if char.isalpha():  # Only encrypt alphabetic characters
                key_char = self.key[key_index % key_length].lower()
                shift_amount = ord(key_char) - ord('a')
                base = ord('A') if char.isupper() else ord('a')
                # Shift character by the key character's shift amount
                cipher_char = chr((ord(char) - base + shift_amount) % 26 + base)
                ciphertext.append(cipher_char)
                key_index += 1
            else:
                ciphertext.append(char)  # Non-alphabetic characters are added unchanged
        
        return ''.join(ciphertext)

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plain_text: The text to be encrypted, str.
        :param rails: The number of rails to use in the cipher, int.
        :return: The ciphertext, str.
        """
        if rails <= 1:
            return plain_text  # No encryption if rails are less than or equal to 1
        
        # Create a list of empty strings for each rail
        rail_fence = ['' for _ in range(rails)]
        direction_down = False
        row = 0

        # Place characters in the rail pattern
        for char in plain_text:
            rail_fence[row] += char
            if row == 0 or row == rails - 1:
                direction_down = not direction_down
            row += 1 if direction_down else -1

        # Concatenate strings from all rails
        ciphertext = ''.join(rail_fence)
        return ciphertext