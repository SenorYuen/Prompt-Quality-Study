class DecryptionUtils:
    def __init__(self, key):
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(shifted_alphabet, alphabet)
        return ciphertext.translate(table)

    def vigenere_decipher(self, ciphertext):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        key = self.key.lower()
        plaintext = ''
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                shift = alphabet.index(key[key_index % len(key)])
                if char.isupper():
                    plaintext += alphabet[(alphabet.index(char.lower()) - shift) % 26].upper()
                else:
                    plaintext += alphabet[(alphabet.index(char) - shift) % 26]
                key_index += 1
            else:
                plaintext += char
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        # Calculate the length of the ciphertext
        length = len(encrypted_text)
        
        # Create a list to store the decrypted text
        decrypted_text = [''] * length
        
        # Calculate the index steps for each rail
        index_steps = []
        for i in range(rails):
            step = (rails - 1 - i) * 2
            if step == 0:
                step = rails * 2 - 2
            index_steps.append(step)
        
        # Initialize the index and the rail index
        index = 0
        rail_index = 0
        
        # Iterate over the rails
        for i in range(rails):
            # Iterate over the indices
            while index < length:
                decrypted_text[index] = encrypted_text[rail_index]
                index += index_steps[i]
                rail_index += 1
        
        # Join the decrypted text into a string
        return ''.join(decrypted_text)