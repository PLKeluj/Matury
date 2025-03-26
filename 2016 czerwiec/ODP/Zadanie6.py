def plik1():
    plik = open("liczby.txt")
    wynik = []
    for linia in plik:
        wynik.append(list(linia.strip()))
    return wynik


plik1 = plik1()

def plik2():
    plik = open("liczby.txt")
    wynik = []
    for linia in plik:
        wynik.append(int(linia.strip()))
    return wynik


def zadanie1():
    wynik = 0
    for liczba in plik1:
        if liczba[len(liczba) - 1] == '8':
            wynik += 1
    return wynik


def zadanie2():
    liczby = 0
    wynik = 0
    for liczba in plik1:
        if liczba[len(liczba) - 1] == '4':
            wynik += 1
            for i in range(len(liczba) - 1):
                if liczba[i] == '0':
                    liczby += 1
                    break
    return (wynik - liczby)


def zadanie3():
    wynik = 0
    for liczba in plik1:
        if liczba[len(liczba) - 1] == '2':
            if (liczba[len(liczba)-2]) == '0':
                wynik += 1
    return wynik


def BinDoDzie(liczba):
    wynik = 0
    for i in range(0, len(liczba)-2):
        if int(liczba[i]) == 1:
            wynik += (pow(2,len(liczba)-(2+i)))
    return wynik

print(zadanie3())
