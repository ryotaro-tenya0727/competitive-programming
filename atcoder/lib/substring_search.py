from collections.abc import Sequence
from typing import TypeVar


T = TypeVar("T")


# 閉区間 [left, right] 内に連続する pattern があるか返す。
# 元メモの S[j:j + lt] == T を、右端からはみ出さない形にしたもの。
# left と right は 0-indexed、両端を含む。空の pattern は True。
def contains_pattern_in_range(
    values: Sequence[T], pattern: Sequence[T], left: int, right: int
) -> bool:
    if not 0 <= left <= right < len(values):
        raise ValueError("left and right must be within values")
    if not pattern:
        return True
    return any(
        values[start : start + len(pattern)] == pattern
        for start in range(left, right - len(pattern) + 2)
    )
