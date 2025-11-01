def dlugoscOpisu(n, ciag):
    d = 1
    for i in range(n-1):
        if ciag[i + 1] != ciag[i]:
            d +=1
        
    return d*2