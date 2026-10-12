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
graph = [[] for _ in range(N)]

for i in range(1, N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, i))
    graph[b].append((a, i))

# 1組の意味：(頂点, 親, 親との辺番号)
q = deque([(0, -1, 0)])
order = []

while q:
    v, parent, edge_id = q.popleft()
    order.append((v, parent, edge_id))

    for to, i in graph[v]:
        if to != parent:
            q.append((to, v, i))

size = [1] * N
add = [0] * N

# 子から親へ
for v, parent, edge_id in reversed(order[1:]):
    below = size[v]
    above = N - below

    if below > above:
        add[v] += edge_id
    else:
        add[0] += edge_id
        add[v] -= edge_id

    size[parent] += below

# 親から子へ
for v, parent, edge_id in order[1:]:
    add[v] += add[parent]

print(*add)
