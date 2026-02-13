plik = open('dane2_4.txt')

klamry = []
for i in plik:
    klamry.append(i.strip())

print(klamry)

wynik = []
for wyraz in klamry:
    flaga = 0
    licznik = 0
    for i in wyraz:
        if i == '[':
            licznik += 1
        else:
            licznik -= 1

        if licznik < 0:
            flaga = 1
            wynik.append('nie')
    if flaga == 0:
        wynik.append('tak')

print(wynik)