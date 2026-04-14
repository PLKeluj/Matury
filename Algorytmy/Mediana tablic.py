tablica1 = [1, 2]
tablica2 = [3, 4]


def sumaTablic(t1, t2):
    wynik = []
    m = len(t1)
    n = len(t2)
    xm = 0
    xn = 0
    while len(wynik) != m + n:
        if xm < m and xn < n:
            if t1[xm] < t2[xn]:
                wynik.append(t1[xm])
                xm += 1
            else:
                wynik.append(t2[xn])
                xn += 1
        else:
            if xm >= m:
                wynik.append(t2[xn])
                xn += 1
            else:
                wynik.append(t1[xm])
                xm += 1

    return wynik


def medianaTablicy(tablica):
    dlugosc = len(tablica)
    if dlugosc % 2 == 1:
        indeks = (dlugosc // 2)
        return tablica[indeks]
    else:
        mediana = (tablica[int(dlugosc / 2)] + tablica[int(dlugosc / 2)] - 1) / 2
        return mediana


print(medianaTablicy(sumaTablic(tablica1, tablica2)))
