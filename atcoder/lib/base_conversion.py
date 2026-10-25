# 非負整数を指定基数の下位桁から順に返す。
# 例: 13 は 2 進数で 1101 なので digits_in_base(13, 2) は [1, 0, 1, 1]。
# 回文判定ではこの並びと逆順を比較できる。0 は [0] を返す。
def digits_in_base(number: int, base: int) -> list[int]:
    if base < 2:
        raise ValueError("base must be at least 2")
    if number < 0:
        raise ValueError("number must be non-negative")
    if number == 0:
        return [0]

    digits = []
    while number:
        digits.append(number % base)
        number //= base
    return digits
