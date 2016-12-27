# python2
import sys

"""
$echo '3 10 23 9 11 7 100' | python fractional_knapsack.py
"""


# item = (values, weights)
def get_optimal_value(capacity, items):
    value = 0.
    cap = capacity
    _items = sorted(items, key=lambda el: float(el[0]) / el[1], reverse=True)
    for i in _items:
        _v = i[0]
        _w = i[1]
        if not cap: return value
        W_sel = min(_w, cap)
        value += W_sel * float(_v) / _w
        cap -= W_sel
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    items = zip(data[2:(2 * n + 2):2], data[3:(2 * n + 2):2])  # (values, weights)
    opt_value = get_optimal_value(capacity, items)
    print("{:.10f}".format(opt_value))
