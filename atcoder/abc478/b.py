import sys

sys.setrecursionlimit(10**7)

# from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
import bisect
# import math
import itertools
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


N, V = imap()
W = ilist()
W = [(i + 1, W[i]) for i in range(N)]

patterns = itertools.combinations(W, 3)

ans = 0
for v in patterns:

    t = 0
    w = 0
    for f in v:
        t += f[0]
        w += f[1]
    if t <= V:
        ans = max(w, ans)

print(ans)
