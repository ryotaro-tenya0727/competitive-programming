MOD = 998244353


# 素数 mod の下で二項係数 nCr を計算する。元の code_lib.py と同じ方式。
# 使い方（N は求めたい n の最大値）:
#     N, K = 5, 2
#     comb = Comb(N)             # mod の省略時は 998244353
#     print(comb.ncr(N, K))     # 10
#     comb13 = Comb(N, 13)      # mod を指定する場合
#     print(comb13.ncr(N, K))   # 10
# fact[i] = i! % mod。初期化 O(N)、ncr 1 回 O(log mod)、メモリ O(N)。
# mod が素数で、0 <= n <= N < mod を前提とする。
class Comb:
    # 0! から n! までを mod で割った余りを前計算する。
    def __init__(self, n: int, mod: int = MOD) -> None:
        self.mod = mod
        self.fact = [1] * (n + 1)

        for i in range(1, n + 1):
            self.fact[i] = self.fact[i - 1] * i % mod

    # nCr = n! / (r! * (n-r)!) を mod で割った余りを返す。
    # 分母の逆元を毎回 pow で求めて掛ける。範囲外の r は 0 を返す。
    def ncr(self, n: int, r: int) -> int:
        if n < 0 or r < 0 or r > n:
            return 0

        denominator = self.fact[r] * self.fact[n - r] % self.mod
        inverse = pow(denominator, self.mod - 2, self.mod)
        return self.fact[n] * inverse % self.mod


# 整理後の名前 Combination でも import できるようにする。
Combination = Comb
