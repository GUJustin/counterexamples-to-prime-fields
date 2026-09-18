# Independent review: norm-one direct list and its significance

Verdict: PASS for the splitting construction and matched finite DKT upper bound, with a stronger elementary exact classification for this particular word. No literature novelty claim is certified here. Primary formulas were read directly in `tmp/eprint-2056/paper.txt`, Lemma 5.6 (54),(56) and Proposition 5.10 (60)–(63).

## Construction and finite certificate

Use p>=4099, E=F_{p³}, L=p²+p+1, G=ker Norm, D={x:x² in G}, N=2L, f=x^{2p+2}. The subgroup G has odd order L, dividing (p³−1)/2, so each member has two square roots in E and D is the order-2L subgroup. For Norm(a)=−1, Q_a=aX²−a^(p²+1) has 2p+2 matches. The substitution y=a^(p²)z is correct: the coefficient of z after division is one and the constant is one, yielding z^{p+1}−z+1. Its threefold Möbius identity, squarefreeness and Norm(z)=−1 prove all p+1 roots are in G after rescaling. The L distinct witnesses are valid.

At A=2p+2 the Johnson pair count gives exactly L as stated; A²−2N=4p. This is classical exact Johnson saturation, above that bound's agreement radius.

At T=2p−ceil(4sqrt(p))−4, the primary support uses m=6, derivative cap 3, B=3T, H=40B. The derivative-weighted coefficient count is Gcoef=4B²−2B and local ranks sum to 62. The conservative graded margin is B(39Gcoef−40N*62)+(Gcoef−N*62). With 29p/5<=B<=6p its inner margin is at least (7196/25)p²−5428p−4960>0 at this onset. Characteristic restriction is p>max(D,3)=3, not p>B. For a fixed word one can directly use Gcoef>N*62; the stronger challenge-degree certificate is harmless.

Equation (54), D=2 and M=3, gives tau=1,u=B,v=4,Freg=7B−12,S=5B−9. Equation (56) therefore gives the codewide bound

 floor[((N−2)/(T−2))(21T−12)+15T−9] <=22N.

The fixed-word provision in Lemma 5.6 explicitly applies a new nonzero fixed-word equation separately. Thus no generic-fiber specialization assumption is being smuggled into the uniform bound. This proves a uniform upper bound over all words and all evaluation sets of size N, not merely this norm word.

## Stronger elementary classification at the advertised threshold

In fact the norm word's list is exactly L already at every threshold T'>p+1 with T'<=2p+2.

Write an arbitrary quadratic Q=aX²+bX+c. For x in D, set y=x^p,z=x^{p²}. Since Norm(x)^2=1, x²y²z²=1. A match gives x²y²=Q(x), and its Frobenius conjugate gives y²z²=a^p y²+b^p y+c^p. Multiplication by x² yields

 r(x):=1−a^p Q(x)−c^p x²=b^p x²y.

If b!=0, eliminate y by squaring:

 r(x)²−b^(2p)x²Q(x)=0.

This is a polynomial of degree at most four. Unless identically zero it permits at most four matches. If identically zero, r/(b^pX) is a rational square root of Q; a rational function whose square is a polynomial is itself polynomial. Thus Q=(uX+v)² over E. Because b=2uv!=0, both u and v are nonzero.

The original unsquared equation fixes the sign and improves the outsider bound. Choose the specific polynomial square root H(X)=r(X)/(b^p X), rather than an arbitrary square root. At every matching nonzero x, r(x)=b^p x² x^p gives

 x^{p+1}=H(x).

Since H is linear, all these matches lie in the zero set of one degree-(p+1) polynomial. Thus the identity case has at most p+1 matches; there is no need to add roots from the other sign branch. Together with the nonidentity quartic bound, every non-even outsider has at most max(4,p+1)=p+1 matches for odd p.

If b=0, put w=x² in G. The equation is w^{p+1}=a w+c. When a,c are nonzero, more than two E-roots forces c=−a^(1+p²). Every one of its p+1 roots then has Norm(w)=−Norm(a): substitute w=a^(p²)z into z^{p+1}−z+1=0. Thus either Norm(a)=−1 and the polynomial is precisely a displayed bank member, or none of those roots lies in G. If the Möbius identity fails, at most two w-roots lift to at most four x-matches. Cases a=0 or c=0 contribute at most four x-matches as well: a=0,c!=0 gives a reciprocal Möbius map whose odd threefold composition cannot be identity; c=0 gives w^p=a and at most one nonzero w; a=c=0 gives none.

Consequently every polynomial outside the L-member bank has at most p+1 matches on D. Since the advertised T exceeds p+1 for p>=4099, its list is exactly N/2. This strengthens the original note's cautious lower-threshold non-completeness statement without changing the construction.

## Candid significance

For this special received word, a new O(N) upper bound does not require DKT: the preceding elementary algebra gives the exact N/2 list and an outsider cutoff p+1. At the actual nearest threshold 2p+2, ordinary Johnson already gives the same exact size.

The 22N comparison is still a genuinely different statement: it bounds every received word at the lower, below-Johnson threshold T. Ordinary Johnson counting is vacuous there because T²−2N<0. The elementary three-coordinate interpolation packing gives only binom(N,3)/binom(T,3)=Theta(N^(3/2)), not O(N). Thus these standard elementary bounds do not subsume the uniform DKT statement. No exhaustive literature claim that no other uniform O(N) theorem exists is made.

The defensible contribution is an explicit classical-geometry list of size N/2 at parameters where a checked first-order certificate gives a uniform O(N) upper bound, with exact classification of the example. The construction uses a two-dimensional witness span and classical projective-plane incidence; presenting its list itself as a new uniform upper-bound phenomenon or as fixed-rate DKT tightness would overstate it. Rate 3/N and normalized agreement both vanish; E is an extension field, not a prime alphabet. It supplies no received-line exception count or two-far statement by itself.
