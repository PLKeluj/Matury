plik = open('2020 kwiecien/ODP/Zadanie4/dane4.txt', 'r')
liczby = []

for i in plik:
    liczby.append(int(i.strip()))

d_max = 0
p = 0
k = 0
d = 2

for i in range(len(liczby)-2):
    luka1 = abs(liczby[i] - liczby[i+1])
    luka2 = abs(liczby[i+1] - liczby[i+2])
    
    if luka1 == luka2:
        d += 1
    else:
        if d > d_max:
            index_k = i + 1
            d_max = d
            k = liczby[index_k]
            p = liczby[index_k - d + 1]
            
        d = 2
            
print(d_max, p, k)