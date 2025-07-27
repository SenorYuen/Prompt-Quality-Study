class EncryptionUtils:
    def __init__(self, key):
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                ciphertext += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                ciphertext += char
        return ciphertext

    def vigenere_cipher(self, plaintext):
        key_index = 0
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                shift = ord(self.key[key_index % len(self.key)].lower()) - 97
                ciphertext += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                key_index += 1
            else:
                ciphertext += char
        return ciphertext

    def rail_fence_cipher(self, plaintext, rails):
        fence = [[] for _ in range(rails)]
        index = 0
        step = 1
        for char in plaintext:
            fence[index].append(char)
            if index == 0:
                step = 1
            elif index == rails - 1:
                step = -1
            index += step
        ciphertext = ""
        for rail in fence:
            ciphertext += "".join(rail)
        return ciphertext