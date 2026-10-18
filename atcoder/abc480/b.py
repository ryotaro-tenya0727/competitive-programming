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


N, M = imap()
vote = [0 for i in range(N)]
S = [list(input()) for i in range(N)]
T = [list(input()) for i in range(M)]

for i in range(M):
    target_t = T[i]

    is_first = False
    for j in range(N):
        if S[j] == target_t:
            vote[j] += 1
            is_first = True
            break
    if is_first:
        continue
    else:
        lt = len(target_t)
        koho = []
        for k in range(N):
            if len(target_t) != len(S[k]):
                continue
            else:
                diff = 0
                for p in range(lt):
                    if target_t[p] != S[k][p]:
                        diff += 1
                if diff == 1:
                    koho.append(k)

        if len(koho) == 1:
            vote[koho[0]] += 1

for v in vote:
    print(v)
