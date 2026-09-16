# Multiplicative relabeling distinguishes binary subspaces by short prefixes

September 16, 2026. Twice self-reviewed; exact checks passed. No
independent coauthor review or novelty claim. This stronger statement fixes the relabeling to be multiplicative,
while permitting all subspaces rather than one multiplicative orbit.

## Statement

Let K=F_(2^m), N=2^m, and let chi:K^* -> E^* be an injective multiplicative
character into a field E of characteristic different from two. Label
v!=0 by x_v=chi(v), or by any affine transform a*chi(v)+b with a!=0.
For an r-dimensional binary subspace U of K, let H_U be its annihilator
under the absolute trace pairing. Put t=2^r-1.

Two distinct punctured supports H_U minus zero and H_V minus zero
cannot share their first 2t-1 locator coefficients. In characteristic
zero or characteristic greater than t, the first t coefficients already
distinguish them. A prefix longer than the locator degree is understood
as unavailable, so the assertion concerns the regime where the indicated
prefix fits. For fixed r, it applies for all sufficiently large N.

For binary codimension two, three leading coefficients suffice when
char(E)>3, and five suffice in every odd characteristic. Thus the
entire binary quadratic family, not just a single orbit, has singleton
prefix classes under this natural multiplicative relabeling once N is
large enough. Arbitrary injective relabelings are not covered.

## 1. Gauss sums transfer moments to the small dual subspace

Let psi(v)=(-1)^Tr_(K/F2)(v), and for 1<=j<N-1 put

    G_j=sum_(v!=0) psi(v)*chi(v)^j.

The multiplicative character chi^j is nontrivial. A direct calculation
gives G_j*G_(-j)=N in E. Indeed write x=ty in the product:

    G_j*G_(-j)
       =sum_(t!=0) chi(t)^j * sum_(y!=0) psi((t+1)y).

The inner sum is N-1 at t=1 and -1 otherwise; the nontrivial character
has total sum zero. Therefore the result is N, nonzero in odd
characteristic. Every G_j is invertible.

Expanding the indicator of H_U with additive characters gives

    sum_(v in H_U minus zero) chi(v)^j
       = (G_j/2^r) * sum_(u in U minus zero) chi(u)^(-j).       (1)

The u=0 term vanishes because chi^j is nontrivial; for u!=0 substitute
y=uv into the inner Gauss sum. Thus equality of the first s moments
of two large primal supports implies equality of the first s moments
of the t-element dual label sets {chi(u)^(-1): u in U minus zero}.

## 2. Recover the dual set

Shared locator prefixes imply shared power sums by Newton identities,
without division. If char(E)=0 or exceeds t, moments 1 through t
recover the t elementary symmetric functions by the reverse Newton
identities, hence recover the dual set and U itself.

In arbitrary odd characteristic, use moments zero through 2t-1.
The zeroth moments agree because both dual sets have t elements. The
difference of their indicator measures has support at most 2t, and
its weights are nonzero signs at points in the symmetric difference.
Distinct dual labels make the square Vandermonde matrix on that support
invertible. Vanishing moments therefore force the symmetric difference
to be empty. Injectivity of chi gives U=V.

For affine relabeling a*chi(v)+b, equal moments imply equal chi-moments
inductively via the binomial expansion: the diagonal coefficient a^j
is invertible. This needs no restriction on binomial coefficients.

## 3. The t-coefficient cutoff is sharp

If r divides m, take U=a*F_(2^r). Its annihilator is F_(2^r)-linear,
so its nonzero elements are a union of multiplicative F_(2^r)^* cosets.
Under chi, each such coset becomes a full coset of the t-th roots of
unity. Its locator is therefore a polynomial in X^t: the first t-1
coefficients below the leading term vanish. There are (N-1)/t distinct
annihilators of this form. Thus the first t-1 coefficients can coincide
on a linear-sized family, while the first t distinguish all of them
in the large-characteristic regime. The sharpness example concerns a
constant prefix length, so its agreement gap shrinks with N.

## Scope

This closes the direct multiplicative or affine-multiplicative lift of
the binary subspace locators into odd fields. It does not close a
nonmultiplicative relabeling mixing many subspace orbits, the remaining
route not ruled out by the earlier transfer theorems. No general
prime-field list bound or quadratic MCA lower bound is inferred.


## Verification

Six prime-field fixtures exhaust 26,114 subspaces, with raw and affine
multiplicative labels. A characteristic-three field of degree 30
checks 155 more subspaces without dividing by three. There are 27
Gauss-product checks and 126,361 primal--dual moment identities.
A separate N=512 codimension-three fixture has 73 locators with six
common zero coefficients and distinct seventh coefficients. The
written argument proves the universal theorem; these checks do not.
