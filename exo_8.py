def harmo(numb):
    if numb<2:
        return 1
    else:
        return 1/numb +(harmo(numb-1))
    
print(harmo(7))
    