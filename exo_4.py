def factorielle(n):
    fact=1
    for i in range(1,n):
        fact*=i
    return fact

print(factorielle(5))