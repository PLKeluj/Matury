wynik = 1


def f(a, b):
    global wynik
    if b == 0:
        return 0
    k = ostatnia(b)
    w = f(a, skroc(b))
    # wynik += 1
    w = dopisz(w)
    while k > 0:
        w = w + a
        # wynik += 1
        k = k - 1
    return w


def skroc(x):
    return x // 10


def dopisz(x):
    return x * 10


def ostatnia(x):
    return x % 10


print(f(2024, 1234))
# print(wynik)
