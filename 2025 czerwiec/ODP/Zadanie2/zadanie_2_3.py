plik = open('liczby2.txt', 'r')
liczby = []
for i in plik:
    liczby.append(int(i.strip()))


def ciecie(x, i):

    a = int(x // (10 ** i))
    b = int(x % (10 ** i))

    return a, b


wynik_max = 0
liczba_max = 0
for liczba in liczby:
    wynik = 0
    kwadrat = liczba**2
    dlugosc = len(str(kwadrat))
    for i in range(1, dlugosc+1):
        a = (ciecie(kwadrat, i))[0]
        b = (ciecie(kwadrat, i))[1]
        suma = a + b
        if suma <= liczba:
            wynik += 1
    if wynik > wynik_max:
        wynik_max = wynik
        liczba_max = liczba

print(wynik_max, liczba_max)
