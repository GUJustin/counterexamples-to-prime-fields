# Final independent audit: far endpoints by two-fiber puncturing

September 18, 2026. **PASS** for `fp3_far_endpoints.tex`. This audit reads the preceding complete all-quadratic theorem, the new fragment, and the finite-census receipt. No main manuscript edits.

## Puncturing and label count

The choice u1=eta*u0 is valid in W and differs projectively from u0. Its image line Iu1=eta^-1 Lambda0 is distinct from Lambda0, while eta*Iu1=Lambda0. Thus every b!=0 in Iu1 yields a coset b+Lambda0 disjoint from Lambda0. The two chosen endpoint labels are distinct and generic, and BOTH have precisely the same unique doubly canonical quadratic Q*.

The p−1 nonzero core fibers have total physical size p²−p, giving a choice of size at most p. All p trimmed fresh fibers for u1 partition D1, also of size p²−p. The two smallest therefore have total at most2p−2. Deleting their union with the selected core fiber deletes at most3p−2 points. These are the entire agreement supports of Q* at the two endpoints, not merely selected sub-supports. Q* has zero remaining endpoint matches. Every other quadratic had at most p+2sqrt(p) matches by the preceding complete classification, and cannot gain matches under puncturing.

The excluded direction plane Ju1 has exactly p² elements and contains Lambda0. Outside it there is a unique qualifying original witness whose quadratic leading coefficient differs from Q*. A common matching point on the deleted core fiber solves Qlambda−Q*=0; a common match on the deleted fresh fiber for gamma solves Qlambda−Q*=lambda−gamma. Each is a nonzero quadratic and has at most two roots. Thus at most six matches are lost. Every competitor remains below T. The surviving p³−p² parameters are genuine distinct singleton lists, transported bijectively by lambda=alpha+t(beta−alpha).

The theorem correctly claims a LOWER count and makes no assertion about the remaining p² labels. Both individual-source bounds are now proved, and their common-agreement bound follows immediately. This repairs the source-distance weakness of the unpunctured all-label theorem without any alphabet extension.

## Finite certificate at the printed onset

The threshold is T=2p−ceil(4sqrt(p))−8. For p>=4099, put B=3T,H=40B,m6,derivative cap3. The previously independently checked primary formulas give G=4B²−2B and R=62.

The changed ceiling/reserve must be checked again; it is valid:

    B>=6p−12sqrt(p)−27
      >=(93/16)p−27
      >=29p/5,

because sqrt(p)<=p/64 and p/80−27>0 at this onset. Also B<=6p and n<=2p². Therefore

    39G−40*62n >=(7196/25)p²−468p>0.

In particular G>62n, and

    (H−B+1)G−(H+1)*62n
      =B(39G−40*62n)+(G−62n)>0.

This is the strict graded row test. The characteristic guard remains p>3, not p>B or p>H.

For Johnson, n>=2p²−4p+1 and T<=2p−4sqrt(p) give

    2n−T² >=16p sqrt(p)−24p+2>0.

For the curve, T>=2p−5sqrt(p) and sqrt(p)>24 imply

    n*a1(3/n) <(7/4)p+sqrt(p)<T.

Finally T−(p+2sqrt(p))>=p−6sqrt(p)−9>0. All displayed finite comparisons hold uniformly for the stated primes.

## Census scope and comparison

The `check_fp3_exact_lists.json` p47 puncturing row explicitly has `all_quadratic_exclusion_applies=false`; it is only a canonical-bank census and is not a counterexample to any all-witness statement. The p53 row has threshold68>53+2sqrt(53) and >16, so the previously proved noncanonical bound excludes every other quadratic. Its guaranteed singleton count146068 equals53³−53². The receipt's scope flags are correct. I did not independently rerun that field census; the theorem audit is algebraic and the finite support inequalities above are independent.

Relative to the older F_(p⁴) theorem, this improves the challenge alphabet to F_(p³), retains characteristic Theta(sqrt(n)), singleton population Theta(n^(3/2)), and both-source gap Theta(sqrt(n)), and raises the certified exceptional probability to at least1−1/p. Its length and constants differ, so this is not a same-domain numerical replacement. It remains an extension-field, vanishing-rate theorem. The proof certifies finite first-order applicability, not a matching universal exceptional-count upper bound and not a better.codes certificate.
