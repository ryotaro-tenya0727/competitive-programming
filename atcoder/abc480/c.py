# ライブラリ
# https://github.com/ryotaro-tenya0727/competitive-programming

import sys

sys.setrecursionlimit(10**7)

from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
# from bisect import bisect_left, bisect_right
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


N, K, T = imap()
A = ilist()
A.sort()
while A and A[-1] > T:
    A.pop()
A.append(T)

la = len(A)
ans = 0
r = 0
for i in range(la):
    if r < A[i]:
        ans += (A[i] - r + K - 1) // K
    r = A[i] + K

print(ans)
