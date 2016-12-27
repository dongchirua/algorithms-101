# python2
import sys

"""
$echo '5 2 3 9 2 2' | python majority_element.py
"""

def get_majority(a):
    n = len(a)
    k = n // 2
    if n == 1: return [(a[0], 1)]
    right = get_majority(a[0:k])
    left = get_majority(a[k:n])

    # print 'a ', a
    # print 'right ', right
    # print 'left ', left

    merge = []
    i, j = 0, 0
    imax = len(left)
    jmax = len(right)
    while i < imax and j < jmax:
        if left[i][0] < right[j][0]:
            merge.append(left[i])
            i += 1
        elif left[i][0] > right[j][0]:
            merge.append(right[j])
            j += 1
        else:
            merge.append((left[i][0], left[i][1] + right[j][1]))
            i += 1
            j += 1
    while i < imax:
        merge.append(left[i])
        i += 1
    while j < jmax:
        merge.append(right[j])
        j += 1

    return merge


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:n + 1]
    r = get_majority(a)
    f = False
    for i in r:
        if i[1] > (n // 2):
            f = True
    if f:
        print 1
    else:
        print 0
