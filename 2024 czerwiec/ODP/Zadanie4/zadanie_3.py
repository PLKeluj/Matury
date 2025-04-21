def plik():
    plik = open('slowa_przyklad.txt')
    linie = plik.readlines()

    for i in range(len(linie)):
        linie[i] = linie[i].rstrip()

    return linie


def zadanie1():
    wynik = 0

    for slowo in plik():
        for i in range(len(slowo) - 2):
            if slowo[i] == 'k' and slowo[i + 2] == 't':
                wynik += 1
            i += 1

    return wynik


def zadanie2():
    wynik = 0

    for slowo in plik():
        for i in range(len(slowo) - 2):
            if slowo[i] == 'k' and slowo[i + 2] == 't':
                wynik += 1
            i += 1

    return wynik


def zadanie3():
    wynik = 0

    for slowo in plik():
        litery = {}
        for i in slowo:
            if i not in litery:
                litery[i] = 1
            else:
                litery[i] += 1

        if litery[max(litery, key=litery.get)] >= len(slowo)/2:
            print(slowo)
            wynik += 1


    return wynik

zadanie3()

print(zadanie3())