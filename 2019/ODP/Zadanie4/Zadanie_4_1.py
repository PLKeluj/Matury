plik = open("liczby.txt")

liczby = []
for i in plik:
    liczby.append(int(i.strip()))
plik.close()

potegi3 = []
i = 3
while i < 100000:
    potegi3.append(i)
    i *= 3


def czyPotega(liczba, potegi):
    l = 0
    p = len(potegi) - 1

    while l <= p:
        s = (l + p) // 2
        if potegi[s] == liczba:
            return True
        if potegi[s] < liczba:
            l = s + 1
        elif potegi[s] > liczba:
            p = s - 1

    return False


wynik = 0
for i in liczby:
    if czyPotega(i, potegi3) == True:
        wynik += 1

print(wynik)
