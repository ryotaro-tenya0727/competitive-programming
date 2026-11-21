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
from collections import Counter

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


N, M = map(int, input().split())
vote_second = [[] for i in range(N)]
cnt_first = [0] * N
for i in range(M):
    a, b = imap()
    a -= 1
    b -= 1
    cnt_first[a] += 1
    vote_second[a].append(b)

cnt_tup = sorted(enumerate(cnt_first), key=lambda x: (-x[1], x[0]))
cnt_tup = sorted(cnt_tup, key=lambda x: (-x[1], x[0]))

number_1 = cnt_tup[0][0]
number_2 = cnt_tup[1][0]

for i in range(N):
    now = 0
    if number_1 == i:
        now = number_2
    else:
        now = number_1
    max_vote = cnt_first[now]

    for k, v in Counter(vote_second[i]).items():
        f = cnt_first[k] + v

        if f > max_vote or (f == max_vote and k < now):
            now = k
            max_vote = f

    print(now + 1)
