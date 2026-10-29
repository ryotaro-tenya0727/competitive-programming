# ライブラリ
# https://github.com/ryotaro-tenya0727/competitive-programming
# https://atcoder.jp/contests/abc481/tasks/abc481_e
import sys

sys.setrecursionlimit(10**7)

from collections import deque
from functools import cmp_to_key
from collections import defaultdict
# from bisect import bisect_left, bisect_right
# import math
# import itertools
# import heapq

# from itertools import groupby, permutations
# import math
# from atcoder.dsu import DSU
# from functools import cache
# from sortedcontainers import SortedSet, SortedList, SortedDict
# from atcoder.segtree import SegTree

# from atcoder.fenwicktree import FenwickTree
from copy import copy, deepcopy
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


def cmp(a, b):
    x, y = a
    u, v = b
    h = y < 0 or (y == 0 and x < 0)
    k = v < 0 or (v == 0 and u < 0)
    if h != k:
        return h - k
    z = x * v - y * u
    return (z < 0) - (z > 0)


t = int(input())
for i in range(t):

    n = int(input())
    p = [tuple(map(int, input().split())) for _ in range(n)]
    p.sort(key=cmp_to_key(cmp))
    p *= 2
    ans = r = 1
    for l in range(n):
        r = max(r, l + 1)
        x, y = p[l]
        while r < l + n:
            u, v = p[r]
            if x * v < y * u:
                break
            r += 1
        ans = max(ans, r - l)
    print(ans)
