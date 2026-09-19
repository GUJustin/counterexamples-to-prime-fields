# Higher-power Frobenius blocks: branch-separation audit

2026-09-18. Independent algebraic verdict: **PASS under the explicit finite guards below**. This is a noncanonical agreement bound and a rate ledger, not a proof of canonical list counts or a new counterexample.

## Setup and guards

Let p be odd, B=F_(p²), E=F_(p⁴), M=p²+1, and s a primitive element of E*. Let h be a positive proper divisor of M and put

    alpha_t=s^((M/h)t),  t=0,...,h-1.

The classes of these elements form the order-h subgroup of E*/B*. Hence

    D0={x in E*: x^h in B*}=disjoint union_t alpha_t B*,
    D1=s D0,

and the two blocks are disjoint, each of size h(p²-1). On them set

    f=x^(hp) on D0,   f=s^(h-hp)x^(hp) on D1,
    g=0 on D0,       g=1 on D1.

Let Q have degree at most D. For the claim below assume

    D<hp,
    max(h-1,D-h)<M/h.

The second condition means |j-h|<M/h for every possible positive exponent j<=D different from h. A negative value of D-h is harmless. These guards hold eventually whenever h=o(p) and D is a fixed positive constant times p, provided that constant is smaller than h so that the first guard holds. In particular D=floor(c*p), 0<c<1, satisfies both eventually for any h>=1 with h=o(p).

## Exact class obstruction

On branch x=alpha_t z of D0, divide the matching equation by alpha_t^(hp), which belongs to B*. The received monomial is z^(hp), and the coefficient of z^j coming from Q is q_j alpha_t^(j-hp). Membership in B is therefore equivalent to q_j alpha_t^j in B.

On branch x=s alpha_t z of D1, divide instead by s^h alpha_t^(hp). The received monomial is again z^(hp). For positive j the coefficient membership condition becomes

    q_j s^(j-h) alpha_t^j in B.

The constant coefficient includes the challenge lambda and has its own normalization. It is not needed in the argument.

Suppose Q is NOT of the form a X^h+b. It has a nonzero coefficient q_j for some positive j different from h. If a branch in each block had every normalized coefficient in B, the two conditions for this particular coefficient would imply

    s^(j-h) * alpha_(t1-t0)^j in B*.

Since s has order M modulo B*, this is the congruence

    j-h + (M/h)j(t1-t0) = 0 mod M.

A necessary and sufficient solvability condition for this congruence in the branch difference is

    (M/h)*gcd(j,h) divides j-h.

It is impossible under 0<|j-h|<M/h. Thus at most one of the two blocks has ANY coefficientwise-B branch. The primitive-s hypothesis is essential to the stated order-M argument.

## Counting actual matches

On a block without a coefficientwise-B branch, apply a nonzero B-linear projection E -> B annihilating B to the normalized matching equation on each branch. The received monomial projects to zero. Some normalized coefficient projects nontrivially, so the resulting polynomial is nonzero and has degree at most D. It has at most D roots in B, hence at most hD matches on that block.

The other block has at most hp matches globally: its matching equation is a nonzero ordinary polynomial of degree hp in x, since its leading monomial coefficient is nonzero and D<hp. This bound applies whether or not that block has a coefficientwise-B branch. Consequently, for every label lambda and every noncanonical Q,

    agr_(D0 union D1)(f+lambda*g,Q) <= hp+hD.

If neither block has a coefficientwise-B branch, the additional bound 2hD also holds. The universal ordinary root bound is 2hp. These alternatives cause no difficulty: the asserted hp+hD upper bound remains valid. Arbitrary puncturing of either block preserves the upper bound, but adding neutral or other coordinates does not follow from this proof.

The argument permits partially or wholly vanishing constant coefficients and includes all positive degrees up to D. It deliberately leaves a X^h+b to separate canonical analysis; there is no claim that all such polynomials are rich or that every challenge has a particular list.

## Dimension, length, and rate

On the full two-block domain,

    n=2h(p²-1),   k=D+1.

For D=floor(c*p), fixed 0<c<1, this gives

    k=Theta(p),   k/n=Theta(1/(hp)).

The same order holds for any retained domain of length Theta(hp²). Growing h therefore does not improve this rate; it decreases it relative to a fixed h while the useful dimension remains Theta(p). To use the displayed noncanonical upper bound below a canonical-scale target near 2hp with a fixed relative gap, this bound requires D bounded below p by a fixed fraction. The larger algebraic branch-separation allowance M/h by itself does not provide a useful larger dimension, because hp+hD would then reach or exceed 2hp. This is a limitation of this estimate, not a universal upper bound on message dimension.

Moreover at n=Theta(hp²), k=Theta(p), and a canonical-scale tested agreement Theta(hp),

    T/sqrt(k*n)=Theta(sqrt(h/p)) -> 0  when h=o(p).

Thus this growing-dimension variant is not in the low-rate first-order/Johnson-scale window. The noncanonical bound alone establishes neither exact source/common agreement nor unchanged threshold lists; those require the separate canonical calculation and an explicitly chosen threshold above hp+hD. There is no neutral padding in this statement.
