nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]


def reszta2(kwota):
    i = 0
    wynik = 0
    while kwota > 0:
        while kwota >= nominaly[i]:
            wynik += 1
            kwota = kwota - nominaly[i]
        i += 1

    return wynik
