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


N, Q = map(int, input().split())
A = list(map(int, input().split()))

cumsum_a = [0]  # cumsum_a[k]: Aの先頭k個の和
length = [0]  # length[k]: 最初のkまとまりの合計要素数
total = [0]  # total[k]: 最初のkまとまりの総和

for i, a in enumerate(A, 1):
    cumsum_a.append(cumsum_a[-1] + a)
    length.append(length[-1] + i)
    total.append(total[-1] + cumsum_a[-1])


def sum_first(x):
    """Bの先頭x個の和を返す"""

    # 全部含められるまとまりの個数
    k = bisect_right(length, x) - 1

    # 次のまとまりから取る要素数
    rest = x - length[k]

    return total[k] + cumsum_a[rest]


for _ in range(Q):
    L, R = map(int, input().split())
    print(sum_first(R) - sum_first(L - 1))
