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
from sortedcontainers import SortedSet, SortedList, SortedDict
# from atcoder.segtree import SegTree

# from atcoder.fenwicktree import FenwickTree
# from copy import copy, deepcopy
import heapq

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


N, M, S, T = imap()
g = [SortedList() for i in range(N)]

for i in range(M):
    a, b = imap()
    a -= 1
    b -= 1

    g[a].add(b)

newg = [[] for i in range(N)]

for i in range(N):
    if not g[i]:
        continue

    min_to = min(g[i])

    for v in g[i]:
        if v == min_to:
            newg[i].append((v, 0))
        else:
            newg[i].append((v, 1))

S -= 1
T -= 1
dq = deque([(S, 0)])
dist = [10**15 for i in range(N)]
while dq:
    now, cost = dq.popleft()

    for v, v_cost in newg[now]:
        newcost = cost + v_cost
        if newcost >= dist[v]:
            continue
        dist[v] = newcost
        if v_cost == 0:
            dq.appendleft((v, newcost))
        else:
            dq.append((v, newcost))

print(dist[T] if dist[T] != 10**15 else -1)
