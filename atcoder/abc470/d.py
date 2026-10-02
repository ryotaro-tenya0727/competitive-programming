import sys

sys.setrecursionlimit(10**7)

from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
from bisect import bisect_left, bisect_right
# import math
# import itertools
# import heapq

# from itertools import groupby
# import math
# from atcoder.dsu import DSU
# from functools import cache
# from sortedcontainers import SortedSet, SortedList, SortedDict
# from atcoder.segtree import SegTree

# from atcoder.fenwicktree import FenwickTree
# import copy
from heapq import heappush, heappop, heappush, heapify

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
P = [v - 1 for v in ilist()]

RP = [0 for i in range(N)]

orderp = defaultdict(int)

for i in range(N):
    orderp[P[i]] = i

for i in range(N):
    RP[i] = orderp[i]
isp = False
for i in range(Q):
    n = ilist()

    if n[0] == 1:
        x = n[1]
        y = n[2]
        x -= 1
        y -= 1
        if not isp:
            P[x], P[y] = P[y], P[x]
            RP[P[x]], RP[P[y]] = RP[P[y]], RP[P[x]]
        else:
            RP[x], RP[y] = RP[y], RP[x]
            P[RP[x]], P[RP[y]] = P[RP[y]], P[RP[x]]

    else:
        isp = not isp

if isp:
    print(*[v + 1 for v in RP])
else:
    print(*[v + 1 for v in P])
