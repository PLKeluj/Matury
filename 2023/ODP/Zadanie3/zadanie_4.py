def plik():
    plik = open('odbiorcy_przyklad.txt')
    linie = plik.readlines()

    komputery = {}
    nr = 1
    for i in linie:
        komputery[nr] = i.strip()
        nr += 1

    return komputery


def zadanie2():
    wynik = 0
    komputery = plik()
    odbiorcy = {}

    for komputer in komputery:
        odbiorca = komputery.get(komputer)
        if odbiorca not in odbiorcy:
            odbiorcy[odbiorca] = 1
        else:
            odbiorcy[odbiorca] += 1

    i = 1
    for x in range(len(komputery)):
        if odbiorcy.get(str(i)) == None:
            wynik += 1
        i += 1

    return wynik

def zadanie3():
    wynik = 0
    komputery = plik()

    for komputer in komputery:
        odbiorca = komputery.get(komputer)
        komputery[odbiorca] = komputer