# A dimension ceiling for the retained canonical higher-power family

2026-09-19. A scoped obstruction, not a bound for arbitrary Reed--Solomon counterexamples.

Use the two weighted tag sets from HIGHER_POWER_SHORT_DOMAIN_MOMENT_AUDIT.md, with weights between 0 and h, totals n_i, and n=n_0+n_1. The code dimension is k=h+1. Suppose each qualifying canonical witness must match at least g>h coordinates in each block. This follows, in particular, when threshold T exceeds the maximum agreement of either source by at least g: a canonical witness on one block can be extended at any challenge by adjusting its intercept, so no one-block contribution exceeds the source maximum.

For one block write r(L)=sum_{y in L} w(y) for each affine prime-plane line and S=sum_y w(y)^2. Distinct points determine exactly one line, whereas each point lies on p+1 lines. Hence

    sum_L [r(L)^2 - sum_{y in L} w(y)^2] = n_i^2-S_i.

On a g-rich line, sum_{y in L}w(y)^2 <= h*r(L), so its nonnegative distinct-point contribution is at least g(g-h). The total number L_i of g-rich lines consequently satisfies

    L_i <= (n_i^2-S_i)/(g(g-h)).

There are at most floor(n_i/g) such lines in any one direction. Nonzero canonical challenge labels have unique pairs of same-direction tag lines. Counting instances also upper-bounds the number of distinct labels, including zero. Therefore

    B <= min( floor(n_0/g)*(n_1^2-S_1)/(g(g-h)),
              floor(n_1/g)*(n_0^2-S_0)/(g(g-h)) ).

This elementary bound has no dependence on p and applies to arbitrary retained subsets and nonuniform fiber weights. It complements rather than replaces the centered variance bound.

If g >= c*sqrt(h*n) for a fixed c>0 and n/h tends to infinity, then g/h tends to infinity and

    B = O_c((n/h)^(3/2)).

Thus B/n tending to infinity requires h=o(n^(1/3)), or equivalently k=o(n^(1/3)), within this canonical family and constant-relative-gap scaling. More quantitatively B>=F*n implies h <= O_c(n^(1/3)/F^(2/3)). In particular this rules out growing dimensions of order n^(1/3) or larger in the stated vanishing-rate regime.

The asymptotic conclusion assumes n/h tends to infinity. It does not by itself exclude every constant-rate partial-weight regime: when g<=h, one occupied tag can already make a line g-rich, and the distinct-point denominator used above is unavailable.

For full fibers with comparable tag-set sizes m, n=Theta(h*m), the bound reads B=O_c(m^(3/2)), and superlinearity requires h=o(sqrt(m)). Keeping m bounded keeps the possible qualifying line pairs bounded whenever each qualifying line contains at least two tags. The dimension increase therefore consumes, rather than creates, the canonical bank's superlinearity budget.

Scope: the gap g=Omega(sqrt(h*n)) is the Johnson-scale constant relative loss regime used here. Other thresholds, smaller gaps, noncanonical exceptional witnesses, and unrelated source constructions are not excluded.
