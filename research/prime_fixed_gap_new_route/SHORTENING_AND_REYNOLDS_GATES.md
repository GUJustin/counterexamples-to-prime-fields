# Common-factor shortening and the characteristic-zero Reynolds gate

Scope: the classified Dickson bank, not arbitrary Reed–Solomon lists. These are obstructions to two specific compression mechanisms, not a global fixed-gap impossibility theorem.

## 1. Common-factor shortening has only O(p/L) degree

Let p=4k+1>5, let L≥2 distinct nonzero square parameters t belong to F_p, and write G_t as in DICKSON_SOLUTION_CLASSIFICATION.md. Let C be the monic gcd of all pairwise differences G_t−G_u. The same gcd applies to the shifted bank P_t=G_t−X^k. Then

    deg C ≤ 1 + p/L−1 + 2(Lp−2L²)/(2L−1)².

The displayed bound is at most 2p/L: for L≥2, 2L²≤(2L−1)². In particular deg C=O(p/L). Subtracting any common polynomial and dividing all bank members by a common polynomial therefore cannot lower their degree by a positive fraction of p when L→∞. This addresses multiplicities and roots over the algebraic closure, not only distinct evaluation coordinates.

Use the polynomial identity

    t[(1+X^(2k))²−4G_t²] = 4X G_t²[X^(2k)−G_t²].        (1)

If two distinct parameters have a common value G at ξ, subtracting (1) forces both (1+ξ^(2k))²−4G²=0 and 4ξG²(ξ^(2k)−G²)=0. Consequently either ξ=0 or ξ^(2k)=±1. Every nonzero common root is thus in F_p^*. At zero the constant term is t^k/2, and, when two constant terms agree, the linear coefficient binom(2k+1,3)t^(k−1) is different for different t. The binomial coefficient is nonzero for p>5. Hence the root at zero is simple.

At a nonsquare x the only shared value is zero. Rewriting (1) as

    t(1+X^(2k))²=4G_t²(t+X^(2k+1)−XG_t²)

and comparing second-order terms at x gives

    G_t'(x)² = t/[16x²(t−x)].

The right side is injective as a function of t (x≠0), so distinct candidates have different derivatives. Every nonsquare common root is simple.

At a square x=s² the shared values are σ=±1. For t=a²≠x the two characters χ(a+s),χ(a−s) both equal σ. Differentiate the actual polynomial identity

    sG_t(s²)=((a+s)^e−(a−s)^e)/2,  e=(p+1)/2.

Since e=1/2 in the field, the first and second derivatives give

    G_t'(x)=−σ/(4x),
    G_t''(x)=3σ/(8x²)+σ/[16x(t−x)].

The second derivative is injective in t, so any two nonendpoint candidates sharing σ have difference multiplicity exactly two. At the endpoint t=x the first derivative is −3σ/(8x), different from every other matching candidate; those pair roots are simple. Thus no nonzero common root has multiplicity above two.

It remains to count common coordinates. Write t_i=a_i². At a nonsquare common zero, χ(t_i−x)=1 for every i. The exact quadratic-character identity gives

    sum_x (sum_i χ(t_i−x))² = Lp−L².

Hence the number of common nonsquare zeros is at most p/L−1. At a common square ±1, put S(s)=sum_i[χ(a_i+s)+χ(a_i−s)]. Then |S(s)|≥2L−1, including the possible single endpoint. Since χ(−1)=1, S is even and S(0)²≥0, while

    sum_s S(s)²=2Lp−4L².

Thus the number of common square coordinates is at most (Lp−2L²)/(2L−1)². Counting multiplicities proves the stated bound.

This strengthens the distinct-common-coordinate observation: neither high multiplicities nor nonrational common roots rescue this particular shortening operation. A rational coordinate change is a separate operation, treated in RATIONAL_DESCENT_OBSTRUCTION.md. Combining operations in a new nonlinear fashion is not ruled out here.

### Consequence for puncturing after polynomial shortening

Let D=k−1 and subtract any polynomial B of degree at most D from all L shifted candidates. Divide by a common factor h, then evaluate the resulting polynomials on any shorter domain of length n′ exceeding their maximum degree. Their original degree-D leading coefficients are −t/8 and are pairwise distinct. Thus max_t deg(P_t−B)=D. Since deg h≤2p/L, the new maximum degree is at least D−2p/L. It follows that

    n′ ≥ (p−1)/4−2p/L.

For L≥16 this implies p≤8n′+2. This entire subtract/divide/puncture mechanism therefore cannot yield n′=o(p) while retaining a growing bank. The statement assumes standard polynomial Reed–Solomon evaluation with dimension not exceeding domain length; it does not cover an unrelated coordinate map or a new nonlinear construction.

## 2. The rational Reynolds lift has no useful collisions

Take an odd prime r and d≥2. The mod-p Reynolds coefficients for p=4dr+1 are reductions of

    c_h=binom(1/2,2dh+1),  V(Y)=sum_(h=0)^(r−1) c_h Y^h.

Indeed 2dr+1=1/2 modulo p and every factorial index is below p. Each c_h is positive over the reals, c_0=1/2, and c_h strictly decreases with h. The total tail is at most

    sum_(j≥3 odd) binom(1/2,j)=1/sqrt(2)−1/2<1/2.

Therefore V on the complex unit circle lies in the disk centered at 1/2 with radius less than 1/2. It never equals any of the four old received values 0, 2, i, −i. This already explains why a characteristic-zero lifting argument cannot inherit the old word's agreements.

There is a stronger arbitrary-word gate. On each coset ξ μ_r, ξ∈μ_4, V is injective. To prove this, let ζ generate μ_r. If V(ξζ^j)=V(ξζ^ell) with j≠ell, form their difference as a polynomial in ζ with degree at most r−1 by reducing exponent residues. The minimal polynomial Φ_r over Q(i) has degree r−1, so every coefficient of this difference must be the same. If one of j,ell is zero, the nonconstant coefficients have the distinct magnitudes c_1,...,c_(r−1), a contradiction since r≥3. If both are nonzero, the constant coefficient is zero, so the entire difference must vanish identically. It then says a nonidentity permutation of the nonzero residues preserves coefficients c_h ξ^h. Their distinct absolute values force every index fixed, again a contradiction.

For the r rotated candidates V(Y/ω), ω∈μ_r, at each of the 4r domain coordinates all candidate values are distinct. Consequently every received word has at most 4r total candidate agreements; a sublist whose candidates each have more than r agreements has fewer than four members. For a coset-constant word the sum of four modal multiplicities is exactly four.

This is a characteristic-zero obstruction only. Reduction modulo primes can create collisions, and the actual p=4dr+1 source is specifically such a reduction. It does not prove the finite-field Reynolds route impossible. It shows that any growing-bank fixed-surplus success must exploit genuinely characteristic-dependent collisions, rather than a lift of the rational coefficient family.

## Remaining constructive escape

These two gates suggest looking for a source in which a low-degree quotient already has many modular value collisions, instead of compressing the full Dickson bank by a common factor or lifting the Reynolds projection. The unresolved finite-field Reynolds modal problem is a concrete such target, but the present note supplies no positive agreement surplus and no new prime-field counterexample.
