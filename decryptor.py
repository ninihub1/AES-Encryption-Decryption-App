from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

class Decryptor:
    def __init__(self, key):
        """
        Initializes the decryptor with the provide AES key.
        :param key: AES key.
        """
        self.key = key

    def decrypt(self, cipher_text):
        """
        Decrypts the provided cipher text.
        :param cipher_text: The cipher text.
        :return: The decrypted cipher text.
        """
        iv = cipher_text[:AES.block_size]
        encrypted_data = cipher_text[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        return plaintext.decode('utf-8')