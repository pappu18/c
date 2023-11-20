import os
import pyaes

# Generate a random 128-bit (16-byte) AES key
key = os.urandom(16)

# Create an AES cipher object for encryption
aes_encrypt = pyaes.AESModeOfOperationCTR(key)

# Plaintext to encrypt
plaintext = input("Enter the text:")

# Encrypt the plaintext
cipherText = aes_encrypt.encrypt(plaintext.encode('utf-8'))  # Encode plaintext as bytes

# Create a new AES cipher object for decryption with the same key
aes_decrypt = pyaes.AESModeOfOperationCTR(key)

# Decrypt the ciphertext
decrypted = aes_decrypt.decrypt(cipherText).decode('utf-8')  # Decode the decrypted bytes to string

print("Original plaintext:", plaintext)
print("Encrypted ciphertext:", repr(cipherText))
print("Decrypted plaintext:", decrypted)
