def plik():
    plik = open('DaneOP/bit18przyklad')
    linie = plik.readlines()

    ciezarowki = []
    for i in linie:
        ciezarowki.append(list((i.strip()).split(' ')))

    return ciezarowki


def zadanie1():
    wynik = 0
    ciezarowki = plik()
    for i in range(len(ciezarowki) - 1):
        if (ciezarowki[i + 1][1] > ciezarowki[i][1]) is False:
            wynik += 1

    return wynik


def zadanie2():
    wynik = 0
    ciezarowki = plik()
    for i in range(len(ciezarowki) - 1):
        if ciezarowki[i + 1][1] > ciezarowki[i][1]:
            wynik += 1

    return wynik


def zadanie3():
    wynikMax = 0
    ciezarowki = plik()
    for i in range(len(ciezarowki) - 1):
        wynik = 0
        if ciezarowki[i + 1][1] > ciezarowki[i][1]:
            wynik = int(ciezarowki[i + 1][1]) - int(ciezarowki[i][1])
        if wynik >= wynikMax:
            wynikMax = wynik

    return wynikMax 

print(zadanie3())