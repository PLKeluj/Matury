liczba_d = 123
liczba_s = 123


def dec_to_sep(liczba):
    wynik = ''
    i = 0
    while liczba > 0:
        cyfra = (liczba % 7)
        wynik = str(cyfra) + wynik

        i += 1
        liczba //= 7

    return wynik


print(dec_to_sep(liczba_d))


def sep_to_dec(liczba):
    wynik = 0
    i = 0
    while liczba > 0:
        cyfra = (liczba % 10) * (7 ** i)
        wynik += cyfra

        i += 1
        liczba //= 10

    return wynik


print(sep_to_dec(liczba_s))
