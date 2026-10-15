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


N, M = imap()
xst = [set() for i in range(N)]
yst = [set() for i in range(N)]

for i in range(M):
    r, c = imap()
    r -= 1
    c -= 1

    for yv in xst[r]:
        if r in yst[yv]:
            yst[yv].remove(r)
    xst[r].clear()
    for xv in yst[c]:
        if c in xst[xv]:
            xst[xv].remove(c)
    yst[c].clear()
    xst[r].add(c)
    yst[c].add(r)
ans = 0
for k in xst:
    ans += len(k)

print(ans)
