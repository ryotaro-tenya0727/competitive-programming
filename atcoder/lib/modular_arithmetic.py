# 割る数 value（分母 B）の、mod（法 P）における逆元を返す。
# A / B (mod P) を求めるなら value に入れるのは B。戻り値は商ではなく B の逆元。
# 例: A, B, P = 120, 12, 13
#     inverse_b = modular_inverse(B, P)  # 12（12 * 12 % 13 == 1）
#     answer = A * inverse_b % P          # 10（5C2 mod 13）
# gcd(value, mod) == 1 のときだけ逆元が存在し、そうでなければ ValueError。
def modular_inverse(value: int, mod: int) -> int:
    return pow(value, -1, mod)


# 1 から size までの逆元を O(size) でまとめて計算する。
# mod は素数、size < mod を前提とする。
# 個別に pow(i, -1, mod) を size 回呼ぶ方法は O(size log mod)。
# inverses[0] は逆元がないため 0 のままにする。
def inverse_table(size: int, mod: int) -> list[int]:
    if size < 0:
        raise ValueError("size must be non-negative")
    if size >= mod:
        raise ValueError("size must be smaller than mod")

    inverses = [0] * (size + 1)
    if size:
        inverses[1] = 1
    for value in range(2, size + 1):
        inverses[value] = mod - (mod // value) * inverses[mod % value] % mod
    return inverses
