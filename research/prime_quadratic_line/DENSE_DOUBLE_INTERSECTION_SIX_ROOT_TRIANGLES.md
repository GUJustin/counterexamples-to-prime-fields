# Dense double intersections force many six-root quadratic pencils

September 19, 2026. Exact combinatorial and algebraic lemma; no scan.
This concerns one received word and its ordinary list, not an affine
received line or singleton lists.

Let D⊂Fp have n elements, with p odd, and let q_1,...,q_M be
distinct polynomials of degree at most two. For a word f on D,
choose exactly T agreement coordinates S_i for each q_i. Assume

    T≥3,       (T−1)²>n−1.

Any two S_i intersect in at most two coordinates. Form the graph
Γ whose edges are the pairs with intersection size two, and let
m=|E(Γ)|. Put

    R=(n−1)(T−2)/[(T−1)²−(n−1)],
    R_+=max(R−2,0).

## 1. An exact six-root triangle bound

The edge count satisfies

    m ≥ [M²(T²/n−1)−M(T−1)]/2.                             (1)

Moreover the number of triangles in Γ whose three pairwise
intersection sets are disjoint is at least

    m(4m−M²)/(3M) − R_+ M(M−1)/3,                          (2)

with a negative right side understood only as a vacuous lower bound.

**Proof of (1).** Write r_x=|{i:x∈S_i}|. Then Σ_x r_x=MT and

    I:=Σ_x binom(r_x,2)
      ≥[(MT)²/n−MT]/2.

Since I counts pair intersections, I≤binom(M,2)+m. Rearranging
gives (1).

**The local multiplicity bound.** Fix x with r_x>0. Remove x
from every S_i containing it. These r_x sets each have T−1
elements on n−1 coordinates and pairwise intersection at most one.
A second incidence count gives

    r_x(T−1)²/(n−1)−(T−1)≤r_x−1,

hence r_x≤R. Equivalently, subtracting one anchor value and dividing
q_i−f(x) by X−x reduces this sublist to distinct affine polynomials;
the count is the elementary linear-code Johnson bound.

**Triangle supply and removal.** If d_i are the graph degrees,
each edge ij has at least d_i+d_j−M common neighbors. Therefore

    3·#triangles ≥ Σ_i d_i²−Mm
                 ≥4m²/M−Mm.

Triangles whose supports have a common coordinate number at most

    Σ_x binom(r_x,3)
       ≤(R_+/3) I
       ≤(2R_+/3) binom(M,2).

Subtracting this from the graph triangle bound proves (2).

A remaining triangle has six distinct coordinates: a coordinate
belonging to two of its pairwise intersection sets would belong to
all three supports. Thus the three disjoint two-element intersections
are indeed six distinct native points. ∎

In particular, suppose n tends to infinity,

    T=(c+o(1))sqrt(n),    sqrt(3/2)<c<sqrt(2),
    M/sqrt(n)→∞.

Then the double-edge density is at least c²−1−o(1)>1/2,
R=O_c(sqrt(n)), and (2) is Ω_c(M³). More explicitly, writing
β=c²−1, the displayed estimates give

    #six-root triangles
       ≥[β(2β−1)/6−o(1)] M³.                              (3)

This strengthens the plain Mantel conclusion: the abundance cannot
be accounted for by triangles sharing a common coordinate, including
common-two-root pencils.

## 2. The exact identity on each surviving triangle

For one such triangle, write its root pairs as

    {a,b}=S_1∩S_2,  {c,d}=S_2∩S_3,  {e,f}=S_3∩S_1.

All six coordinates are distinct. Each difference q_i−q_j has
degree exactly two and has precisely its displayed pair as roots.
The three differences sum to zero, so their monic coefficient
vectors are linearly dependent:

    det [ 1  a+b  ab
          1  c+d  cd
          1  e+f  ef ] = 0.                               (4)

The three (sum,product) points are distinct. Hence they lie on one
unique affine line, which can be written

    α uv + β0(u+v)+γ=0                                    (5)

for each of the three unordered pairs, with (α,β0,γ) nonzero.
It is nondegenerate:

    β0²−αγ ≠0.

Indeed, if this scalar vanished, then α≠0 and (5) would factor as

    α(u+β0/α)(v+β0/α)=0,

forcing all three pairs to share a root. This contradicts their
disjointness.

Consequently the unique projective transformation

    ι(z)=−(β0 z+γ)/(α z+β0)                               (6)

is a nonidentity involution over Fp, and it swaps a↔b, c↔d, e↔f.
Its matrix squares to (β0²−αγ) times the identity. None of the
six denominators vanishes, by (5) and nondegeneracy.

Thus (3) supplies Ω(M³) polynomial triangles, each determining a
quadratic pencil with three distinct split fibers and six native
roots. The pencils need not be distinct. This is an exact relation,
not only a statement that all relevant discriminants are squares.

## 3. What this does and does not force

A triangle with two common roots has collinear coefficient points.
A triangle with exactly one common root lies in its evaluation plane.
Both kinds are included in the O_c(M²sqrt(n)) removed term.

For each surviving triangle, the quadratic differences span a
two-dimensional linear space determined by its involution. Its three
coefficient points lie in an affine translate of that space.
The result does not identify these spaces for different triangles.
Even the same involution may arise in several parallel affine
coefficient planes.

In particular, no common conic, global coefficient plane, or large
common-root pencil is proved. Nor is a counterexample to such stronger
rigidity in the full M≫sqrt(n) regime constructed here. The new
necessary input for that regime is the quantitative supply (3) of
nondegenerate six-root identities (4)–(6). Exploiting it requires
control of how many triangles can share one involution or one
coefficient plane; counting all involutions alone supplies no such
control.
