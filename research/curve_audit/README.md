# Polynomial-curve corollary: independent referee report

The proof of `cor:puncturing-curves` is correct. The theorem's degree factor is also sharp at the one-coordinate-gap endpoint, as proved below.

## Audit of the existing argument

The primary source is Ben-Sasson, Carmon, Ishai, Kopparty, and Saraf, *Proximity Gaps for Reed–Solomon Codes*, [ECCC TR20-083, revision 3](https://eccc.weizmann.ac.il/report/2020/083/revision/3/download/), Theorem 6.1. Its unique-radius statement includes equality and gives joint agreement of all coefficient words when the number of nearby parameters exceeds the curve degree times the block length. Its code dimension is its degree parameter plus one; the manuscript consistently uses dimension k instead.

* After deleting d coordinates, the minimum distance is 2s+1. Thus at most one polynomial witness belongs to each parameter; converting the parameter count to a witness-pair count is valid.
* In the jointly explained case, the codeword curve is close at every parameter and is the unique nearby witness. Outside its full coefficient agreement set, a discrepancy is a nonzero **formal** polynomial of degree at most e. Its number of distinct field roots is at most e even when e is at least the field size. A polynomial can then vanish everywhere, but the stated bound is still valid.
* An unexplained entire support contains an unexplained (k+1)-subset: interpolate all coefficient words on the same k positions, then keep one failure of any interpolant. That one extra point suffices independently of the number of coefficient words.
* The error support can be padded to an r-set avoiding the protected subset because its complement has size n-k-1 >= r. Deleting any d points of this padded set leaves at most r-d=s errors. The protected subset remains, so explanation cannot appear after puncturing.
* Distinct witnesses remain distinct after restriction because the punctured domain has at least k points. Distinct parameter values remain distinct pairs even if the curve maps them to the same received word.
* For e=0, the nearby polynomial itself explains the entire support. The count is zero; the corollary's statement is correct.

The existing checker enumerates every parameter and codeword of 300 deterministic fixtures, not every possible curve. Its coverage description correctly states that limitation. Its modular arithmetic only tests prime fields, although the proof works over all finite fields.

## Endpoint sharpness for every positive curve degree

Fix n and k with 1 <= k <= n-2, and a positive integer e. Over a sufficiently large finite field whose characteristic does not divide e, there is a degree-e curve for which the number of nearby witness pairs at radius

    r/n = (n-k-1)/n

is exactly

    e * binom(n,k+1).

All nearby words have unique witnesses. The coefficient words have no joint agreement on k+1 coordinates. Thus the endpoint of the manuscript's curve bound is attained.

**Construction and proof.** Start with a finite field F of characteristic not dividing e and a domain D whose (k+1)-subset sums s_T are distinct. Choose b outside this set of sums, enlarging F first if necessary. Pass to a finite extension E splitting all polynomials Z^e+b-s_T. Each polynomial has exactly e distinct roots: its constant term is nonzero and its derivative is e Z^(e-1). Roots belonging to different T are disjoint. Set

    h(z) = z^e+b,
    f(z)(x) = x^(k+1) - h(z) x^k.

For any z and any polynomial P of degree less than k, agreement on k+1 positions T forces

    X^(k+1) - h(z) X^k - P(X) = product_{x in T}(X-x).

Comparing coefficients gives h(z)=s_T. Conversely every such parameter has exactly that polynomial witness. Distinct subset sums give uniqueness. There are therefore e*binom(n,k+1) distinct parameter-witness pairs. The coefficient of z^e in f is -X^k, which cannot agree with a polynomial of degree less than k at k+1 distinct points. This proves the required failure of joint agreement.

No assertion that the roots already split in the starting field is needed. All splitting fields in this construction are finite. Choosing the characteristic larger than e is a simple sufficient condition.

If the starting domain also has the manuscript's exact generic list profile, that profile survives extension of the field by the manuscript's extension-field corollary. Consequently the curve variant can retain actual maximum list size n-k-1.

## Exact degree-e concurrency

For the same construction, a parametrized codeword curve Q(z,X) of degree at most e in z and degree less than k in X contains at most

    e(n-k)

selected pairs, and this maximum is attained. This uses the original parameter z.

To prove the upper bound, let B be the coordinates where f(z)(x)=Q(z,x) holds identically as a formal polynomial in z, and put b0=|B|. Comparing leading z-coefficients gives b0 <= k. Every other coordinate contributes at most e roots. If m selected pairs lie on Q, then

    m(k+1) <= b0*m + e(n-b0),
    m <= e(n-b0)/(k+1-b0) <= e(n-k).

For equality, choose any k-subset A of D, let V_A(X)=product_{a in A}(X-a) and s_A=sum A, and compose the affine extremizer with h:

    Q(z,X) = X^(k+1) - (X+s_A)V_A(X)
             + h(z)(V_A(X)-X^k).

Both displayed coefficient polynomials have degree less than k. This curve contains precisely the e(n-k) selected pairs indexed by T=A union {a}, a outside A. The count is therefore sharp.

## Optional finite-field cap

The corollary can replace e(n-d) by min(|F|,e(n-d)): a puncture has at most one witness at each of its |F| parameters. This improves the displayed numerical bound only when e(n-d)>|F|. It is an elementary cap, not a new decoding theorem.

One must **not** replace the formal degree by the degree after reduction modulo Z^q-Z while keeping the original coefficient-agreement condition. For example, over F_q take f(z)(x)=(z^q-z)x^k. Every parameter gives the zero word and has the unique nearby witness zero whenever r<n-k+1. However, its coefficient words include X^k and -X^k, so they have no joint agreement on k+1 positions, and all q entire supports are unexplained. Thus treating this functionally constant curve as degree zero would give a false zero upper bound. At the unique radius, this example attains the optional q cap exactly. The manuscript's existing formal-degree wording correctly avoids this error.

## Reproducible validation

Run `python3 research/curve_audit/verify_curve_endpoint.py`. Six fixtures have degrees 2 through 5, include k=2 and k=3, and enumerate every field parameter and every codeword. The checker also constructs the attained degree-e concurrency curve and verifies exact agreement supports. The output is written beside the checker.
