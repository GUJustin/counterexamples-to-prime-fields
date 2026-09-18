# Elementary finite eight-word baseline: useful scope correction

There is an elementary finite eight-word example above the audited first-order
curve after a cubic pullback. This should not be confused with either an
unbounded-list construction or an eighth word at the saturated quarter-rate
parameters. Earlier shorthand saying simply 'no eight-word example' was too broad.

## Exact nearest-list extension lemma

Let a word on N distinct coordinates over an infinite field have maximum
agreement A with degree-at-most-D polynomials, and complete nearest list of size L.
Choose a polynomial Q outside that list with b old agreements, where D+1<=b<A.
Let I be the finite set of all degree-at-most-D polynomials interpolating any
D+1 old received points. Append A-b distinct fresh coordinates t, giving each
received value Q(t), and avoid every root of Q-R for R in I other than Q.

Then Q has exactly A agreements. Every other R with at least D+1 old agreements
belongs to I and gains none. Every R with at most D old agreements gains at most
A-b, hence has at most D+A-b<A. Therefore the maximum agreement remains A and
the complete nearest list is exactly the old list together with Q.

For either seven-cubic bank, there are1001 four-subsets of the14 old coordinates,
but at most7*35=245 are contained in an old seven-agreement set. A four-subset
outside those sets gives a fresh cubic Q with at least four old matches. Exact
modular screening followed by characteristic-zero replay in this directory
shows that neither archived rigid bank has a fresh cubic with five old matches.
Thus this construction uses b4 and appends three nodes, giving a complete
8-element nearest list at n17,k4,A7. It does not produce n16 by this method.

## Explicit orbit-2 instance

Use the exact orbit-2 field q^3-10q^2+3q+1=0 and bank from
../prime_line_strengthening/fano_seven/orbit2_independent_field_audit.json.
Interpolate the old zero-based indices2,6,7,11. The exact resulting cubic and
all14 evaluations are in orbit2_five_exact.json. It has exactly those four old
matches. Append the rational coordinates1,2,3 with values Q(1),Q(2),Q(3).

padded_eight_certificate.py/json records their exact values and verifies all
3000 avoidance inequalities modulo the prime10847 at q=100. Every old coordinate
denominator is a unit, all14 old nodes stay distinct, and the other1000
four-point interpolation subsets produce cubics distinct from Q modulo that
prime. Thus all the required inequalities hold in characteristic zero.
The finite nearest-list extension lemma proves completeness; no heuristic
sampling is involved.

## First-order parameters after pullback

Choose a cubic polynomial cover T^3+b with b avoiding all17 source coordinates
and adjoin its51 distinct fiber points. The eight composed polynomials have
degree at most9 and at least21 agreements on51 nodes. Hence

rho=10/51, a=21/51=7/17,
F_rho(a)=(8-rho)a^2-6rho*a+rho(4rho-5)=536/44217>0.

This rate is above11-3sqrt(13), so the audited high-rate first-order formula
applies. The capacity gap is11/51. After excluding finitely many bad primes,
completely split primes preserve the construction, giving arbitrarily large
prime-field instances. We assert at least eight nearby polynomials after the
pullback, not completeness of its nearest list.

The example has fixed list size8 and fixed length51. Repeated covers keep list
size fixed. It therefore establishes neither intrinsic length-exponent tightness
nor a better.codes improvement. Its role is to make the baseline accurate and
prevent a finite eighth word at relaxed parameters from being mistaken for the
requested breakthrough.
