# python2
import sys


def calc_fib(n):
    if n < 0: return 0
    if n <= 1: return n
    a, b = 0, 1
    n -= 2
    while n >= 0:
        a, b = b, a + b
        n -= 1
    return b


n = int(sys.stdin.readline())
print(calc_fib(n))
