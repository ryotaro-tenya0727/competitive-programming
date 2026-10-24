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


N, D = imap()
T = [0 for i in range(2 * 10**6 + 10)]

for i in range(N):
    s, t = imap()
    if (t - s) - D >= 0:
        T[s] += 1
        T[t - D + 1] -= 1

lt = len(T)

ans = 0
for i in range(1, lt):
    T[i] += T[i - 1]

for i in range(lt):
    if T[i] >= 2:
        ans += (T[i] * (T[i] - 1)) // 2

print(ans)
