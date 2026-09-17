# Independent audit of the symmetrized-translation feasibility gate

September 17, 2026. The symbolic proof in SYMMETRIZED_TRANSLATIONS.md
was independently checked. No mathematical issue was found.

The addition-law numerator is correct. At x=u it equals 4v^2,
so a non-two-torsion point has a double pole and reduced map degree2.
When v=0 the numerator has a simple zero at u because nonsingularity
gives 3u^2+a!=0; the reduced map has degree1. The map is nonconstant
in both cases, and finite at infinity.

The isogeny x-map has degree h^2. For h>=2 this differs from degree
at most2; for h=1 the pole at infinity distinguishes x from S_u.
Thus the rational functions are never identical. Clearing denominators
gives at most h^2+2 finite equalities. On E[m], multiplication by h
has image E[m/h], giving at most (m/h)^2 received x-values; each value
has at most two preimages under S_u. The complementary bound
2(m/h)^2 is valid. Optimizing their minimum gives exactly
1+sqrt(1+2m^2), hence O(m).

The number of finite x-coordinates of E[m] is
(m^2+|E[m][2]|-2)/2. Removing the received poles for h<=m/2 leaves
Theta(m^2) coordinates; the endpoint h=m is entirely undefined and
correctly excluded. Additional candidate-pole removal preserves the
conclusion only when a fixed fraction of the original domain remains,
as explicitly stipulated. A separately selected O(m)-point domain is
not excluded by this proof.

Clearing common denominators preserves all agreements away from their
zeros and costs degree at most2L for L distinct non-two-torsion poles.
It cannot convert the proved O(sqrt(N)) agreement bound on a retained
full torsion domain into positive agreement fraction. The decision not
to enumerate this particular construction is therefore justified.

This audit excludes only the displayed translation/isogeny-word scheme,
not arbitrary elliptic, algebraic-geometric, or sparse-domain sources.
