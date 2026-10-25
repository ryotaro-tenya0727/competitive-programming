"""Euler Tour によって根付き木の部分木を配列の区間へ変換する。

使い方:

    children = [[1, 2], [3, 4], [], [], []]
    tour = EulerTour(children)
    left, right = tour.subtree_range(1)

この例では ``tour.order == [0, 1, 3, 4, 2]`` となり、頂点 1 の部分木は
``tour.order[left:right] == [1, 3, 4]`` で取得できる。

``tin[v]`` は頂点 ``v`` が DFS 順で現れる位置、``tout[v]`` はその部分木の
直後の位置である。したがって部分木は常に半開区間 ``[tin[v], tout[v])`` に
対応する。頂点番号順の重み ``weights`` をセグメント木などで扱う場合は、
``tour.values_in_order(weights)`` を使って DFS 順へ並べ替える。

頂点番号と tour 上の index は区別する。たとえば頂点番号順の重みが
``weights = [10, 20, 30, 40, 50]`` で、DFS 順が
``order = [0, 1, 3, 4, 2]`` の場合を考える。

* ``weights[4] == 50`` は「頂点 4 の重み」を表す。
* ``order[3] == 4`` は「tour の位置 3 に頂点 4 がある」ことを表す。
* ``tin[4] == 3`` は「頂点 4 の重みを tour 上で操作する位置」を表す。

このため、セグメント木には頂点番号順の ``weights`` をそのまま渡さず、
``tour.values_in_order(weights)`` による ``[10, 20, 40, 50, 30]`` を渡す。
頂点 1 の部分木なら ``[tin[1], tout[1]) == [1, 4)`` となり、その区間は
頂点 ``[1, 3, 4]``、重み ``[20, 40, 50]`` に対応する。

AtCoder Library の ``SegTree`` と組み合わせる例:

    from atcoder.segtree import SegTree

    tour = EulerTour(children)
    seg = SegTree(lambda left, right: left + right, 0,
                  tour.values_in_order(weights))

    vertex = 1
    left, right = tour.subtree_range(vertex)
    subtree_sum = seg.prod(left, right)

    vertex = 4
    position = tour.tin[vertex]
    seg.set(position, seg.get(position) + 7)

``prod(left, right)`` は right を含まない半開区間を計算する。そのため、部分木の
和は ``seg.prod(tin[v], tout[v])`` と書ける。頂点 ``v`` の値を更新するときは、
頂点番号 ``v`` をセグメント木の index として直接使わず、必ず ``tin[v]`` を使う。

元の Library Checker「Vertex Add Subtree Sum」で親配列 ``parents`` から
``children`` を作り、クエリを処理する例:

    children = [[] for _ in range(N)]
    for vertex in range(1, N):
        children[parents[vertex - 1]].append(vertex)

    tour = EulerTour(children)
    seg = SegTree(lambda a, b: a + b, 0, tour.values_in_order(weights))
    answers = []
    for query in queries:
        vertex = query[1]
        if query[0] == 0:  # 頂点 vertex に query[2] を加算
            position = tour.tin[vertex]
            seg.set(position, seg.get(position) + query[2])
        else:  # 頂点 vertex の部分木の和
            left, right = tour.subtree_range(vertex)
            answers.append(seg.prod(left, right))

ここで ``weights[v]`` は頂点番号 ``v`` の初期重み、``tour.order[k]`` は
DFS 順の位置 ``k`` にある頂点番号を表す。
"""

from collections.abc import Sequence


# 根付き木を DFS 順に並べ、各部分木を半開区間へ変換する。
class EulerTour:
    # children[v] に頂点 v の子を並べ、root を根として DFS 順を作る。
    def __init__(self, children: Sequence[Sequence[int]], root: int = 0) -> None:
        vertex_count = len(children)
        if not 0 <= root < vertex_count:
            raise ValueError("root is out of range")

        self.tin = [-1] * vertex_count
        self.tout = [-1] * vertex_count
        self.order: list[int] = []

        stack = [(root, False)]
        while stack:
            vertex, exiting = stack.pop()
            if exiting:
                self.tout[vertex] = len(self.order)
                continue

            self.tin[vertex] = len(self.order)
            self.order.append(vertex)
            stack.append((vertex, True))
            for child in reversed(children[vertex]):
                stack.append((child, False))

    # vertex の部分木に対応する半開区間 [left, right) を返す。
    def subtree_range(self, vertex: int) -> tuple[int, int]:
        return self.tin[vertex], self.tout[vertex]

    # 頂点番号順の値を Euler Tour 順に並べ替える。
    def values_in_order(self, values: Sequence[int]) -> list[int]:
        return [values[vertex] for vertex in self.order]
