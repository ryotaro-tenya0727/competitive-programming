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


N = int(input())
S = input()

# 左からABCが揃う最初の位置
left = max(S.find(c) for c in "ABC")

# 右からABCが揃う最初の位置
right = min(S.rfind(c) for c in "ABC")

# 中央の区間だけ取り出す
T = S[left + 1:right]

last = {"A": -1, "B": -1, "C": -1}

ans = 0

for i, c in enumerate(T):
    last[c] = i
    ans += min(last.values()) + 1

print(ans)
