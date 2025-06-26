k = 120050


def ciecie(x):
    dlugosc = 0
    i = x
    while i > 0:
        dlugosc += 1
        i = i // 10
    polowa = dlugosc / 2

    a = int(x // (10 ** polowa))
    b = int(x % (10 ** polowa))

    return a, b


print(ciecie(k))
