def pgcd (a,b):
    low=min(a,b)
    high=max(a,b)


    if low==0:
        return high
    elif low==1:
        return 1
    else:
        return pgcd(low,high%low)

print(pgcd(12,4))