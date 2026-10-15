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

for _ in range(T):
    N = int(input())
    S = input().strip()
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    # p[i]: S[i], S[i+1]を「RS」にする利益
    p = []
    for i in range(N - 1):
        gain = Y[i]

        if S[i] != "R":
            gain -= X[i]
        if S[i + 1] != "S":
            gain -= X[i + 1]

        p.append(gain)

    # dp[i]: ペア0〜iまで考えたときの最大値
    dp = [0] * (N - 1)
    dp[0] = max(0, p[0])

    for i in range(1, N - 1):
        # ペアiを選ぶ
        take = p[i]
        if i >= 2:
            take += dp[i - 2]

        # ペアiを選ばない場合と比較
        dp[i] = max(dp[i - 1], take)

    print(dp[-1])
