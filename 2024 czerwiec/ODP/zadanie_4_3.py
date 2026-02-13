plik = open('odbiorcy.txt')
plikw = open('wynik_4_3.txt', 'w')

odbiorcy = []
pakiet = []
licznik = 0
for i in plik:
    odbiorcy.append(int(i.strip()))
    licznik += 1
    pakiet.append(licznik)

pakiety = []
pakiety.append(pakiet)

# pakiety = [[1, 2, 3, 4, 5, 6]]
# odbiorcy = [4,3,5,3,1,2]
# licznik = 6


def wyslanie(pakiet):
    wynik = [0] * licznik
    for i in range(len(pakiet)):
        wynik[i] = odbiorcy[pakiet[i] - 1]

    return wynik

flaga = 1
for i in range(10):
    p = wyslanie(pakiety[i])
    for x in range(len(p)):
        if p[x] == x + 1 and flaga == 1:
            plikw.write(f'{i + 1} {x + 1}')
            flaga = 0

    pakiety.append(p)

