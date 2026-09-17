# Independent audit: fourth-power standard-support ledger

September 17, 2026. The proof in STANDARD_SUPPORT_FOURTH_POWER.md was
checked independently against UNIFORM_FINITE_LENGTH_CONVERSE.md and
FINITE_LENGTH_GAP_COSTS.md in first_order_support_audit, and the current
reconstruction formulas recorded in this directory. No mathematical gap
was found. This is not formal verification or independent human review.

The conclusion applies only to the complete coefficient-prefix standard
supports with derivative cap b and total jet cap B, the Eq63 graded row
certificate, and the declared Eq54--56 numerical reconstruction ledgers.
It assumes characteristic zero or larger than every retained total jet
degree. It does not cover Eq64, arbitrary missing small monomials,
nonmonomial spaces, improved actual-degree accounting, or global kernel
dependencies. It establishes no lower bound on actual lists or exceptions.

1. Summing degree contributions by prefixes gives the graded identity
exactly, including H below the largest retained degree. A positive sum
forces a positive prefix, to which the finite-length parameter converse
applies. This gives m>c0/epsilon*, B>m/4, b>=m/8 and H>=floor(m/8).

2. The uniform bound on EVERY prefix is valid, not only positive ones.
Diagonals with Lq<m have nonpositive exact surplus by the half-rank lemma.
Deleting them preserves downward closure and increases surplus. The
remaining exact coefficient counts are bounded by ma*−q/4, with
 a*=(An−8)/(n(n−8)), and their local rank is saturated. All retained
benefits at a* are positive, so q<4ma*<2m and the support has at most
2m²+m<=3m² monomials. At a0, deleting nonpositive-benefit monomials
preserves the applicability of the critical-support converse and can
only increase surplus. Thus every prefix is at most 3 epsilon* m³.
The empty retained-support case also satisfies this bound.

3. For q<=floor(m/8), b and B force all q+1 jet monomials to be present.
A>=D+2 guarantees Lq>=m>q, so all coefficient prefixes are nonempty
and the local rank formula is saturated. The terms with
ell=q,...,m−q−1 each have rank q+1, giving at least
(m−2q)(q+1)>=3m(q+1)/4. The exact benefit is at most ma*(q+1), and
a*<0.47 yields degree surplus <=−m(q+1)/4.

4. Prefix summation yields Pj<=−m(j+1)(j+2)/8. With J=floor(m/8),
the forced negative area exceeds m⁴/12288 because J+1>m/8.
Each positive prefix contributes at most 3 epsilon* m³. Thus positivity
requires H+1>m/(36864 epsilon*), and H>m/(73728 epsilon*).
No moment-preserving compression or optimizer uniqueness is used.

5. For tau=2D−3, u=1+tau(B−1), v=min(u,tau(b−1)+D),
F=Bv+b(u−v), all necessary signs hold: D>=2, 1<=b<=B,
0<=v<=u, tau>=D/2. Hence F>=DBb/4>Dm²/128.
The regular-family joint ledger is at least D²HBb/4 and therefore
strictly greater than D²m³/(9437184 epsilon*), then greater than
D²c0³/(9437184 (epsilon*)⁴). The incidence multiplier is at least one,
so optimizing that multiplier cannot defeat this declared-cost bound.
The list ledger similarly exceeds Dc0²/(128 (epsilon*)²).

The numerical constants and strict/weak inequality transitions were
checked algebraically. The existing finite verifier is corroboration;
the uniform theorem depends on the stated quantified critical-support
and finite-length arguments, not on a finite census.
