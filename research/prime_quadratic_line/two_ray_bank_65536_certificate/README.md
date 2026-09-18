# An exact finite two-ray RS certificate

September 18, 2026. **PASS.** This is an explicit instance of the finite
square/constant-bank lemma in `../square_linear_block_bank.tex`. Its gap
and agreement statements follow from the finite lemma with the recorded
parameters; there is no gap override or unverified asymptotic-onset premise.

| Parameter | Exact value |
| --- | ---: |
| Field | F_131071 |
| Ordinary RS dimension | 3, i.e. degree at most 2 |
| Length | 65536 |
| Bank size parameter t | 16 |
| Fresh block size D | 330 |
| Both endpoint maximum agreements | 330 |
| Common agreement | 330 |
| Nearby agreement threshold T | 362 |
| Labels with singleton threshold lists | 257 |

The domain is the explicit selected subset of the prime field described
below. The dimension and domain are part of the certificate.

Run `python verify.py` with Python 3.10 or later, without `-O`. The verifier
uses only the standard library and takes approximately half a second on
the research workstation. It reconstructs every artifact in this folder.

## Exact field and finite-lemma checks

Primality is proved by trial division by all 72 primes through 362.
The verifier factors

```
131070 = 2*3*5*17*257
```

and proves that `g=3` is primitive by checking its powers for every prime
factor. In the displayed factor order, the results are

```
g^((p-1)/ell) mod p = 131070, 109165, 119782, 32768, 120519.
```

None is 1. These are exact certificates, not probable-prime or random
generator tests.

All finite-lemma hypotheses hold:

```
D=330 > 4t+3=67,
t^2=256 < (p-1)/2=65535,
n=65536 >= 2t^2+tD=5792,
p=131071 > n+6t+1=65633.
```

The block size D is a free parameter of this finite lemma. This instance
does not need to specialize D to an asymptotic multiple of t.

## Deterministic domain and words

Put `z=g^2=9`, `a_i=z^i`, and `b_j=z^(16j)` for `0<=i,j<16`.
The bank consists of the pure quadratics `a_i X^2` and the constants
`b_j`. Every bank parameter is a nonzero square.

At the core coordinates

```
x = +g^(16j-i), -g^(16j-i),
```

put `f(x)=b_j` and `v(x)=0`. Exponents are reduced modulo 131070.
All 512 core coordinates are distinct. The verifier evaluates every
member of both bank rays at each core point and checks that its exact
owners are the quadratic indexed by i and the constant indexed by j.
Each bank word has exactly 32 core matches.

For each j in order, take the 330 least positive coordinates not already
in the core or an earlier fresh block. On this block put

```
f(x)=0,  v(x)=x^2/b_j.
```

There are 5280 distinct fresh coordinates. Next take the 59744 least
positive unused coordinates, excluding:

- the 16 coefficients a_i;
- every root of `x^3=b_j` for any j;
- all 32 coefficients `3/b_j` and `27/b_j`.

On these neutral coordinates put `f(x)=x^3` and `v(x)=0`. The verifier
enumerates the field to obtain all 18 cube roots in the second exclusion
set. The union of neutral exclusions, including zero, has size 66.
No domain coordinate is zero, and all 65536 coordinates are distinct.

The native line is `W_lambda=f+lambda*v`. Choose the endpoints

```
F=W_3,  G=W_27.
```

Both endpoint labels are nonsquares. The usual parameter u in
`(1-u)F+uG` corresponds to native `lambda=3+24u`. Every certified nearby
label has its corresponding u recorded and checked to lie outside
`{0,1}`.

## Exact profiles for every label

For a pure quadratic `c X^2`, count its matches on the fixed core and
neutral block. The verifier obtains this count by assigning each fixed
coordinate to its unique coefficient `c=f(x)/x^2`. The exact answer is

```
32 if c is one of the a_i,
 1 if c is a neutral coordinate,
 0 otherwise.
```

For nonzero c, it also matches all 330 coordinates of fresh block j
exactly at native label `lambda=c*b_j`. These 16 labels are distinct.
The zero quadratic matches all 5280 fresh coordinates at label zero
and has no other matches.

