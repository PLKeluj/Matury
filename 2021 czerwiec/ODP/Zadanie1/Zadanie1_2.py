n = 23

dl = 0
while n > 0:
    liczba = 1
    while liczba**2 <= n:
        liczba +=1
    dl += 1
    n -= (liczba-1)**2

print(dl)