import sys

sys.setrecursionlimit(10**7)

# from collections import deque
# from functools import cmp_to_key
# from collections import defaultdict
# from bisect import bisect_left, bisect_right
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


N, M = imap()

ans = []


def f(m, k, ar):

    if len(ar) == N:

        ans.append(tuple(reversed(ar)))
        return

    for v in range(m, 10 * k - 9 - 1, -1):
        ar.append(v)
        f(v - 10, k - 1, ar)
        ar.pop()


f(M, N, [])

ans = sorted(ans)
print(len(ans))
sys.stdout.write("\n".join(" ".join(map(str, v)) for v in ans) + "\n")
