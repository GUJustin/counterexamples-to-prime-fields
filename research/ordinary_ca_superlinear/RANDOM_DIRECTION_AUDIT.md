# Independent audit of random padding directions

September 17, 2026. Audited the proposed RANDOM_DIRECTION_QUADRATIC.md
against CONSTANT_EXTENSION_PADDING.md, PROOF.md, the current ordinary-CA
appendix, and the quadratic-indicator rigidity appendix. No mathematical
flaw found. The conclusions require sufficiently large members of the
unbounded source family, as stated; this is an existence proof, not an
efficient algorithm for finding directions.

## Direction exclusion and ordinary correlated agreement

For any nonzero degree-<K polynomial G with T direction agreements,
choose exactly T of its agreements. If z are old coordinates, z<=K-1
because the old direction is zero, and j=T-z lie among the new points.
The z homogeneous evaluation constraints have rank z, so there are
H^(K-z) candidate polynomials (including zero, harmless for an upper
bound). A fixed candidate has probability at most (H-1)^(-j) of matching
the independent nonzero direction values. If any prescribed value is
zero this probability is actually zero. Thus the displayed union bound
is valid. Every term is H^(-Delta)(1-1/H)^(-j), and j<=t yields the stated
coarser estimate after summing the binomial coefficients.

For a putative ordinary-CA pair (F,G), G!=0 is excluded on its direction
condition alone, regardless of F or the intercept. If G=0, no fresh
coordinate can be a joint agreement because its direction is nonzero;
on the core F has at most T-1 agreements. This checks all polynomial
pairs, rather than just the selected nearest list. Enlarging the
coefficient field also cannot create a direction witness when T>=K:
K matched field-valued evaluations force its coefficients into E.

## Source operations and order of choices

Common-zero blocks preserve the true maximum for all polynomials, and
preserve each of the r selected candidates. Subsequent coefficient
extension preserves that maximum by interpolation. One incidence anchor
retains at least M' r/N' candidates; subtraction and division is injective
on this selected bank, lowers dimension and each selected agreement
count by one, and preserves the true maximum (any larger quotient lifts
to a contradiction). Its distinct quotients have degree <K, so each
pair has at most K-1 equal evaluations.

The coordinates can therefore be selected first by diversity. The
random-direction argument works for every such selection of distinct
fresh coordinates. Once a good nonzero direction is fixed, independently
uniform intercepts give independent uniform translations of the scaled
evaluation sets. Scaling does not change their cardinalities. There is
no conditioning on intercepts in the direction certificate, so this
order of choices introduces no dependency problem. Each counted label
has T-1 core matches and a fresh match.

Writing S=H-N_c, pairwise-root counting gives mean diversity at least
ell*S/(S+(ell-1)(K-1)). This is >=ell/2 for large r in every claimed
case. The sum on the t best points is >=t*ell/2. Independent translations
have expected union H[1-product_x(1-a_x/H)], which is at least
H[1-exp(-t*ell/(2H))]. If t*ell/(2H)<=1 this is >=t*ell/4. The same
reasoning applies with Delta counted points and arbitrary extra points.

## Exact rate 1/8 and gap 1/16

The full-field rigidity corollary gives m<=5r/3 after orbit descent;
it applies because p=4k+1>8k/3 and p>5. Together with m>=3r/2,
r/2+1<=Delta<=2r/3+1. For r>=6, Delta<=r-1, so
s=2Delta-r+1 lies in [1,Delta] and one quadratic zero block suffices.
After anchoring, (N_c,K,T)=(3r+2Delta,2Delta,3Delta), and appending
t=14Delta-3r points gives n=16Delta exactly.

The available field has H=p^2>16r^2; all required coordinate counts are
O(r). For r>=21, t<=7r and hence t*ell/(2H)<7/32, using ell<=r.
Also r<=2Delta-2 implies t>=8Delta+6. The retained count satisfies
ell>=3Delta*r/(3r+2Delta+1)>=2Delta/3 whenever 3r>=4Delta+2;
r>=3(Delta-1)/2 suffices when Delta>=13. Thus J>=n^2/192, with
ceiling justified because J is an integer. K-1=2Delta-1<p.

The logarithm of the direction failure bound is
n*log(2)-Delta*log(H)-t*log(1-1/H), which tends to minus infinity:
its negative term is Omega(r log r), its first positive term is O(r),
and its last positive term is O(1/r). Thus a good direction exists.

## Parameter family

For fixed b in {2,3,4,5} and d>=b+7, s=bDelta-r+1 is positive and at
most (b-1)Delta. At most b-1 quadratic blocks suffice, and all resulting
field degrees divide 2^(b-1); enlargement to E=F_(p^(2^(b-1))) is valid.
After anchoring, N_c=3r+bDelta, K=bDelta, T=(b+1)Delta. Padding with
t=(d-b)Delta-3r gives n=dDelta and t>=Delta+6. All lengths remain O_(b,d)(r),
so the direction estimate tends to zero over this fixed-degree field.

The retained count is >=(b+1)Delta*r/(3r+bDelta+1)
>=(b+1)r/(b+6), since 3r+1<=6Delta. Counting only Delta diverse points,
Delta*ell/(2H)<1 for large r and J>=Delta*ell/4. Since r>=Delta,
this gives (b+1)n^2/[4(b+6)d^2]. Finally
K-1<=5(2r/3+1)-1<4r+1<=p for r>5. The final agreement-rate difference
is exactly 1/d; the usual characteristic-Elias correction tends to zero.

## Scope

The proof establishes the proposed quadratic-extension special case
and the stated fixed-degree family. It does not provide a prime-ambient
example, an intrinsic first-order lower bound, or a better.codes gain.
The proposal contains a harmless typographical `divide,+retaining`.
