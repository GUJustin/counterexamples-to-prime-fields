# What ordinary padding and composition preserve

September 18, 2026. A scoped transform audit of the translated-grid
quadratic construction; no paper edits and no claim about all possible
fixed-rate compilers.

Use `(n,k,A,T,B,q)` for length, RS dimension, exact endpoint/common
agreement, nearby threshold, number of certified singleton labels, and
alphabet size. Here

```
k=3, d=T-A,
T ~ A ~ sqrt(2n), d=Theta(n^(1/6)/log n),
B=Omega(n^(4/3) log n), q=Theta(n^(4/3)(log n)^4).
```

Distinguish the source loss `d/n`, capacity margin `(T-k)/n`, and DKT
margin `T/n-a1(k/n)`. Their first ratio is

```
R = (T-A)/(T-k) = Theta(n^(-1/3)/log n).
```

The same proofs also apply to the subsequently audited regular collision
bank: they use only two bank owners per core coordinate, exact uniform A,
and the outsider inequalities L+2M+3<A and 2M+2<A. For that family,
d=Theta(n^(1/4)/log n), p=Theta(n^(5/4)log n), and the loss/capacity
ratio is Theta(n^(-1/4)/log n). Replace the old gap exponents accordingly;
the preservation formulas, loss of fixed-rate first-order placement,
and domain/characteristic qualifications are unchanged.

## 1. Full-fiber composition: an exact transform for this construction

Choose an integer m prime to the characteristic and a field E in which
every seed coordinate has m distinct roots. The seed domain has no zero.
Let D' consist of all these roots, and pull back the two words by
`Y=X^m`. Use the **full ordinary RS code** of dimension `2m+1`, not
merely the subcode of compositions. Its parameters are

```
(n',k',A',T',B',q') = (mn, 2m+1, mA, mT, B, |E|),
```

where B' denotes the same certified set of labels; the statement does
not assert that B was the entire exceptional population.

Singletons and both exact maxima really are preserved here. Bank
polynomials become `theta+X^(2m)/theta`. A nonbank polynomial of degree
at most2m has at most mL matches on the lifted core, because each match
has two bank owners and each bank difference has at most2m roots. At
each of the M grid rows it has at most2m matches, except for the same
constant/zero cases as before. On neutral padding its difference from
`X^(3m)` has at most3m roots. Hence the nonbank bound is

```
m(L+2M+3) < mA.
```

This includes every non-composed witness. A nonzero direction witness
has at most `m(2M+2)<mA` matches; a zero direction gives exactly the
lifted core maximum mA. Each bank's entire agreement profile is
multiplied by m. Thus the old singleton labels stay singleton, and
both endpoints and common agreement are exactly mA.

The normalized loss is unchanged. The capacity-margin ratio changes
only by the degree-versus-dimension endpoint correction:

```
(T'-A')/(T'-k') = d/(T-k+1-1/m),
k'/n' = (k-1+1/m)/n,       T'/n'=T/n.
```

For growing seed n, the rate still tends to zero for **every** choice
of m. The ratio is asymptotically unchanged. Fixing one seed and
letting m grow gives a fixed positive rate, but keeps the certified
label population B fixed; it does not turn the growing-seed result
into a fixed-rate exceptional-count lower bound.

The exact Johnson comparison is preserved:

```
(T')^2 < (k'-1)n'  iff  T^2 < (k-1)n.
```

The DKT first-order placement is preserved as well: the agreement
fraction is unchanged and the rate decreases from 3/n to
`(2+1/m)/n`. On the relevant low-rate branch, a1 is increasing directly
from `u_rho^2(u_rho+3)=sqrt(rho/2)` and
`a1(rho)=sqrt(rho/2)(1+u_rho)`. This uses the curve in the local primary
source `tmp/eprint-2056/paper.txt`, Section4.3, Eq31.
Numerical placement above the curve is separate from the theorem's
characteristic hypotheses: a first-order counting application still
requires characteristic greater than the new message degree2m and its
chosen derivative-degree cap. Enlarging the alphabet by extension does
not enlarge the characteristic. In particular an unbounded-m lift of a
single fixed-characteristic seed eventually fails that guard.

**Field/domain condition.** For a fixed prime-field seed, some finite
extension E always supplies the roots when gcd(m,p)=1; for example it
suffices to choose r with `m(p-1) | p^r-1` and take E=F_(p^r). This
does not preserve a prime alphabet or a fixed extension degree. Over
the original field, all seed coordinates must already be mth powers
and m must divide q-1. Choosing a different prime with the required
split fibers requires a separate realization argument; no polynomial
alphabet bound is furnished by composition alone. The result is a
union of selected fibers, not automatically a prescribed NTT subgroup.

Increasing the message dimension instead to mk is not the same proved
transform: arbitrary degree-<mk witnesses need a new exclusion argument.
The advertised ratio would then be exactly R only **if** the claimed
agreement profile were separately established. The present proof uses
the sharp composition dimension `m(k-1)+1`.

## 2. Common-root padding: the attractive formula is conditional

Append s new coordinates S, let Z be their locator, multiply the old
received values and selected witnesses by Z, and put zero at S.
Selected witnesses in the enlarged RS code have dimension k+s and
gain s agreements. If all maxima and lists were preserved, the formula
would be

```
(n+s,k+s,A+s,T+s,B,q'),
(T+s-(A+s))/(T+s-(k+s)) = R.                  (1)
```

