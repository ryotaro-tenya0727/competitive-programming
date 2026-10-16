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
ar = []

for i in range(N):
    l, r = imap()
    ar.append((l, r))

ar = sorted(ar, key=lambda x: x[1])

S = []
now = -10**15
for i in range(N):
    l, r = ar[i]
    if now < l:
        S.append((l, r))
        now = r

if len(S) < K:
    print(-1)
    exit()

ok = -1
ng = 10**10


def check(x):

    now = -10**15
    cur = 0
    for j in range(N):
        l, r = ar[j]

        if now + x <= l:
            cur += 1
            now = r

    if cur >= K:
        return True
    else:
        return False


while ng - ok > 1:
    mid = (ok + ng) // 2

    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
