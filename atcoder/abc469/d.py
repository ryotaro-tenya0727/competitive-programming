import sys

sys.setrecursionlimit(10**7)

# from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
from bisect import bisect, bisect_left, bisect_right
# import math
# import itertools
# import heapq

# from itertools import groupby
# import math
# from atcoder.dsu import DSU
# from functools import cache
# from sortedcontainers import SortedSet, SortedList, SortedDict
from atcoder.segtree import SegTree

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
cnt = defaultdict(int)
cnt_pair = defaultdict(int)

for _ in range(M):
    a, b = imap()
    cnt[a] += 1
    cnt[b] += 1
    cnt_pair[(a, b)] += 1

# 0回のプレイヤーも含めてソート
p_counts = sorted(cnt[player] for player in range(1, N + 1))

ans = 0
for i in range(N):
    match_j = bisect_left(p_counts, M - p_counts[i], i + 1)
    ans += N - match_j

# 同じペアは1回だけ補正
for (x, y), pair_count in cnt_pair.items():
    total = cnt[x] + cnt[y]
    if total >= M and total - pair_count < M:
        ans -= 1

print(ans)
