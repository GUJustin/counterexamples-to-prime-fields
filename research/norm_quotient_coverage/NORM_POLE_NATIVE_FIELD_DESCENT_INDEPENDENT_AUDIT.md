# Norm-pole compiler and native coefficient-field descent

2026-09-18. **PASS for the algebraic compiler.** The numerical target-subset coverage certificate is a separate premise; this note does not independently certify an unstated seed instance.

## Precise assumptions

Let E=Fp^6, let e divide 6, and set K=Fp^(6/e). Choose b of degree exactly six over Fp. Then K(b)=E, and

    T(Y)=Norm_(E/K)(Y−b)

is the monic degree-e minimal polynomial of b over K. It has no Fp root. Choose m dividing p−1 and s+1 distinct tags in the image of x↦x^m on Fp*, one reserved tag a0 and a set G of s other tags. The domain consists of their full m-point fibers, so n=(s+1)m. Let R∈Fp[X] be the monic locator of w distinct reserved-fiber points, with 0≤w<m. Put Y=X^m and require r≥e+1, r≤s and

    J−1=w+(r−e−1)m.

For an r-subset S⊂G, write VS(Y)=∏_(a∈S)(Y−a). Suppose VS(b)=λ lies in K*. The product is automatically nonzero because b∉Fp.

## Descent and degree cancellation

VS(Y)−λ belongs to K[Y] and vanishes at b, so T divides it in K[Y]. Therefore

    hS = R [T(Y)Y^(r−e)+λ−VS(Y)]/T(Y)

is a polynomial over **K**, not merely E. The two monic degree-r terms cancel in its numerator. Its degree in Y after division is at most r−e−1, hence its degree in X is at most J−1.

Both received words

    f=R Y^(r−e),        g=R/T(Y)

are K-valued on the Fp domain. Thus the code is the ordinary K-linear evaluation code of polynomials of degree <J, with native challenge field K. E is an auxiliary field for producing labels. The degree-six hypothesis on b is essential to this proof: without K(b)=E, the norm can repeat the minimal polynomial and divisibility by the full norm need not follow.

## Exact represented-label agreement

For each represented λ∈K*,

    f+λg−hS = R VS(Y)/T(Y).

The denominator is nonzero throughout the domain. The zeros consist of w reserved points and the r full tag fibers, disjoint by construction. Thus the agreement is

    T_agree=w+rm=J+(e+1)m−1.

For any degree-<J polynomial h, clearing the denominator gives

    R T(Y)Y^(r−e)+λR−T(Y)h.

The first term is monic of degree w+rm, while the last has degree at most em+J−1=w+(r−1)m. Consequently this is always nonzero with degree exactly T_agree. Every represented label has **exact maximum agreement** T_agree, and no pencil label can exceed it. The calculation does not assert uniqueness of the nearest witness.

## Source and ordinary common agreements

The polynomial source f is monic of degree

    A=w+(r−e)m=J+m−1.

Subtracting any degree-<J message leaves a nonzero degree-A polynomial, proving agr(f)≤A. Choose any r−e tags U⊂G. Interpolate Y^(r−e) and 1/T(Y), separately, on U by polynomials of degree at most r−e−1. After substituting Y=X^m and multiplying by R, these are degree-<J witnesses for f and g. Both match on the same (r−e)m+w=A coordinates. Thus

    agr(f)=CA(f,g)=A,       agr(g)≥A.

The upper bound for CA follows already from agr(f). Clearing the denominator in g−h gives R−T(Y)h, a nonzero polynomial of degree at most

    J+em−1.

It is nonzero since T(X^m), of degree em, cannot divide the nonzero R of degree w<m. Hence

    A≤agr(g)≤J+em−1=T_agree−m.

Do not replace this interval by an exact source-agreement claim when e>1. Both endpoints are nevertheless farther than the represented-label threshold by at least m coordinates; the polynomial endpoint and ordinary common agreement have the larger exact deficit em.

## Fixed parameter ledger

For n=262144, J=131072, m=1024, s=255 and w=1023, one has r=128+e. All four cases are admissible:

| e | Native field | r | Exact polynomial source and CA | Upper bound for g | Exact represented-label agreement |
|---|---|---:|---:|---:|---:|
| 1 | Fp^6 | 129 | 132095 | 132095 | 133119 |
| 2 | Fp^3 | 130 | 132095 | 133119 | 134143 |
| 3 | Fp^2 | 131 | 132095 | 134143 | 135167 |
| 6 | Fp | 134 | 132095 | 137215 | 138239 |

The normalized capacity surplus is ((e+1)1024−1)/262144. In particular the prime-native case has surplus 7167/262144, while its guaranteed second-endpoint separation remains 1024/262144.

## Coverage interface and affine mixtures

Apply the independently audited target-subset second-moment lemma with Γ=E* and target B=K*. For a genuine uniform P-element tag population, a certificate V/a≤2^−22 guarantees existence of distinct tags representing at least (1−2^−22)|K*| of precisely the required λ values. This is not a count in an arbitrary coset: K-membership is what makes the polynomial division descend.

For normalized mixtures (1−t)f+tg with t∈K\{1}, the corresponding pencil parameter is λ=t/(1−t). Thus λ=−1 is omitted from finite normalized mixtures, and λ=0 corresponds to endpoint t=0. A represented-label count L therefore guarantees at least L−1 represented interior mixtures; one should not silently state exactly the same count for the affine-mixture convention. The endpoints remain f and g, with the bounds above.

This is a finite field/degree tradeoff on a chosen union of base-field fibers. It is not an asymptotic breakthrough, an explicit tag construction without a separate certificate, or a result on a prescribed NTT domain.
