# python2
import sys


def lcm(a, b):
    gcd, tmp = a, b
    while tmp:
        gcd, tmp = tmp, gcd % tmp
    return a * (b / gcd)


if __name__ == '__main__':
    a = [int(x) for x in sys.stdin.readline().split()]
    print(lcm(a[0], a[1]))
