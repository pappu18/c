from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

k=get_random_bytes(16)
m=b"hello world"

#encryption
cipher=AES.new(k, AES.MODE_EAX)
nonce=cipher.nonce
e=cipher.encrypt(m)

#decryption
decipher=AES.new(k,AES.MODE_EAX,nonce=nonce)
d=decipher.decrypt(e)

print("Encrypted text: ",e)
print("Decrypted text: ",d)
