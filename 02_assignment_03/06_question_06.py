def gcd(a,b): 
    if a==0 : 
        return b 
    return gcd(b%a,a)

a = 10 
b = 15 
gcd(a,b)
print('GCD of ',a," and ",b," is : ",gcd(a,b))