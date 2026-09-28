import sys

sys.setrecursionlimit(10**7)

# from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
# from bisect import bisect_left, bisect_right
# import math
# import itertools
# import heapq

from itertools import groupby
# import math
# from atcoder.dsu import DSU
# from functools import cache
# from sortedcontainers import SortedSet, SortedList, SortedDict
# from atcoder.segtree import SegTree

# from atcoder.fenwicktree import FenwickTree
# import copy
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
P = ilist()
S = []

for i in range(N - 1):
    if P[i] < P[i + 1]:
        S.append("<")
    else:
        S.append(">")


def runLengthEncode(arr: list) -> list[tuple]:
    res = []
    grouped = groupby(arr)
    for k, v in grouped:
        res.append((k, len(list(v))))
    return res


SR = runLengthEncode(S)

lsr = len(SR)
ans = 0
for i in range(lsr):
    if SR[i][0] == "<" and i + 2 < lsr:
        ans += SR[i][1] * SR[i + 2][1]

print(ans)
