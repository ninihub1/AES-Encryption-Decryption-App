from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

class Encryptor:
    def __init__(self, key):
        """
        Initializes the Encryptor with the provided AES key.
        :param key: AES key.
        """
        self.key = key

    def encrypt(self, plaintext):
        """
        Encrypts the provided plaintext with the provided AES key.
        :param plaintext: The plaintext to be encrypted.
        :return: Encrypted plaintext.
        """
        cipher = AES.new(self.key, AES.MODE_CBC)
        iv = cipher.iv
        cipher_text = cipher.encrypt(pad(plaintext.encode('utf8'), AES.block_size))
        return iv + cipher_text