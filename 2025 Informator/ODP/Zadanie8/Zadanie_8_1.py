plik = open('dane8.txt', 'r')

liczby = []
for i in plik:
    liczby.append(int(i.strip()))

p = 0
np = 0

for i in range(len(liczby) - 1):
    l = liczby[i] - liczby[i + 1]
    if l < 0:
        l = -l

    if l % 2 == 0:
        p += 1

    else:
        np += 1

print(p, np)
