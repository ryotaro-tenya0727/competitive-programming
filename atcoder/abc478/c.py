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


Q = int(input())
S = list(input())
T = list(input())

ls = len(S)
lt = len(T)
ar = []
for i in range(ls - lt + 1):
    if S[i:i + lt] == T:
        ar.append(i)
lar = len(ar)
for i in range(Q):
    l, r = imap()
    l -= 1
    r -= 1
    if len(ar) == 0:
        print("No")
        continue

    t = bisect_left(ar, l)
    if t < lar and ar[t] + lt - 1 <= r:
        print("Yes")
    else:
        print("No")
