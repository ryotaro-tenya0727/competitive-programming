import sys

sys.setrecursionlimit(10**7)

# from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
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


N, Q = imap()
tile_state = [0] * N
queries = [(2, "a")]
for i in range(Q):
    n = input().split()
    if n[0] == "1":
        t = int(int(n[1]) - 1)
        tile_state[t] ^= 1
        queries.append((1, t))
    else:
        queries.append((2, n[1]))

lq = len(queries)
st = set(i for i in range(N) if tile_state[i] == 0)
ans = ["" for i in range(N)]

for i in range(lq - 1, -1, -1):
    n, s = queries[i]

    if n == 1:
        if ans[s] == "":
            if tile_state[s] == 0:
                st.remove(s)
            else:
                st.add(s)
            tile_state[s] ^= 1
    else:
        for v in st:
            if ans[v] != "":
                continue
            ans[v] = s
        st.clear()

print("".join(ans))
