# Independent quotient-variable compiler and generic image bound

September18,2026. **PASS** for the compiler, exact shifted-source/common agreements, and the collision bounds below. Product-surjectivity is a separate character-sum input owned by the other audit; it is not assumed in the generic bound.

Let E have q elements, let s be a proper divisor of q-1, put m=(q-1)/s, and G=mu_s. Assume2<=r<=s-1 and choose b outside G union{0}. Use the full domain E and the strict code dimension

    K=(r-2)m+1.

For every r-subset S of G, let V_S(Y)=∏_(a in S)(Y-a) and p_S(Y)=Y^r-V_S(Y). Its degree is at most r-1. Put Y=X^m and define

    f=Y^r/(Y-b), g=-1/(Y-b),
    lambda_S=p_S(b),
    h_S=(p_S(Y)-p_S(b))/(Y-b).

The denominator never vanishes on E, because the image of X↦X^m is G union{0}. The witness is polynomial of degree at most(r-2)m, hence admissible. The difference is

    f+lambda_S g-h_S=V_S(Y)/(Y-b).

Consequently every witness has **exactly rm matches**, the m nonzero preimages of each of the r tags. Zero is not an additional match because V_S(0)!=0. Different supports can produce the same label or witness; no injectivity is assumed.

## A useful source shift: both sources are exactly far

Replace f by

    f*=f+b^r g=(Y^r-b^r)/(Y-b).

This is a monic polynomial of degree r-1 in Y. Its bank labels become

    lambda*_S=lambda_S-b^r=-V_S(b),

all nonzero. For every admissible Q(X), f*-Q is nonzero of degree(r-1)m, and (Y-b)Q+1 is nonzero of degree at most(r-1)m. Thus both f* and g have agreement at most(r-1)m.

For the matching lower bound, fix any r-1 tags in G. Interpolate the values of f* and g separately at these tags by polynomials in Y of degree at most r-2. The two admissible witnesses match on the SAME(r-1)m full fibers. Therefore, on the full E domain,

    agr_K(f*)=agr_K(g)=CA_K(f*,g)=(r-1)m.

This is exact ordinary common agreement. The threshold rm has gap m above both sources. Zero challenge is far. If the fixed-size products {V_S(b)} cover E*, then **every nonzero challenge is near**, with exact bad-label set E* at this threshold. This implication needs no extension of E and no additional source projection.

## Generic averaged pole bound with all exclusions accounted for

Let L=C(s,r), B=q-s-1, and average b over the B admissible poles. For S!=T, p_S-p_T=V_T-V_S is nonzero of degree at most r-1. It vanishes at every element of S intersect T, all of which are excluded poles. If the root products agree it also vanishes at0, another excluded pole. Hence the number of admissible collision poles is at most

    r-1-|S intersect T|-1_(product(S)=product(T)).

This is nonnegative: when the intersection has size r-1, equal products would force S=T. Let L_c be the number of r-subsets with product c in G, and C=C(s-1,r-1). Summing the preceding bound over ordered distinct pairs gives

    D=(r-1)L(L-1)-s C(C-1)-Σ_c L_c(L_c-1).

Thus some admissible b has sum_lambda multiplicity(lambda)^2 <= L+D/B, and Cauchy gives

    #image >= ceil(B L²/(B L+D)).

This is a rigorous root-count/second-moment guarantee, not a claim of the best possible image bound by every method. The parallel elementary collision bound also gives #image>=ceil(L-D/(2B)); take the larger useful bound, capped by the evident range, if L is small.

Omitting the product correction gives the simpler explicit form

    #image >= ceil[B/(r-1-r²/s+(B+1)/L)].

The product correction is exactly computable by cyclic subset-product counts. Without computing them, writing L=as+t with0<=t<s gives ΣL_c²>=s a²+t(2a+1), a rigorous balanced-occupancy improvement. One must not assume product counts or moment coefficients are random.

## Population and coverage scales

For r~rho*s with fixed0<rho<1, the collision coefficient r-1-r²/s is asymptotic to rho(1-rho)s. If s=o(q) and L is at least a constant times q/s, the displayed bound is of order q/s. Thus s=Theta(log q), with C(s,r)>=Omega(q/s), gives the desired generic q/log q scale. Merely increasing L beyond q/s removes the population term but leaves the order-s collision term. It does not prove constant-fraction or nearly complete coverage in this fixed-density regime.

There ARE different regimes where the generic bound is stronger: fixed r gives a constant fraction once L is sufficiently large, and r=2 with s/sqrt(q)→infinity and s=o(q) gives q-o(q) labels directly. For E=Fp^5, s=(q-1)/(p-1)~p^4 and r=2 is such an example. Its code has dimension1 and threshold2(p-1), however; it is not a fixed-rate or first-order benchmark construction.

A separate elementary structural improvement occurs for G=Fp*, E=Fp^5, r<=5 and b outside Fp. Every p_S has base-field coefficients and degree at most4, so evaluation at the degree-five element b is injective on these polynomials. Hence all C(p-1,r) labels are distinct for every such b. At r=5 this gives asymptotic fraction1/120 of E, but again the resulting rate tends to zero. This fact does not justify surjectivity when r grows.

For the intended fixed-rate choice G=Fp*, r proportional to p, the generic bound is only order q/p. A proof that the products of r DISTINCT factors b-a cover E* would improve it to q-1 via the exact source shift above. That is a real additional character-sum theorem, not a consequence of pair-collision averaging. The collaborator's separate Katz/product proof is the appropriate input to audit.

## Scope

For G=Fp*, m=p^4+p³+p²+p+1. Fixed r/(p-1) gives a fixed asymptotic code rate and source gap m=Theta(q^(4/5)), while characteristic is q^(1/5). The message degree is much larger than p, so the DKT large-characteristic guard is not met. The domain/alphabet are the full extension field, not a prescribed short prime-field NTT domain. These compiler statements alone imply no better.codes score or prime-alphabet result.
