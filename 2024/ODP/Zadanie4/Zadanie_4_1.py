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
wynik = 0
for i in liczby_p:
    for j in liczby_c:
        if j % i == 0:
            wynik += 1
            break

print(wynik)
