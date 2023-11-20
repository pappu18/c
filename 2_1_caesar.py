def encrypt(m,s):
    res=""
    for i in m:
        if i.isupper():
            res=res+chr((ord(i) + s - 65)%26 + 65)
        elif i.isdigit():
            res=res+chr((ord(i) + s - 48)%10 +48)
        elif i.islower():
            res=res+chr((ord(i) + s - 97)%26 + 97)
        else:
            res+=i
    return res

def decrypt(e,s):
    res=''
    for i in e:
        if i.isupper():
            res=res+chr((ord(i) - s - 65)%26 + 65)
        elif i.isdigit():
            res=res+chr((ord(i) - s - 48)%10 + 48)
        elif i.islower():
            res=res+chr((ord(i) - s - 97)%26 +97)
        else:
            res+=i
    return res
            

m=input("Enter plain text:")
s=int(input("Enter the shift value:"))
e=encrypt(m,s)
print("The encrypted message is:",e)
d=decrypt(e,s)
print("The decrypted message is:",d)
