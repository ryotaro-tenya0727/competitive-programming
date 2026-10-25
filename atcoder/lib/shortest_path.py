import heapq
from typing import Sequence


# 非負重み有向グラフの始点からの最短距離を返す。
# graph[v] は (行き先, 重み) のリスト。到達不能な頂点の距離は 10**30。
def dijkstra(graph: Sequence[Sequence[tuple[int, int]]], start: int) -> list[int]:
    inf = 10**30
    distance = [inf] * len(graph)
    distance[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, vertex = heapq.heappop(queue)
        if current_distance != distance[vertex]:
            continue

        for next_vertex, weight in graph[vertex]:
            next_distance = current_distance + weight
            if next_distance >= distance[next_vertex]:
                continue
            distance[next_vertex] = next_distance
            heapq.heappush(queue, (next_distance, next_vertex))

    return distance
