# Positive projective quotient and quadratic pullback: independent audit

September 18, 2026. **PASS**, for every prime p≥5. This gives a larger length exponent than the uncompressed p^5 construction, while retaining large characteristic and a threshold above first order and below exact Johnson.

## Exact construction

Write S_j=1+p+...+p^(j-1), n=S_5, N=2n. Let B=F_(p^5), F=F_(p^15), and theta in F outside B. Then 1,theta,theta² are B-independent.

The map X→Y=X^(p-1) sends B* onto the subgroup mu_n, with fibers the nonzero F_p-lines. Every source term X^(p^j-1) and every canonical witness alpha X^(p-1)+beta factors through it. The compressed source pair is

    F0(Y)=Y^S4+theta Y^S3+theta² Y^S2,
    G0(Y)=Y^S2.

For odd p, 2n divides p^5-1. Thus D=mu_(2n) is an N-point subgroup of B*, and T→T² maps D onto mu_n exactly two-to-one. Define the final sources

    f(T)=T^(2S4)+theta T^(2S3)+theta²T^(2S2),
    g(T)=T^(2S2).

Use code dimension K=3, i.e. arbitrary degree-at-most-two witnesses over F. The characteristic guard p>2 holds.

For each three-dimensional subspace W≤B, its locator supplies the previously audited nonzero distinct challenge z_W and canonical witness alpha_W X^(p-1)+beta_W. On the new domain use h_W(T)=alpha_W T²+beta_W. Its exact agreement support is the inverse image of the projectivization of W minus zero, so its size is

    A=2S_3=2(p²+p+1).

All labels stay distinct: only the evaluation domain and witness representation changed. Their number is

    M=[5 choose2]_p=n(p²+1)=(N/2)(p²+1).

In particular M>N^(3/2)/4, and M/N^(3/2) tends to 1/(2sqrt(2)). This counts distinct bad challenges, not a list of that size at one word.

## Both sources and common agreement

The direction g has degree 2p+2>2, strictly less than N. Therefore its agreement with any quadratic is at most 2p+2. Projection of f onto the theta² coordinate gives g and preserves the quadratic degree bound, giving the same upper bound for f. Common agreement is bounded by either individual agreement.

For any two-dimensional F_p-subspace U≤B, the old simultaneous strict witnesses obtained by additive remainders have shape alpha X^(p-1)+beta. They descend to linear functions of Y and lift to quadratic functions of T. Their common support has exactly 2S_2=2(p+1) coordinates. Thus

    agr(f)=agr(g)=CA(f,g)=C=2(p+1).

These upper bounds include arbitrary quadratics with a nonzero odd coefficient. They are not restricted to inherited even witnesses.

## Strict threshold comparison

Advertise A0=2p²+p. Then C<A0<A. The exact finite Johnson threshold is sqrt(N(K-1))=sqrt(2N). Direct arithmetic gives

    2N-A0²=3p²+4p+4>0.

Let rho=K/N=3/(2n). This is in the low-rate branch for p≥5. The primary DKT estimate gives

    N*a1(rho)≤sqrt(3n)+(3n)^(1/4)/sqrt(2).

Since n<p^4*p/(p-1) and p≥5, one has 3n<4p^4. Therefore the first term is strictly less than 2p² and the second is strictly less than p. Hence

    N*a1(rho)<A0<sqrt(2N).

Every constructed label violates ordinary common agreement at A0, because its actual agreement is A>C and the pair's common agreement is C. It also fails full-agreement-set recovery. The complete classification below shows there are exactly M such labels, with singleton lists at A0, even allowing arbitrary quadratic witnesses.

## Exact completeness for arbitrary quadratics

Put ell=(p-1)/2. The single map T=X^ell sends B* onto D=mu_(2n), with every fiber of size ell. Any quadratic h(T), including an odd term, pulls back to H(X)=h(X^ell) of degree at most p-1. The pulled-back received sources are exactly the original p^5 source pair.

If h has more than C=2p+2 matches, it has at least C+1 and H has at least

    ell(C+1)=p²-1+ell>p²

matches on B* for every p≥5. The previously independently proved all-witness classification at more than p² old matches therefore forces a primary Gaussian label and H=alpha X^(p-1)+beta. Since the monomials 1,X^ell,X^(2ell) are distinct, h=alpha T²+beta; its odd coefficient vanishes. Its exact new agreement is A, and uniqueness follows from the old classification.

Thus this line has an exact two-level nearest-agreement spectrum: M primary labels at A, with singleton lists at every threshold C<T≤A; every other label has nearest agreement exactly C. The lower bound C at every label follows from the simultaneous source explanations already constructed. In particular the exact bad-label count at A0 is M, and the classification includes every quadratic over the entire challenge field. Zero in the old domain introduces no problem, since the argument only uses the nonzero pulled-back matches as a lower bound.

Independently, frontier's alternative Frobenius proof also checks: coefficient projection gives F4+z0F2=h0 and F3+z1F2=h1 on the match set. The polynomial identity

    (z0+z1^(p+1))F2=h0-T²h1^p+z1^p h1

has degree at most C and more than C roots. Its T^(p+2) coefficient kills the odd term of h1, and its T coefficient kills the odd term of h0. This supplies another direct route to the same classification; no additional finite-field census is needed.

## Comparison and admission scope

Relative to the uncompressed seed, length drops from p^5 to 2S_5=Theta(p^4), witness degree drops from p-1 to two, and the full Gaussian population Theta(p^6) survives. Thus the large-characteristic, above-first-order exceptional exponent improves from 6/5 to 3/2. The new domain is multiplicative, not an F_p-linear domain. This quotient-plus-pullback extraction was not found in the current binary manuscript's construction sections; the underlying locator compiler is still existing work and should be cited as such.

The rate 3/N tends to zero and the absolute first-order margin tends to zero. The below-Johnson deficit in agreement count tends to 3/4; the first-order margin in agreement count is Theta(p²). The ambient alphabet remains F_(p^15), not a prime field. This improves a matched varying-rate lower-count result, not a fixed-rate/fixed-margin or prime-ambient theorem. The direct quotient map below transfers the original complete classification to arbitrary quadratics, including their possible odd terms.

No main manuscript files were edited and no finite-field scan is required for this proof.
