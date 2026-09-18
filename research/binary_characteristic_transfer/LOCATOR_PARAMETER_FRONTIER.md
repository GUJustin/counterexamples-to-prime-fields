# Parameter frontier of the unmodified locator compiler

This optimizes the existing Gaussian locator compiler, not all possible subspace constructions or new witness identities. In particular it uses the compiler's declared strict witness degree, with no new cancellations or selection of a special lower-degree witness family.

Let the additive domain have size N=p^d. Let s>=1 be the codimension of the matching subspaces and r=d-s>=2 their dimension. The standard compiler parameters are

    K0=p^(r-2),  A=p^r-1,
    C=p^(r-1)-1,
    M=[r+s choose s]_p.

With sufficiently many independent exterior coefficients all M affine labels are distinct; a further independent source shift gives exact individual-source and common agreement C. The Gaussian count has leading order

    M ~ p^(rs) = N^(rs/(r+s)).

## 1. First-order agreement already forces s<=2

At the compiler's smallest declared dimension K0,

    rho=K0/N=p^(-s-2),
    (A/N)/sqrt(rho) < p^(1-s/2).

For p>=3 and s>=3 the right side is at most 1/sqrt(3), whereas the first-order low-rate curve is strictly greater than sqrt(rho/2). These rates are all in its low-rate branch. Thus **every s>=3 member is below first order**, not merely asymptotically. Enlarging the code dimension only worsens this comparison.

Codimension one is above Johnson but gives exponent r/(r+1)<1. Codimension two is the near-Johnson row and gives

    exponent 2r/(r+2)=2-4/(r+2).

This is the route by which the fixed-characteristic compiler approaches a quadratic bad-label population.

## 2. Large characteristic forces r<=3

The message-degree guard p>K0-1 is equivalent, for these prime-power dimensions, to K0<=p. Hence r<=3. Combining it with the preceding first-order requirement leaves this table:

| matching dimension r | codimension s | N | K0 | leading count exponent |
|---:|---:|---:|---:|---:|
| 2 | 1 | p³ | 1 | 2/3 |
| 2 | 2 | p⁴ | 1 | 1 |
| 3 | 1 | p⁴ | p | 3/4 |
| 3 | 2 | p⁵ | p | 6/5 |

The constant-message rows require their own harmless K=1 theorem conventions; they cannot improve the exponent. The nonconstant optimum is exactly the p^5 row already audited. Its fixed derivative cap two proves actual admissibility, so this is not just a necessary-parameter comparison.

For contrast, at s=2 the tempting stronger rows are

| r | exponent | witness dimension |
|---:|---:|---:|
| 4 | 4/3 | p² |
| 6 | 3/2 | p⁴ |
| 18 | 9/5 | p^16 |
| r tending to infinity | tending to 2 | p^(r-2) |

Every one violates the large-characteristic message-degree guard. Varying p cannot change that inequality. In this unmodified family, 6/5 is the largest asymptotic length exponent simultaneously in the first-order and large-characteristic regimes.

## 3. Simple alterations do not change this optimization

Using a base field b=p^e instead gives K0=p^(e(r-2)). For e>=2 the guard permits only r=2 (constant witnesses), whose first-order Gaussian exponent is at most one. It does not bypass the prime-characteristic constraint.

Common-zero multiplication inserts its degree into the witness dimension. The r=3 row already uses K0=p, so there is no insertion budget under K<=p. The r=2 row has at most p-1 such degrees available; it cannot turn its at-most-linear first-order Gaussian population into a superlinear one. This observation does not address fresh witnesses created after multiplication or an independently chosen punctured/correlated family.

Fixed positive rate is also absent on the full additive domains here: in the nonconstant optimum rho=p^-4 tends to zero, and all allowed nontrivial rows have N growing faster than p while K<=p. Arbitrary puncturing or new witnesses require a separate argument; the companion `INHERITED_FIXED_RATE_TRANSFER_LIMIT.md` addresses inherited transformations of the p^5 seed, rather than proving a universal barrier.

## 4. What a stronger construction would have to change

To approach exponent two while retaining first-order agreement, increasing codimension is ineffective: it moves below the first-order curve immediately. Increasing the matching-space dimension at codimension two is effective for the count, but its current witnesses have degree p^(r-2)-1. A successful new identity would therefore need a genuinely lower-degree witness family (or a different source family), not merely additional exterior label parameters or another choice of the ambient extension field.

For example the first unclosed target in this direction is the s=2,r=4 population on N=p^6: its subspaces have p^4 points and Gaussian population ~p^8=N^(4/3), but the present witness degree is p²-1. Reducing that degree below p while preserving a substantial part of the population would be a new algebraic construction. The present compiler does not supply such a reduction, and this note makes no impossibility claim for it.

## 5. A precise common-source cancellation barrier

For every codimension-two family on B=F_(p^(r+2)), r>=3, write the top locator coefficients as

    L_W=X^(p^r)+a X^(p^(r-1))+c X^(p^(r-2))+d X^(p^(r-3))+... .

With theta of degree at least three over B, its label and leading witness coefficient are

    z_W=c^p-a^(p+1)+theta a,
    gamma_W=-d^p-(theta-a^p)c.

Both lie in the B-plane E=B+B theta. If common polynomial subtraction from the two sources lowers the degree of every retained witness, its leading coefficients must satisfy

    gamma_W=alpha+beta z_W

for fixed alpha,beta in the challenge field. At most |B|=N locators can satisfy this equation.

Indeed, if beta is not in B, then E and beta E are different two-dimensional B-subspaces and intersect in dimension at most one. To see they differ, beta E=E would imply beta=u+v theta with v!=0 and beta theta in E, forcing theta² in E, a contradiction. Thus z lies in an affine B-space of dimension at most one, containing at most N labels. If beta is in B, either alpha is outside E and there are no solutions, or its theta component gives c=-alpha_theta-beta a, again at most N pairs (a,c). Finally (a,c) uniquely determines a codimension-two subspace: two such locators differ by degree at most p^(r-3), but their subspaces intersect in at least p^(r-2) points.

Hence common affine-in-label subtraction cannot turn the superlinear Gaussian population into a lower-degree superlinear population. In particular it cannot repair the s=2,r=4 row to dimension p. This is a scoped cancellation theorem, not a barrier to a different outer additive polynomial, correlated source coefficients, or genuinely new witnesses.
