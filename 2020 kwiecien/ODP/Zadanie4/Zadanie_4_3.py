plik = open('2020 kwiecien/ODP/Zadanie4/dane4.txt', 'r')
liczby = []

for i in plik:
    liczby.append(int(i.strip()))

wystepowanie = {}    
for i in range(len(liczby) - 1):
    luka = abs(liczby[i]- liczby[i+1])
    if luka not in wystepowanie:
        wystepowanie[luka] = 1
    else:
        wystepowanie[luka] += 1


krotnosc_max = 0
luki = []        
for luka, krotnosc in wystepowanie.items():
    if krotnosc > krotnosc_max:
        krotnosc_max = krotnosc
        luki = [luka]
    elif krotnosc == krotnosc_max:
        luki.append(luka)
        
print(krotnosc_max, luki)