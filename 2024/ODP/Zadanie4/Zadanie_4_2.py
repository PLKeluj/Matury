plik = open('liczby_.txt', 'r')
liczby = []

for wiersz in plik:
    l = []
    wiersz = wiersz.split(' ')
    for i in wiersz:
        l.append(int(i.strip()))
    liczby.append(l)

liczby_p = liczby[0]
liczby_c = liczby[1]

for i in range(len(liczby_p) - 1):
    for j in range(len(liczby_p) - i - 1):
        if liczby_p[j] < liczby_p[j + 1]:
            liczby_p[j], liczby_p[j + 1] = liczby_p[j + 1], liczby_p[j]

print(liczby_p[101])
