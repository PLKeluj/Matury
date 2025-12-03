plik = open('dane3.txt')
pary = []

for i in plik:
    pary.append((i.strip()).split())

print(pary)

dlugosci = {}
for i in pary:
    dlugosc = int(i[1]) - int(i[0]) + 1
    if dlugosc not in dlugosci:
        dlugosci[dlugosc] = 1
    else:
        dlugosci[dlugosc] += 1

max = 0
wynik = 0
for klucz, wartosc in dlugosci.items():
    if wartosc > max:
        max = wartosc
        wynik = int(klucz)
    elif wartosc == max:
        if int(klucz) > wynik:
            max = wartosc
            wynik = int(klucz)

print(wynik)
