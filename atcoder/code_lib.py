# string runlength
# def runLengthEncode(arr: list) -> list[tuple]:
#     res = []
#     grouped = groupby(arr)
#     for k, v in grouped:
#         res.append((k, len(list(v))))
#     return res

# int runlength
# def runLengthEncode(arr: list) -> list[tuple]:
#     res = []
#     grouped = groupby(arr)
#     for k, v in grouped:
#         res.append((k, len(list(v))))
#     return res

# s = [1, 2, 3, 4, 5]
# N = len(s)
# for i in range(1, N + 1):
#     for j in range(N - i + 1):
#         print(s[j:j + i])

# def dijkstra(graph, start):
#     # 初期化
#     n = len(graph)
#     visited = [False] * n
#     distance = [sys.maxsize] * n
#     distance[start] = 0
#     pq = [(0, start)]

#     while pq:
#         dist, u = heapq.heappop(pq)
#         if visited[u]:
#             continue

#         visited[u] = True

#         for v, weight in graph[u]:
#             if not visited[v]:
#                 new_distance = distance[u] + weight
#                 if new_distance < distance[v]:
#                     distance[v] = new_distance
#                     heapq.heappush(pq, (new_distance, v))

#     return distance

# class Trie:

#     def __init__(self):
#         self.to = [{}]  # to[v] = {char: node_index}
#         self.ans = 0
#         self.ng = []
#         self.num_y = []

#     def add(self, s: str) -> int:
#         v = 0
#         for c in s:
#             if c not in self.to[v]:
#                 u = len(self.to)
#                 self.to[v][c] = u
#                 self.to.append({})
#             v = self.to[v][c]
#         return v

#     def init(self):
#         self.ans = 0
#         n = len(self.to)
#         self.ng = [False] * n
#         self.num_y = [0] * n

#     def addx(self, v: int):
#         if self.ng[v]:
#             return
#         self.ng[v] = True
#         self.ans -= self.num_y[v]
#         for u in self.to[v].values():
#             self.addx(u)

#     def addy(self, v: int):
#         if self.ng[v]:
#             return
#         self.ans += 1
#         self.num_y[v] += 1

# def dec_to_n(num: int, base: int) -> list:
#     digits = []
#     while num > 0:
#         digits.append(num % base)
#         num //= base
#     return digits  # 逆順のままリストで返す（回文チェックはreverse比較）

# MOD = 998244353

# class Comb:

#     def __init__(self, n, mod=MOD):
#         self.mod = mod

#         # fact[i] = i! % mod
#         self.fact = [1] * (n + 1)

#         for i in range(1, n + 1):
#             self.fact[i] = self.fact[i - 1] * i % mod

#     def ncr(self, n, r):
#         if n < 0 or r < 0 or r > n:
#             return 0

#         # nCr = n! / (r! * (n-r)!)
#         denominator = self.fact[r] * self.fact[n - r] % self.mod

#         # 分母で割る代わりに、分母の逆元を掛ける
#         inverse = pow(denominator, self.mod - 2, self.mod)

#         return self.fact[n] * inverse % self.mod

comb = Comb(N)

print(comb.ncr(N, K))

# 出力高速化
# sys.stdout.write("\n".join(" ".join(map(str, v)) for v in ans) + "\n")

# if l <= nowl and nowr <= r:
#     print("Yes")
#     continue
# isok = False
# for j in range(l, r + 1):
#     if S[j:j + lt] == T:
#         nowl = l
#         nowr = r
#         isok = True

# if isok:
#     print("Yes")
# else:
#     print("No")
# if nowl < l:
#     l = max(nowl, l)
#     for j in range(l, r + 1):
#         if S[j:j + lt] == T:
#             nowl = l
#             nowr = r
# if r < nowr:
#     r = min(nowr, r)
#     for j in range(l, r + 1):
#         if S[j:j + lt] == T:
#             nowl = l
#             nowr = r

# if l <= mini and r <= maxi:
#     print("Yes")
# else:
#     print("No")
