# ライブラリ
# https://github.com/ryotaro-tenya0727/competitive-programming
import sys

sys.setrecursionlimit(10**7)

from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
from bisect import bisect_left, bisect_right
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


H, W, N, Q = imap()
cntr = defaultdict(int)
cntc = defaultdict(int)

for i in range(N):
    r, c = imap()
    r -= 1
    c -= 1
    cntr[r] += 1
    cntc[c] += 1

rkeys = sorted(list(cntr.keys()))
ckeys = sorted(list(cntc.keys()))


def f(d):
    keys = sorted(list(d.keys()))
    for i in range(1, len(keys)):
        d[keys[i]] += d[keys[i - 1]]


f(cntr)
f(cntc)

for i in range(Q):
    n = ilist()

    if n[0] == 1:
        u = n[1]
        d = n[2]
        u -= 1
        d -= 1
        tu = bisect_left(rkeys, u)
        td = bisect_right(rkeys, d)
        # print("tu", tu, "td", td, "rkeys[td-1]", rkeys[td - 1], "rkeys[tu-1]",
        #       rkeys[tu - 1])
        if td == 0:
            print(0)
            continue
        print(cntr[rkeys[td - 1]] - (0 if tu == 0 else cntr[rkeys[tu - 1]]))
        # print("cntr[rkeys[td - 1]] ", cntr[rkeys[td - 1]])
        # print("0 if rkeys[tu] == u else cntr[rkeys[tu - 1]]",
        #       0 if tu == 0 else cntr[rkeys[tu - 1]])

    else:
        l = n[1]
        r = n[2]
        l -= 1
        r -= 1
        tl = bisect_left(ckeys, l)
        tr = bisect_right(ckeys, r)
        if tr == 0:
            print(0)
            continue
        print(cntc[ckeys[tr - 1]] - (0 if tl == 0 else cntc[ckeys[tl - 1]]))
