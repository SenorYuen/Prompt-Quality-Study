class DecryptionUtils:
    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        """
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        """
        Deciphers the given ciphertext using the Caesar cipher
        :return: The deciphered plaintext, str.
        """
        plaintext = []
        for char in ciphertext:
            if char.isalpha():
                shift_amount = shift % 26
                shifted = ord(char) - shift_amount
                if char.islower():
                    if shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted < ord('A'):
                        shifted += 26
                plaintext.append(chr(shifted))
            else:
                plaintext.append(char)
        return ''.join(plaintext)

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :return: The deciphered plaintext, str.
        """
        plaintext = []
        key_length = len(self.key)
        key_as_int = [ord(i) for i in self.key]
        ciphertext_int = [ord(i) for i in ciphertext]
        
        for i in range(len(ciphertext_int)):
            if ciphertext[i].isalpha():
                value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
                if ciphertext[i].islower():
                    plaintext.append(chr(value + ord('a')))
                else:
                    plaintext.append(chr(value + ord('A')))
            else:
                plaintext.append(ciphertext[i])
        
        return ''.join(plaintext)

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :return: The deciphered plaintext, str.
        """
        if rails == 1:
            return encrypted_text
        
        # Create an empty matrix to mark the rail positions
        matrix = [['\n' for _ in range(len(encrypted_text))] for _ in range(rails)]
        
        # Mark the rail positions with '*'
        direction_down = None
        row, col = 0, 0
        
        for i in range(len(encrypted_text)):
            if row == 0:
                direction_down = True
            if row == rails - 1:
                direction_down = False
            
            matrix[row][col] = '*'
            col += 1
            
            if direction_down:
                row += 1
            else:
                row -= 1
        
        # Fill the matrix with the encrypted text
        index = 0
        for i in range(rails):
            for j in range(len(encrypted_text)):
                if matrix[i][j] == '*' and index < len(encrypted_text):
                    matrix[i][j] = encrypted_text[index]
                    index += 1
        
        # Read the matrix in a zigzag manner to decrypt
        result = []
        row, col = 0, 0
        for i in range(len(encrypted_text)):
            if row == 0:
                direction_down = True
            if row == rails - 1:
                direction_down = False
            
            if matrix[row][col] != '\n':
                result.append(matrix[row][col])
                col += 1
            
            if direction_down:
                row += 1
            else:
                row -= 1
        
        return ''.join(result)