# Explicit prime-field certificate: p65537, n2842, rate1/2

The first deterministic sample passes. The field is F65537, the evaluation
domain has2842 explicitly listed points, and witnesses have degree at most1420.
The two source words have exact individual and common agreement1422.
Every one of the65536 nonzero pencil labels has an admissible witness with
1424 matches. Both endpoints on the interpolation line are far, giving
65535 nearby interpolation parameters out of65537.

This is a finite construction on a selected union of quadratic fibers.
It is not the prescribed practical NTT-domain certificate, and its
capacity margin is3/2842. The individual nearby witnesses are proved to
exist by an exact representation count; they have not been enumerated.

## Explicit data

Set p=65537, M=p-1=65536, m=2, b=3 and a0=1. The integer3 is primitive
because 3^32768=-1 mod65537 and M is a power of two. Let H be the subgroup
of quadratic residues. In particular b is outside H.

`tags_and_domain.json` contains all1420 sampled tags G, their factor logs
log_3(3-a), and the complete domain

    D={x in F65537*: x^2 in G union {1}}, |D|=2842.

The sample is fully specified: Python Random(20260918), sampling1420
entries without replacement from the increasing list H\{1}, then sorted.
The saved data are the construction; reproducibility does not depend on
rerunning that pseudorandom generator. The exact exponential-series bounds
also certify1420=ceil(128 log65537).

## Exact character-bias certificate

Let A be the0/1 indicator on Z/65536 of the saved factor logs. Thus
for each multiplicative character chi of F65537*,

    Ahat(chi)=sum_{a in G} chi(3-a).

Compute the cyclic triple convolution c3=A*A*A. A priori every coefficient
is at most1420^2=2016400: after selecting the first two factors, their sum
and the target determine at most one third factor. This is smaller than
998244353. Consequently cubing the indicator polynomial modulo998244353
and folding degrees modulo65536 recovers every integer c3 coefficient
exactly. This is not an approximate Fourier computation.

The saved coefficient vector has

    sum c3=2863288000=1420^3,
    max c3=45723,
    E3:=sum c3^2=125113995212860.

Parseval gives the exact identity

    sum_{chi!=1} |Ahat(chi)|^6
      =65536*E3-1420^6
      =1052619325992960
      <128100283921000000=710^6.

Every summand on the left is nonnegative, so every nontrivial character
has |Ahat(chi)|<710=s/2. Ordered triples in the moment calculation may
repeat factors; this does not assert anything about distinct subsets.
Distinctness is imposed in the next generating-function step.

## Exact product-coverage certificate

For r712 and s1420, theta=r/s=178/355. The fixed-cardinality Cauchy bound
and character orthogonality show that every c in F65537* has a
representation by an r-subset of G if

    65535*1421*exp[-theta(1-theta)*710]<1.

The exponent is exactly u=63012/355, and the prefactor is93125235.
Positivity needs no floating-point calculation: the rational inequality

    exp(u)>u^5/120>93125235

is checked in `build_fixture.py`. The certified total Fourier-error upper
bound is

    875100428675898359375/13796973344392650723456 < 1.

Thus every nonzero field element is a product of exactly712 distinct
factors3-a with a in the saved G. This conclusion holds for all65536
products, without enumerating subsets.

## Words, degree bounds, and exact sources

Write Y=X^2. On the saved domain define

    f(X)=(Y^712-3^712)/(Y-3),
    g(X)=-1/(Y-3).

The denominator has no root in F65537, and f is a monic polynomial of
degree1422. Let J1421 denote the strict degree bound. Root counting
therefore gives agr_J(f)<=1422. For g and any degree<=1420 witness h,
the agreement polynomial1+(X^2-3)h is nonzero of degree at most1422,
so agr_J(g)<=1422 as well.

The same1422 coordinates attain both upper bounds. Choose any711 tags
T from G and put V_T(Y)=prod_{a in T}(Y-a). Explicit witnesses are

    h_f(X)=(Y^712-3^712)/(Y-3)-V_T(Y),
    h_g(X)=[V_T(Y)/V_T(3)-1]/(Y-3).

Both are polynomials of degree at most1420 in X. The leading terms
cancel for h_f; the numerator vanishes at Y=3 for h_g. Both match on
exactly the711 selected quadratic fibers. Hence

    agr_J(f)=agr_J(g)=CA_J(f,g)=1422.

For any lambda!=0, product coverage provides a712-subset S of G with
V_S(3)=-lambda. Define P_S(Y)=Y^712-V_S(Y) and

    h_S(X)=[P_S(Y)-P_S(3)]/(Y-3).

This is a polynomial of degree at most1420, and

    f+lambda*g-h_S=V_S(Y)/(Y-3).

It vanishes at exactly1424 points of D. Thus every nonzero pencil label
is nearby at threshold1424, while lambda0 and the projective direction g
are far. Equivalently, (1-t)f+t*g is nearby for all t except0 and1.

## Files and reproduction

- `build_fixture.py`: deterministic construction, FLINT convolution, and
  exact rational checks.
- `run_bounded.py`: owned-process58-second/512-MiB watchdog.
- `tags_and_domain.json`: explicit tag, exponent, and domain lists.
- `cyclic_triple_convolution_u32le.bin`:65536 little-endian unsigned32-bit
  convolution coefficients.
- `receipt.json`: exact integer results and SHA-256 digests.
- `resources.json`: observed runtime and watchdog receipt.

Run with `/Users/jthaler/.local/share/research-toolchain/venv/bin/python`.
The first build took about0.087seconds and peaked at51658752bytes. One
sample was used. An independent NTT replay is owned by the separate audit
agent; its files are recorded separately.
