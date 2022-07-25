def series(numb):
    if numb<1:
        return 0
    else:
        return numb+series(numb-2)

print(series(12))