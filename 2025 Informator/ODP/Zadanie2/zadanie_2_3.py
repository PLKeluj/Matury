plik = open('dane2_3.txt')

klamry = []
for i in plik:
    klamry.append(i.strip())

print(klamry)

wynik = []
for wyraz in klamry:
    max = 0
    licznik = 0
    for i in wyraz:
        if i == '[':
            licznik += 1
        else:
            if licznik > max:
                max = licznik
            licznik -= 1

    wynik.append(max)

print(wynik)
