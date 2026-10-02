import sys

sys.setrecursionlimit(10**7)

# from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
# from bisect import bisect_left, bisect_right
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


N, W = imap()

cols = [[] for _ in range(W)]

for i in range(N):
    x, y = imap()
    x -= 1
    cols[x].append((y, i))

for col in cols:
    col.sort()

INF = 10**18
times = [INF] * N

# 全列に存在する段数
h = min(len(col) for col in cols)

for k in range(h):
    maxt = max(cols[x][k][0] for x in range(W))

    for x in range(W):
        _, i = cols[x][k]
        times[i] = maxt

Q = int(input())

for _ in range(Q):
    t, a = imap()
    a -= 1

    print("Yes" if t < times[a] else "No")
