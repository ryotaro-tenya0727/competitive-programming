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

parent = [-1] * N
parent_edge = [0] * N  # parent_edge[v]: vと親を結ぶ辺の番号
parent[0] = 0

order = []
q = deque([0])

while q:
    v = q.popleft()
    order.append(v)

    for to, i in graph[v]:
        if to == parent[v]:
            continue
        parent[to] = v
        parent_edge[to] = i
        q.append(to)

size = [1] * N
add = [0] * N

# 子から親へ。人数を数えながら、その辺の加算も記録する
for v in reversed(order[1:]):
    below = size[v]
    above = N - below
    i = parent_edge[v]

    if below > above:
        add[v] += i
    else:
        add[0] += i
        add[v] -= i

    size[parent[v]] += size[v]

# 親から子へ。記録を反映する
for v in order[1:]:
    add[v] += add[parent[v]]

print(*add)
