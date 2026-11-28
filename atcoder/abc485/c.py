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


def run_length_encode(values: Iterable[T]) -> list[tuple[T, int]]:
    return [(value, len(list(group))) for value, group in groupby(values)]


C = run_length_encode(C)

lc = len(C)
ans = []
for i in range(lc):
    if i == 0:
        for j in range(C[i][1], 0, -1):
            ans.append(j)
    elif i == lc - 1:
        for j in range(1, C[i][1] + 1):
            ans.append(j)
    else:
        if C[i][1] % 2 == 0:
            for j in range(1, (C[i][1] // 2) + 1):
                ans.append(j)
            for j in range((C[i][1] // 2), 0, -1):
                ans.append(j)
        else:

            for j in range(1, ((C[i][1] + 1) // 2) + 1):
                ans.append(j)
            for j in range((C[i][1] // 2), 0, -1):
                ans.append(j)
print(*ans)
