dzialanie_inf = '4*3+2 = '
dzialanie_onp = '7 3 2 + *'
pr = {'(': 3, ')': 3, '^': 2, '*': 1, '/': 1, '+': 0, '-': 0}


def priorytet(x):
    return pr[x]


def inf_to_onp(liczba):
    wynik = ''
    stos = []
    for i in liczba:
        if i == ' ':
            continue
        elif i not in pr:
            wynik += i + ' '
        elif i == '=':
            while len(stos) != 0:
                if stos[-1] != '(':
                    wynik += str(stos[-1] + ' ')
                stos = stos[:-1]
        else:
            if i == '(':
                stos.append(i)
            elif i == ')':
                while len(stos) != 0 and stos[-1] != '(':
                    if stos[-1] != '(':
                        wynik += str(stos[-1] + ' ')
                    stos = stos[:-1]
                stos = stos[:-1]
            else:
                while len(stos) != 0 and stos[-1] != '(':
                    pr_t1 = pr[i]
                    pr_t2 = priorytet(stos[-1])
                    if pr_t1 <= pr_t2:
                        wynik += str(stos[-1] + ' ')
                        stos = stos[:-1]
                    else:
                        break
                stos.append(i)

    return wynik[:-3]


def onp_to_inf(liczba):
    stos = []
    for i in liczba:
        if i == ' ':
            continue
        elif i not in pr:
            stos.append(int(i))
        elif len(stos) >= 2:
            a = stos[-2]
            b = stos[-1]
            stos = stos[:-2]
            stos.append(f'( {a} {i} {b} )')
    wynik = (str(stos))[4:-4]

    return wynik


print(inf_to_onp(dzialanie_inf))
print(onp_to_inf(dzialanie_onp))
