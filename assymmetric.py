import rsa

# Generate RSA key pair with small key sizes (for educational purposes)
public_key, private_key = rsa.newkeys(512)

# Message to encrypt
message = "Hello, RSA!"

# Encrypt the message using the public key
encrypted_message = rsa.encrypt(message.encode(), public_key)
print("Encrypted message:", encrypted_message)

# Decrypt the message using the private key
decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
print("Decrypted message:", decrypted_message)
