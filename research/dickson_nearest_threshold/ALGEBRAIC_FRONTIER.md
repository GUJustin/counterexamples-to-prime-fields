# Algebraic frontier for the nearest Dickson word

September 17, 2026. The exhaustive F17 and F41 results have maximum
agreement3/8. No general3/8 ceiling is proved. The following elementary
strict improvement of the degree bound is valid, but is not claimed new
and does not resolve the exact-gap quadratic-extension target.

## A strict degree bound on any fourth-root domain

Let E have characteristic different from2 and5, and suppose X^(4k)-1
has4k distinct roots in E. Put W=(X^k-1)^2/2. For every P of degree<k,
W-P agrees with zero on at most2k-1 points of mu_(4k).

Proof. Suppose F=2(W-P)=X^(2k)-2X^k+A, deg A<k, divides X^(4k)-1.
Its monic quotient necessarily has the form

    G=X^(2k)+2X^k+B, deg B<k.

Indeed, comparison of degrees4k-1 down through3k gives the asserted
high coefficients. Comparing degrees3k-1 down through2k in FG forces
A+B=4. Set C=A-2, so B=2-C. The identity FG=X^(4k)-1 becomes

    C^2-4CX^k=5.

If C is nonzero, the left side has degree k+deg C>2deg C, contradicting
its being constant. If C=0, it forces5=0, also excluded. Thus F cannot
have2k distinct roots in the domain. This is a purely algebraic proof
and applies to the descended domains as well as the full prime-field
word. It is only a one-coordinate improvement over the trivial bound.

## Primary-source comparison

Solymosi, White, and Yip, *On the number of distinct roots of a lacunary
polynomial over finite fields*, arXiv:2008.09962v1, Theorem1.1 recalls
Redei's classification of degree(q-1)/2 divisors of X^(q-1)-1 with
second degree at most(q-1)/4. Its exceptional products also rule out
the coefficient -2 here outside characteristic5. Thus the strict
full-domain bound above should not be advertised as a new theorem.
Their Theorems2.1 and2.3 specialize with d=2, ell=0, deg g=k and
q-1=4k to the degree bound2k; their stated parameter improvements
do not give3k/2 at this boundary.
Source: https://arxiv.org/html/2008.09962

Li and Wan, *Distance Distribution in Reed-Solomon Codes*,
arXiv:1806.00152v3, Theorem1.5 gives a general main term and error
estimate for a received polynomial of degree k+m. Their Corollary1.9
uses m=p^delta with delta<1/4; the Dickson word has m=k=(p-1)/4,
so that asymptotic corollary does not apply. Their discussion also
states that m must be bounded by sqrt(q) for their estimate to be
nontrivial. No3/8 agreement ceiling follows from the quoted results.
Source: https://arxiv.org/html/1806.00152

The finite census supplies exact nearestness at p41. Neither that
census nor either cited result justifies assuming nearestness of the
3/8 Dickson bank at every larger prime. Current asymptotic proofs
correctly retain an unknown nearest agreement m in [3r/2,2r].
