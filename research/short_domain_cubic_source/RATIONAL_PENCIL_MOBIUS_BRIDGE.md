# Square-discriminant normalization and Möbius section families

This corrects the unresolved-quadratic-denominator discussion in RATIONAL_PENCIL_BUCHI_BRIDGE.md. Once one nonzero square specialization is available, no splitting-cover genus increase is needed. The conclusion is a Möbius family, not necessarily an affine polynomial family.

## 1. Normalize at an existing section

Let k be algebraically closed, char(k)≠2, K=k(X), and let N(u),T(u) in K[u] be coprime with max(deg N,deg T)=2. Write

    N−C T=a(C)u²+b(C)u+d(C),
    F(C)=b(C)²−4a(C)d(C).

Here a,b,d are affine in C, and a is not identically zero. The polynomial F has degree at most two and is not a square in K(C): otherwise N−CT factors over K(C), contrary to the degree-two rational map N/T. Every polynomial section P with finite label c supplies a square specialization

    F(c)=(2a(c)P+b(c))².

Choose a section label c0 with F(c0)=s²≠0. There are at most two excluded labels, so any family with at least three distinct labels permits this choice. Set

    H(Z)=Z² F(c0+1/Z)/s².

It is monic of degree two. Every other section label c supplies a square value at the distinct nonzero constant Z=1/(c−c0). If H has constant coefficients, undoing the substitution gives

    F(C)=s² q(C),  q in k[C], deg q≤2.

If H is a square in K[Z], F would be a square in K(C), impossible. Consequently Pasten's characteristic-zero Theorem 3.9 gives the displayed constant-shape discriminant as soon as nine distinct section labels exist. The positive-characteristic application and explicit height bound are handled separately by the frontier agent.

## 2. The constant-shape discriminant gives a Möbius family

Assume F=s²q as above. The polynomial q is nonsquare in k(C), so, over the algebraically closed constant field, it is a squarefree polynomial of degree one or two. The smooth projective conic

    v²=q(c)

has rational function field k(t). One can choose any of its constant points and use lines through that point to obtain a rational parameter t. No assertion about arbitrary rational fibrations is used.

Inside K(u), put c=N(u)/T(u) and

    v=(2a(c)u+b(c))/s.

Then v²=q(c), and conversely u=(sv−b(c))/(2a(c)). Thus

    K(u)=K(c,v)=K(t).

Since u generates K(t), it is a rational function of t of degree one. Equivalently,

    u=(A(X)t+B(X))/(C(X)t+E(X)),  AE−BC≠0,

with coefficients in K. Every actual polynomial section corresponds to a constant point of the conic and hence a parameter t in P¹(k). To justify this also at degree-drop labels, use the isomorphism between the smooth projective rational curves rather than dividing a(c) at that label. Distinct polynomial sections give distinct constant parameters.

The family need not be an affine polynomial line. For distinct constants t_j, put B(X)=product_j(X+t_j). The functions B(X)/(X+t_j) are polynomial members of one Möbius family and generally span more than an affine line. This example makes the local collision argument below necessary.

## 3. Local collision lemma

Let P_1,...,P_L be distinct polynomial members of a fixed Möbius family, all of degree at most D. At any coordinate x, write the coefficient matrix over the discrete valuation ring k[X]_(X−x), after clearing poles and dividing by its greatest common uniformizer power. Its reduction is nonzero and therefore has rank one or two.

If its rank is two, the reduced projective transformation is injective on P¹(k); all selected finite polynomial values are distinct. If its rank is one, every constant parameter except the unique kernel point maps to the same projective image. That image is finite because L≥2 and all selected functions are regular at x: at least one selected parameter is not the kernel point. Thus all but at most one selected polynomial have a common value at x. The possible kernel parameter can have another finite limit. This argument allows arbitrary poles in the originally written matrix coefficients and makes no bound on their degrees.

## 4. Degree-controlled agreement bound (sharpened by frontier audit)

Take n distinct coordinates and any received word. Let a be a lower bound on every selected candidate's agreement count, with L>1. At each coordinate let m_x count received matches and b_x count all agreeing candidate pairs. The local lemma gives m_x in {0,1,L−1,L}. Thus

    (m_x−1)(L−1) ≤ 2 b_x.

For m_x=L−1 use b_x≥binom(L−1,2); for m_x=L use b_x=binom(L,2); the other cases are immediate. The polynomial degree bound gives sum_x b_x≤D*binom(L,2), so

    (L a−n)(L−1) ≤ D L(L−1),
    L(a−D) ≤ n.

At surplus a−D≥eta*n, therefore L≤1/eta. This stronger direct-incidence argument supersedes the earlier h-coordinate estimate, which lost an unnecessary factor. It is valid for actual Möbius polynomial families in every characteristic.

In characteristic zero, fewer than nine labels supply at most sixteen sections; otherwise the Möbius bound applies. Thus the entire quadratic/quadratic rational-pencil class has at most max(16,floor(1/eta)) selected sections with surplus eta*n. In positive characteristic p>max(2,10D), the twenty-one-label height gate gives max(40,floor(1/eta)).

## Primary input

Hector Pasten, Theorem 3.9, printed page 5, author manuscript:
https://people.math.harvard.edu/~hpasten/preprints/pAdicTAMS.pdf

The nine-label statement uses eight remaining labels after reciprocal normalization. The present note does not extrapolate its characteristic-zero hypothesis to finite fields; that requires the separate Pasten–Wang height argument.
