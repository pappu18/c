def encrypt(message, key):
    # Calculate the number of columns needed
    num_columns = len(key)
    # Pad the message with spaces to make its length a multiple of the number of columns
    padded_message = message + ' ' * (num_columns - (len(message) % num_columns))
    
    # Create a list of columns
    columns = [padded_message[i::num_columns] for i in range(num_columns)]
    
    # Arrange columns according to the key
    sorted_columns = [column for _, column in sorted(zip(key, columns))]
    
    # Concatenate the columns to get the encrypted message
    encrypted_message = ''.join(sorted_columns)
    
    return encrypted_message

def decrypt(encrypted_message, key):
    # Calculate the number of columns needed
    num_columns = len(key)
    
    # Calculate the number of rows needed
    num_rows = len(encrypted_message) // num_columns
    
    # Create a list of columns
    columns = [encrypted_message[i*num_rows:(i+1)*num_rows] for i in range(num_columns)]
    
    # Arrange columns according to the key
    sorted_columns = [column for _, column in sorted(zip(key, columns))]
    
    # Concatenate the columns to get the decrypted message
    decrypted_message = ''.join([''.join(row) for row in zip(*sorted_columns)])
    
    return decrypted_message

# Example usage:
message = "HELLOWORLD"
key = [3, 1, 4, 2]
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
