class DecryptionUtils:
    def __init__(self, key):
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                shift_amount = shift % 26
                shifted = ord(char) - shift_amount
                if char.islower() and shifted < ord('a'):
                    shifted += 26
                elif char.isupper() and shifted < ord('A'):
                    shifted += 26
                plaintext += chr(shifted)
            else:
                plaintext += char
        return plaintext

    def vigenere_decipher(self, ciphertext):
        plaintext = ''
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                shift_amount = ord(self.key[key_index % len(self.key)].lower()) - ord('a')
                shifted = ord(char) - shift_amount
                if char.islower() and shifted < ord('a'):
                    shifted += 26
                elif char.isupper() and shifted < ord('A'):
                    shifted += 26
                plaintext += chr(shifted)
                key_index += 1
            else:
                plaintext += char
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        if rails == 1:
            return encrypted_text

        n = len(encrypted_text)
        rail = [['\n' for _ in range(n)] for _ in range(rails)]
        dir_down = None
        row, col = 0, 0

        for _ in range(n):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False
            rail[row][col] = '*'
            col += 1
            row += 1 if dir_down else -1

        index = 0
        for i in range(rails):
            for j in range(n):
                if rail[i][j] == '*' and index < n:
                    rail[i][j] = encrypted_text[index]
                    index += 1

        result = []
        row, col = 0, 0
        for _ in range(n):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False
            if rail[row][col] != '\n':
                result.append(rail[row][col])
                col += 1
            row += 1 if dir_down else -1
        return ''.join(result)