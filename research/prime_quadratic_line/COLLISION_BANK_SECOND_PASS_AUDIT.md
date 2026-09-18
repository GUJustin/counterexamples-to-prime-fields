# Regular collision bank: second independent proof audit

September 18, 2026. **PASS**, for the asymptotic theorem in
`collision_bank_constant_fraction.tex`. This audit does not certify a
finite onset. It also approves replacing the claimed exact first-order
limit by the established upper bound recorded below.

## Exact core accounting

Use two disjoint K_(t,t) components, with all four prime-label sets
disjoint. There are L=2t² bank parameters. Coherent choices
theta_ab=alpha_a/beta_b with alpha_a²=a/z and beta_b²=b/z ensure the
two diagonal products in every rectangle are equal as field elements,
not merely equal after squaring. The common quartic class makes alpha,
beta, and therefore theta squares.

Conversely, squaring any product equality and clearing denominators
gives an integer equality because both sides are at most H^4<p.
Unique factorization fixes both numerator and denominator multisets.
There is only one edge pairing unless it is a rectangle within one
component, in which case there are exactly two. A cross-component
pair has no alternative pairing. Shared-vertex and repeated-edge
products introduce no additional representation.

For a two-pair product, its two square roots are assigned one to each
pair. Their sums differ: equal sum and product would identify the
unordered parameter pairs. At a root assigned to theta,phi, matching
by another parameter eta forces (eta-theta)(eta-phi)=0. Every core
coordinate therefore has exactly two owners, even though the received
values at the positive and negative roots can differ.

Each bank edge has exactly (t-1)² opposite partners in rectangles.
It loses one of two potential matches for those partners, giving

    A=2(L-1)-(t-1)²=3t²+2t-3.

As a separate count, the number of two-pair product classes is
R=2*binom(t,2)²=t²(t-1)²/2. Hence the distinct core size is

    N0=2*binom(L,2)-2R
      =t²(3t²+2t-3)=LA/2.

The usual outsider core bound remains L: every outsider match is
counted against its two owning bank words, each of which differs
from the outsider at a nonzero polynomial of degree at most two.

## Prime selection and probability constants

The selection is not circular. First let v_H count integer primes in
[H/2,H], set t=floor(v_H/16), L=2t², M=floor(L/8), and Q0=LHM.
Then choose p=1 mod4 in (4096Q0,8192Q0). The prime number theorem
in a fixed progression supplies this eventually. Regardless of that
prime's quartic character distribution, one class contains at least
v_H/4>=4t small primes. A reference z can be chosen among them.
Because Q0=Theta(H^5/(log H)^4), one also has p>H^4 eventually.

The expected retained grid count is (1/2-o(1))M². Both ratio-collision
and core-ratio deletion losses divided by M² are O(L²/p)=O(1/H).
Thus retained count at least M²/4 has probability at least 1/3-o(1).
For K=3HM, cross-bank raw-label collisions C satisfy

    E C <= binom(L,2) K²/p,
    Pr[C>LHM/64] <= 288 LHM/p <288/4096.

The latter constant is approximately 0.070313, strictly below 1/3.
Probability subtraction, without any independence assumption, yields
a simultaneous translation for all sufficiently large H.

The existing rich-fiber arithmetic then supplies at least LHM/16
rich bank-label pairs. Removing both endpoints of each cross-bank
collision leaves at least LHM/32 labels with a unique bank owner.
Deleting the zero-polynomial label leaves Q0/32-1. Since
p<8192Q0, this is greater than p/2^18-1 and hence at least p/2^19
eventually. The numerical constant in the theorem is valid.

## Code, sources, and threshold

Neutral padding is possible:

    A~(3/2)L,  N0~(3/4)L²,
    X<=M²<=L²/64,  n~(9/8)L².

The field has p much larger than n. Excluding at most 3L roots of
X³-P_theta preserves exact bank agreement A. Away from lambda=-c0,
an outsider has at most L+2M+3<A total matches. The zero polynomial
at that single exceptional label is correctly removed. Collision
screening used the full raw intervals, so another bank cannot acquire
even an unnoticed non-rich grid fiber at a retained unique-owner label.

There are many finite labels with exact maximum agreement A; choosing
any two as endpoints is valid. A nonzero quadratic explaining the
direction has at most two matches on the zero-direction coordinates
and at most 2M on the grid. A zero explaining direction restricts
common matches to the core and neutral block, with maximum exactly A.
Thus ordinary common agreement is exactly A. The invertible change
to the selected endpoints preserves this quantity, and affine mixture
parameters give a bijection of the original pencil, losing no labels.

Finally, d/A tends to zero, so A/sqrt(n) and T/sqrt(n) tend to sqrt(2).
The exact definition n=floor(T²/2)+1 gives T²<2n. To place the source
above first order, it is sufficient and preferable to use

    n*a1(3/n) <= sqrt(3n/2)+(3n/8)^(1/4).

Its right side divided by sqrt(n) tends to sqrt(3/2)<sqrt(2).
No exact asymptotic equality for a1 is needed. The root agent's
replacement of the original equality claim by this bound is approved.

## Result and scope

The scales are d=Theta(n^1/4/log n), p=Theta(n^5/4 log n), and a
fixed positive fraction at least 2^-19 of prime labels with singleton
threshold lists. Both endpoints and common agreement are exact; the
good witness agreements need not equal T exactly. The relaxed list
bound is line-local, not code-wide. Message dimension remains three,
and loss/capacity-margin ratio tends to zero. No fixed-rate, prescribed-
domain, finite-onset, or literature-priority conclusion is implied.
