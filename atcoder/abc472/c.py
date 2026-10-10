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


N, M, K = imap()
A = ilist()
total = 0
eat = [False for i in range(N)]
ans = [False for i in range(N)]
for i in range(N):
    if i >= M:
        if eat[i - M]:
            total -= A[i - M]
    if total + A[i] <= K:
        total += A[i]
        ans[i] = True
        eat[i] = True

for v in ans:
    if v:
        print("Yes")
    else:
        print("No")
