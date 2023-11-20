from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad

def encryption(m,k):
    cipher=DES.new(k,DES.MODE_ECB)
    pt=pad(m,DES.block_size)
    e=cipher.encrypt(pt)
    return e
def decryption(e,k):
    decipher=DES.new(k,DES.MODE_ECB)
    upt=decipher.decrypt(e)
    d=unpad(upt,DES.block_size)
    return d
    

k=get_random_bytes(8)
m=b"hello world"
e=encryption(m,k)
print("Encrypted text: ",e)
d=decryption(e,k)
print("Decrypted text: ",d)
  
