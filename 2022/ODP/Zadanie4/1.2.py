n = 3
A = [1, 2, 1]

def sortowanie():

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                already_sorted = False

        if already_sorted:
            break

    return A

print(sortowanie())
