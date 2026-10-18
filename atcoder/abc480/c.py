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


N, K, T = imap()
A = ilist()
A.sort()
ans = 1
start = 0
if A[0] == 0:
    ans = 0
    start = 1
now = K
for i in range(start, N):
    if A[i] >= T:
        break
    if now >= A[i]:
        now = max(now, A[i] + K)
        continue

    cnt = (A[i] - now) // K
    if (A[i] - now) % K != 0:
        cnt += 1
    ans += cnt
    now = max(A[i] + K, now + cnt * K)

ans += ((T - (now)) // K)
if (T - now) % K != 0:
    ans += 1
print(ans)
