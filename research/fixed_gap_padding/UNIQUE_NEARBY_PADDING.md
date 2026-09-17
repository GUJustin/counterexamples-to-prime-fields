# Fixed-gap lines with a unique nearby codeword at every nearby point

September 17, 2026. Strengthening of the anchored-padding construction.

Let the old domain have N=mB-1 points, let its word be evaluations of
F_old of degree A-1, and let the code dimension be K<A. Add q points,
where K-1+q<A. Suppose L distinct degree-<K polynomials have exactly
A-1 old agreements. The original construction supplies such a family.

## Control every candidate using the old coordinates

Let T be the set of ALL degree-<K polynomials interpolating F_old on
some K-subset of the old domain. There are at most M=binom(N,K) of
them. Any polynomial nearby at threshold A on the eventual extended
domain has at least A-q>=K old agreements and therefore belongs to T.

Choose the q new points x_j so that every evaluation map

    T -> F_p,  P -> P(x_j)

is injective. The nonzero pairwise differences exclude at most
(K-1)*binom(M,2) points, so it suffices that

    p > N+1+q+(K-1)*binom(M,2).

The extra one permits reserving the removed anchor. Choose offsets b_j
so that the labels P(x_j)-b_j are distinct across ALL pairs (P,j) in
T times {1,...,q}. At step j, at most (j-1)*M^2 offsets are forbidden;
p>(q-1)*M^2 suffices. Both bounds are uniform in the splitting prime,
so they can be imposed before the Chebotarev choice. The polynomials
and coordinates themselves may depend on that prime.

Set g=0,f=F_old on the old domain and g=1,f=b_j at the new points.
Every nearby polynomial belongs to T and can agree at at most one new
point. Since it has at most A-1 old agreements, it must have exactly
A-1 old agreements and exactly one new agreement. Conversely every
P in T with A-1 old agreements is nearby at exactly q labels.
The full label injection ensures that no two candidates are nearby at
the same label. Thus every line word is either outside the radius or
has EXACTLY ONE nearby codeword, at EXACTLY the threshold distance.

If L_boundary denotes the entire old boundary-list size, the exact
number of nearby labels is q*L_boundary >= q*L. No global list-size
bound is asserted. The no-correlated-agreement proof is unchanged:
zero direction gives at most A-1 old agreements, while nonzero
direction gives at most K-1+q<A total common agreements.

## Consequence and scope

The prescribed-gap coefficient theorem therefore holds at every
sufficiently small rational gap with MAXIMUM LIST SIZE ON THE RECEIVED
LINE equal to one. All fields remain prime; no extension-field alphabet
or subfield is used. The domains can still satisfy n=o(p), and strict
Elias can be imposed.

This shows that the large nearby-parameter count need not arise from
multiple nearby codewords at any individual parameter. It does NOT
show that the code's maximum list over all received words is one or
bounded, and does NOT refute a conjecture using that global maximum.
It also does not make the fixed-gap count superlinear in block length.

## The same code still has ambiguous received words

Write L_boundary for the entire old boundary list. For every integer
0<=r<=min(q,L_boundary), this SAME code has a received word with
exactly r nearby codewords at threshold A. Keep F_old on the old
coordinates. Assign r distinct boundary polynomials to r distinct new
coordinates and set each new value to its assigned polynomial's value.
At every remaining new coordinate choose a value outside the evaluation
image of T, which is possible since p>|T|.

Every possible nearby polynomial again belongs to T. Injectivity of
each padding evaluation map means that only the assigned polynomial
hits its coordinate. The assigned polynomials have A-1 old agreements
and one new agreement; all others have no new agreement. Thus the list
is exactly the r assigned polynomials. For r>=2 this word is necessarily
off the displayed line, because every word on that line has list size
at most one.

In particular the code's global maximum list is at least
min(q,L_boundary). For any fixed selected seed list of size L, q grows
without bound, so the global maximum is eventually at least L. This
explicitly rules out interpreting line-wise uniqueness as global
unique decodability. The verifier constructs all available cardinalities
0,1,2 for each of its two fixtures and exhausts the entire candidate pool.
