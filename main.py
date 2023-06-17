import random

def coPrime(x, y):
    r = True
    i = 1

    while i != 0:
        i += 1
        if x%i == 0 and y%i== 0:
            r = False
            break
        if i >= x or i >= y:
            break
    return r

def primeNumb(x, y):
    ra = []
    def primeCheck(a):
        r = True
        for i in range(2, int((a/2)+1)):
            if a%i == 0:
                r = False
        return r
    
    for k in range(x, y+1):
        if primeCheck(k) == True and k != 1:
            ra.append(k)
    
    return ra

def phi(n):
    primeSmallerThann = primeNumb(1, n)
    primeFactorsn = []
    val = 1

    for i in range(0, len(primeSmallerThann)):
        if n%primeSmallerThann[i] == 0:
            primeFactorsn.append(primeSmallerThann[i])
    
    for i in range(0, len(primeFactorsn)):
        val *= primeFactorsn[i]-1
    
    return val

def main(data):
    q = 0
    p = 0

    while p == q:
        p = primeNumb(data["primeRange"]["lower"], data["primeRange"]["upper"])[random.randint(0, len(primeNumb(data["primeRange"]["lower"], data["primeRange"]["upper"]))-1)]

        q = primeNumb(data["primeRange"]["lower"], data["primeRange"]["upper"])[random.randint(0, len(primeNumb(data["primeRange"]["lower"], data["primeRange"]["upper"]))-1)]
    
    n = p*q

    e = 0
    phin = phi(n)

    for i in range(2, phin):
        if coPrime(phin, i) == True:
            e = i
            break
    
    k = 1

    while True:
        if (1+phin*k)%e == 0:
            break
        k += 1
    
    d = (1+phin*k)/e

    cypher = (data["plainText"]**e)+1

    while True:
        if (cypher-(data["plainText"]**e))%n == 0:
            break
        cypher += 1
    
    return {"keys": {"publicKey": [e,n], "privateKey": [d,n]}, "cypherText": cypher}