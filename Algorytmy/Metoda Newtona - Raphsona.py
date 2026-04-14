x = 3


def pierwiastek(liczba):
    e = 0.0001
    a = 1
    b = liczba
    P = a * b

    while abs(a - b) >= e:
        a = (a + b) / 2
        b = P / a

    return a


print(pierwiastek(x))
