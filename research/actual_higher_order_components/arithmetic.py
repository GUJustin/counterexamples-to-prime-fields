"""Small exact prime-field polynomial operations for the finite checks."""
def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p, sign=1):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += sign * x
    return trim([x % p for x in c])


def mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % p
    return trim(c)


def deriv(a, p):
    return trim([i*a[i] % p for i in range(1, len(a))] or [0])


def scale(a, c, p):
    return trim([c*x % p for x in a])


def power_linear(a, e, p):
    ans = [1]
    for _ in range(e):
        ans = mul(ans, [-a % p, 1], p)
    return ans


def eval_poly(a, x, p):
    ans = 0
    for c in reversed(a):
        ans = (ans*x+c) % p
    return ans
