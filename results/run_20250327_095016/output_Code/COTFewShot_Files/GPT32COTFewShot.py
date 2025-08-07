class DecryptionUtils:
    def __init__(self, key):
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        plaintext = ''
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
                plaintext += chr(shifted)
            else:
                plaintext += char
        return plaintext

    def vigenere_decipher(self, ciphertext):
        plaintext = ''
        key_length = len(self.key)
        key_as_int = [ord(i) for i in self.key]
        ciphertext_int = [ord(i) for i in ciphertext]
        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value + 65)
        return plaintext.lower()

    def rail_fence_decipher(self, encrypted_text, rails):
        if rails == 1:
            return encrypted_text
        rail = [['\n' for _ in range(len(encrypted_text))]
                for _ in range(rails)]
        dir_down = None
        row, col = 0, 0
        for i in range(len(encrypted_text)):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False
            rail[row][col] = '*'
            col += 1
            if dir_down:
                row += 1
            else:
                row -= 1
        index = 0
        for i in range(rails):
            for j in range(len(encrypted_text)):
                if rail[i][j] == '*' and index < len(encrypted_text):
                    rail[i][j] = encrypted_text[index]
                    index += 1
        result = []
        row, col = 0, 0
        for i in range(len(encrypted_text)):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False
            if rail[row][col] != '*':
                result.append(rail[row][col])
                col += 1
            if dir_down:
                row += 1
            else:
                row -= 1
        return ''.join(result)