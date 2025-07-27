class EncryptionUtils:
    def __init__(self, key):
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                shift_amount = shift % 26
                shifted_char = chr((ord(char.lower()) - ord('a') + shift_amount) % 26 + ord('a'))
                if char.isupper():
                    shifted_char = shifted_char.upper()
                ciphertext += shifted_char
            else:
                ciphertext += char
        return ciphertext

    def vigenere_cipher(self, plaintext):
        ciphertext = ""
        key_length = len(self.key)
        key_as_int = [ord(i) for i in self.key]
        plaintext_int = [ord(i) for i in plaintext]
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        return ciphertext

    def rail_fence_cipher(self, plain_text, rails):
        if rails == 1:
            return plain_text
        rail = ['' for _ in range(rails)]
        direction_down = False
        row = 0
        for char in plain_text:
            rail[row] += char
            if row == 0 or row == rails - 1:
                direction_down = not direction_down
            row += 1 if direction_down else -1
        return ''.join(rail)