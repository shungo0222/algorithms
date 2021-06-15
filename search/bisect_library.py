# Array bisection algorithm
# https://docs.python.org/3/library/bisect.html

import bisect

a = [1, 2, 3, 3, 5, 7, 7, 10]

i = bisect.bisect_left(a, 3)
print(i)

i = bisect.bisect_right(a, 7)
print(i)

bisect.insort_left(a, 2)
print(a)

bisect.insort_right(a, 6)
print(a)