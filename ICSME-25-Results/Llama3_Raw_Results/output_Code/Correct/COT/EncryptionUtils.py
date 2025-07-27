class EncryptionUtils:
    def __init__(self, key):
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                ascii_offset = 97 if char.islower() else 65
                ciphertext += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                ciphertext += char
        return ciphertext

    def vigenere_cipher(self, plaintext):
        key = self.key
        key_index = 0
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                ascii_offset = 97 if char.islower() else 65
                shift = ord(key[key_index % len(key)].lower()) - 97
                ciphertext += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                key_index += 1
            else:
                ciphertext += char
        return ciphertext

    def rail_fence_cipher(self, plaintext, rails):
        if rails == 1:
            return plaintext
        fence = [[] for _ in range(rails)]
        dir = 1
        rail = 0
        for char in plaintext:
            fence[rail].append(char)
            if rail == 0:
                dir = 1
            elif rail == rails - 1:
                dir = -1
            rail += dir
        ciphertext = ""
        for rail in fence:
            ciphertext += "".join(rail)
        return ciphertext