plik = open('liczby.txt', 'r')
liczby = []
for i in plik:
    liczby.append(int(i.strip()))

def czyPierwsza(liczba):
    dzielnik = 2
    while dzielnik < liczba:
        if liczba%dzielnik == 0:
            return False
        dzielnik += 1
    return True

wynik = 0
for i in liczby:
    if czyPierwsza(i-1) == True:
        wynik += 1

print(wynik)