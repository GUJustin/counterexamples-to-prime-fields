# Quotient heads with assigned kernel values and small rational denominators

2026-09-19. Exact CRT representatives, agreement bounds, and scoped
intersection tests. No finite scan or new counterexample is claimed.

Use the setup of [SEXTIC_TRACE_HEAD_PULLBACK_GATE.md](SEXTIC_TRACE_HEAD_PULLBACK_GATE.md):
`ell >= 23` is prime, all `E[ell]` is rational over `Fp`,

    D = x(E[ell] \ {O}),       n = (ell^2-1)/2,
    k = n-4ell+1,             t = (ell-1)/2,
    T_d = n-2ell-d,           d in {5,6}.

The code is `RS_k(D)`, with degree strictly below `k`, over any coefficient
field extending `Fp`. For each order-`ell` subgroup write

    Phi = K_H M_H,
    Y_H = N_H / K_H^2,
    deg K_H = t,  deg N_H = ell,  deg M_H = n-t.

The factors `K_H,M_H` are squarefree and coprime, and
`gcd(N_H,K_H)=1`. The normalized map satisfies `Y_H=X+O(X^-1)`.
For different subgroups their kernel x-sets are disjoint.

## 1. Exact polynomial representatives of the assigned words

Let `I_H` be the word equal to one on the kernel x-set and zero elsewhere.
Let `Yhat_H` equal the rational value `Y_H(x)` off the kernel and zero on
the kernel. Their unique interpolation polynomials of degree below `n`
are

    I_H    = M_H * (M_H^(-1) mod K_H),
    Yhat_H = K_H * (N_H K_H^(-3) mod M_H).                  (1)

All inverses here are in the indicated polynomial quotient ring. Indeed,
the first expression is one modulo `K_H` and zero modulo `M_H`; the
second is zero modulo `K_H` and `N_H/K_H^2` modulo `M_H`.
Both displayed representatives have degree at most `n-1`.

More generally, let `S_H` be the full `t`-dimensional space of words
supported on the kernel x-set. If a polynomial `r` of degree below `t`
specifies arbitrary values there, its representative is

    M_H * (M_H^(-1) r mod K_H).                            (2)

Thus prescribing different values at every kernel point is included,
not only prescribing one uniform value. In the quotient by the RS code,
define

    W_H = span([Yhat_H]) + [S_H].                          (3)

Any unweighted affine quotient head `alpha Y_H+beta`, with arbitrary
assigned kernel values, has a class in `W_H`: its global constant `beta`
is a codeword, and the remaining discrepancy is supported on the kernel.
In particular zero-extending both heads `Y_H,1` gives
`span([Yhat_H],[I_H])`, since the second head is `1-I_H`.

## 2. Exact threshold profile of this space

**Proposition.** For `v=alpha Yhat_H+u`, with `u in S_H`:

* If `alpha != 0`, then

      agr(v,RS_k) <= k+ell-2+t = n-(5ell+3)/2 < T_d.       (4)

* If `alpha=0`, its exact nearest agreement is

      agr(u,RS_k) = n-wt(u),

  and the zero polynomial is its unique witness at threshold `T_d`.

These statements are unchanged by adding a codeword, with the witnesses
translated by that codeword.

**Proof.** Off the kernel, agreement of `alpha Yhat_H+u` with a polynomial
`q` of degree below `k` requires

    alpha N_H - q K_H^2 = 0.

For `alpha != 0` this polynomial cannot vanish identically, because
`N_H` is coprime to `K_H`. Its degree is at most `k+ell-2`; this dominates
`ell` in the present parameter range. At most `t` additional agreements
are possible at the kernel. This proves the first bound. Its strict
distance from the tested threshold is

    T_d - (k+ell-2+t) = (ell+3)/2-d > 0.

For a kernel-supported word the zero polynomial matches exactly
`n-wt(u) >= n-t` coordinates. Any nonzero codeword has at most `k-1`
zeros off the kernel and at most `t` matches on it, so its agreement is
at most `k-1+t`. Both

    k-1+t < T_d <= n-t

hold here. This proves the second assertion, including uniqueness.

Consequently the high-agreement locus in (3) consists exactly of its
kernel-supported subspace. A genuine affine source line in `W_H` which
is not entirely contained in that subspace can meet it in at most one
parameter. Arbitrary kernel prescriptions therefore do not produce the
desired bank from these unweighted heads even for one subgroup.

## 3. Distinct subgroups give disjoint syndrome spaces

**Proposition.** Each `W_H` has dimension `t+1`, and

    W_H intersect W_H' = {0}              for H != H'.      (5)

**Proof.** Dimension follows from Section 2: no nonzero element of
`span(Yhat_H)+S_H` is a codeword.

