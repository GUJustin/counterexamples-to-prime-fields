"""Elementary finite-field polynomial arithmetic used by the exact checks."""

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


def eval_poly(a, x, p):
    ans = 0
    for c in reversed(a):
        ans = (ans*x+c) % p
    return ans


def divmod_poly(a, b, p):
    a = trim(a[:])
    q = [0]*max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        k = len(a)-len(b)
        c = a[-1]*pow(b[-1], -1, p) % p
        q[k] = c
        for i, v in enumerate(b):
            a[k+i] = (a[k+i]-c*v) % p
        trim(a)
    return trim(q), a


def gcd_poly(a, b, p):
    while b != [0]:
        a, b = b, divmod_poly(a, b, p)[1]
    return scale(a, pow(a[-1], -1, p), p)


def degree_at_most_on_support(xs,ys,D,p):
    # Full Newton divided differences; coefficient j is degree-j term.
    coefficients=ys[:]
    for j in range(1,len(xs)):
        for i in range(len(xs)-1,j-1,-1):
            coefficients[i]=(coefficients[i]-coefficients[i-1])*pow(xs[i]-xs[i-j],-1,p)%p
    return all(c==0 for c in coefficients[D+1:])
