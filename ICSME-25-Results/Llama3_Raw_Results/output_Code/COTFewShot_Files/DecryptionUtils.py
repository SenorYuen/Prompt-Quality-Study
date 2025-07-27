class DecryptionUtils:
    def __init__(self, key):
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = 97 if char.islower() else 65
                plaintext += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                plaintext += char
        return plaintext

    def vigenere_decipher(self, ciphertext):
        key = self.key
        key_index = 0
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = 97 if char.islower() else 65
                shift = ord(key[key_index].lower()) - 97
                plaintext += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                key_index = (key_index + 1) % len(key)
            else:
                plaintext += char
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        # Calculate the length of each rail
        rail_lengths = [0] * rails
        index = 0
        for i in range(len(encrypted_text)):
            rail_lengths[index] += 1
            if index == 0:
                direction = 1
            elif index == rails - 1:
                direction = -1
            index += direction

        # Initialize the rails
        rails_list = [''] * rails
        index = 0
        for i in range(len(encrypted_text)):
            rails_list[index] += encrypted_text[i]
            if index == 0:
                direction = 1
            elif index == rails - 1:
                direction = -1
            index += direction

        # Reconstruct the plaintext
        plaintext = [''] * len(encrypted_text)
        index = 0
        for i in range(rails):
            for j in range(rail_lengths[i]):
                plaintext[index] = rails_list[i][j]
                if i == 0:
                    direction = 1
                elif i == rails - 1:
                    direction = -1
                index += (rails - 1) * direction if i == 0 or i == rails - 1 else direction

        return ''.join(plaintext)