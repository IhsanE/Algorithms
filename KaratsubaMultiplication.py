import math
def Karatsuba(x,y):
    n=len(str(x))
    m=len(str(y))
    if (n==1 or m==1):
        return x*y
    else:
        a=int(str(x)[:round(n/2)])
        b=int(str(x)[round(n/2):])
        c=int(str(y)[:round(m/2)])
        d=int(str(y)[round(m/2):])
        return int((10**n)*Karatsuba(a,c)+(10**(n/2))*(Karatsuba(a,d)+Karatsuba(b,c))+Karatsuba(b,d))
print(Karatsuba(1234,5678))
