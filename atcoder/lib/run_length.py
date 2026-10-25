from itertools import groupby
from typing import Iterable, TypeVar


T = TypeVar("T")


# 文字列や数列の連続する同じ値を (値, 個数) に圧縮する。
# 例: run_length_encode("aaabb") == [("a", 3), ("b", 2)]。
# 離れた位置の同じ値はまとめない。
def run_length_encode(values: Iterable[T]) -> list[tuple[T, int]]:
    return [(value, len(list(group))) for value, group in groupby(values)]
