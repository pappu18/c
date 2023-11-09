import hashlib

# Input string
input_string = "Hello, SHA-256!"

# Create a SHA-256 hash object
sha256 = hashlib.sha256()

# Update the hash object with the input string (encoded as bytes)
sha256.update(input_string.encode('utf-8'))

# Get the hexadecimal representation of the hash
hashed_string = sha256.hexdigest()

# Print the SHA-256 hash
print("SHA-256 Hash:", hashed_string)

'''
from cryptography.fernet import Fernet

# Generate a random symmetric encryption key
key = Fernet.generate_key()

# Create a Fernet cipher with the generated key
cipher = Fernet(key)

# Input data to be encrypted
input_data = b"Hello, encryption and decryption!"

# Encrypt the data
encrypted_data = cipher.encrypt(input_data)
print("Encrypted Data:", encrypted_data)

# Decrypt the data using the same key
decrypted_data = cipher.decrypt(encrypted_data)
print("Decrypted Data:", decrypted_data.decode('utf-8'))

'''
