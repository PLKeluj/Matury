def dec_to_any(liczba, system):
    wynik = ''
    i = 0
    while liczba > 0:
        cyfra = (liczba % system)
        wynik = str(cyfra) + wynik

        i += 1
        liczba //= system

    return wynik


liczba_d = 123
system_liczbowy = 10
print(dec_to_any(liczba_d, system_liczbowy))