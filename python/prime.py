import math
def isprime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True

print(isprime(8))