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
from collections import Counter

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


N, M = map(int, input().split())

votes = [0] * N
second = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    votes[a] += 1
    second[a].append(b)

# 第一希望の得票数が多い上位2人
top2 = sorted(range(N), key=lambda i: (-votes[i], i))[:2]

for k in range(N):
    # 辞退しない方の上位候補者を選ぶ
    winner = top2[0] if top2[0] != k else top2[1]
    best = votes[winner]

    # kが辞退したことで増える票を集計
    for b, added in Counter(second[k]).items():
        score = votes[b] + added

        if score > best or (score == best and b < winner):
            winner = b
            best = score

    print(winner + 1)
