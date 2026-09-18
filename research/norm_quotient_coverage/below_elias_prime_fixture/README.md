# Explicit length-48 prime-field certificate

This certificate uses F65537, an explicitly listed 48-point domain, and
the strict degree bound J=24. Both source words have exact individual and
common agreement 25. Every nonzero pencil label has exact agreement 27.
The radius is 21/48=7/16, and the integer certificate below proves
H_65537(7/16)<1/2. No probabilistic or character-sum estimate is needed
for this finite instance.

## Explicit tags, domain, and source words

Set p=65537, b=3 and m=2. The element 3 is primitive and is a nonsquare.
The 23 tags, in the saved support-mask order, are

    25703, 16562, 45729, 40011, 19330, 14018, 39598, 39860,
    36881, 40752, 56378, 11224, 11940, 40844, 22047, 23180,
    33705, 65375, 48969, 314, 27487, 55681, 29802.

They are distinct quadratic residues, none equal to 1. Call this set G.
Define

    D={x in F65537*: x^2 in G union {1}},
    Y=X^2, R=X-1,
    f(X)=R*(Y^13-3^13)/(Y-3),
    g(X)=-R/(Y-3).

The domain consists of 24 quadratic fibers and has exactly 48 points.
The denominator never vanishes over F65537. The reserved fiber is
{1,-1}, and the one-point core is {1}. The full domain, the values of
f and g, the polynomial coefficients of f, and two common witnesses are
saved in `tags_domain_words.json`.

## Complete product coverage, checked in three ways

Every nonzero field element occurs as

    product_{a in S}(3-a),  S subset G, |S|=13.

The verifier establishes this with three exact checks:

1. A Boolean cyclic dynamic program on the base-3 logarithms marks all
   65536 residues as attainable by 13 distinct indices. Updates descend
   in cardinality, so an index is never reused.
2. An independent meet-in-the-middle calculation enumerates all
   C(23,13)=1144066 subsets using two half tables. All 65536 products
   occur; their multiplicities range from 3 to 36.
3. One support mask per product is saved, and all 65536 masks are checked
   directly by multiplying their 13 factors in F65537.

`product_counts_u32le.bin` contains the exact multiplicities.
`witness_supports_u32le.bin` contains one 23-bit support mask per product.
Both have 65536 little-endian unsigned 32-bit entries. Entry t corresponds
to the product 3^t and hence to the pencil label lambda=-3^t. Bit i of a
support mask selects the i-th tag in the displayed order. These files give
a concrete witness bank for every nonzero label, not only an existence
claim.

The canonical set was found by the root agent's first sample with seed
2026091823. The verifier does not resample. Root also independently
enumerated all subsets by field multiplication without logarithms; its
reported multiplicities agree with the meet-in-the-middle result here.

## Exact degree and agreement proof

The word f is monic of degree 25, so any degree-at-most-23 polynomial
matches it at at most 25 coordinates. For g the agreement equation with
such a witness h is

    R+(X^2-3)h=0.

This is a nonzero polynomial of degree at most 25: deg R=1 is below
the denominator degree 2. Thus the same upper bound applies to g.

Take any 12 tags T from G, and write V_T(Y)=product_{a in T}(Y-a).
The polynomials

    h_f=R*[(Y^13-3^13)/(Y-3)-V_T(Y)],
    h_g=R*[V_T(Y)/V_T(3)-1]/(Y-3)

have degree at most 23 in X. They match the two sources on the same
25 points: the 12 selected fibers and the core point 1. The verifier
constructs their coefficients and checks their values on all 48 domain
points. Consequently

    agr_24(f)=agr_24(g)=CA_24(f,g)=25.

For lambda!=0, choose its saved 13-tag support S with V_S(3)=-lambda.
Put P_S(Y)=Y^13-V_S(Y). Then

    h_S=R*[P_S(Y)-P_S(3)]/(Y-3)

is a polynomial of degree at most 23, and

    f+lambda*g-h_S=R*V_S(Y)/(Y-3).

It matches on exactly 27 points: 13 quadratic fibers and the core point.
For any admissible witness h, clearing the denominator gives

    R*(Y^13-3^13)-(Y-3)h-lambda*R,

a monic polynomial of degree 27. Hence no witness can match at more
than 27 points, proving exact agreement 27 at every nonzero pencil label.
The lambda=0 source and projective direction g remain at agreement 25.

There are 65536 nearby nonzero pencil labels. On the affine interpolation
line (1-t)f+t*g, exactly the 65535 parameters outside {0,1} are nearby;
both endpoints are far. The source-to-near distance gap is 1/24 and the
capacity margin is 1/16.

## Exact entropy certificate

The q-ary entropy comparison H_65537(7/16)<1/2 is equivalent to

    (65537-1)^7 * 16^16 < 65537^8 * 7^7 * 9^9.

The two integer sides are

    95780971304118053647396689196894323976171195136475136
    108582871902291753903353686974292588554886020758912367,

respectively. Their positive difference is recorded in `receipt.json`.
This certifies the strict entropy comparison without floating-point logs.

## Reproduction and scope

Run `verify_fixture.py` with Python 3.10 or later; it uses only the
standard library. The tested interpreter is
`/Users/jthaler/.local/share/research-toolchain/venv/bin/python`.
`run_bounded.py` enforces an owned-process 58-second/512-MiB watchdog.
The completed verification took about 0.325 seconds and peaked at
31883264 bytes. `receipt.json` includes SHA-256 digests of the saved data.

This is a finite prime-alphabet example on the displayed union of fibers.
It does not use the field or prescribed NTT domain of the better.codes
benchmark. The original length-2842 and length-386 certificates remain
unchanged in their separate directories.

Embedding these same words and domain into an extension field creates
no additional nearby labels: every label outside F65537 has exact
agreement 25. The general scalar-extension proof and exact label counts
are in `../SCALAR_EXTENSION_AGREEMENT_IDENTITY.md`.
