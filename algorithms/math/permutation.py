def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def perm(A, R, q = 0) :
    if len(R) == q :
        print(R)
        return

    for i in range(q, len(A)):
        swap(A, i, q)
        R[q] = A[q]
        perm(A, R, q+1)
        swap(A, i, q)

A = [1, 2, 3]
R = [0] * 3
perm(A, R)