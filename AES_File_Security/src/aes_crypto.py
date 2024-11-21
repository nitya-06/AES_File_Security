from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class AESFileSecurity:
    def __init__(self, key: bytes):
        self.key = pad(key, 16)  # Ensure the key is 16 bytes (128 bits)

    def encrypt(self, input_file: str, output_file: str):
        cipher = AES.new(self.key, AES.MODE_CBC)
        with open(input_file, 'rb') as f:
            plaintext = f.read()
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        with open(output_file, 'wb') as f:
            f.write(cipher.iv)  # Write IV to the beginning of the file
            f.write(ciphertext)

    def decrypt(self, input_file: str, output_file: str):
        with open(input_file, 'rb') as f:
            iv = f.read(16)  # Read the IV
            ciphertext = f.read()
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        with open(output_file, 'wb') as f:
            f.write(plaintext)
