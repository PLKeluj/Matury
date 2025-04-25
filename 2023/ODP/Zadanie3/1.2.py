n = 3
A = [1, 2, 1]
B = []

for i in range(n):
    B[i] = 0
    k = 0
for i in A:
    if A[i] <= n:
        A[B[i]] = B[A[i]] + 1
    else:
        k += 1
for i in A:
    if B[i] > 1:
        k += 1 + B[i]

print(k)



