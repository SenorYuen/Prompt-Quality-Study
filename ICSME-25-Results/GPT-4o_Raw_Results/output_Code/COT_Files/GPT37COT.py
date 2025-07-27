class EncryptionUtils:
    def __init__(self, key):
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                shift_amount = shift % 26
                shifted = ord(char) + shift_amount
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                ciphertext += chr(shifted)
            else:
                ciphertext += char
        return ciphertext

    def vigenere_cipher(self, plaintext):
        ciphertext = ''
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
        row, col = 0, 0

        for char in plain_text:
            rail[row] += char
            if row == 0 or row == rails - 1:
                direction_down = not direction_down
            row += 1 if direction_down else -1

        return ''.join(rail)