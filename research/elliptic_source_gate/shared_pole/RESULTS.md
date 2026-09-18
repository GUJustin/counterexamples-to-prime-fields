# Shared-pole Paley elliptic pilot: exact result

The proposed ell=5 fixture exists. On E/F211:y²=x³+16 there are225 rational points and25 rational5-torsion points. The verified basis is(2,92),(28,92). There are112 finite rational x-coordinates, of which12 are torsion poles and100 are offpole.

The explicit formula in the parent target note produces13 DISTINCT polynomials: one has degree24, the other twelve degree25. The group-algebra identity c*c=25 delta0-1 and the polynomial identity Q0+2 sum_(S!=0 modulo sign)Q_S=0 are verified exactly. Polynomial evaluation agrees with direct elliptic translation sums at every offpole coordinate, for all13 candidates.

On the112 rational-elliptic x-coordinates, largest equal-value bucket sizes have histogram

    {1:70, 2:29, 3:1, 6:12}.

The twelve size-six buckets are the torsion poles. On the100 offpole nodes the total maximal incidence is131, so no word can give every candidate more than floor(131/13)=10 matches. Allowing the best100-node domain among all112 coordinates raises the maximal total incidence to191, hence minimum agreement is at most14. A deterministic maximal-bucket word on that selected domain has per-candidate counts

    [7,21,14,17,16,11,15,14,12,14,16,20,14].

These counts are merely a checked word, not an optimized lower bound.

The conclusion is still negative if all211 affine F211 coordinates are allowed, including x-values not attained by rational elliptic points: the best100 maximal buckets sum to227, hence minimum agreement<=17. The first-order target at n100,k26 requires at least48 matches. In particular, this fixture is below capacity before any word optimization. No integer-programming or larger search is justified by this result.

Runtime0.067seconds. `pilot.py/json` contain the curve, basis, torsion labels, all13 coefficient vectors, the112 detailed bucket records, and the all-field incidence bounds. This is a finite-field fixture rejection, not an exclusion of the shared-pole family over other fields or characteristic zero.

## Growing-parameter incidence requirement

For ell odd prime, set M=ell² and L=(M+1)/2. The candidate degree cap is M, and a quarter-rate test uses n=4M, k=M+1. Its limiting first-order agreement threshold is a0=(3+sqrt133)/31.

At a nonzero torsion pole T, candidate values are proportional to c_(T-S)+c_(T+S). Exact quadratic-character counts give bucket sizes

    (M-1)/4 for value0,
    (M-1)/8 each for values+2 and-2,
    1 for value c_T.

Here S ranges over H/{+/-}, and p>5 keeps these four values distinct. The zero bucket is largest. This follows by counting opposite/equal signs in c_(T-S)c_(T+S), whose sum over H is-1, and quotienting S by sign. Thus all(M-1)/2 pole coordinates together contribute at most(M-1)²/8 candidate-word incidences.

To achieve A>=4a0 M+o(M) for every candidate, the remaining approximately(7/2)M coordinates must supply at least

    [2a0-1/8] M²+o(M²)

incidences. Their average equal-value bucket must therefore be at least

    [(2a0-1/8)/(7/2)]M+o(M),

approximately0.23216M, or approximately46.43% of the whole candidate bank. A shared pole divisor alone does not supply these large offpole fibers. The explicit convolution identity proves the bank and its dependency, but a new offpole collision identity is still indispensable. The pilot's offpole buckets, averaging1.31 on the rational-elliptic domain, are far from this requirement.
