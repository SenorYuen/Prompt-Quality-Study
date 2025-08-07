class DecryptionUtils:
    """
    This is a class that provides methods for decryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption,str.
        """
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        """
        Deciphers the given ciphertext using the Caesar cipher
        :param ciphertext: The ciphertext to decipher,str.
        :param shift: The shift to use for decryption,int.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.caesar_decipher('ifmmp', 1)
        'hello'
        """
        plaintext = []
        for char in ciphertext:
            if char.isalpha():
                shift_amount = shift % 26
                shifted = ord(char) - shift_amount
                if char.islower() and shifted < ord('a'):
                    shifted += 26
                elif char.isupper() and shifted < ord('A'):
                    shifted += 26
                plaintext.append(chr(shifted))
            else:
                plaintext.append(char)
        return ''.join(plaintext)

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'
        """
        plaintext = []
        key_length = len(self.key)
        key_int = [ord(i) for i in self.key]
        ciphertext_int = [ord(i) for i in ciphertext]
        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_int[i % key_length]) % 26
            plaintext.append(chr(value + 65))
        return ''.join(plaintext).lower()

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'
        """
        if rails == 1:
            return encrypted_text

        rail = [['\n' for i in range(len(encrypted_text))]
                for j in range(rails)]

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