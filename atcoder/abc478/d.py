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


N, Q = imap()
events = [[] for i in range(N + 1)]

for i in range(Q):
    l, r, x = imap()
    l -= 1
    events[l].append((1, x))
    events[r].append((-1, x))

num = 0
ans = []
cnt = defaultdict(int)
for i in range(N):
    for plus_minus, x in events[i]:
        if plus_minus == 1:
            cnt[x] += 1

            if cnt[x] == 1:
                num += 1
        else:
            cnt[x] -= 1

            if cnt[x] == 0:
                num -= 1
    ans.append(num)

print(*ans)
