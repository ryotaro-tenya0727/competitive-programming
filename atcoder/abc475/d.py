import sys

sys.setrecursionlimit(10**7)

# from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
from bisect import bisect_left, bisect_right
# import math
# import itertools
# import heapq

# from itertools import groupby
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


S = list(input())
ls = len(S)
nums = []

isp = [False] * (10**7 + 10)
for i in range(2, 10**7 + 1):
    if isp[i]:
        continue

    nums.append(i)
    t = i
    while t <= 10**7:
        isp[t] = True
        t += i

for v in nums:
    vs = list(str(v))
    lvs = len(vs)
    if lvs != ls:
        continue
    isok = True
    for i in range(0, lvs - 1):
        for j in range(i, lvs):
            if (S[i] == S[j]) != (vs[i] == vs[j]):
                isok = False
    if isok:
        print("".join(vs))
        exit()

print(-1)
