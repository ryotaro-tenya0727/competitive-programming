# AtCoder 用ライブラリ

元の `atcoder/code_lib.py` と `library_checker/euler_tour.py` の内容を用途ごとに分けた。各 `.py` は提出コードに貼り付けても使える。手元で読み込む場合は `atcoder` ディレクトリをカレントディレクトリにする。

```python
from lib import Comb, EulerTour, dijkstra, run_length_encode
```

## 偏角ソート: `angle_sort.py`

原点から見た角度で、右方向（正の x 軸）を始点に反時計回りに並べる。同じ方向では原点に近い順で、原点 `(0, 0)` は先頭に置く。元のリストは変更しない。`is_same_dir(a, b)` は原点から見て同じ方向か判定し、どちらかが原点なら `False` を返す。

```python
from lib.angle_sort import angle_sort, is_same_dir

points = [(0, -1), (-1, 0), (0, 0), (2, 0), (1, 0), (0, 1)]
assert angle_sort(points) == [
    (0, 0), (1, 0), (2, 0), (0, 1), (-1, 0), (0, -1)
]
assert is_same_dir((1, 1), (2, 2))
assert not is_same_dir((0, 0), (1, 1))
```

AtCoder ABC481 E での使用例は [`angle_sort_exmpple.py`](angle_sort_exmpple.py) にある。

## ランレングス圧縮: `run_length.py`

文字列と整数列のどちらにも使える。**連続している**同じ値だけを `(値, 個数)` にまとめるため、離れた位置の同じ値は別の組になる。元メモの string / int の 2 例は同じ関数で扱える。

```python
from lib.run_length import run_length_encode

assert run_length_encode("aaabbaba") == [
    ("a", 3), ("b", 2), ("a", 1), ("b", 1), ("a", 1)
]
assert run_length_encode([1, 1, 2, 2, 1]) == [(1, 2), (2, 2), (1, 1)]
```

## 連続部分列の列挙: `subarrays.py`

元メモの二重ループ `s[j:j+i]`。長さ 1、2、… の順に、各長さで左から右へ列挙する。要素数を `N` とすると、空でない部分列は `N(N+1)/2` 個あり、全てを実際にスライスする時間は O(N³)。

```python
from lib.subarrays import contiguous_slices

assert list(contiguous_slices([1, 2, 3])) == [
    [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]
]
```

## 最短経路: `shortest_path.py`

非負重みの有向グラフに対するダイクストラ法。`graph[v]` に `(行き先, 重み)` を並べ、始点を渡す。距離が更新された頂点をヒープに入れ、古い距離の要素は取り出した時点で飛ばす。到達不能な頂点の距離は `10**30`。計算量はおおむね O((V+E) log V)。無向辺は両方向に追加する。

```python
from lib.shortest_path import dijkstra

graph = [[(1, 2), (2, 5)], [(2, 1)], []]
assert dijkstra(graph, 0) == [0, 2, 3]
```

## Trie: `trie.py`

`Trie` は文字列を登録して完全一致を判定する。`insert(word)` は単語末尾の頂点番号を返し、`contains(word)` は文字列が登録されているかを返す。頂点 `v` の次の文字と行き先は `children[v]` に入る。

```python
from lib.trie import Trie

trie = Trie()
trie.insert("apple")
assert trie.contains("apple")
assert not trie.contains("app")
```

元メモの `Trie` にあった X / Y の処理は `MarkedTrie` に分けた。**全ての文字列を先に `insert` する**。`add_x(v)` は頂点 `v` 以下を塞ぎ、その範囲にすでにある Y を答えから引く。`add_y(v)` は塞がれていない頂点に Y を 1 個足す。`answer` が有効な Y の合計。元の `init()` に相当する `reset_marks()` で印を消せる。

```python
from lib.trie import MarkedTrie

trie = MarkedTrie()
apple = trie.insert("apple")
banana = trie.insert("banana")
trie.add_y(apple)
trie.add_y(banana)
assert trie.answer == 2
trie.add_x(apple)
assert trie.answer == 1
trie.reset_marks()
assert trie.answer == 0
```

## 基数変換: `base_conversion.py`

元の `dec_to_n` と同様、桁を**下位から上位**の順で返す。例えば 13 は 2 進数で `1101` なので `[1, 0, 1, 1]` となる。回文判定には結果と `digits[::-1]` を比較できる。`0` は `[0]` を返す。

```python
from lib.base_conversion import digits_in_base

assert digits_in_base(13, 2) == [1, 0, 1, 1]
assert digits_in_base(0, 10) == [0]
```

## 二項係数: `combinatorics.py`

元の `code_lib.py` と同じ方式の `Comb`。`Comb(N)` で `0!` から `N!` までの階乗だけを前計算する。`fact[i]` は `i! % mod`。整理後の名前 `Combination` も `Comb` の別名として使える。

