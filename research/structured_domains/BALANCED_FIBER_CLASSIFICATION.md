# Classification of full balanced polynomial fibers

September 15, 2026. Pure coding-theory note. This classifies the inner
polynomial maps of a complete-fiber construction; it does not classify
all lists, affine received-word lines, or rational inner maps.

## Theorem

Let F be a field, let n >= 1, and suppose F contains n distinct nth
roots of unity D=mu_n. Let R in F[X] have degree B >= 1. Suppose R(D)
has M elements and each fiber in D has exactly B elements. Then
n=BM and

    R(X) = a X^B + b,       a != 0.

Conversely, for every B dividing n, every such polynomial has exactly
n/B images on mu_n and exactly B points in each fiber.

Thus the proposed hypothesis char(F)=p>n is sufficient, but stronger
than necessary. The distinct-root assumption already implies that the
characteristic does not divide n; that is enough for the theorem.

## Product identity and the proposed derivative proof

Let S=R(D), P(Y)=product_{y in S}(Y-y), and a=lc(R). The polynomial
P(R(X)) has degree BM=n, leading coefficient a^M, and all n elements
of D as roots. Hence

    P(R(X)) = a^M (X^n-1).                         (1)

Under p>n, differentiating gives

    P'(R(X)) R'(X) = a^M n X^(n-1).

The right side is a nonzero monomial. Every nonzero polynomial factor
of a monomial is a monomial, so R' is one. Its degree is B-1, since
p>B, and therefore R'=aB X^(B-1). All positive degrees below B are
also invertible in F, so integration gives R=aX^B+b. This proves the
original proposed version, including B=1 and B=n.

## Coefficient proof under the optimal separability hypothesis

Write b=R(0), T=R-b, and Q(Y)=P(Y+b). Thus Q is monic of degree M,
T(0)=0, and Q(T)=a^M(X^n-1). Suppose T has a nonzero coefficient
c_j at some degree 0<j<B, and choose the largest such j. The
coefficient of X^(n-B+j) in T^M is

    M a^(M-1) c_j.

It is nonzero: the characteristic does not divide n=BM, hence does
not divide M. Terms using two or more lower-degree factors have
smaller degree; every lower power of T appearing in Q(T) has degree
at most (M-1)B=n-B. Therefore the displayed nonzero coefficient
survives in Q(T), contradicting (1). Thus T=aX^B.

For the converse, x -> x^B is a group homomorphism mu_n -> mu_(n/B)
with kernel mu_B of size B; a nonzero affine change of its output
does not change its fibers.

The same conclusion holds with D a multiplicative coset c mu_n:
the product identity has X^n-c^n in place of X^n-1, and its other
coefficients still vanish.

## Edge cases and the actual scope of the result

* B=1: every degree-one polynomial has singleton fibers, as asserted.
* B=n, M=1: a full fiber means R-y=a(X^n-1). No exception occurs.
* n=1: necessarily B=1, and the same statement is valid.
* n=p in characteristic p: mu_p does not contain p distinct elements;
  X^p-1=(X-1)^p. The theorem's domain hypothesis is impossible.
* p<=n but p does not divide n: the coefficient proof still works.
  One must not merely integrate the derivative proof here, since
  polynomials in X^p have zero derivative.
* A degree-B polynomial whose fibers have a smaller common size is
  outside the hypothesis. So is a family using only some points of
  each polynomial fiber or a proper subset of the evaluation domain.

## Consequence for the saved divisor search

The reviewed note
`/Users/jthaler/Documents/stwo_audit_2026-09-15/agents/better_codes_divisor_search.md`
enumerates the divisors B of the fixed subgroup order, using inner
maps X^B and the incumbent generic fixed-core certificate. The theorem
shows that **every degree-B polynomial inner map using all subgroup
coordinates in full B-point fibers has that same partition**, up to
an affine relabeling. First-coefficient signature classes are preserved
under an invertible affine relabeling of fixed-cardinality subsets:
the transformed elementary symmetric coefficients are an invertible
triangular function of the originals. This does not require dividing
by small characteristic integers.

Accordingly, replacing X^B by another full balanced polynomial map
cannot enlarge the class of fiber partitions searched in that note.
This is a structural justification for its divisor restriction. It
does not independently verify its numerical table, eliminate nonlinear
coefficient statistics, or prove optimality outside its fixed template.
The phrase "rational pencil" in that note describes its outer
received-word construction; it does not make the inner map rational.

## Genuine rational escapes

The classification does not extend to rational inner maps. Here is
a uniform example. Suppose n is even, char(F) does not divide n,
and c is a nonsquare in the cyclic group mu_n. On D=mu_n define

    R(x) = x + c/x.

This rational map has degree two and no pole on D. For nonzero x,y,

    R(x)=R(y)  iff  (x-y)(xy-c)=0.

Consequently the fibers are {x,c/x}. They have two distinct points
because c is not a square in mu_n. Thus R is a full balanced map
with n/2 images. More generally, if 2d divides n, choose a nonsquare
c in mu_(n/d). Then

    R(x)=x^d+c/x^d

has rational degree 2d, no domain poles, and exactly 2d points in
every fiber on mu_n. Its image need not be a multiplicative coset.

There is an even broader elementary example when M=2. Partition
mu_(2B)=A disjoint-union A' into B-element sets, and let U,V be
their monic vanishing polynomials. Then R=U/(U+V) has fibers A and
A' with values 0 and 1. Its denominator is nonzero on both sets,
and its rational degree is B (U and V are coprime). This argument
is valid in characteristic two as well when the distinct-root
hypotheses permit the domain, but mu_(2B) cannot have 2B distinct
points in characteristic two. An independently checked cubic example
and critical-point analysis appear in
[`../gram_norm/BALANCED_FIBER_REVIEW.md`](../gram_norm/BALANCED_FIBER_REVIEW.md).

Rational pullback retains a useful code-theoretic degree bound. Write
R=A/C in reduced form with max(deg A,deg C)=B and C nonzero on D.
For every polynomial f of degree less than k,

    C(X)^(k-1) f(A(X)/C(X))

is a polynomial of degree at most B(k-1). Multiplying the composed
received word by the same nonzero coordinate function C^(k-1)
preserves all agreements. Balanced B-point rational fibers therefore
transfer a base list into dimension B(k-1)+1 on the full domain.
This statement alone provides no large base list or improved
certificate: both require additional analysis of the image domain.

## Nonfull polynomial escapes

The degree count in (1) uses all n roots and all B roots of every
selected fiber. Dropping either condition destroys that identity.
For example, over F_7, R=X^2+X has two full two-point fibers on
D'={1,2,4,5}, a proper subset of mu_6=F_7^*. The values are 2 on
{1,5} and 6 on {2,4}. This polynomial is not aX^2+b. The missing
coordinates are exactly where an argument based on full-domain
balanced fibers ceases to apply; puncturing changes code length,
rate, and gap and must be accounted for separately.

## Reproducibility

`verify_balanced_fibers.py` exhaustively checks normalized polynomial
maps in small prime fields, tests both boundary degrees, verifies
the rational involution families and denominator-scaled polynomial
pullback, and checks the nonfull example. Normalization removes the
irrelevant leading coefficient and constant output shift. Results
are recorded in `balanced_fiber_verification.json`. No protocol
experiments or acceptance claims are involved.
