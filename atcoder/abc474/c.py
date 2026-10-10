import sys

sys.setrecursionlimit(10**7)

# from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
# from bisect import bisect_left, bisect_right
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


N, Q = imap()
P = ilist()
A = [int(input()) for i in range(Q)]
sta = set(A)
not_a_in_p = [p for p in P if not p in sta]
# print("not_a_in_p", not_a_in_p)
# print(not_a_in_p + sorted(set(A), key=A.index))
sa = set()
t = []

for i in range(Q - 1, -1, -1):

    if A[i] in sa:
        continue
    else:
        sa.add(A[i])
        t.append(A[i])

print(*(not_a_in_p + list(reversed(t))))
