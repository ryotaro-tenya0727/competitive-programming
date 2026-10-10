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
from sortedcontainers import SortedSet, SortedList, SortedDict
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


N = int(input())
A = SortedList(ilist())

now = 0
ans = 0
for i in range(N):
    now_gteq = bisect_left(A, now)
    l = max(0, now_gteq - 1)
    r = min(len(A) - 1, now_gteq)

    labs = abs(now - A[l])
    rabs = abs(now - A[r])
    nxt = A[l] if labs <= rabs else A[r]
    ans += abs(nxt - now)
    now = nxt
    A.remove(nxt)

print(ans)
