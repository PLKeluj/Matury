def przestaw2(n):
    wynik = 0
    i = 1
    while n // 10 > 0:
        wynik += n % 10 * (10 ** i)
        wynik += ((n % 100) // 10) * (10 ** (i - 1))
        n = n // 100
        i += 2
    if n // 10 == 0:
        wynik += (n % 10) * (10 ** (i - 1))
    return wynik


print(przestaw2(154005710))
