w = 4
k = 4
n = 179

def liczbaBin(n):
    wynik = []

    while n > 0:
        bin = n % 2
        n = n // 2
        wynik.append(bin)

    wynik = wynik[::-1]
    return wynik


def ostatniaLiczba():
    liczba = liczbaBin(n)
    wielTab = w * k
    wielLicz = len(liczba)

    while wielTab > wielLicz:
        wielTab -= wielLicz

    wynik = liczba[(wielTab - 1)]
    return wynik


print('x = ' + str(ostatniaLiczba()))
