import random

# Shared prime number and base (you can choose different values)
prime = 23
base = 9

# Alice and Bob's private keys (randomly chosen)
private_key_alice = random.randint(1, prime - 1)
private_key_bob = random.randint(1, prime - 1)

# Function to calculate modular exponentiation (a^b % m)
def mod_exp(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b = b // 2
    return result

# Calculate public keys for Alice and Bob
public_key_alice = mod_exp(base, private_key_alice, prime)
public_key_bob = mod_exp(base, private_key_bob, prime)

# Exchange public keys (simulated over a network)
# In a real implementation, these values would be sent to each other securely
shared_secret_alice = mod_exp(public_key_bob, private_key_alice, prime)
shared_secret_bob = mod_exp(public_key_alice, private_key_bob, prime)

# Both Alice and Bob now have the same shared secret
print("Shared Secret (Alice):", shared_secret_alice)
print("Shared Secret (Bob):", shared_secret_bob)
