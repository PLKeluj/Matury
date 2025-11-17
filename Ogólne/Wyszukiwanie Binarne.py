liczby = [1, 3, 4, 5, 6, 7, 8, 12, 13, 23, 24, 28, 30]


def wyszukiwanieBinarne(tablica, liczba_poszukiwana):
    l = 0
    p = len(tablica)
    while l <= p:
        s = (l + p) // 2
        if tablica[s] == liczba_poszukiwana:
            return s
        elif tablica[s] > liczba_poszukiwana:
            p = s - 1
        elif tablica[s] < liczba_poszukiwana:
            l = s + 1

    return False

print(wyszukiwanieBinarne(liczby, 5))
