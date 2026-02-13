plik = open('dane3.txt')
pary = []

for i in plik:
    pary.append((i.strip()).split())

print(pary)


min1 = 1000000
min2 = 1000000
for i in pary:
    dlugosc = int(i[1]) - int(i[0]) + 1
    if dlugosc < min1:
        min1, min2 = dlugosc, min1
    elif dlugosc < min2:
        min2 = dlugosc

print(min1, min2)



