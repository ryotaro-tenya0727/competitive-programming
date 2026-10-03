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
mini = 10**15
maxi = -1
for i in range(N):
    if A[i] != AS[i]:
        mini = min(mini, i)
        maxi = max(maxi, i)

if mini == 10**15:
    print("Yes")
    exit()

if maxi - mini + 1 <= K:
    print("Yes")
else:
    print("No")
