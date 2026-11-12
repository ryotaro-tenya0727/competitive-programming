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
A = list(map(int, input().split()))

# pos[i]: i回移動した後の座標
pos = [0]
for a in A:
    pos.append(pos[-1] + a)

# pos[i]以降の最小座標・最大座標
right_min = pos.copy()
right_max = pos.copy()

for i in range(N - 1, -1, -1):
    right_min[i] = min(right_min[i], right_min[i + 1])
    right_max[i] = max(right_max[i], right_max[i + 1])

# 反転しない場合
ans = max(pos) - min(pos) + 1

# 反転する位置より前の最小座標・最大座標
left_min = 0
left_max = 0

# A[i]を反転する場合をすべて試す
for i, a in enumerate(A):

    # 反転後の全体の最小座標・最大座標
    low = min(left_min, right_min[i + 1] - 2 * a)
    high = max(left_max, right_max[i + 1] - 2 * a)

    ans = max(ans, high - low + 1)

    # 次の反転候補に進む準備
    left_min = min(left_min, pos[i + 1])
    left_max = max(left_max, pos[i + 1])

print(ans)
