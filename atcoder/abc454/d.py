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


T = int(input())

for i in range(T):
    A = list(input())
    B = list(input())
    la = len(A)
    lb = len(B)
    ta = []
    tb = []
    for j in range(la):
        ta.append(A[j])

        if len(ta) >= 4 and ta[-4] == "(" and ta[-3] == "x" and ta[
                -2] == "x" and ta[-1] == ")":

            for k in range(4):
                ta.pop()
            ta.append("x")
            ta.append("x")

    for j in range(lb):
        tb.append(B[j])
        if len(tb) >= 4 and tb[-4] == "(" and tb[-3] == "x" and tb[
                -2] == "x" and tb[-1] == ")":
            for k in range(4):

                tb.pop()
            tb.append("x")
            tb.append("x")

    if "".join(ta) == "".join(tb):
        print("Yes")
    else:
        print("No")
