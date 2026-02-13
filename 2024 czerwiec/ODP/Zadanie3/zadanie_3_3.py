plik = open('slowa.txt')
plikw = open('wynik_3_3.txt', 'w')
slowa = []
for i in plik:
    slowa.append(i.strip())

wynik = []
for i in slowa:
    flaga =1
    dl = len(i)
    if dl % 2 == 1:
        dl = dl // 2 + 1
    else:
        dl = dl // 2
    litery = {}
    for x in i:
        if x not in litery:
            litery[x] = 1
        else:
            litery[x] += 1

    for key, item in litery.items():
        if item >= dl and flaga == 1:
            wynik.append(i)
            flaga = 0

for i in wynik:
    plikw.write(f'{i}\n')
    print(i)
