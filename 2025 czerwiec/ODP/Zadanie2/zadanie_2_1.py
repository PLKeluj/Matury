k = 120050

def ciecie(x):

    dlugosc = 0
    while x > 0:
        dlugosc += 1
        x = x // 10
    polowa = dlugosc / 2

    a = int(k // (10**polowa))
    b = int(k % (10 ** polowa))

    return a,b

print(ciecie(k))