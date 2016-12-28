# python2
import sys

"""
$echo '20 4 5 7 12 18' | python knapsack.py
"""


def optimal_weight(W, items):
    n = len(items)
    value = [[0] * (n + 1) for _ in range(W + 1)]
    for j in range(1, n + 1):
        for i in range(1, W + 1):
            value[i][j] = value[i][j - 1]  # case 1
            if items[j - 1] <= i:
                val = value[i - items[j - 1]][j - 1] + items[j - 1]  # case 2
                value[i][j] = max(value[i][j], val)
    return value[W][-1]


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    W, nBar = data[0:2]
    items = data[2:3 + nBar]
    print optimal_weight(W, items)
    # print optimal_weight(10, [1, 4, 8])
    # print optimal_weight(20, [5, 7, 12, 18])
