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

# (頂点, 親, 親と結ぶ辺番号)
order = [(0, -1, 0)]

for v, p, _ in order:
    for nv, i in graph[v]:
        if nv != p:
            order.append((nv, v, i))

# 部分木サイズ
size = [1] * N

for v, p, i in reversed(order[1:]):
    size[p] += size[v]

# 加算を記録
ans = [0] * N

for v, p, i in order[1:]:
    if 2 * size[v] > N:
        ans[v] += i
    else:
        ans[0] += i
        ans[v] -= i

# 親から子へ加算を伝える
for v, p, i in order[1:]:
    ans[v] += ans[p]

print(*ans)
