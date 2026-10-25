import sys
from collections.abc import Iterable
from typing import TextIO


# 各行の値を空白で、行同士を改行で結んで一度に出力する。
# 元の sys.stdout.write("\n".join(" ".join(map(str, row)) for row in rows) + "\n")
# に対応する。rows は二次元の反復可能オブジェクト。空なら何も出力しない。
def write_rows(rows: Iterable[Iterable[object]], stream: TextIO | None = None) -> None:
    if stream is None:
        stream = sys.stdout
    lines = [" ".join(map(str, row)) for row in rows]
    if lines:
        stream.write("\n".join(lines) + "\n")
