# ライブラリ
# https://github.com/ryotaro-tenya0727/competitive-programming
import sys

sys.setrecursionlimit(10**7)

from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
from bisect import bisect_left, bisect_right
from itertools import groupby
from typing import Iterable, TypeVar

T = TypeVar("T")
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
C = ilist()

left = [N] * N
right = [N] * N

for i in range(1, N):
    if C[i] != C[i - 1]:
        left[i] = 1
    else:
        left[i] = left[i - 1] + 1

for i in range(N - 2, -1, -1):
    if C[i] != C[i + 1]:
        right[i] = 1
    else:
        right[i] = right[i + 1] + 1

ans = [min(left[i], right[i]) for i in range(N)]

print(*ans)
