class EncryptionUtils:
    """
    This is a class that provides methods for encryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.
        """
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.caesar_cipher("abc", 1)
        'bcd'
        """
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                shift_amount = shift % 26
                start = ord('a') if char.islower() else ord('A')
                new_char = chr(start + (ord(char) - start + shift_amount) % 26)
                ciphertext += new_char
            else:
                ciphertext += char
        return ciphertext

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        """
        ciphertext = ""
        key_length = len(self.key)
        key_int = [ord(i) for i in self.key]
        plaintext_int = [ord(i) for i in plaintext]
        for i in range(len(plaintext_int)):
            if plaintext[i].isalpha():
                value = (plaintext_int[i] + key_int[i % key_length]) % 26
                start = ord('a') if plaintext[i].islower() else ord('A')
                ciphertext += chr(start + value)
            else:
                ciphertext += plaintext[i]
        return ciphertext

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plain_text: The plaintext to encrypt, str.
        :param rails: The number of rails to use in the cipher, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'
        """
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