N, M = imap()

ans = []


def f(m, k, ar):
    if m // 10 == 0:
        ar.append(m)
        ans.append(tuple(ar))
        return

    for v in (m, 10 * (k - 9), -1):
        ar.append(v)
        f(v - 10, k - 1, ar)
        ar.pop()


f(M, N, [])

print(ans)

N, Q = imap()
P = ilist()
a = [int(input()) for i in range(Q)]

sta = set(a)
br = [v for v in P if not v in sta]

stbk = set()
ansbk = []
for v in reversed(a):
    if v in stbk:
        continue
    else:
        ansbk.append(v)
        stbk.add(v)

print(*(br + list(reversed(ansbk))))
