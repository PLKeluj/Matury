def plik():
    plik = open("przyklad.txt")
    liczby = []
    for linia in plik:
        liczba = linia.strip()
        liczby.append(int(liczba))
    plik.close()

    return liczby


liczby = plik()


def zadanie1():
    wynik = 0
    for liczba in liczby:
        while liczba > 1:
            liczba = liczba / 3
        if liczba == 1:
            wynik += 1

    return wynik


def silnia(liczba):
    wynik = 1
    while liczba > 0:
        wynik *= liczba
        liczba -= 1

    return wynik


def zadanie2():
    wynik = []
    for liczba in liczby:
        cyfry = []
        suma = 0
        for cyfra in str(liczba):
            cyfry.append(int(cyfra))
        for i in range(len(cyfry)):
            suma += silnia(cyfry[i])
        if suma == liczba:
            wynik.append(liczba)

    return wynik


def nwd(n, k):
    x = 0
    while k != 0:
        x = n % k
        n, k = k, x
    return n


def zadanie3():
    wynik_liczba = 0
    wynik_dlugosc = 0
    wynik_NWD = 0


    for x in range(len(liczby) - 2):
        i = 0 + x
        liczba = liczby[i]
        dlugosc = 1
        NWD = 0
        NWD1 = 0

        while NWD == NWD1 and NWD != 1:
            NWD = nwd(nwd(liczby[i], liczby[i + 1]), liczby[i + 2])
            NWD1 = nwd(liczby[i + 1], liczby[i + 2])

            dlugosc += 1
            i += 1

        if dlugosc > wynik_dlugosc:
            wynik_dlugosc = dlugosc
            wynik_liczba = liczba
            wynik_NWD = nwd(nwd(liczby[i-1], liczby[i]), liczby[i + 1])


    return wynik_liczba, wynik_dlugosc, wynik_NWD

print(zadanie3())