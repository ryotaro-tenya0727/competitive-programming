import sys

sys.setrecursionlimit(10**7)

# from collections import deque
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


N, Q = imap()

toggle_times = [[] for _ in range(N)]

paint_times = []
paint_colors = []

for t in range(1, Q + 1):
    typ, v = input().split()

    if typ == "1":
        x = int(v) - 1
        toggle_times[x].append(t)
    else:
        paint_times.append(t)
        paint_colors.append(v)


def last_paint(L, R):
    i = bisect_left(paint_times, R) - 1

    if i >= 0 and paint_times[i] >= L:
        return paint_colors[i]

    return None


ans = ["a"] * N

for x in range(N):
    L = 1
    has_tile = False

    for t in toggle_times[x]:
        if not has_tile:
            color = last_paint(L, t)

            if color is not None:
                ans[x] = color

        else:
            L = t + 1

        has_tile = not has_tile

    if not has_tile:
        color = last_paint(L, Q + 1)

        if color is not None:
            ans[x] = color

print("".join(ans))
