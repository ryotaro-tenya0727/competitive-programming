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


H, W, N, Q = imap()
R = []
C = []

for i in range(N):
    r, c = imap()
    R.append(r)
    C.append(c)
R.sort()
C.sort()

for i in range(Q):
    n = ilist()

    if n[0] == 1:
        u = n[1]
        d = n[2]

        ut = bisect_left(R, u)
        dt = bisect_right(R, d)
        print(dt - ut)
    else:
        l = n[1]
        r = n[2]
        lt = bisect_left(C, l)
        rt = bisect_right(C, r)
        print(rt - lt)
