# python2
import sys


def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        # print 'left, right ', left, right
        # print 'a[left], a[right] ', a[left], a[right]
        # print 'x, mid ', x, a[mid]
        if (x > a[mid]):
            left = mid + 1
        elif (x < a[mid]):
            right = mid - 1
        else:
            return mid
    return -1

    # write your code here


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    result = []
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        result.append(binary_search(a, x))
    print ' '.join([str(i) for i in result])
