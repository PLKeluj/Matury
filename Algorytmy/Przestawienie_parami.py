x = 12345


def Dlugosc(liczba):
    wynik = 0
    while liczba > 0:
        wynik += 1
        liczba //= 10

    return wynik


def Przestaw(liczba):
    wynik = 0
    while liczba >= 10:
        d = 10 ** (Dlugosc(liczba) - 2)
        l = liczba // d
        p = l // 10
        q = l % 10
        wynik = wynik * 100 + (q * 10 + p)

        liczba = liczba % d
    if liczba > 0:
        wynik = wynik * 10 + liczba

    return wynik


print(Przestaw(x))
