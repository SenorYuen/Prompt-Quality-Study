class DecryptionUtils:
    def __init__(self, key):
        # Initialize the decryption utility with a key
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        # Decipher the given ciphertext using the Caesar cipher
        # Create a string of lowercase and uppercase alphabets
        lowercase_alphabets = 'abcdefghijklmnopqrstuvwxyz'
        uppercase_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        # Initialize an empty string to store the deciphered text
        plaintext = ''
        
        # Iterate over each character in the ciphertext
        for char in ciphertext:
            # Check if the character is an alphabet
            if char.isalpha():
                # Find the index of the character in the alphabet string
                if char.islower():
                    index = lowercase_alphabets.index(char)
                    # Shift the character back by the given shift value
                    new_index = (index - shift) % 26
                    # Append the deciphered character to the plaintext
                    plaintext += lowercase_alphabets[new_index]
                else:
                    index = uppercase_alphabets.index(char)
                    # Shift the character back by the given shift value
                    new_index = (index - shift) % 26
                    # Append the deciphered character to the plaintext
                    plaintext += uppercase_alphabets[new_index]
            else:
                # If the character is not an alphabet, append it as is
                plaintext += char
        
        # Return the deciphered plaintext
        return plaintext

    def vigenere_decipher(self, ciphertext):
        # Decipher the given ciphertext using the Vigenere cipher
        # Create a string of lowercase and uppercase alphabets
        lowercase_alphabets = 'abcdefghijklmnopqrstuvwxyz'
        uppercase_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        # Initialize an empty string to store the deciphered text
        plaintext = ''
        
        # Convert the key to lowercase
        key = self.key.lower()
        
        # Initialize a key index to keep track of the current key character
        key_index = 0
        
        # Iterate over each character in the ciphertext
        for char in ciphertext:
            # Check if the character is an alphabet
            if char.isalpha():
                # Find the index of the character in the alphabet string
                if char.islower():
                    index = lowercase_alphabets.index(char)
                    # Find the index of the current key character in the alphabet string
                    key_char_index = lowercase_alphabets.index(key[key_index % len(key)])
                    # Shift the character back by the given key character value
                    new_index = (index - key_char_index) % 26
                    # Append the deciphered character to the plaintext
                    plaintext += lowercase_alphabets[new_index]
                else:
                    index = uppercase_alphabets.index(char)
                    # Find the index of the current key character in the alphabet string
                    key_char_index = lowercase_alphabets.index(key[key_index % len(key)])
                    # Shift the character back by the given key character value
                    new_index = (index - key_char_index) % 26
                    # Append the deciphered character to the plaintext
                    plaintext += uppercase_alphabets[new_index]
                # Increment the key index
                key_index += 1
            else:
                # If the character is not an alphabet, append it as is
                plaintext += char
        
        # Return the deciphered plaintext
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        # Decipher the given ciphertext using the Rail Fence cipher
        # Calculate the length of the ciphertext
        length = len(encrypted_text)
        
        # Initialize a 2D list to represent the rail fence
        fence = [['' for _ in range(length)] for _ in range(rails)]
        
        # Initialize variables to keep track of the current rail and direction
        curr_rail = 0
        dir = 1
        
        # Iterate over each character in the ciphertext
        for i in range(length):
            # Place the character in the current rail
            fence[curr_rail][i] = encrypted_text[i]
            
            # Update the current rail and direction
            if curr_rail == 0:
                dir = 1
            elif curr_rail == rails - 1:
                dir = -1
            curr_rail += dir
        
        # Initialize an empty string to store the deciphered text
        plaintext = ''
        
        # Read the characters from the fence in a zig-zag manner
        for col in range(length):
            for row in range(rails):
                # Check if the current cell is not empty
                if fence[row][col] != '':
                    # Append the character to the plaintext
                    plaintext += fence[row][col]
        
        # Return the deciphered plaintext
        return plaintext