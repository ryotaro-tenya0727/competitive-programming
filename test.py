# ライブラリ
# https://github.com/ryotaro-tenya0727/competitive-programming
# import sys

# sys.setrecursionlimit(10**7)

# from collections import deque
# from functools import cmp_to_key
# from collections import defaultdict
# from bisect import bisect_left, bisect_right
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
# from copy import copy, deepcopy
# import heapq

# dr = [
#     (0, -1),
#     (-1, 0),
#     (0, 1),
#     (1, 0),
# ]

# def input():
#     return sys.stdin.readline().strip()


def imap():
    return map(int, input().split())


def ilist():
    return list(map(int, input().split()))


N, M, P = imap()

ar = []

for i in range(N):
    ar.append([i for i in range(1, M + 1)])

for i in range(P):
    i, j = imap()
    i -= 1
    j -= 1
    ar[i][j] += 1

5 7 5 1
1 1
2 3
2 5
4 3
5 7
2 1 6