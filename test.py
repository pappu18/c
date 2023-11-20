def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def e_gcd(a,b):
    if a==0:
        return b,0,1
    g,x1,y1=e_gcd(b%a,a)
    x=y1-(b//a)*x1
    y=x1
    return g,x,y

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
g=gcd(a,b)
print(g)
eg=e_gcd(a,b)
print(eg)
