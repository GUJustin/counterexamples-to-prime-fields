# Recovered fixed-gap Dickson construction: scope audit

September 17, 2026. This is recovered prior research, not a new discovery.
Source: `Research-Restored-2026-09-16/Documents/mca_exponent_one/dossier/CHECKPOINT_fixed_gap_n2_counterexample.md`, updated September 8.
The archive explicitly records that the owner did not accept n=p-1 as a
solution to the n=o(p) research target. Preserve that restriction.

## Mathematical verdict

The seed-list proof and unchanged-domain full-set MCA construction pass
direct proof review. The independent `verify.py` checks six primes, including
p=257 and 337 where the seed radius is certified strictly below Elias.
It verifies every seed evaluation and every designated label, using pairs
in the independent basis (1,theta). No extension multiplication is needed.

For p=1 mod 8, n=p-1, k=n/4, e=(p+1)/2, define

    G_a(X) = sum_{j=0}^k binom(e,2j+1) a^(e-2j-1) X^j,
    H_a(X) = G_a(X)-X^k,
    w(x) = (1+chi(x))/2-x^k,  x in F_p^*.

The leading remaining coefficient is -a^2/8, so these give n/2 distinct
degree-(k-1) polynomials indexed by nonzero a modulo sign. Each has exactly
n/8 square-coordinate agreements and n/4 nonsquare-coordinate agreements.
Consequently the list has size n/2 at exact rate 1/4 and agreement 3/8.
The capacity gap is exactly 1/8, independent of p and n.

Proof details checked independently:

* On nonsquare x, take s^2=x in F_(p^2). For u=(a+s)^e,
  u^2=a^2-x and (a-s)^e=u^p. Thus G_a(x)=0 iff chi(a^2-x)=1.
  The elementary quadratic-character sum gives n/4 such x.
* On square x=s^2, the expression is
  ((a+s)chi(a+s)-(a-s)chi(a-s))/(2s).
  Off s=0,+a,-a it equals 1 precisely when both characters are +1.
  The weighted character-sum count is n/4 in the s variable. Removing
  s=0 and correcting the half-weight contributions at +/-a cancel
  exactly, since chi(2)=1. Dividing by two gives n/8 coordinates.
* The character-sum identity sum_t chi(t^2-c)=-1 for c!=0 follows by
  counting (t-y)(t+y)=c, so no unproved distribution assertion is needed.
* For p>256, H_p(5/8) <= 5/8+1/log_2(p) < 3/4. Thus the radius 5/8 is
  strictly below the characteristic-based Elias radius at rate 1/4.

This refutes ANY finite list bound depending only on rate and positive
gap if all prime-field lengths up to p-1 are allowed. It is stronger than
an exponent-coefficient obstruction in that broad regime, but has no
short-domain conclusion. Priority has not been settled.

## What the line construction does and does not prove

For p=16m+1, change m nonsquare coordinates R. Set (f,g)=(w,0) off R and
(f,g)=(theta*x,1) on R, with theta outside F_p. At any x in R the seed
polynomials take exactly 4m+1 distinct values: 4m parameter classes give
G_a(x)=0, and the other 4m give distinct nonzero values with
G_a(x)^2=a^2/x-1. The labels v-theta*x are distinct across x and v.

Every selected seed retains at least 5m core agreements and acquires its
designated coordinate. Its full agreement set cannot have a direction
polynomial of degree <4m: that polynomial would have at least 5m zeros
and also a value 1. This gives m(4m+1)=n^2/64+n/16 full-set MCA failures
at fixed agreement 5/16 over any extension degree at least two.

However, (H_a,0) still explains the retained core agreements. The core
already has at least 5m coordinates, exactly the advertised fixed
agreement threshold. Therefore this is NOT a counterexample to a
definition allowing a correlated subset of that size. In particular,
the full-set MCA count must not be substituted for the manuscript's
selected-witness or ordinary correlated-agreement failure count.

Neither field extension nor ordinary puncturing fixes n/p -> 1.
Inherited degree k-1 requires any punctured rate-1/4 code to have length
at least 4k=p-1. The relevant short-domain target remains open.

## Editorial decision

Keep the full construction in research notes for now. Do not advertise
it as the sought short-domain proximity-gap result, and do not silently
change the user's recorded n=o(p) target. Before ePrint release, explain
this full-length comparison and check attribution; an unrestricted
conceptual claim that only the reciprocal-gap exponent is known to fail
would omit the simpler fixed-gap obstruction in this regime.

Related primary source inspected: Gao--Yang--Xu--Kan,
https://arxiv.org/html/2607.10572v1 (July 12, 2026). Their list-to-full-set-MCA
transfer supports the need to distinguish this notion from ordinary
correlated agreement. It does not by itself establish priority for this
specific Dickson seed or the multi-coordinate count.