Preservation is not automatic for the full RS code. A concrete failure
is F7, old domain `{1,2,3}`, dimension1, and word `w(x)=1/x`. Its maximum
agreement is1. Append0 and multiply by X, raising dimension to2. The
new word is1 on all three old points and0 at0. The constant polynomial1
has three agreements, exceeding the nominal old maximum plus one,2.

If one restricts the code to `{ZP:deg P<k}`, list preservation is
automatic, but the dimension remains k and the added coordinates are
identically zero. This is not the full dimension-(k+s) RS code. On the
old domain alone, multiplication by nonzero Z is merely a generalized
RS multiplier and changes none of `(n,k,A,T,B)`.

## 3. A rigorous root-padding version uses a quadratic extension

The established conjugate-avoiding padding lemma *does* give (1) for
the old certified labels, with an explicit size restriction. Start over
F_q, take E=F_(q^2), and choose s new roots outside F_q, with S disjoint
from its q-Frobenius conjugate. If

```
s <= A-k+1   and   s <= T-k,
```

then endpoint/common agreement becomes A+s and the threshold-T+s lists
are exactly the lifted threshold-T lists. For T>=A+1, the first
restriction implies the second.
The root choice also requires `s<=(q^2-q)/2`, automatically satisfied
in the translated-grid applications considered here.

For completeness, suppose a new witness matches j padding roots, and
put h=s-j. Divide out those roots. On at least T+h old points its
quotient is a rational function with numerator degree<k+h and
denominator degree h, all of whose poles are in S. Its Frobenius
conjugate agrees at the same old points. Their cross difference has
degree<k+2h and vanishes because `T+h>=k+2h`. The rational function
descends to F_q; its reduced denominator divides two disjoint
conjugate pole sets, hence is constant. The witness is therefore Z
times an old degree-<k witness, proving exact threshold-list
correspondence. To exclude agreement A+s+1 at an endpoint, use
`A+h+1>=k+2h` instead. Old common witnesses give the lower bound for
common agreement, and the individual upper bound gives its upper bound.

This is deterministic and holds simultaneously for all certified old
labels. It introduces no new certified native labels: the transported
set has size B. Further labels in the enlarged alphabet are not
classified by this padding lemma.

For the translated-grid family one block adds at most
`A-k+1=Theta(sqrt n)` coordinates. It therefore cannot raise the rate
to a fixed positive value. This allowance remains invariant under
successive blocks. Raising the rate by adding Theta(n) coordinates via
this specific lemma takes Theta(sqrt n) quadratic-extension steps,
giving alphabet size `q^(2^Theta(sqrt n))`. This is a cost of the
audited lemma, not a lower bound against every possible padding method.

## 4. Even ideal fixed-rate root padding loses first-order placement

Grant exact preservation in (1), irrespective of how it is proved.
For a fixed target rate rho in (0,1), choose

```
s = (rho*n-k)/(1-rho)
```

when integral, or use an adjacent integer for an asymptotically equal
rate. The new agreement fraction is

```
(T+s)/(n+s) = rho + (T-k)/(n+s) -> rho.
```

The capacity margin remains Theta(n^(-1/2)), the normalized source loss
remains Theta(n^(-5/6)/log n), and their ratio is exactly R. Since
`a1(rho)>rho` for every fixed 0<rho<1, these padded examples eventually
lie **below**, rather than above, the DKT first-order curve. The
first-order margin is not invariant under padding, even though R is.

Combining composition and ideal root padding gives

```
(mn+s, m(k-1)+1+s, mA+s, mT+s, B, q'),
ratio = d/(T-k+1-1/m),
```

independent of s. Taking the growing seed to fixed rate again sends
the agreement fraction to capacity and loses first-order placement.
Neither operation amplifies the certified label population.

## 5. Same-domain dimension shifting cannot retain the source profile

Merely enlarging RS_k to RS_(k+s), whether or not selected words are
multiplied by a degree-s polynomial, supplies no upper bound on new
witnesses and no singleton guarantee. Any length-n received word has
agreement at least k+s with RS_(k+s), by interpolation. Preserving
the exact old source agreement A thus requires `k+s<=A`.

The formal ratio would increase to `d/(T-k-s)`, but s is then at most
A-k, so it is at most1 and the rate is at most `A/n=Theta(n^(-1/2))`.
Thus an unchanged-threshold/source dimension shift cannot obtain fixed
rate. A construction that raises the threshold and proves new maxima
is a different task, not ruled out here.

## Finite arithmetic illustration

For the checked toy `(1405,3,52,53,486,10125000000029)`, R=1/50.
Composition by64 has `(n',k',A',T')=(89920,129,3328,3392)` and ratio
64/3263, slightly less than1/50.

Ideal half-rate root padding uses s=1399 and gives
`(n',k',A',T')=(2804,1402,1451,1452)`, still with ratio1/50. Its
agreement fraction is less than2/3, whereas
`a1(1/2)=(1+sqrt6)/5>2/3`. The proved quadratic-extension route permits
only50 roots per block and takes28 blocks for this s, with extension
degree2^28 over the original prime field. No such giant fixture is built.

`verify_translated_grid_transforms.py/json` checks these exact arithmetic
claims and exhausts the small F7 padding counterexample. The proof above
supplies the conditional and construction-specific transform statements.
