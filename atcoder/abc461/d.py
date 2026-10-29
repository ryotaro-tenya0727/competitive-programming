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
from sortedcontainers import SortedSet, SortedList, SortedDict
# from atcoder.segtree import SegTree

# from atcoder.fenwicktree import FenwickTree
# from copy import copy, deepcopy
import heapq

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


H, W, K = imap()
S = []

for i in range(H):
    S.append([int(i) for i in list(input())])


def f(u):
    ans = 0
    for i in range(H):
        t = [0 for _i in range(W)]
        for j in range(i, H):

            for k in range(W):
                t[k] += S[j][k]
            r = 0
            total = 0
            cur = 0
            for l in range(W):
                while r < W and total + t[r] <= u:
                    total += t[r]
                    r += 1

                cur += (r - l)
                if r == l:
                    r += 1
                else:
                    total -= t[l]

            ans += cur

    return ans


print(f(K) - f(K - 1))
