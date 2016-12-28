# python2
import sys

"""
$echo "100" | python primitive_calculator.py
"""

def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def optimal_sequence(n):
    # (a, b) : dp, number before
    if n == 1:
        return 0, -1
    sol = (optimal_sequence(n - 1)[0] + 1, n - 1)
    if n % 2 == 0:
        tmp = optimal_sequence(n // 2)
        if sol[0] > tmp[0]:
            sol = (tmp[0] + 1, n // 2)
    if n % 3 == 0:
        tmp = optimal_sequence(n // 3)
        if sol[0] > tmp[0]:
            sol = (tmp[0] + 1, n // 3)
    return sol


def print_sequence(n):
    sequence = []
    while optimal_sequence(n)[1] != -1:
        sequence.append(n)
        n = optimal_sequence(n)[1]
    sequence.append(1)
    sequence.reverse()
    print len(sequence) - 1
    for i in sequence:
        print i,


if __name__ == '__main__':
    n = sys.stdin.read()
    n = int(n)
    for i in range(1, n):
        optimal_sequence(i)
    print_sequence(n)
