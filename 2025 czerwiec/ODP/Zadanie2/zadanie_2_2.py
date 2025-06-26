plik = open('liczby1txt', 'r')
liczby = []
for i in plik:
    liczby.append(int(i.strip()))


def pol(x):
    pol = len(str(x)) / 2
    a = int(x // (10 ** pol))
    b = int(x % (10 ** pol))

    return a, b


def nwd(a, b):
    i = 0
    while b != 0:
        i = a % b
        a, b = b, i

    return a


wynik = 0
for liczba in liczby:
    a = (pol(liczba))[0]
    b = (pol(liczba))[1]
    x = nwd(a, b)

    if x == 1:
        wynik += 1

print(wynik)
