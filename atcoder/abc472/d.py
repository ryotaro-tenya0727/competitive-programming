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


H, W, K = imap()
S = [list(input()) for i in range(H)]

row_ng = [False] * H
col_ng = [False] * W

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            row_ng[i] = True
            col_ng[j] = True

sti = [i for i in range(H) if not row_ng[i]]
stj = [j for j in range(W) if not col_ng[j]]
dq = deque()
ans = 0
re = [[False for i in range(W)] for i in range(H)]
for i in sti:
    for j in stj:
        dq.append((i, j, 0))
        # ans += 1
        re[i][j] = True

while dq:
    x, y, cnt = dq.popleft()
    ans += 1

    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if not (0 <= nx <= H - 1 and 0 <= ny <= W - 1):
            continue

        if S[nx][ny] == "#":
            continue
        if re[nx][ny]:
            continue

        if cnt == K:
            continue
        re[nx][ny] = True

        dq.append((nx, ny, cnt + 1))

print(ans)