The verifier enumerates every field coefficient and all 2097120
nonzero-coefficient/block pairs. The resulting exact maximum-agreement
profile over all 131071 labels is:

| Maximum agreement | Number of labels |
| ---: | ---: |
| 330 | 31 |
| 331 | 130783 |
| 362 | 256 |
| 5280 | 1 |

The 256 labels in the third row are exactly
`a_i*b_j=z^(i+16j)`, equivalently `z^k` for `0<=k<256`.
Their unique threshold witness is `a_i X^2`, with 32 core and 330
fresh agreements. The fourth row is native label zero, whose unique
threshold witness is the zero polynomial.

To exclude every other quadratic, let Q be non-pure. A nonconstant Q
has at most two core matches for each constant b_j; a nonzero constant
has at most one complete 32-point core row. Thus Q has at most 32 core
matches. Its difference from `(lambda/b_j)X^2` is nonzero on each fresh
block, giving at most 32 fresh matches. Its difference from `X^3` has
at most three neutral roots. Therefore

```
agreement(Q,W_lambda) <= 4t+3 = 67 < 330
```

for every label. This proves that the computed pure-quadratic maxima
are the maxima over the entire ordinary RS code. No enumeration of
all `p^3` codewords is claimed.

Consequently exactly 257 labels have a singleton list at threshold 362.
At threshold 330, every nonzero native label has exactly the 16 witnesses
`(lambda/b_j)X^2`, and native zero has only the zero witness.

## Exact endpoints and common agreement

Each endpoint coefficient `3/b_j` or `27/b_j` is nonsquare, so it has
no core matches, and it is excluded from neutral coordinates. Its
agreement set is precisely fresh block j. In addition to the coefficient
table, the verifier directly evaluates all 32 endpoint witnesses on
all 65536 coordinates, totaling 2097152 comparisons. The exact endpoint
maxima are both 330.

For common agreement, normalize the difference between the two explaining
codewords by the endpoint-label difference. This produces a polynomial
q of degree at most two which must agree with v:

- If q is a nonzero pure quadratic, it matches v on at most one fresh
  block and nowhere where v=0, giving at most D=330 matches.
- If q is non-pure and nonzero, it has at most two matches per fresh
  block and at most two zeros elsewhere, giving at most 34 matches.
- If q=0, common matches lie in the core and neutral blocks. The
  intercept has at most `2t+3=35` matches there.

The endpoint witnesses for any fixed j match simultaneously on its
330-point fresh block. Hence common agreement is exactly 330.

## Exact first-order, Johnson, and gap arithmetic

The low-rate first-order bound and the certified strict inequalities give

```
3n < 2*314^2,
3n < 8*13^4,
n*a1(3/n) <= sqrt(3n/2)+(3n/8)^(1/4) < 327 < 330.
```

The threshold is below the degree-two Johnson agreement:

```
T^2 = 362^2 = 131044 < 131072 = 2n.
```

The normalized source loss is `(T-A)/n=32/65536=1/2048`.
The capacity margin at T is `(T-k)/n=359/65536`, so the ratio of source
loss to capacity margin is exactly `32/359`.

## Reproducible artifacts

- `verify.py`: reconstruction and exact checks.
- `recipe.json`: coefficients, endpoint witnesses, exclusions, ordering,
  binary formats, and deterministic domain recipe.
- `domain.bin`: 65536 little-endian uint32 triples `(x,f(x),v(x))`;
  exactly 786432 bytes.
- `agreement_profile.bin`: one little-endian uint16 maximum-agreement
  value for every native label, in order; exactly 262142 bytes.
- `singleton_labels.json`: all 257 labels, witnesses, exact agreements,
  and parameters relative to the chosen endpoints.
- `receipt.json`: exact counts, field certificates, inequalities, and
  SHA256 hashes of the complete domain and its three constituent blocks.

The complete-domain SHA256 is
`10b6a2fc334de9fb741b2395bd0f65331fc94fdfda3a6c52eca8acc2e21a0e82`.
The complete agreement-profile SHA256 is
`480f7ffafbeb70c88ef36e82f0aa0372cdf2bc3b9729c0e1aeb0f9261ef24866`.
