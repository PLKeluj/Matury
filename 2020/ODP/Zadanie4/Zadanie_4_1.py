plik = open('2020 kwiecien/ODP/Zadanie4/dane4.txt', 'r')
liczby = []

for i in plik:
    liczby.append(int(i.strip()))
    
max = 0
min = 1000
for i in range(len(liczby)-1):
    luka = abs(liczby[i] - liczby[i+1])
    
    if luka > max:
        max = luka
    if luka < min:
        min = luka
        
print(min, max)