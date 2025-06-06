plik = open('liczby.txt', 'r')
liczby = []
for i in plik:
    liczby.append(int(i.strip()))


def czyPierwsza(liczba):
    dzielnik = 2
    while dzielnik < liczba:
        if liczba % dzielnik == 0:
            return False
        dzielnik += 1
    return True


wynik_max = 0
liczba_max = 0
wynik_min = 100
liczba_min = 0
for i in liczby:
    wynik = 0
    for p in range(2, (i // 2)+1):
        q = i - p
        if czyPierwsza(p) and czyPierwsza(q):
            wynik += 1
    if wynik > wynik_max:
        wynik_max = wynik
        liczba_max = i
    elif wynik < wynik_min:
        wynik_min = wynik
        liczba_min = i

print(liczba_max, wynik_max, liczba_min, wynik_min)
