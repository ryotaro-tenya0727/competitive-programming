# ライブラリ
# https://github.com/ryotaro-tenya0727/competitive-programming
import sys

sys.setrecursionlimit(10**7)

from collections import deque
# from functools import cmp_to_key
from collections import defaultdict
# from bisect import bisect_left, bisect_right
# import math
# import itertools
# import heapq

# from itertools import groupby, permutations
# import math
# from atcoder.dsu import DSU
# from functools import cache
from sortedcontainers import SortedSet, SortedList, SortedDict
# from atcoder.segtree import SegTree

# from atcoder.fenwicktree import FenwickTree
# from copy import copy, deepcopy
import heapq

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
    S = list(input())
    ls = len(S)
    cnt = defaultdict(int)
    isok = True
    for s in S:
        cnt[s] += 1

        if cnt[s] > ((ls + 1) // 2):
            isok = False
    if isok:
        print("Yes")
    else:
        print("No")
        continue

    if isok:
        prev = "-"

        t = []
        while True:
            maxcnt = 0
            for j in range(97, 97 + 26):
                st = chr(j)

                if st == prev:
                    continue

                if cnt[st] > maxcnt:
                    maxcnt = cnt[st]
                    target = st
                    break
            if maxcnt > 0:
                t.append(target)
                prev = target
                cnt[target] -= 1
            else:
                break

    print("".join(t))
