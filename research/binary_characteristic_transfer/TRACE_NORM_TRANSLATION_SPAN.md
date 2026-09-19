# Canonical translation span: exact finite test

Scope: canonical witnesses of the trace–norm compiler, at one fixed nonzero norm coefficient a and normalized constant c=1. This is not an impossibility theorem for other witnesses or arbitrary coordinate transformations.

## General exact reduction

Let B have n elements, P=P_0 have degree D<n, and P_b(X)=P(X+b), b in B. Write

`H_l(X)=sum_{i>=l} c_i binom(i,l) X^(i-l)`

for its Hasse derivatives. Then, over any coefficient field containing B,

`V=span_b(P_b-P_0)=span_{1<=l<=D} H_l`.

Indeed P_b-P_0=sum b^l H_l, and the functions b,b^2,...,b^D on B are linearly independent since D<n. This also supplies the exact finite rank calculation: form the Hasse coefficient matrix, with binomial coefficients computed modulo p (equivalently by Lucas's digit criterion). One must take its rank, not merely count the union of its nonzero monomials: different degrees can remain coupled.

The witness difference is the negative of
`T_beta(v)=(v(X)-v(beta))/(X-beta)`.
Since H_D is a nonzero constant, V contains constants, and the kernel of T_beta on V is exactly that one-dimensional space. Thus the affine witness span has dimension dim(V)-1.

The joint span of witness differences and label differences is the image of
`v -> (-T_beta(v),v(beta))`.
It contains the pure label direction (0,1). Consequently, replacing every witness by itself plus one fixed polynomial plus its label times another fixed polynomial H cannot reduce its difference span: the new span is exactly `T_beta(V)+span(H)`, up to irrelevant signs. This remains true after evaluation on any retained coordinate set. Hence affine-in-label corrections do not remedy a rank obstruction when such an obstruction is actually present.

## Exact p=3, Q=9 computation

For a=c=1,

`G=X^30+X^10+1`, `F=X^3`, `Lambda=X^81-X`,

and exact division gives

`P=F Lambda/G=X^54-X^34-X^24+X^14-X^4`.

The translation-difference space V has the following basis over F3, and the same basis remains independent over every extension:

```
X^33+X^13,
X^31+X^21+X^11,
X^30-X^10,
X^28+X^18,
X^27,
X^15+X^5,
X^12, X^9, X^7, X^6, X^4, X^3, X^2, X, 1.
```

Therefore dim(V)=15 and the canonical witness difference span has dimension **14**, whereas the ambient strict RS dimension is k=34. In particular it does not span the full RS code. The suggested full-dimension obstruction is false already in this finite example.

The exact basis and rank are independently reproducible with `verify_trace_norm_translation_span.py`; its JSON receipt records ordinary modular polynomial division and row reduction. This is a coefficient calculation, with no codeword enumeration or search over received words.

## What this does and does not say about shortening

For a retained set S, the exact restriction rank is

`rank(ev_(S union {beta})(V))-1`.

It is at most 14; it is 14 whenever |S|>=33, because T_beta(V) has maximum degree 32. Since V contains every monomial of degree at most four, it is also at least min(|S|,4) for every set of distinct coordinates S. No claim of full rank for every intermediate set size is made.

This provides a potential compression into an arbitrary 14-dimensional linear code for this fixed-a subbank, but it does not put that subbank in ordinary RS_14: the displayed basis has high, coupled degrees. Moreover the fixed-a subbank has only 81 labels, so by itself it supplies no superlinear bank. Combining all a values, proving an RS shortening identity, preserving the desired agreements after coordinate removal, and retaining the source-distance requirements are separate unresolved obligations.
