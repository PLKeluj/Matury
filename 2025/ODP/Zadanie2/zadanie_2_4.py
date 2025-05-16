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


def num_to_znak(num):
    znaki = {0: 'o', 1: '+', 2: '*'}
    wynik = ''
    for i in range(len(num)):
        wynik += znaki[int(num[i])]

    return wynik


def tri_to_dec(liczba):
    wynik = 0
    for i in range(12, 0, -1):
        wynik += int(liczba[12 - i]) * (3 ** (i - 1))

    return wynik


def dec_to_tri(liczba):
    e = liczba // 3
    q = liczba % 3
    if liczba == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return dec_to_tri(e) + str(q)


suma = 0
for wiersz in symbole:
    liczba_tri = znak_to_num(wiersz)
    liczba = tri_to_dec(liczba_tri)
    suma += liczba

suma_tri = dec_to_tri(suma)
suma_znaki = num_to_znak(str(suma_tri))

print(suma, suma_znaki)

