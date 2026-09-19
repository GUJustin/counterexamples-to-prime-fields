# Independent audit: failure of nearestness-preserving fiber symmetrization

2026-09-19. Outcome: PASS. Read the final countertheorem together with
EXCEPTIONAL_PRIME_SUPPORT_IDEAL.md, the archived prime-order coset-word
obstruction and its independent audit, PROOF.md, and the p=41 census
summary. No new prime search or census was run.

## Uniform exceptional-prime cutoff

For prime r>5, M=r+3 lies in the support criterion's range r<M<=2r.
The quotient degree is a=2r−M=r−3, so the required generators are
h_(r−2), h_(r−1), and h_r−2. If all were zero in characteristic zero,
the denominator-free criterion would construct a degree-below-r polynomial
with r+3 matches. This contradicts the prime-order theorem: nonconstant
polynomials have at most r+2 matches, and a constant has at most r since
the four values of W_r are distinct. Thus EVERY selected support has a
nonzero generator, although the chosen generator may depend on the support.

Each generator is a cyclotomic integer. Every complex embedding sends
each support element to a root of unity, so
|h_j|<=binom(M+j−1,j)<=binom(3r−1,r) for j<=r and M<=2r.
The h_r−2 generator adds at most two. The field has degree
phi(4r)=2(r−1). Consequently its nonzero integer norm has absolute value
at most B(r)=(binom(3r−1,r)+2)^(2(r−1)), exactly as stated.
No denominator, discriminant factor, or support-count factor is missing.

For p congruent to 1 modulo 4r, reduction can send a chosen complex
primitive root to any chosen primitive 4r-th root in F_p: the corresponding
prime ideal is (p,zeta−eta). Also p does not divide 4r, so the roots remain
distinct. A putative finite-field support forces ALL its generators into
that same ideal, including the chosen nonzero one. Hence p divides its
nonzero norm, contradicting p>B(r). The bound is simultaneous over every
support without enumerating supports; different generators for different
supports cause no gap. No conclusion is claimed at exceptional p<=B(r).

## Invariance and the counterfamily

For k=dr=(p−1)/4, mu_d-invariance is exactly the condition that the
nonzero monomial exponents are divisible by d. Thus invariant candidates
are V(X^d), deg V<r, and their best agreement is exactly d M_r(p),
not merely bounded by this value. The full nearest maximum is at least
3k/2 under the chosen p congruent to 9 modulo 16. Since r>5,
d(r+2)<3dr/2, so no invariant candidate is truly nearest. The strict
guaranteed deficit d(r−4)/2 is correct.

Reynolds averaging is defined because d<p, and maps every polynomial into
the invariant subspace. Applying the established bound to its output
therefore proves agreement loss for every actual nearest polynomial.
No unjustified claim that averaging preserves partially matched fibers
is used.

For R>=40 and prime r>R, the moduli 16, r, and the product of odd primes
at most R are pairwise coprime. Their prescribed residues 9, 1, and −1
are all units. The Chinese remainder theorem and Dirichlet's theorem
therefore give arbitrarily large primes in this single reduced class.
They are 1 modulo 4r. The consequences v_2(k)=1, k=1 modulo 3, and
absence of odd prime divisors of k at most R follow exactly as claimed.
Primes can additionally be chosen above B(r) and any required scale,
so prescribed r tending to infinity, p/r tending to infinity, and
d tending to infinity are simultaneously possible.

## Quantifier and provenance boundaries

The symbol r in this construction is a prescribed quotient order. If an
actual nearest polynomial has mu_k-orbit size rho, its stabilizer is
mu_(k/rho), and mu_d-invariance is equivalent to rho dividing r. The
countertheorem excludes this divisibility, not every possible short actual
nearest orbit. It cannot establish that all nearest orbits have size
comparable to p, nor close the exceptional split-prime source problem.
The final note makes all these distinctions explicitly.

The p=41 paragraph matches the archived complete census and the r=5
all-split-prime result. Its r=2 statement uses the archived eight-point
certificate, whose exceptional characteristics exclude 41. These are
corroborating archived facts, not new computations in this audit. The
asymptotic proof does not depend on the census.

## Audited artifact

`FIBER_SYMMETRIZATION_COUNTERTHEOREM.md` SHA256:
`147468d7ce822a3a5ada7039c0577841b717c9d18ff8cb081b0fe2f149e34417`
