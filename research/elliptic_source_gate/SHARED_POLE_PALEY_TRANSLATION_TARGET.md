# A distinct shared-pole elliptic target

The simple symmetrized-translation family is blocked by `ARBITRARY_WORD_POLE_BARRIER.md`. The following explicit family changes the pole geometry: each candidate uses essentially the same LARGE pole divisor. It is not a claimed construction; its required agreement inequality is stated as an exact bounded gate.

Let ell>=3 be odd prime, E a nonsingular elliptic curve in characteristic p>3, p!=ell, and H=E[ell] with a chosen basis identifying H with F_ell². Put M=ell². Choose a nonsquare nu in F_ell and define

    c_(a,b)=quadratic_character_ell(a²-nu*b²), c_(0,0)=0.

Thus c_T=c_-T, and c_T is+/-1 for T!=0. Define

    F(P)=sum_(T in H) c_T*x(P+T),
    G_S(P)=F(P+S)+F(P-S), S in H/{+/-}.

Each G_S is even in P and therefore a rational function of X=x(P). Let t_T=x(T) and

    D0(X)=product_(T in (H\{0})/{+/-})(X-t_T)²,
    R_t(X)=2[tX²+(t²+A)X+At+2B]/(X-t)².

Then the explicit polynomial candidate is

    Q_S(X)=D0(X)[2c_S X + sum_(T nonzero modulo sign)
                    (c_(T-S)+c_(T+S))*R_(t_T)(X)].

No elliptic function evaluation is needed after the t_T have been tabulated. The common denominator has degree M-1, and deg Q_S<=M (equal to M for S!=0). There are exactly (M+1)/2 DISTINCT candidates, and their linear span has dimension (M-1)/2, in characteristic zero or any characteristic p not dividing2ell. Here is an elementary certificate. In the additive group algebra of H, the coefficient array c is the quadratic character of F_(ell²), so

    c*c = M delta_0 - 1_H.

Indeed the coefficient at0 is M-1, and every other coefficient is-1 by the elementary quadratic-character sum for x(t-x). Thus convolution by c is invertible on the augmentation-zero subspace, with inverse c/M. Two translates symmetrized by sign correspond to h_S=delta_S+delta_-S. If c*h_S=c*h_T, their augmentation-zero difference must vanish, so S=+/-T. Finally the h_S span the even functions, dimension(M+1)/2; convolution kills exactly the constant array and has rank(M-1)/2 there. The rational functions inherit this rank because their principal parts at the distinct torsion poles recover the coefficient arrays. Consequently

    Q_0 + 2 sum_(S nonzero modulo sign) Q_S = 0

is the unique linear relation up to scale. This supplies a genuine scalable algebraic bank and an exact dependency, but still no high-agreement word.

This is not the old R_(t_S) disjoint-pole family. At a given pole t_T many Q_S can have nonzero values, and differences retain poles across H rather than only at two label-specific points. Thus the constant4 residual pair-intersection bound is absent. The old arbitrary-word obstruction does not apply.

## Concrete first gate

Use ell=5, M=25, thirteen labels S modulo sign, degree bound25. Seek E/F211 with full rational5-torsion and at least100 finite x-coordinates of rational points (a curve with225 points would suffice). This is a finite, inexpensive existence check, not an assumption. If such a curve is unavailable, change the small split prime while retaining the same thirteen-label test; no broad search is implied.

For each finite rational x-coordinate, evaluate all thirteen Q_S, including the cleared pole coordinates by polynomial evaluation. Let b(x) be the largest equal-value bucket. On any100-node domain and for any word, minimum agreement of the FULL thirteen-candidate bank is at most

    floor(sum_(100 largest b(x)) b(x)/13).

At k=26,n=100 the required first-order threshold is a1(26/100); compute its exact quadratic inequality. If this upper bound is below the threshold, discard this fixture before word optimization. If it passes, solve the finite bucket-selection balancing problem: choose at most one value bucket at each selected coordinate, maximizing the minimum candidate coverage. A positive word must then be verified by direct evaluation; an average bound alone is not existence.

This is one explicit untested mechanism and a bounded falsification gate, not an established improvement. A finite hit would still require a scalable identity or family argument. The torsion model's divisor ledger is favorable only in the limited sense that it avoids the already-proved moving-pole pair bound; it supplies no agreement estimate by itself.
