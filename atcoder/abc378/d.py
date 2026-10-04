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


H, W, K = imap()
S = [list(input()) for i in range(H)]

ans = 0

re = [[False for i in range(W)] for i in range(H)]

ans = 0


def f(cnt, re, x, y):
    global ans
    if cnt == K:
        ans += 1
        return

    for dx, dy in dr:
        nx, ny = x + dx, y + dy

        if not (0 <= nx <= H - 1 and 0 <= ny <= W - 1):
            continue
        if S[nx][ny] == "#":
            continue

        if re[nx][ny]:
            continue

        re[nx][ny] = True
        f(cnt + 1, re, nx, ny)
        re[nx][ny] = False


for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        re = [[False for i in range(W)] for i in range(H)]
        re[i][j] = True
        f(0, re, i, j)

print(ans)
