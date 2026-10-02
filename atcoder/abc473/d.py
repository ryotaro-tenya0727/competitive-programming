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


N, K = imap()
ans = []


def f(k, ar, n):

    if n == 1:
        ar.append(k)
        ans.append(tuple(reversed(ar)))
        ar.pop()
        return
    t = k // n
    for i in range(0, t + 1):
        ar.append(i)
        # print("before ar", ar, "k", k)
        f(k - n * i, ar, n - 1)
        # print("after ar", ar, "k", k)
        ar.pop()


f(K, [], N)
ans.sort()
# print(ans)
sys.stdout.write("\n".join(" ".join(map(str, v)) for v in ans) + "\n")
# print(ans)