For the intersection, suppose

    alpha Yhat_H + u - alpha' Yhat_H' - u' = q  on D,
    u in S_H,  u' in S_H',  deg q < k.

Off the two kernel sets, of total size `2t`, this implies

    alpha Y_H - alpha' Y_H' = q.

Clear the denominator `K_H^2 K_H'^2`. The resulting numerator has degree
at most

    max(2ell-1, k-1+4t) = n-2ell-2.

It has `n-2t=n-ell+1` roots, strictly more than that degree, so the equality
is an identity of rational functions. The `H` term has genuine double
poles at its kernel coordinates if `alpha != 0`; the other map and `q`
are regular there. Therefore `alpha=0`, and similarly `alpha'=0`.

Now `q=u-u'` is supported on at most `2t` coordinates. The RS minimum
distance is `n-k+1=4ell > 2t`, hence `q=0`. The two kernel supports are
disjoint, so also `u=u'=0`. This proves (5).

This is disjointness of the entire assigned-kernel syndrome spaces,
not merely a failure of one source normalization. It does not concern
received functions with additional nonconstant weights.

## 4. A common denominator shifts the polynomial degree gate

Now consider a different regularization. Let `S` be a polynomial of
degree `r`, nonzero at every point of `D`. For each subgroup let
`C_H` be a polynomial divisible by `K_H^2`, and put

    F_H = C_H Y_H,       G_H = C_H,
    deg F_H = L_H,       deg G_H = L_H-1.

All values of `F_H/S,G_H/S`, including their kernel values, are the actual
values of these fractions; there are no separate kernel assignments.
Normalize the polynomials to be monic without changing their syndrome
planes. Suppose

    k+r+4 <= L_H < n,      k+r+4 <= L_H' < n.               (6)

Then for `H != H'` the planes

    span([F_H/S],[G_H/S]) and span([F_H'/S],[G_H'/S])         (7)

are different and each is two-dimensional.

To see this, multiply a putative equality by `S`. The relevant code
subspace becomes `S*RS_k`, whose polynomials have degree below `k+r`.
All polynomials being compared have degree below `n`, by (6), so
evaluation introduces no multiple of `Phi`. The same degree flag as in
the polynomial-weight lemma forces a common `L` and

    G_H' = G_H + S Q,
    F_H' = F_H + a G_H + S P,       deg P,deg Q < k.

The zero constant term of both normalized `Y` maps forces `a=0`, and

    Y_H'-Y_H = O(X^(k+r-L+1)) = O(X^-3).

The Laurent-coefficient lemma in the preceding note forces `H=H'`, a
contradiction. Notice that no claim that `S*RS_k=RS_(k+r)` is used; only
the degree bound on this subspace is needed.

At a target threshold `T`, a word with nonzero syndrome class, minus a
codeword, has a nonzero numerator of degree at most `max(L_H,k+r-1)`.
Thus if `T>k+r-1`, existence of a target witness for such a class forces
`L_H>=T`.
In particular, at `T=T_d`, the sufficient denominator bound

    r <= T_d-k-4 = 2ell-d-5                              (8)

puts every such plane capable of supplying a target witness into (6),
provided its numerator degrees are below `n`. This excludes the common
source-plane identification for that entire range of common denominators.
For `ell=23`, (8) permits degrees through 36 for `d=5`, and through 35
for `d=6`; this arithmetic is not a new finite construction.

## 5. Different denominators and the exact remaining scope

The denominators need not originally be equal. Call them `S,S'`, with
degrees `r_H,r_H'` and numerator degrees `L_H,L_H'`. Clear the product
`S S'`. The preceding argument applies under the explicit conditions

    L_H >= k+r_H+4,       L_H' >= k+r_H'+4,
    L_H+r_H' < n,         L_H'+r_H < n.                    (9)

Indeed the cleared numerator degrees are `L_H+r_H'` and `L_H'+r_H`,
both at least `k+r_H+r_H'+4`, while the multiplied code has degree below
`k+r_H+r_H'`. Their common degree flag and the Laurent argument are
therefore valid. Conditions (9) themselves ensure that the multiplied
code also has degree below `n`.

If both planes are to contain target words at `T_d`, it suffices that
each denominator separately obey (8), together with the two strict
cross-multiplied degree bounds in (9). A small bound on the sum of the
denominator degrees is sufficient but is not needed for this argument.

The results above cover unweighted quotient heads with arbitrary kernel
prescriptions, and polynomial pole-clearing weights divided by controlled
denominators nonzero on the domain. They do not cover additional kernel
corrections on the latter weighted heads, denominators vanishing on the
domain with newly assigned values, or cross-multiplied degrees reaching
`n`, where reduction modulo `Phi` can matter. Nor do they classify general
moving sextic residual cofactors. A constructive continuation needs an
explicit identity outside these hypotheses; the two quotient trace heads
alone do not supply it.
