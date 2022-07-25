def geometric(numb):
    if numb<0:
        return 0
    else:
        return 1/ (pow(2,numb)) +geometric(numb-1)
    
print(geometric(7))
    