# Independent audit: restricted curvature source and graded rank savings

**PASS, with one output-label correction requested.** Audited
`RESTRICTED_CURVATURE_GATE.md`, `CLOSED_CURVATURE_RANK.md`,
`ROOT_CHALLENGE_GRADING.md`, and the restricted, closed-bound, and graded
scripts. The proved result is a sufficient interpolation source gate;
it is not a second-order factor/routing theorem or a better.codes gain.

## Contact and global source

Backward Hasse Taylor is valid in arbitrary characteristic:
P(x+t)-P(x)=t P^[1](x+t)-t^2 P^[2](x+t)+t^3 E(t).
Thus imposing the formal map Y -> tR-t^2V+t^3E modulo t^m is sufficient
for m-fold contact at every agreement. Treating E,R,V as independent
formal variables strengthens the constraints and is safe for existence
via a dimension lower bound. No claim that all formal jets are actual
candidate jets is needed.

For candidate degree <=w, the assigned weights w,w-1,w-2 bound the
degrees of P,P^[1],P^[2]. Hence a source with weighted degree <mA
vanishes identically after substitution if it has m-fold contact at A
distinct coordinates. This is the usual interpolation implication,
independent of the still-missing factor/routing argument.

The scalar coefficient count and its challenge-degree first moment are
exact: for each (i,j,k), the available X powers number
max(mA-wi-(w-1)j-(w-2)k,0), and the challenge powers number
L+1-i-j-k when L>=J. Translating X enlarges only the local t box.
Translating Y by f+Zg lowers jet degree and increases challenge degree
by no more than the lost amount; j<=S and k<=1 remain valid.

## Exact finite matrix and baseline rank

The displayed output expansion has coefficient
(-1)^v binom(i,b)binom(i-b,v), and exponent tuple
(a+i+v+2b,b,v+k,i-b-v+j). It determines both block invariants
ell=i+j+k and h=a+i-k. Different blocks therefore have disjoint row
supports. Each block's columns are indexed by the at most
(S+1)(K+1) possible (j,k). The script implements this expansion and
sparse Gaussian elimination exactly modulo the pinned prime.
Its truncation break is safe because t degree increases with v.
The eight unblocked comparisons test the decomposition, not the full
symbolic rank-saving theorem.

For the first-jet baseline, put r=a+i. Terms r>=m vanish. For each
0<=r<m the remaining source rectangle has u degree <=r and R degree
<=S. Substitution u=R+tE has kernel exactly the multiples of
(u-R)^(m-r). The quotient rectangle loses m-r in each degree cap.
This proves the recorded baseline rank R0 in every characteristic;
monicity of u-R avoids characteristic-dependent binomial assumptions.

## Explicit extra kernel classes

Take m>=2S, z=Y-tR, and

    Q=t^(m-1-i-2b) Y^i R^j z^(b-1)(z+t^2V),
    1<=b<=S, 0<=i<=m-1-2b, 0<=j<=S-b.

Actual substitution gives contact order at least m. Its slope degree
is at most j+b<=S, its V degree is at most one, and its total jet
degree is i+j+b<=m+S-3. Expanded t and Y exponents are below m.
When m=2S,b=S, the index range is empty and contributes zero.

The two embedded baseline kernels map to zero after replacing their
formal E by -V+tE. Modulo their direct sum, Q has image

    t^(m-1) R^(i+j) (E^b,E^(b-1)).

One choice for each pair (b,i+j) gives independent classes, already
in the first component. Their count is S(2m-S-3)/2. Thus the enlarged
box rank is at most 2R0 minus this count. Restricting by J or global
weights can only reduce rank; J>=m+S-3 is not necessary for this
enlarged-box upper bound. It only guarantees the displayed vectors
themselves fit that particular restricted source.

This proof establishes an upper bound. Agreement with twelve exact
matrix ranks is a useful regression, not a proof of equality for all
parameters. The scripts correctly use the symbolic bound as a bound.

## Graded challenge improvement

The local map preserves total jet degree ell. After the received-value
translation, the image of a source of joint degree <=L is contained
in the direct sum of its ell-homogeneous images times
1,Z,...,Z^(L-ell). Consequently its rank is at most

    sum_ell (L+1-ell) R_ell.

For a first-jet block r, the rectangle has degree sum
(r+1)(S+1)(r+S)/2. Its removed kernel rectangle, shifted by the
homogeneous factor (u-R)^(m-r), has the SAME mean degree (r+S)/2.
This verifies `moments()` and its exact integer divisions.

If the baseline total rank and degree moment are R0,T0, the paired
curvature baseline has rank 2R0 and moment 2T0+R0. Each extra class
above has degree b+l. Writing num=m+S-3b, its saved moment is

    sum_b [num*b+num*(num-1)/2].

Subtract these independent classes separately in each degree. For
L>=m+S all challenge weights are nonnegative, giving the valid joint
upper bound (L+1)Rbar-Tbar. Here Rbar,Tbar are respectively the total
and moment of this proved per-degree upper profile. Importantly,
Tbar is NOT asserted to lower-bound the actual rank moment after
source restriction. The JSON field originally called
`rank_degree_moment_lower` should therefore be renamed to describe
the upper profile; this naming fix has been sent to the author.

The resulting sufficient dimension surplus is
(L+1)(C-n Rbar)-M+n Tbar. For positive gap C-n Rbar, choosing
L=max(J,m+S,floor((M-n Tbar)/gap)) indeed gives strict positivity,
including when the quotient is an integer or negative.

## Independent arithmetic and benchmark scope

Independently recomputed the source count and first moment by direct
integer summation, without importing either numerical script:

* m72,S22,J99: C=23786472350, Rbar=90737,
  C-nRbar=312222; conservative challenge cap3037135 checks.
* m96,S30,J132: C=56682315118, Rbar=215917,
  C-nRbar=80969070; conservative challenge cap37350 checks.

This arithmetic took a fraction of a second; no expensive matrix job
or parameter search was rerun. The source improvement is real within
the stated sufficient gates. However the source now depends on V,
and existing first-order factor, characteristic, helper, packing, and
challenge-label bounds cannot simply be reused. Differentiating along
candidate solutions introduces a further derivative. No numerical
rank percentage can be deducted from the incumbent ledger deficit.
A quantitative curvature-compatible routing theorem remains necessary
before these source gains can affect a certified benchmark score.
