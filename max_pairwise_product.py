# python2
import sys

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]
assert (len(a) == n)

result = 0
# print 'n ', n
# print 'a ', a

i = 0
max1 = 0
max2 = 0
while i < n:
    m = max(max1, max2)
    if a[i] > m:
        # print '#1 a[i] ', a[i], ' max ', max(max1,max2)
        if a[i] > max1 >= max2:
            # print '#1a'
            max2 = max1
            max1 = a[i]
        elif a[i] > max2 > max1:
            # print '#1b'
            max1 = max2
            max2 = a[i]
    elif a[i] == m:
        # print '#2 a[i] ', a[i], ' max ', max(max1,max2)
        if a[i] == max1:
            max2 = a[i]
        else:
            max1 = a[i]
    else:
        # print '#3 a[i] ', a[i], ' max ', max(max1,max2)
        if a[i] > max1:
            max1 = a[i]
        elif a[i] > max2:
            max2 = a[i]
        else:
            pass
    i += 1
result = max1 * max2

# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]

print(result)
