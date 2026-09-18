# A fiber-breaking cubic lift: a complete small decoding gate for an eighth word

This is a proposed constructive search, not a construction or a claimed improvement. It differs from the completed one-pole search on the fourteen-point bank: a new numerator may choose different subsets inside cubic fibers and need not descend to a rational function of the base coordinate.

Start with the verified affine seven-cubic bank on fourteen nodes, each candidate matching seven nodes. Choose a cubic map psi(U)=U^3+c with all fourteen fibers disjoint and separable. On the resulting forty-two-point domain the seven known polynomials H_i(psi(U)) have degree at most9 and each matches21 positions.

Fix b outside that domain. Seek a polynomial N of degree at most10 such that

    N(U)/(U-b)

matches the pulled-back word on at least21 core points and N(b) is nonzero. Clearing the denominator gives seven old polynomials (U-b)H_i(psi(U)) and the new polynomial N, all of degree at most10. Add the point b with word value0, and one further point d with word value N(d), chosen off the core and the finitely many old/new coincidences. Every old polynomial then has22 matches and N has at least22 matches on44 points. The RS dimension is11: exactly quarter rate and half agreement, with eight distinct candidates.

The finite-field search can use the explicit F97 bank and F97^3: every nonzero base-field element has three cube roots in that extension, since97 is1 modulo3 and(97^3-1)/3 is divisible by96. Choose c different from all fourteen base nodes. This alone would yield an extension-field example, not a prime-field theorem. A positive witness would still require a characteristic-zero lifting certificate, or a separate direct prime-field realization. An unsuccessful finite search would not prove nonexistence.

## Why this gate is algorithmically complete for a fixed pole

For the modified core word (U-b)w(U), decoding degree10 polynomials with21 matches among42 points is strictly above the Guruswami--Sudan threshold, since21^2>42*10. Use multiplicity11 and weighted degree230 for weights(1,10):

    sum_{j=0}^{23}(231-10j)=2784

monomials versus42*11*12/2=2772 interpolation conditions. A nonzero Q(U,Y) exists. Every candidate N has Q(U,N(U)) identically zero, since21*11=231>230. Polynomial root extraction therefore enumerates every candidate for that fixed pole.

All seven known graphs are forced factors of Q. At each triple node their product has ordinary point multiplicity3; at each quadruple node it has multiplicity4. After dividing their product, the residual interpolation problem has weighted degree160 and multiplicities8 at the21 triple preimages,7 at the21 quadruple preimages. It has

    sum_{j=0}^{16}(161-10j)=1377

unknowns versus21*(8*9/2+7*8/2)=1344 conditions. This provides a smaller polynomial-module interpolation problem. No dense2772-by2784 elimination is needed; use a structured interpolation module and weak-Popov reduction, then extract polynomial roots and independently verify matches/properness.

Any proper new candidate with exactly21 selected core matches must use at least14 triple-node preimages. Indeed its total pairwise intersections with the seven old polynomials cannot exceed7*10=70, while t triple matches and21-t quadruple matches contribute84-t. Thus t>=14. On such a selected support the residual interpolant has at least8t+7(21-t)>=161 zeros along N, exceeding its weighted degree160, as required.

## Why cubic lifting is the distinguished small case

For an m-fold lift of the fourteen-point bank and a denominator of degree h, clearing denominators and adding h common-old poles plus h fresh-new points yields quarter rate precisely when h=m-2. The numerator degree is then4m-2, the core length14m, and the needed core agreement7m. The GS threshold surplus is

    (7m)^2-(14m)(4m-2)=7m(4-m).

Thus m3,h1 is above the threshold, m4,h2 is exactly at it, and larger m are below it. This makes cubic lifting the natural bounded complete-decoding gate. It does not guarantee an eighth root exists: the seven known roots may exhaust every decoded list, and a finite-field root need not lift to characteristic zero.
