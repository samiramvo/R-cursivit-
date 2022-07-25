def fibonnaci(n):
    if n==1 or n==2:
        return 1
    else:
        return(fibonnaci(n-1)+fibonnaci(n-2))

print(fibonnaci(10))