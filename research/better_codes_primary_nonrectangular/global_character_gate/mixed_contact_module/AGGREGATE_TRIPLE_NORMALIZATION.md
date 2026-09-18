# Aggregate triple determinants: forced content and exact nonuniform ledger

Research note. These are bounds on the stated guaranteed-contact/nominal-degree construction. Additional polynomial content, higher contact from tangencies, and cancellation among sums remain outside this bound. No claim excludes all actual interpolation helpers.

Let distinct candidate polynomials P_i have degree at most w. For a triple T form the determinant with first row (1,Y,Y^2,R) and the three graph rows (1,P_i,P_i^2,P_i'). Its weighted degree is at most 4w-1 for weights (1,w,w-1), its Y-degree at most2, and its R-degree1.

## Local contact and a forced divisor

At a received node matched by two members of T its weighted first-jet contact is at least2. At a node matched by all three it is at least4: substitute Y=f+hR+h^2E, subtract f from the Y coordinate, and replace the R column by R-Y/h. The Y, Y^2, and modified R columns then have factors h,h^2,h respectively. These column operations may be performed in the Laurent series field, and the resulting product certifies divisibility by h^4 of the original polynomial substitution.

A triple coincidence has a forced polynomial content of order at least2, even when the common value differs from the received word. For an explicit check, put u=P_1-P_0,v=P_2-P_0,y=Y-P_0,r=R-P_0'. Up to overall sign the determinant is

    uv(u-v)r + (uv'-vu')y^2 + (v^2u'-u^2v')y.

At a common root of u,v, the three displayed coefficients have orders at least3,2,2. Thus divide each determinant by the square of the squarefree locator of all its triple coincidences, over the algebraic closure (the resulting divisor is Galois invariant). After this forced division the guaranteed received contact is2 if at least two members match, and0 otherwise. At a simple generic triple collision the content is exactly2; additional content is not included in this normalization ledger.

## All triples, arbitrary incidence buckets

Put N=binom(L,3). At a node with received bucket size b the product of all normalized determinants has guaranteed contact

    mu_b=2[binom(b,2)(L-b)+binom(b,3)].

Let the complete partition of candidate values at that coordinate have bucket sizes s. The forced degree credit there is 2 sum_s binom(s,3). For every nonnegative target multiplicity m,

    2 sum_s binom(s,3)+min(m,mu_b)-m(1-b/L)
       <= 4(L-2)/3 * sum_s binom(s,2).               (1)

Indeed min(m,mu_b)-m(1-b/L)<=b*mu_b/L. For the matched bucket the difference between the right side and these two contributions is exactly

    4/(3L) * (L-b)(L-b-1) * binom(b,2),

which is nonnegative. Every other bucket separately satisfies
2 binom(s,3)<=4(L-2)/3 binom(s,2).

Sum (1) over the domain. Include all off-domain triple coincidences using the same inequality with no received contact term. The total pair-collision count is at most binom(L,2)w. If every candidate has at least A received matches, adding locator powers to bring the product to uniform contact m gives nominal weighted cap

    D_nom=(4w-1)N - 2*(total triple coincidences)
                     + sum_domain max(m-mu_b,0)
          >= mA-N.

Thus in this construction the only possible improvement over the critical mA budget is at most one weight unit per triple. Forced content is not a macroscopic source saving: this bound is O(1/w) of the raw degree. It uses actual nonuniform incidences, not an assumption that every bucket has its mean size.

## Selective products under the actual derivative cap

Choose any multiset of Z triples (nonnegative integer weights allowed). Let T_t be the number of distinct triple-coincidence coordinates for triple t, anywhere, and U_t the number of received coordinates matched by at least two of its members. Its three pair-root budgets imply

    T_t+U_t <= 3w.

A received triple coincidence contributes2 to the left but3 to the pair count; a received exact-pair coincidence contributes1 to each; an off-domain or differently-valued triple coincidence contributes1 versus3.

If target m>2Z, the guaranteed normalized contact is everywhere below m, so padding is linear. The nominal weighted cap after normalization and padding satisfies

    D_nom-mA
      =m(n-A)+(4w-1)Z-2 sum_t(T_t+U_t)
      >=m(n-A)-(2w+1)Z.                              (2)

At the benchmark m=115,n=262144,A=181275,w=131071, the R-degree cap permits Z<=35. Equation (2) is at least

    115*80869 - 35*262143 = 124930 > 0.

Therefore arbitrary selective products of these normalized triple determinants, completed by locator padding using the certified contact orders, cannot win the benchmark ledger. This is a statement about that construction and its degree bound. Extra content, extra contact, or cancellation of leading coefficients is a necessary escape, not ruled out by (2).

The corresponding exact optimization for a proposed cancellation improvement is explicit: retain triple weights z_t, measured extra content degrees, actual local contacts, and the original source caps; minimize weighted cap plus sum of contact deficits. Merely reallocating triples within the presently certified contact/content model cannot remove the positive gap above.

## Stronger closure: full content, exact contacts, actual weight

The following lemma supersedes the limitations of the forced-content ledger for products. It allows all scalar content, tangencies, and lower actual weight of individual determinants.

**Primitive first-order quadratic lemma.** Let

    Q(X,Y,R)=a_2(X)Y^2+a_1(X)Y+a_0(X)+d(X)R,

with d nonzero and gcd(a_2,a_1,a_0,d)=1. Its weighted first-jet contact at any received node is at most2. Moreover every positive-contact node is a root of d. Thus, on any distinct-node domain,

    sum_a contact_a(Q) <= 2 deg d <= 2(W-w+1),       (3)

where W is the actual weighted degree for weights (1,w,w-1).

Proof: translate Y by the received value f and write Q=A_2 Y^2+A_1Y+A_0+dR in that translated coordinate. Under Y=hR+h^2E, contact at least3 forces A_2(a)=0 from the coefficient h^2R^2, A_1(a)=0 from h^2E, d(a)=0 from the constant-in-h R coefficient, and A_0(a)=0 from the constant term. These imply all original coefficients vanish at a, contradicting primitivity. This proof works also in characteristic2 (no division by2 is used). Positive contact alone already implies d(a)=0. Finally deg d<=W-(w-1).

**Product obstruction.** Choose Z triples of distinct degree-at-most-w polynomials, with repetition allowed. Divide each triple determinant by its full X-content, obtaining primitive Q_t of actual weight W_t<=4w-1 and nonzero R coefficient. Let H(X) be any polynomial, and suppose

    H(X) product_t Q_t(X,Y,R)

has contact at least m at every one of n received nodes. If m>2Z, then (3) and additivity of contact imply

    deg H >= mn - sum_t sum_a contact_a(Q_t),

and hence its ACTUAL weighted degree satisfies

    deg_weight(H product Q_t)
      >= mn - sum_t W_t + 2(w-1)Z
      >= mn - (2w+1)Z.                              (4)

Here weighted degree is additive under multiplication; scalar content retained from the original determinants can be absorbed into H. Contact is additive because the substituted leading polynomials in R,E lie in a domain.

The product has R-degree exactly Z, since all the R coefficients are nonzero. Therefore under the benchmark R-degree cap35, m115>2Z automatically, and (4) is at least mA+124930. Such products cannot be strict-weight helpers. This is now an actual-degree obstruction, not just a negative nominal ledger.

Individual leading cancellation only lowers W_t, which strengthens the first inequality in (4). Additional content is absorbed into H; all tangency-induced contact is already covered by (3). The remaining escapes are additive combinations of different products, factors with d=0 (for example graph-only factors), or genuinely different higher-degree/higher-jet factors. The argument does not rule those out and does not cover all list-conditioned source spaces.
