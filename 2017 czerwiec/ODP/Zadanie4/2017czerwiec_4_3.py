def otworz_plik():
    plik = open("punkty.txt", "r")
    wspolrzedne = [[0] * 2 for j in range(len(plik.readlines()))]
    i = 0
    plik = open("punkty.txt", "r")
    for liczba in plik:
        liczba1, liczba2 = liczba.split(' ')
        wspolrzedne[i][0] = int(liczba1.strip())
        wspolrzedne[i][1] = int(liczba2.strip())
        i += 1
    return wspolrzedne

wspolrzedne = otworz_plik()