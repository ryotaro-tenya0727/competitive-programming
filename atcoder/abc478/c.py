import sys

sys.setrecursionlimit(10**7)

# from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
from bisect import bisect_left
# import math
# import itertools
# import heapq

from itertools import groupby
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


N, K = imap()
A = ilist()
AS = sorted(A)

l = 0

for i in range(N):
    if A[i] != AS[i]:
        break
    l += 1

r = 0

for i in range(N - 1, -1, -1):
    if A[i] != AS[i]:
        break
    r += 1

if l + r + K >= N:
    print("Yes")
else:
    print("No")
