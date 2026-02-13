plik = open('odbiorcy.txt')
plikw = open('wynik_4_4.txt', 'w')

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


for i in range(8):
    p = wyslanie(pakiety[i])
    pakiety.append(p)

def maxPakietow(index):
    komputery = {}
    temp = pakiety[index]
    for i in range(len(temp)):
        if temp[i] not in komputery:
            komputery[temp[i]] = 1
        else:
            komputery[temp[i]] += 1

    max = 0
    for key, item in komputery.items():
        if item > max:
            max = item

    return max

plikw.write(f'{maxPakietow(1)} {maxPakietow(2)} {maxPakietow(4)} {maxPakietow(8)}')