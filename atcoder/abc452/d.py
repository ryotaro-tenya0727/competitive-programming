import sys

sys.setrecursionlimit(10**7)

# from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
import bisect
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
from heapq import heappush, heappop, heappush, heapify

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
T = list(input())

ls = len(S)
lt = len(T)

so = defaultdict(list)

for i in range(ls):
    so[S[i]].append(i)
ans = 0
for i in range(ls):
    target = i - 1

    for j in range(lt):
        t = T[j]
        tp = bisect.bisect_right(so[t], target)

        if tp == len(so[t]):
            target = ls
            break

        target = so[t][tp]

    ans += target - i

print(ans)
