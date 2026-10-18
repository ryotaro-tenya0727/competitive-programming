# ライブラリ
# https://github.com/ryotaro-tenya0727/competitive-programming

import sys

sys.setrecursionlimit(10**7)

from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
from bisect import bisect_left, bisect_right
# import math
# import itertools
# import heapq

# from itertools import groupby, permutations
# import math
# from atcoder.dsu import DSU
# from functools import cache
# from sortedcontainers import SortedSet, SortedList, SortedDict
# from atcoder.segtree import SegTree

# from atcoder.fenwicktree import FenwickTree
from copy import copy, deepcopy
# from heapq import heappush, heappop, heappush, heapify

dr = [
    (0, -1),
    (-1, 0),
    (0, 1),
    (1, 0),
]


def input():
    return sys.stdin.readline().strip()


def imap():
    return map(int, input().split())


def ilist():
    return list(map(int, input().split()))


N, Q = imap()
A = ilist()
sa = [0]

for a in A:
    sa.append(sa[-1] + a)
p = [i for i in range(1, N + 1)]
num_ar = [0]
for pv in p:
    num_ar.append(num_ar[-1] + pv)

sum_ar = [0]

for i in range(1, N + 1):
    sum_ar.append(sum_ar[-1] + sa[i])

for i in range(Q):
    l, r = imap()
    l -= 1

    r_t = bisect_right(num_ar, r)
    another_r_sum = r - num_ar[r_t - 1]
    r_sum = sum_ar[r_t - 1] + sa[another_r_sum]

    l_t = bisect_right(num_ar, l)
    another_l_sum = l - num_ar[l_t - 1]
    l_sum = sum_ar[l_t - 1] + sa[another_l_sum]

    print(r_sum - l_sum)
