def funkcja(x):
    if x == 0:
        wynik = 0
    else:
        wynik = 2 + funkcja(x // 2)

    return wynik


print(funkcja(3))
