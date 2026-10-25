from collections.abc import Iterator, Sequence
from typing import TypeVar


T = TypeVar("T")


# 空でない連続部分列を長さ順、同じ長さでは左から順に列挙する。
# 元の二重ループ values[start:start + length] に対応する。
# 要素数 N のとき列挙する部分列は N(N+1)/2 個。
def contiguous_slices(values: Sequence[T]) -> Iterator[Sequence[T]]:
    for length in range(1, len(values) + 1):
        for start in range(len(values) - length + 1):
            yield values[start : start + length]
