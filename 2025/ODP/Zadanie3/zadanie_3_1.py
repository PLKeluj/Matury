plik = open('dron.txt')

ruchy = []
for i in plik:
    i = i.strip()
    ruchy.append(i.split(' '))


def nwd(a, b):
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a%b

    return a


wynik = 0
for i in ruchy:
    a = abs(int(i[0]))
    b = abs(int(i[1]))
    if nwd(a, b) > 1:
        wynik += 1

print(wynik)
