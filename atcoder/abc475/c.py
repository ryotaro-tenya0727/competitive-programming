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


N, S, L = imap()
A = ilist()
AS = [0]

for i in range(N - 1):
    AS.append(AS[-1] + A[i])

ans = 0

for i in range(S):
    for j in range(S - 1, N):
        t = (AS[S - 1] - AS[i]) * 2 + AS[j] - AS[S - 1]
        f = (AS[S - 1] - AS[i]) + (AS[j] - AS[S - 1]) * 2
        if t <= L:
            ans = max(ans, j - i + 1)
            continue
        if f <= L:
            ans = max(ans, j - i + 1)
print(ans)