`nCr = n! / (r! × (n-r)!)` なので、mod の下では分母で直接割らず、`ncr` を呼ぶたびに `pow(denominator, mod - 2, mod)` で逆元を求めて掛ける。初期化 O(N)、各 `ncr` は O(log mod)、メモリ O(N)。

```python
from lib.combinatorics import Comb

N, K = 5, 2
comb = Comb(N)  # デフォルト mod = 998244353
assert comb.fact[5] == 120
assert comb.ncr(N, K) == 10
assert comb.ncr(3, 4) == 0
```

`0 <= n <= N < mod` かつ `mod` が素数であることが前提。`r < 0` や `r > n` は 0 を返す。`n > N` には対応していない。

## 出力高速化: `fast_output.py`

元メモの `sys.stdout.write("\n".join(" ".join(map(str, v)) for v in ans) + "\n")` を関数にした。複数行をまとめて書き出す。`rows` は二次元の配列または反復可能オブジェクトで、各行の要素を空白で結ぶ。空の `rows` は何も出力しない。結果を一度メモリに保持するため、非常に大きい出力では適宜分割する。

```python
from lib.fast_output import write_rows

ans = [[1, 2], [3, 4]]
write_rows(ans)  # 1 2\n3 4\n と出力
```

1 行に 1 値なら `sys.stdout.write("\n".join(map(str, ans)) + "\n")` を直接使える。

## 範囲内の部分文字列・部分列: `substring_search.py`

元メモの `S[j:j+lt] == T` は、`j` が範囲の終わりに近いと `T` が右端をはみ出し得る。`contains_pattern_in_range(S, T, l, r)` は **0-indexed で両端を含む** `[l, r]` に `T` 全体が収まる場合だけ `True` を返す。文字列にもリストにも使える。

```python
from lib.substring_search import contains_pattern_in_range

assert contains_pattern_in_range("abcabc", "bc", 1, 3)
assert not contains_pattern_in_range("abcabc", "bc", 2, 3)
```

元の `nowl` / `nowr` / `mini` / `maxi` を使った条件は、変数の意味や更新条件がメモに残っていない問題固有の途中式。以前の `[nowl, nowr]` に **完全に収まる** 一致が確認済みなら、それを含む新しい範囲にも一致がある。ただし元の `for j in range(l, r + 1)` は右端を越えて比較する場合があり、そのままでは「範囲内で一致した」という保証がない。上の関数はこの境界条件を明示して直接調べる。

## mod の逆元: `modular_arithmetic.py`

`A / B (mod P)` を計算するときは `A * B⁻¹ % P` とする。`modular_inverse(value, mod)` の **`value` には分母の `B`、`mod` には `P`** を渡す。返るのは `B⁻¹` であり、`A / B` の結果そのものではない。`B⁻¹` は `B × B⁻¹ ≡ 1 (mod P)` を満たす数。`B` と `P` が互いに素なら存在し、`pow(B, -1, P)` で求められる。存在しなければ `ValueError`。これが元メモの「mod を取りながら割り算したい → 逆元を掛ける」という意味。

```python
from lib.modular_arithmetic import inverse_table, modular_inverse

# 5C2 = 120 / 12 = 10。mod 13 で計算する例。
numerator, denominator, mod = 120, 12, 13
answer = numerator * modular_inverse(denominator, mod) % mod
assert answer == 10
```

逆元を 1 から N まで求める方法は 2 通りある。

```python
N, mod = 4, 11
simple = [0] + [pow(i, -1, mod) for i in range(1, N + 1)]
fast = inverse_table(N, mod)
assert simple == fast == [0, 1, 6, 4, 3]
```

前者は O(N log mod)。後者は `inv[i] = mod - (mod // i) * inv[mod % i] % mod` を使い O(N)。`inverse_table` は **素数 mod かつ N < mod** を前提とする。`inv[0]` は逆元がないので 0 のまま。

## オイラーツアー: `euler_tour.py`

根付き木を DFS 順に並べ、各部分木を連続区間に変換する。`children[v]` に頂点 `v` の子を入れる。`tin[v]` は頂点 `v` の DFS 順での位置、`tout[v]` はその部分木の直後の位置。部分木は半開区間 `[tin[v], tout[v])` になる。

```python
from lib.euler_tour import EulerTour

children = [[1, 2], [3, 4], [], [], []]
tour = EulerTour(children)
assert tour.order == [0, 1, 3, 4, 2]
assert tour.subtree_range(1) == (1, 4)

weights = [10, 20, 30, 40, 50]  # 頂点番号順
assert tour.values_in_order(weights) == [10, 20, 40, 50, 30]
```

頂点番号と tour の位置は別物。頂点 4 の重みをセグメント木で更新する位置は `4` ではなく `tin[4] == 3`。区間和を取得する場合は `seg.prod(tin[v], tout[v])` とする。元の `library_checker/euler_tour.py` の具体例とセグメント木での更新方法は [`euler_tour.py`](euler_tour.py) の冒頭にも残している。
