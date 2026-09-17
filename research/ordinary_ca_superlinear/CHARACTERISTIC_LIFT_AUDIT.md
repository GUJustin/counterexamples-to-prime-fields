# Exact characteristic dependence of the quadratic ordinary-CA source

September 17, 2026. Algebraic feasibility audit; no new census and no
claim that every moving-node lift is impossible.

## Which part of the strongest construction is characteristic-specific?

The current n^2/192 ordinary-CA construction over F_(p^2) starts with the
TRUE nearest list extracted in PROOF.md: N=4r, dimension r, at least r
nearest polynomials, maximum m>=3r/2. It then performs common-zero padding,
one anchor, nonzero random directions, and label-union amplification.
The indispensable characteristic-specific input occurs BEFORE all of
these operations: the full-field Dickson lower bound and its orbit
descent. The later operations do not manufacture the nearest source.

For p=4k+1 with p=1 mod8, set e=(p+1)/2=2k+1 and

    G_a(X)=sum_j binom(e,2j+1) a^(e-2j-1)X^j,
    H_a(X)=G_a(X)-X^k.

For s^2=x, the polynomial identity

    G_a(x)=((a+s)^e-(a-s)^e)/(2s)                 (1)

holds over characteristic zero as well. Also deg H_a<k holds identically:
the leading coefficient of G_a is1. Thus neither the binomial formula
nor degree cancellation is itself the missing lift.

The agreement count uses the following additional identities.

* If x is nonsquare in F_p, then s^p=-s and a^p=a. Hence

      ((a+s)^e)^2=(a+s)^(p+1)
                  =(a+s)(a^p+s^p)=a^2-x,       (2)
      (a-s)^e=((a+s)^e)^p.

  These make G_a(x)=0 equivalent to chi(a^2-x)=1 and reduce the other
  possible values to a quadratic relation. The exact n/4 nonsquare
  agreement count then follows from a prime-field character sum.

* If x=s^2 is square with s in F_p, Euler's criterion gives

      (a+s)^e=(a+s) chi(a+s),
      (a-s)^e=(a-s) chi(a-s).                    (3)

  This converts agreement to the two simultaneous quadratic-character
  conditions and gives n/8 square agreements.

The Frobenius equality in (2) is precisely where binomial mixed terms
vanish modulo p. Over characteristic zero,

    (a+s)^(p+1)-(a^2-s^2)

is a nonzero polynomial (its leading s^(p+1) coefficient is1), not an
identity. Likewise, (3) for nonzero a+s forces (a+s)^(p-1)=1. The full
finite-field argument requires those torsion conditions after MANY
additive translates a+s, not merely x^(p-1)=1 for the original nodes.
Replacing the multiplicative domain by roots of unity therefore preserves
the word W_k and its multiplicative symmetry but does not preserve the
additive/Frobenius agreement calculation. The exact count3k/2 has no
characteristic-zero proof supplied by these formulas.

This identifies the actual missing identity. It is stronger and more
specific than observing that the final label field is an extension.

## Orbit descent does not repair the missing identity

The nearest source has P(X)=V(X^d), d=k/r, and domain mu_(4r). Its
nearest maximum and r-member orbit follow from the full-field maximum
M=d*m and its stabilizer. The cyclic received word W_r has a perfectly
valid characteristic-zero definition. But the particular V and its
agreement supports are obtained by solving interpolation constraints
modulo the original p; their consistency need not lift.

For a fixed descended support pattern on roots of unity, record the
augmented Vandermonde determinants asserting that W_r restricts to a
degree-below-r polynomial on each support. These determinants are
algebraic integers in Q(zeta_(4r)). The native construction says they
vanish modulo a prime above p. A characteristic-zero lift of that same
word/support pattern requires that they vanish AS ALGEBRAIC NUMBERS.
Divisibility of a nonzero norm by p does not imply such vanishing.
If one instead allows a new received word, use the corresponding
homogeneous interpolation-constraint matrix and its maximal minors.
The same distinction applies.

Existing exact audits make this failure concrete, without proving a
universal descended-source obstruction:

* Natural cyclotomic lifts of the full seed patterns at p0=17,41,97,193
  have only global-codeword received words in characteristic zero.
* Both full seed orbits are likewise excluded in the checked p0>=41
  cases through337.
* For the full n=16 support pattern, the integral determinant certificate
  has norm factorization supported on2 and17; characteristic17 is the
  ONLY possible characteristic for a nontrivial realization on that
  natural cyclic domain.

These statements are certified in dickson_fixed_gap/
CYCLOTOMIC_LIFT_AUDIT.md and CYCLOTOMIC_EXCEPTION_AUDIT.md. They do not
classify the unknown varying descended orbit patterns for all r, nor
moving-node lifts or selected sublists.

## Can lifting the remaining operations work?

Yes, conditional on a characteristic-zero nearest source. Once a finite
source with a true nearest boundary and distinct candidates is defined
over a number field, agreement/nonagreement, interpolation rank, and
candidate distinctness are finite polynomial equalities and inequalities.
A reduction outside finitely many bad primes preserves them. At a
completely splitting prime the entire finite configuration, including
any algebraic padding data, reduces into the PRIME field. Candidate
and label collisions are avoided by excluding the norms of their
nonzero differences. Thus collisions are not a fundamental obstruction
to an actual algebraic source lift.

The existing CYCLOTOMIC_PRIME_TRANSFER.md gives the precise positive
transfer theorem for cyclotomic sources, including a fixed rate/gap,
ordinary-CA exclusion, and Omega(NL) labels. Its hypothesis is exactly
what is missing: fixed positive nearest margin and L tending to infinity
in characteristic zero. Padding and random directions cannot replace it.

## What can and cannot be concluded about p versus output length

The original full-field Dickson step has p=4k+1. But AFTER orbit descent,
the source length is4r with r dividing k, and the final length isTheta(r).
Only p>=4r+1 is known. It would be WRONG to infer p=O(n) for the strongest
ordinary-CA construction: its own proof explicitly leaves p/r uncontrolled.
This audit proves reliance on modulo-p cancellation, not a linear upper
bound on characteristic in terms of the descended length.

For a fixed cyclic pattern that fails in characteristic zero, only
finitely many new characteristics can realize it, since a nonzero
algebraic minor has finitely many prime norm divisors. That finiteness
is not uniform in r and does not force p=O(r). For example, an augmented
(r+1)-row Vandermonde minor with final W_r column has each complex
conjugate bounded by 2(r+1)^((r+1)/2); its norm can be exponential in
O(r^2 log r). Even this elementary bound permits primes vastly larger
than the domain. It supplies no useful asymptotic prime-size obstruction.

## Verdict and exact open alternative

A literal characteristic-zero lift of the Dickson counting argument
fails at (2) and (3). Tested natural support lifts are genuinely
inconsistent, not merely subject to accidental label collisions.
There is nevertheless no proof here excluding all algebraic lifts of
all descended nearest sources. A new moving-node or new-support source
could transfer, and a family of exceptional characteristics much larger
than the descended domain is also not ruled out.

The concrete next requirement is an explicit sequence of descended
nearest supports whose characteristic-zero interpolation minors vanish,
or a proof that their realizing exceptional primes grow fast enough
relative to r to run a same-prime compiler. Neither follows from the
current orbit argument. Reusing the binomial formulas or taking a larger
splitting prime without such a source certificate does not preserve the
fixed-gap nearest bank.
