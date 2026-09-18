# Fixed-cardinality subset products from a character-sum bound

Root derivation, September 18, 2026. Independent audit requested. This is an elementary consequence of a standard character-sum estimate, not a novelty claim.

Let A be an s-element subset of a finite abelian multiplicative group H of order M. Suppose every nontrivial character chi satisfies |sum_(a in A) chi(a)| <= B < s. For 0 < r < s, put theta=r/s and

    epsilon = (s+1) exp(-theta(1-theta)(s-B)).

For every y in H, let N_r(y) count r-element subsets S of A with product y. Then

    | M N_r(y) / binom(s,r) - 1 | <= (M-1) epsilon.

In particular every y is represented if (M-1)epsilon < 1.

## Proof

Fix a nontrivial character and write v_a=chi(a). For t>0 and any real phi,

    |1+t exp(i phi)v_a|^2
      = (1+t)^2 - 2t(1-Re(exp(i phi)v_a)).

Using 1-u <= exp(-u), including the zero-factor case by continuity, gives

    |product_a(1+t exp(i phi)v_a)|
      <= (1+t)^s exp(-t(s-B)/(1+t)^2).

The coefficient of z^r is the sum of chi(product S) over r-subsets. Cauchy's coefficient bound therefore gives its absolute value at most

    t^(-r)(1+t)^s exp(-t(s-B)/(1+t)^2).

Choose t=r/(s-r). In a Binomial(s,r/s) distribution, r is a mode, so its probability is at least 1/(s+1). Consequently

    t^(-r)(1+t)^s <= (s+1)binom(s,r).

This proves the relative bound epsilon on each nontrivial Fourier coefficient. Character orthogonality and the triangle inequality over M-1 nontrivial characters prove the claim. This argument does not assume that powers of a nontrivial character remain nontrivial.

## Degree-five affine-line specialization

Let E=F_(p^5), let b generate E over F_p, and take

    A={b-a : a in F_p*},  s=p-1,  M=p^5-1.

Katz, *An estimate for character sums*, JAMS 2(2), 1989, Theorem 1, gives the bound 4 sqrt(p) on the full affine line for every nontrivial character of E*. Removing a=0 gives B=4 sqrt(p)+1. The original theorem was retrieved and visually checked on printed page 197:

https://web.math.princeton.edu/~nmk/old/estcharsums.pdf

It follows that every nonzero element of E is an r-subset product whenever

    log((p^5-2)p) < theta(1-theta)(p-2-4sqrt(p)),
    theta = r/(p-1).

For every fixed theta bounded away from zero and one this holds for sufficiently large p. This gives all p^5-1 values of the nonzero product, not all p^5 affine labels: the quotient labels b^r-product(S) necessarily omit b^r. The separate polynomial compiler, agreement bounds, comparison to known constructions, and finite onset require their own audits.

## Optional subgroup version

For a multiplicative subgroup G of F_p* of size s, Katz's Theorem 2 on the etale algebra E x F_p, regular element (b,0), bounds the mixed sums by 5 sqrt(p). Expanding the indicator of G in base-field multiplicative characters gives B=5 sqrt(p) for A=b-G. Thus the same lemma applies whenever

    log((p^5-2)(s+1)) < theta(1-theta)(s-5sqrt(p)).

This statement is conditional on an available divisor s of p-1. It does not assert that a divisor near sqrt(p), or near log(p), exists for every prime. The extra field factor in the etale algebra is what accounts for the larger constant five.
