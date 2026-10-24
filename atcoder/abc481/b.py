# ライブラリ
# https://github.com/ryotaro-tenya0727/competitive-programming
import sys

sys.setrecursionlimit(10**7)

from collections import deque
# from functools import cmp_to_key
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


N, K = imap()
A = ilist()
ans = 0
used = defaultdict(bool)
for i in range(N - 1):
    t = (i + 1, A[i])
    s = (i + 2, A[i + 1])

    if used[i + 1] or used[i + 1]:
        continue

    if min(t[1], s[1]) <= K <= max(t[1], s[1]):
        ans += 1
        if t[1] == K:
            used[i + 1] = True
        if s[1] == K:
            used[i + 2] = True

print(ans)
