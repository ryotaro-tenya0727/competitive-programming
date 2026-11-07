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


S = []

for i in range(5):
    S.append(list(input()))
ans = 10**15
for i in range(5):
    t = 0
    for j in range(5):
        if S[i][j] == ".":
            t += 1
    ans = min(ans, t)

for i in range(5):
    t = 0
    for j in range(5):
        if S[j][i] == ".":
            t += 1
    ans = min(ans, t)

p = 0
for i in range(5):
    if S[i][i] == ".":
        p += 1
ans = min(ans, p)
q = 0
for i in range(5):
    if S[i][4 - i] == ".":
        q += 1
ans = min(ans, q)

print(ans)
