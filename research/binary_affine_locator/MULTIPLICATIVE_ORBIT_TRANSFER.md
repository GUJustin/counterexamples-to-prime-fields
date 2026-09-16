# Every fixed multiplicative orbit has a sublinear transfer bound

September 16, 2026. Generalization of the F4-linear calculation in
`F4_HYPERPLANE_TRANSFER.md`; this is the authoritative general proof.
Twice self-reviewed; exact checks passed in both stabilizer cases and
at codimension three. No independent coauthor review or novelty claim.

## Statement

Let K=F_(2^m), N=2^m, m>=6, and fix a two-dimensional binary subspace
U of K. For a!=0 define the codimension-two subspace

    H_a={v in K: Tr_(K/F2)(a*u*v)=0 for every u in U}.

Injectively label K minus zero into a field E of odd characteristic.
If a collection C of the distinct H_a has punctured locators sharing
their first s=N/8-1 coefficients, then

    |C| <= (4/h) N^(15/16),
    h=|{c in K^*: cU=U}| in {1,3}.

For h=3 this is precisely the F4-linear hyperplane case, with bound
(4/3)N^(15/16). Otherwise the multiplicative orbit has N-1 members,
and its common-prefix subfamily still has size o(N). The result allows
arbitrary injective odd-field relabeling. It does not cover an arbitrary
union of an increasing number of multiplicative orbits.

## Proof

Let A contain all normals a for hyperplanes in C, so |A|=h|C|.
Newton identities give equal power sums through order s, including the
common zeroth moment N/4-1; no division by the moment index is needed.

Suppose A contains a five-flat a_e=a_0+sum e_i*w_i. For beta!=0 its
normalized Walsh coefficient at v!=0 is

    c_beta(v)=1/32 sum_e (-1)^(beta dot e) 1[v in H_(a_e)].

All moments sum_v c_beta(v) x_v^j vanish for 0<=j<=s. The trace
character identity for the annihilator of U is

    1[v in H_a]=(1/4) sum_(u in U) (-1)^Tr(a*u*v).

Consequently

    c_beta(v)=(1/4) sum_(u in U minus zero:
                               Tr(w_i*u*v)=beta_i for all i)
                            (-1)^Tr(a_0*u*v).

For fixed nonzero u, multiplication by u preserves independence of
the five w_i. The trace pairing is nondegenerate, so its fiber has
N/32 points. Thus the support of c_beta has size at most 3N/32.
At least one such vector is nonzero over E: otherwise invertibility
of the Walsh transform would make all 32 incidence rows identical,
whereas at most three normals can give one H_a. (The annihilator aU
contains each scalar's fixed nonzero-U multiple, giving that bound.)

Since s+1=N/8>=3N/32, a square Vandermonde minor on that support
contradicts the vanishing moments. Thus A is five-flat-free. The
elementary quotient induction in `F4_HYPERPLANE_TRANSFER.md` gives
|A|<=4N^(15/16), proving the count.

For the stabilizer assertion, the set {c in K: cU subset U} is a
finite subfield: it contains zero and one and is closed under addition
and multiplication; every nonzero element acts bijectively on U.
The binary dimension of U is two, so that subfield has size two or
four. The latter case makes U a scalar copy of F4 and requires even m.
The nonzero stabilizer size is therefore one or three.

## What this changes

A linear-sized common-prefix list would suffice for quadratic MCA by
the paper's padding reduction. Neither one multiplicative orbit nor
any bounded number of such orbits can supply that list after odd-field
transfer. In fact a collection of cN supports would have to occupy at
least (c/4)N^(1/16) different orbits, from the uniform per-orbit bound.

The full binary codimension-two family has quadratically many supports
and linearly many multiplicative orbits. The global O(N^(3/2)) bound
still permits a linear-sized common-prefix collection spread across
many orbits. That remaining route is not ruled out here.

## General fixed codimension

The same proof works for any r-dimensional binary subspace U. The
incidence character expansion has 2^r-1 nonconstant characters. At a
binary b-flat of parameters, each nonzero Fourier coefficient has
support at most (2^r-1)N/2^b. Choose

    b=ceil(log2((2^r-1)N/(s+1)))

for 0<=s<=N/2^r-2, and assume b<=m. The cube has more parameters
than the at-most-2^r-1 normals giving one hyperplane, and the support
bound is at most s+1. The identical Vandermonde argument excludes a
b-flat. With h the nonzero scalar stabilizer size, the result is

    |C| <= (4/h) N^(1-2^(1-b)).

For fixed r and a fixed positive prefix fraction (s+1)/N, b is bounded,
so this is o(N) for each multiplicative orbit. The proof applies to
every fixed codimension, not just F4-linear or codimension-two families.
The stabilizer is the nonzero part of a subfield of binary degree
dividing r, hence h<=2^r-1. The finite checks include a codimension-three
orbit over F256 with seven-dimensional affine parameter sections.


## Exact checks

The standard-library checker verifies 7,495 Fourier coefficient vectors
across 217 affine parameter sections. Forty injective odd-field
relabelings cover 1,480 locators. A characteristic-two control violates
the affine-flat exclusion, while a small N=16 odd-field example
transfers all five supports. The generic Vandermonde and flat-free
count arguments remain written proofs, not consequences of finite tests.
