symbole = []
plik = open('symbole.txt', 'r')

for i in plik:
    symbole.append(i.strip())


def znak_to_num(znak):
    znaki = {'o': 0, '+': 1, '*': 2}
    wynik = ''
    for i in range(len(znak)):
        wynik = str(znaki[znak[-(i + 1)]]) + wynik

    return wynik


def tri_to_dec(liczba):
    wynik = 0
    for i in range(12, 0, -1):
        wynik += int(liczba[12 - i]) * (3 ** (i - 1))

    return wynik


liczba_max = 0
for wiersz in symbole:
    liczba_tri = znak_to_num(wiersz)
    liczba = tri_to_dec(liczba_tri)
    if liczba > liczba_max:
        liczba_max = liczba

print(liczba_max)
