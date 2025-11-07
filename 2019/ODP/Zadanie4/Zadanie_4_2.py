plik = open("liczby.txt")

liczby = []
for i in plik:
    liczby.append(int(i.strip()))
plik.close()

silnie = [1]
for i in range(1, 10):
    silnie.append(silnie[i - 1] * i)


def sumaSilniCyfr(liczba):
    suma = 0
    for i in str(liczba):
        suma += silnie[int(i)]
    if suma == liczba:
        return True
    else:
        return False


wynik = []
for i in liczby:
    if sumaSilniCyfr(i) == True:
        wynik.append(i)

print(wynik)
