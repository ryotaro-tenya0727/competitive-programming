import sys

sys.setrecursionlimit(10**7)

from collections import deque
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

N = len(S)

# 文字ごとに出現位置を保存
pos = [[] for _ in range(26)]

for i, c in enumerate(S):
    pos[ord(c) - ord('a')].append(i)

ans = 0

# 左端を固定
for l in range(N):
    r = l - 1  # 最初は開始位置の1つ前

    for c in T:
        indices = pos[ord(c) - ord('a')]

        # rより後ろの位置を探す
        i = bisect.bisect_right(indices, r)

        if i == len(indices):
            r = N
            break

        r = indices[i]

    ans += r - l

print(ans)
