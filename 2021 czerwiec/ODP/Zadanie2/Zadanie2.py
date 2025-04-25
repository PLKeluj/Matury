def modyfikuj1(s, k):
    if s + k < n:
        modyfikuj1(s + k, k)
    i = s + 1
    while i <= n and i <= (s + k):
        tabela[s - 1] = tabela[s - 1] + tabela[i - 1]
        i += 1

    return tabela


n = len(tabela)
tabela = [4, 2, 6, 2, 9, 3, 5, 2, 7, 4, 3, 2, 3]
s = 4
k = 4

print(modyfikuj1(s, k))


def modyfikuj2(s, k):
    if s + k < n:
        modyfikuj2(s+k, k)
    i = s + 1
    while i <= n and i <= (s+k):
        tabela[s-1] = tabela[s-1] + tabela[i-1]
        i += 1

    print(1)

n = 2021
s = 20
k = 35
tabela = []
for i in range(n):
    tabela.append(1)

print(modyfikuj2(s, k))