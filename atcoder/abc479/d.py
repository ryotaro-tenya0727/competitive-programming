import sys

sys.setrecursionlimit(10**7)

# from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
# from bisect import bisect, bisect_left, bisect_right
# import math
# import itertools
# import heapq

# from itertools import groupby
# import math
# from atcoder.dsu import DSU
# from functools import cache
# from sortedcontainers import SortedSet, SortedList, SortedDict
from atcoder.segtree import SegTree

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
L = ilist()
R = ilist()
lenl = len(L)
min_R = SegTree(min, 10**15, R)
min_L = SegTree(min, 10**15, L)
for i in range(Q):
    s, t = imap()
    # 右へ進む
    if s < t:
        ans = R[s - 1]

        if s >= 2:
            ans = min(ans, L[s - 2] + min_R.prod(0, s - 1))

    # 左へ進む
    else:
        ans = L[s - 2]

        if s <= N - 1:
            ans = min(ans, R[s - 1] + min_L.prod(s - 1, N - 1))

    print(ans)
