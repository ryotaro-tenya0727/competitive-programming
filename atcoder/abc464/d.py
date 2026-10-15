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


T = int(input())

for i in range(T):
    N = int(input())
    S = list(input())
    X = ilist()
    Y = ilist()
    ans = 0
    p = []
    for i in range(N - 1):
        t = 0
        if S[i] != "R":
            t -= X[i]
        if S[i + 1] != "S":
            t -= X[i + 1]

        t += Y[i]
        p.append(t)

    dp = [0 for k in range(N - 1)]
    dp[0] = max(p[0], 0)
    ans = dp[0]
    if len(dp) >= 2:
        dp[1] = max(p[1], 0, p[0])
        ans = max(ans, dp[1])

    for j in range(2, N - 1):
        pl = max(p[j], 0)
        # print("pl", pl)
        dp[j] = max(dp[j - 2] + pl, 0, dp[j - 1])
        ans = max(ans, dp[j])

    print(ans)
