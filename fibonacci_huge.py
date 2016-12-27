# python2
import sys

"""
Using matrix linear combination method
if modulo=False, just compute fibonacci
$echo '1000 3' | python fibonacci_huge.py
"""

def multipleMatrixes(A, B, modulo=False, m=None):
    B = list(zip(*B))
    if not modulo:
        return [[sum(ai * bj for ai, bj in zip(Ai, Bj)) for Bj in B]
                for Ai in A]
    else:
        return [[sum((ai % m * bj % m) % m for ai, bj in zip(Ai, Bj)) % m for Bj in B]
                for Ai in A]


def generateIdentityMatrix(size):
    r = list(range(size))
    return [[1 if i == j else 0 for i in r] for j in r]


def computeMatrixPower(A, n, eyeA, modulo=False, m=None):
    if n == 0:
        return eyeA
    elif n == 1:
        return A
    else:
        Ak = computeMatrixPower(A, n // 2, eyeA, modulo, m)
        if n % 2:
            tmp = multipleMatrixes(Ak, Ak, modulo, m)
            An = multipleMatrixes(A, tmp, modulo, m)
        else:
            An = multipleMatrixes(Ak, Ak, modulo, m)
    return An


def fib(n, m, modulo=False):
    A = [[1, 1], [1, 0]]
    eyeA = generateIdentityMatrix(len(A))
    coordinates = [[1], [0]]
    An = computeMatrixPower(A, n - 1, eyeA, modulo, m)
    Lu = multipleMatrixes(An, coordinates, modulo, m)
    if modulo:
        return Lu[0][0] % m
    else:
        return Lu[0][0]


if __name__ == '__main__':
    n = [int(x) for x in sys.stdin.readline().split()]
    print(fib(n[0], n[1], True))
