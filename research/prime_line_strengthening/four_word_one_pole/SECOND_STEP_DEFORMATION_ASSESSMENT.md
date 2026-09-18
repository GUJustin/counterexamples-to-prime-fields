# A different second-step route: deformation and a squared-value bridge

## The two fresh nodes are an open guard, not two fixed interpolation equations

Keep the 26-point paired core of the first extension, but do not freeze its two fresh coordinates. Suppose a proper rational function R=N/(T−b), deg N<=7, agrees on twelve core coordinates. Let G5 be the new polynomial from the first extension. If

    N(T)−(T−b)G5(T)

has two distinct roots outside the core and outside b, choose those as the two fresh coordinates and give them received values G5. Then all four old polynomials already have fourteen matches in the core; G5 has twelve core matches and the two fresh ones; R has twelve core matches and the same two fresh ones. Thus the next one-pole input is obtained. The root guard must actually be checked: the difference polynomial may have repeated or forbidden roots.

This reduces the genuine next-step target to a twelve-match core witness, not a witness forced to match two previously arbitrary fresh points. It does not prove such a witness exists.

## Exact determinantal deformation target

Take the reciprocal-quadratic seed with parameters a1,...,a4 and its first pole a0. Let phi(T)=T²+c, with c avoiding the twelve base coordinates and a0. Select one point T_j above each of the twelve base nodes x_j; thus

    T_j²=x_j−c.

The corresponding received values are W_j=(x_j−a0)w(x_j). A prospective numerator-degree7/denominator-degree1 witness exists only if the following twelve-by-ten homogeneous interpolation matrix has a nonzero kernel:

    row_j=(1,T_j,...,T_j^7,−W_j,−T_j W_j).

The kernel vector's last two entries define the denominator. They must give a genuine linear denominator, with its root off the full core, and the resulting numerator must not vanish at that root. These are separate guards, not consequences of rank loss.

For a general twelve-by-ten matrix, rank<=9 has codimension three. This structured family has four seed parameters and the independent quadratic critical value c, before removing scaling. Hence a deformation route is dimensionally plausible. But a map from a five-dimensional parameter space can avoid that determinantal locus entirely; expected dimension is not an existence theorem. Finite choices of signs of the T_j and the selected first one-pole support also matter. No broad search of these branches was run.

The transversal support is genuinely different from the three-double-fiber ansatz previously excluded: here all twelve selected core fibers contribute one point. Its intersections with each old lifted candidate have size six, so it is not immediately prohibited by the degree-seven difference root bound.

## A concrete squared-value bridge with the right rational degree

Let t1,...,t4 be nonzero parameters and let R0(T) be their generic one-pole function from `generalization/GENERIC_ONE_POLE.md`. Thus at the six positive pair products,

    R0(t_i t_j)=t_i²+t_j².

Now use a_i=t_i² as the four parameters of a new reciprocal seed. Its received values on the positive base edges are t_i⁴+t_j⁴. Therefore

    R0(T)²−2T²

has exactly those six values at T=t_i t_j. Let alpha be the pole of R0, and let a0 be the first pole of the squared-parameter seed. If the explicit parameter equation

    a0=alpha² != 0

holds, then

    S(T)=(T²−a0)(R0(T)²−2T²)

is proper with numerator degree at most seven and a single pole at alpha. Indeed, writing R0=U/(T−alpha), the numerator before cancellation is

    (T²−alpha²)[U²−2T²(T−alpha)²].

One factor T−alpha cancels, leaving denominator T−alpha and numerator degree at most seven. Its value at the remaining pole is 2alpha U(alpha)²!=0. Thus this is a genuine degree-compatible mechanism, not the earlier operation of multiplying a received word by a linear factor.

However, it currently supplies only six core matches. Twelve are needed. To use both signs of the six product fibers would additionally require

    R0(−t_i t_j)²=R0(t_i t_j)²

for all six edges. No admissible parameter family satisfying those equations and the pole constraint is proved here.

In elementary symmetric notation for the t_i, the first pole is alpha=e1 e4/e3. The squared-parameter pole a0 has the same formula with t_i replaced by t_i². These make the degree-compatible pole equation explicit and testable.

The obvious specialization e1=e2=0 gives R0(T)=−T+e4/T, which is odd and supplies both signs. But it has alpha=a0=0; S becomes the polynomial

    −T^4−2e4 T²+e4²,

and phi(T)=T² has critical value equal to the first pole. Consequently the required two-point pole fiber collapses, and this specialization does not supply the one-pole extension. It illustrates exactly which nondegeneracy must survive a deformation.

## Assessment

The proven result in this note is the fresh-node selection lemma and the rational degree/pole calculation. The promising unresolved target is a proper twelve-match transversal witness in the displayed determinantal family, or a deformation of the squared-value identity that adds six matches without forcing alpha=0. This differs from previously excluded old-polynomial-part correction patterns. No new growing bank or second valid extension is claimed.
