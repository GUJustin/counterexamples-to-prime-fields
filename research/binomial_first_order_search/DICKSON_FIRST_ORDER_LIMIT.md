# Why the growing Dickson list does not reach the first-order regime

Update: PUNCTURING_LIMIT.md extends this argument to arbitrary punctured
domains and all resulting rates. The full-domain restriction below is
the scope of this original statement, not the limit of the follow-up.

September 17, 2026. Restricted-family theorem; not a general upper bound
for Reed--Solomon lists. This uses the character-mask Fourier argument
already developed in ../two_coset_candidate_lists/BINOMIAL_BRANCH_BOUND.md,
with the previously excluded r=2,j=1 case evaluated at its actual
agreement density rather than at capacity.

Let p=4k+1 be prime, k>=2, n=4k, and let the domain be F_p^*. Set

    G(X)=sum_{j=0}^k binom(2k+1,2j+1) X^j.

For h in H=mu_k, P_h(X)=G(hX)-X^k has degree<k. For ANY L-element
subset of these candidates and ANY received word, their minimum number
of agreements is at most

    3k/2 + 4 Lambda + 8 Lambda sqrt(k/L) + 36k/L + 1,
    Lambda=8(sqrt(p)+3).                              (1)

The same estimate applies to the second twisted orbit in the full
2k-candidate binomial bank. Consequently fewer than 2^22 members of
that full bank can simultaneously agree above the first-order
quarter-rate curve a0=(3+sqrt133)/31, independently of p.

Thus the existing linear-size Dickson list below the curve cannot be
moved above that curve by choosing a different word or a subset of
its candidates on the same full domain. This does not cover arbitrary
other polynomial families or punctured domains.

## Character masks and the bound

For square x=t^2, the root filter is

    G(x)=((1+t)^(2k+1)-(1-t)^(2k+1))/(2t).

Away from t=+/-1, the two quadratic characters chi(1+t),chi(1-t)
explain two constant branches: G=1 if both are1, and G=-1 if both
are-1. Each has density1/4 on each of the two square H-cosets.
The remaining branches are +/-1/t and have bounded fibers.

For nonsquare x, let t^2=x in F_(p^2), so t^p=-t. Put
Y=(1+t)^((p+1)/2). Then Y^2=1-x and Y^p=chi(1-x)Y.
Thus G(x)=0 when chi(1-x)=1, giving a constant mask of density1/2
on each of the two nonsquare H-cosets. Otherwise
G(x)^2=(1-x)/x, whose fixed-value fibers are bounded.

The character-mask calculations from the cited local proof now use
at most the three roots0,1,-1 (or0 and the two roots of1-dT^2).
For every mask on an H-coset, its count differs from its density times
k by at most Lambda, and every nontrivial H-Fourier coefficient has
absolute value at most Lambda. These estimates follow by expanding
the two quadratic-character indicators (plus the coset selector),
and applying the same non-power multiplicative-character sum bound.
The constant is deliberately generous. All nonconstant branches,
including excluded base points, have at most9 preimages per fixed
value in any one H-coset; the displayed formulas give even smaller
bounds, but9 matches the already audited general argument.

For a selected candidate subset S, convolve each mask with1_S on H.
Parseval bounds its squared deviation from its mean by Lambda^2 L.
On a square coset, the word may choose either of two constant values;
Cauchy--Schwarz bounds their combined deviation in total agreements by
2 Lambda sqrt(kL). On a nonsquare coset there is only one value, so
this deviation is at most Lambda sqrt(kL). Summing four cosets and
dividing by L gives baseline3k/2, mean error4 Lambda, and deviation
at most6 Lambda sqrt(k/L), which is bounded by the8 Lambda term in(1).
At every coordinate, a nonconstant value is taken by at most9 orbit
candidates; its contribution after division is at most36k/L.
The extra1 is harmless (the displayed domain does not contain zero).
Minimum agreement is at most this average, proving(1).

## Passing from one orbit to the complete bank

The complete bank is

    Q_a(X)=sum_{j=0}^{k-1} binom(2k+1,2j+1) a^(2k-2j) X^j,

indexed by a modulo sign in F_p^*. Since
Q_a(X)=a^(2k)G(a^-2 X)-X^k, it splits into two k-element orbits.
One has a^(2k)=1 and a^-2 in H. The other has a^(2k)=-1 and a^-2
in a fixed coset h0H with h0^k=-1. Changing x to h0x, negating the
received word, and adjusting the common X^k term reduces the latter
to the same mask calculation. These operations merely permute the
full nonzero domain and change the arbitrary word.

At least half of any selected full-bank subset lies in one orbit.
Within it L<=k and Lambda<42 sqrt(k), so(1) divided by k is at most

    3/2 + 504/sqrt(L) + 37/L.

For L>=2^21 the last two terms are less than3/8, whereas
4a0>15/8. Hence that orbit cannot have L>=2^21 candidates all above
the first-order threshold. The complete bank therefore has fewer than
2^22 such candidates. The constant is not optimized.

## Research implication

Allowing p comparable to n was a valid relaxation for intrinsic list
size, but this familiar source still cannot prove linear list-size
tightness in the first-order regime. A growing list at quarter rate
and agreement above a0 needs a different polynomial family or a
substantial domain change. This result does not establish a general
constant-list conjecture; it only closes the stated Dickson route.
