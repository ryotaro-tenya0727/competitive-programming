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
    lg = len(g[i])
    for j in range(lg):
        if j == 0:
            newg[i].append((g[i][j], 0))
        else:
            newg[i].append((g[i][j], 1))

S -= 1
T -= 1


def dijkstra(graph, start):
    # 初期化
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        dist, u = heapq.heappop(pq)
        if visited[u]:
            continue

        visited[u] = True

        for v, weight in graph[u]:
            if not visited[v]:
                new_distance = distance[u] + weight
                if new_distance < distance[v]:
                    distance[v] = new_distance
                    heapq.heappush(pq, (new_distance, v))

    return distance


t = dijkstra(newg, S)

print(-1 if t[T] == sys.maxsize else t[T])

# dq = deque()
# dq.append((S, 0))

# re = [False for i in range(N)]
# re[S] = True
# ans = 10**15
# print(newg)
# while dq:
#     now, cost = dq.popleft()

#     for v, new_cost in newg[now]:
#         if v == T:
#             ans = min(ans, cost + new_cost)
#             continue
#         if re[v]:
#             continue

#         re[v] = True
#         dq.append((v, cost + new_cost))

# print(-1 if ans == 10**15 else ans)
