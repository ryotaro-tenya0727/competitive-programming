# https://judge.yosupo.jp/problem/vertex_add_subtree_sum
import sys

sys.setrecursionlimit(10**7)

from atcoder.segtree import SegTree


def input():
    return sys.stdin.readline().strip()


def imap():
    return map(int, input().split())


def ilist():
    return list(map(int, input().split()))


N, Q = imap()
A = ilist()
P = ilist()

children = [[] for _ in range(N)]
for v in range(1, N):
    children[P[v - 1]].append(v)

tin = [0] * N
tout = [0] * N
tour = []


def dfs(v):
    tin[v] = len(tour)
    tour.append(v)

    for w in children[v]:
        dfs(w)

    tout[v] = len(tour)


dfs(0)

seg = SegTree(lambda a, b: a + b, 0, [A[v] for v in tour])
ans = []

for _ in range(Q):
    query = ilist()
    v = query[1]

    if query[0] == 0:
        x = query[2]
        i = tin[v]
        seg.set(i, seg.get(i) + x)
    else:
        ans.append(str(seg.prod(tin[v], tout[v])))

print("\n".join(ans))

# オイラーツアー：頂点番号と tour 上の index の対応

# オイラーツアーで部分木を区間に変換するときは、**頂点番号と、その頂点が tour 上のどの位置にいるかを区別すること**が大事。

# A[i] の i は頂点番号。一方、セグメント木には tour 順に重みを並べるので、頂点 i の重みを操作する位置は tin[i] になる。

# ## 各配列の役割

# tour は、木全体の頂点をDFSで初めて訪れた順に並べたlist。各部分木の頂点が連続するように並ぶ。親へ戻るときには頂点を追加しない。

# | 書き方 | 意味 |
# |---|---|
# | A[i] | 頂点 i の初期重み |
# | tour[k] | tour のindex kにある頂点番号 |
# | tin[i] | 頂点 i のtour上のindex。その部分木の開始位置でもある |
# | tout[i] | 頂点 i の部分木の終了位置。この位置は含めない |

# 頂点 i の部分木は、tour[tin[i]:tout[i]] で取り出せる。

# ## 頂点番号と index の具体例

# 例えば、初期状態が次のようになっているとする。

# ```python
# A = [10, 20, 30, 40, 50]
# tour = [0, 1, 3, 4, 2]
# ```

# 頂点4は tour のindex 3にある。

# ```python
# tour[3] == 4
# tin[4] == 3
# ```

# tour では「位置から頂点番号」を読み、tin では「頂点番号から位置」を調べる。

# ## 重みも tour の順番に並べる

# セグメント木を作るときは、重みを tour の順番に取り出す。

# ```python
# weights = [A[v] for v in tour]
# # [10, 20, 40, 50, 30]

# seg = SegTree(lambda a, b: a + b, 0, weights)
# ```

# | tour 上のindex | 0 | 1 | 2 | 3 | 4 |
# |---|---|---|---|---|---|
# | 頂点番号 | 0 | 1 | 3 | 4 | 2 |
# | セグ木に保存する重み | 10 | 20 | 40 | 50 | 30 |

# 頂点4の重み A[4] = 50 は、セグ木のindex 3に保存される。

# lambda a, b: a + b は、2つの区間の計算結果を足し合わせる指定。今回は区間の重みの合計を求めるので、足し算を使う。

# ## 部分木の合計を求める

# 頂点1の部分木では、tin[1] = 1、tout[1] = 4 となる。

# ```python
# tour[1:4]  # [1, 3, 4]
# ```

# 重みも同じ位置に並べているので、初期状態での合計は次のように求められる。

# ```python
# seg.prod(tin[1], tout[1])
# # seg.prod(1, 4)
# # 20 + 40 + 50 = 110
# ```

# prod(left, right) は、index left から right の手前までを計算する。今回の設定では、その区間の和を返す。

# ## 1頂点の重みを更新する

# 頂点 i に x を加えるときは、先に tin[i] でセグ木の位置を調べる。

# ```python
# pos = tin[i]
# seg.set(pos, seg.get(pos) + x)
# ```

# get(pos) は、その位置の現在の重みを読む。
# set(pos, value) は、その位置の値を上書きする。

# 例えば、頂点4に7を加えるなら、

# ```python
# i = 4
# x = 7
# pos = tin[i]  # 3

# seg.set(pos, seg.get(pos) + x)
# # index 3の重みを、50から57に更新する
# ```

# **頂点番号 i をそのままセグ木のindexにせず、tin[i] で tour 上の位置に変換して使う。**
