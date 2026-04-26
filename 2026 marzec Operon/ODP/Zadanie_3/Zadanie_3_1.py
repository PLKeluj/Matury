plik = open('pociagi.txt')
wagony = []

for i in plik:
    a, b = (i.strip()).split(' ')
    wagony.append([int(a), int(b)])


def czy_pierwsza(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


wagony_pierwsze = 0
wagony_41 = 0

for i in wagony:
    if czy_pierwsza(i[1]):
        wagony_pierwsze += 1
    if i[1] == 41:
        wagony_41 += 1

print(wagony_pierwsze)
print(wagony_41)