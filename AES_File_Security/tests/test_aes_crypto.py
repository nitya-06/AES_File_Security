import unittest
from src.aes_crypto import AESFileSecurity
import os

class TestAESFileSecurity(unittest.TestCase):
    def setUp(self):
        self.key = b"testkey12345678"
        self.aes = AESFileSecurity(self.key)
        self.sample_file = "resources/sample.txt"
        self.encrypted_file = "resources/sample.encrypted"
        self.decrypted_file = "resources/sample_decrypted.txt"
        with open(self.sample_file, "w") as f:
            f.write("Hello, AES!")

    def test_encrypt_decrypt(self):
        self.aes.encrypt(self.sample_file, self.encrypted_file)
        self.aes.decrypt(self.encrypted_file, self.decrypted_file)

        with open(self.sample_file, "r") as f1, open(self.decrypted_file, "r") as f2:
            self.assertEqual(f1.read(), f2.read())

    def tearDown(self):
        os.remove(self.sample_file)
        os.remove(self.encrypted_file)
        os.remove(self.decrypted_file)

if __name__ == "__main__":
    unittest.main()
