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
X, Y = imap()
A = ilist()
B = ilist()
A.sort()
B.sort()
PA = [A[0]]
PB = [B[0]]

for i in range(1, N):
    PA.append(PA[-1] + A[i])
for i in range(1, M):
    PB.append(PB[-1] + B[i])
ta = bisect_right(PA, X + K * Y)
ans = ta

for i in range(M):
    sb = (B[i] + K - 1) // K
    cur = 0

    if Y < sb:
        break
    Y -= sb

    cur = i + 1

    X += K * sb - B[i]
    cur += bisect_right(PA, X + K * Y)
    ans = max(cur, ans)

print(ans)
