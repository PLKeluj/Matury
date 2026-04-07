def f(x):
    return x ** 3 - 3 * (x ** 2) + 2 * x - 6


def metodaPolawiania(l, p):
    e = 0.001
    if f(l) * f(p) <= 0:
        while p - l > e:
            s = (l + p) / 2

            if f(s) == 0:
                return s
            elif f(l) * f(s) < 0:
                p = s
            else:
                l = s

    return s


print(metodaPolawiania(-10, 10))
