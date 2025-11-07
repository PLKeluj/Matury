plik = open('liczby.txt', 'r')
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

wynik = []
for liczba in liczby_c:
    x = liczba
    for i in range(len(liczby_p)):
        if x % liczby_p[i] == 0:
            x /= liczby_p[i]
        elif x == 1:
            continue
    if x == 1:
        wynik.append(liczba)

print(wynik)
