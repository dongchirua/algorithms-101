# python2
import sys


def get_change(m, denominations=[1, 5, 10]):
    result = 0
    need = m
    while len(denominations):
        _d = denominations.pop()
        ex = need // _d
        if ex:
            result += ex
            need -= _d * ex
    # write your code here
    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(get_change(n))
