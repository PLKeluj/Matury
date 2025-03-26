def otworzPlik():
    plik = open('przyklad.txt')
    linie = plik.readlines()

    for i in range(len(linie)):
        linie[i] = int(linie[i].rstrip())

    return linie


def odwrocLiczbe(liczba):
    wynik = 0
    i = 0
    liczba1 = liczba

    while liczba1 > 0:
        i += 1
        liczba1 = liczba1 // 10

    wsp = i

    while liczba > 0:
        wynik += (10 ** -i) * (liczba % 10)
        liczba = liczba // 10
        i += 1

    return wynik * (10 ** (wsp +1))


def odwroconeLiczby(liczby):
    wynik = []
    i = 0
    for x in liczby:
        wynik.append(int(odwrocLiczbe(liczby[i])))
        i += 1

    return wynik

def zadanie1():
    wynik = []
    i = 0
    liczby = odwroconeLiczby(otworzPlik())
    for x in liczby:
        liczba = int(liczby[i])
        if liczba % 17 == 0:
            wynik.append(liczba)
        i += 1

    return wynik

print(odwrocLiczbe(131))