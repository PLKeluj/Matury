plik = open('dron.txt', 'r')
ruchy = []

for i in plik:
    ruchy.append((i.strip()).split(' '))

def NWD(a, b):
    if b == 0:
        return a
    else:
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a


wynik = 0

for ruch in ruchy:
    wysokosc = int(ruch[1])
    if int(ruch[1]) <= 0 :
        wysokosc = -int(ruch[1])
    nwd = NWD(int(ruch[0]), wysokosc)
    if nwd > 1:
        wynik += 1

print(wynik)