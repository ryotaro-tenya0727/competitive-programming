import sys

sys.setrecursionlimit(10**7)

from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
import bisect
# import math
# import itertools
# import heapq

# from itertools import groupby
# import math
# from atcoder.dsu import DSU
# from functools import cache
# from sortedcontainers import SortedSet, SortedList, SortedDict
from atcoder.segtree import SegTree

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


N = int(input())
G = [[] for _ in range(N)]
edges = []

for _ in range(N - 1):
    a, b = imap()
    a -= 1
    b -= 1

    edges.append((a, b))
    G[a].append(b)
    G[b].append(a)

tin = [0] * N
tout = [0] * N
tour = []


def dfs(v, parent):
    tin[v] = len(tour)
    tour.append(v)

    for to in G[v]:
        if to == parent:
            continue
        dfs(to, v)

    tout[v] = len(tour)


dfs(0, -1)

# tour 上の区間加算を記録する差分配列
diff = [0] * (N + 1)


def add(left, right, value):
    # tour[left:right] の全頂点に value を加える
    diff[left] += value
    diff[right] -= value


for i, (a, b) in enumerate(edges, start=1):
    # 辺の両端のうち、どちらが子かを決める
    child = a if tin[a] > tin[b] else b

    left = tin[child]
    right = tout[child]

    child_count = right - left
    other_count = N - child_count

    if child_count > other_count:
        # 子の部分木側が多い
        add(left, right, i)
    else:
        # 子の部分木以外が多い
        add(0, left, i)
        add(right, N, i)

# 累積和で tour 上の各位置の値を求める
# ans は元の頂点番号順に戻す
ans = [0] * N
current = 0

for pos, v in enumerate(tour):
    current += diff[pos]
    ans[v] = current

print(*ans)
