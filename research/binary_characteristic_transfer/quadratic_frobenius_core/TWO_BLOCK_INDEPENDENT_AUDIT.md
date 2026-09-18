# Independent audit: two Frobenius blocks with neutral padding

PASS for the algebraic construction below. The first-order statement at N=9p² is certified here for primes p≥19, not all p≥11. This audit uses the complete quadratic classification in PROOF.md; no scan or rental.

Let E=F_(p⁴), B=F_(p²), p≥5. Choose a square eta in E outside B (there are such squares). Let D0={x:x²∈B*}, D1={x:x²∈eta B*}. Each has 2(p²−1) points, and they are disjoint. On D0 set f=x^(2p), g=0. On D1 set f=eta*(x²/eta)^p, g=1.

For norm-one a∈B, write Ia={y^p−ay:y∈B}. These are exactly the p+1 distinct one-dimensional F_p-subspaces of B: b∈Ia iff b^p=−a^p b, and every nonzero b determines a uniquely.

For Q=aX²+b, with b∈Ia, label z=b−eta*v, v∈Ia, gives matches on both blocks. Each contributes 2p if its respective constant b or v is nonzero, and 2p−2 if zero. Since 1,eta are independent over B, the F_p-planes Ia+eta Ia intersect pairwise only at zero, and (b,v) is uniquely determined by z within its plane. Thus precisely

    M=(p+1)(p−1)²

labels have b,v both nonzero. They have one canonical witness each with exactly 4p active-block matches. Labels on the two axes of a plane have 4p−2; label zero has p+1 canonical witnesses with 4p−4.

## Exhaustiveness, including coefficients outside B

On D1, choose u²=eta and substitute x=u t, then divide the equation f+z=Q by eta. It becomes the original D0 equation for a quadratic with coefficients in E and shifted constant (b−z)/eta. Hence on each block all noncanonical quadratics have at most p matches (p≥5).

A quadratic canonical on either block is even and has a∈B of norm one. On the other block, if its shifted constant is outside B there are no matches; if the constant is in B but not in Ia there are again no matches. Thus a quadratic canonical on one block either is canonical on both, or has zero matches on the other. If neither block is canonical, total matches are at most 2p. This proves completeness above 2p before padding, apart from the explicitly listed secondary canonical levels.

## Neutral coordinates

Add t=5p²+4 distinct points outside D0∪D1, giving N=9p². On these set f=x³,g=0. Exclude every root of x³−Q(x), for every one of the p(p+1) core-canonical Q (including b=0). At most 3p(p+1) points are forbidden by this condition. There are enough points since

    p⁴−4(p²−1)−3p(p+1) >= 5p²+4

for p≥5. Every core-canonical Q gains zero neutral matches; every quadratic gains at most three.

Therefore at threshold T=4p the raw line f+zg has exactly M qualifying labels and each list is a singleton. The secondary canonical values remain 4p−2 and 4p−4. All noncanonical-on-both witnesses have ≤2p+3<4p matches. A witness canonical only on D1 has ≤2p+3; one canonical on D0 gains zero neutral matches. In particular, at every label outside the union of the p+1 planes, nearest agreement is at most 2p+3 and at least 2p.

## Common agreement and two far sources

A simultaneous explanation of f,g uses two quadratic polynomials F,G. If G is neither constant zero nor constant one, it matches g at at most two zero-block coordinates and at most two one-block coordinates, so simultaneous agreement≤4. If G=0, only D0 and the neutral block are available, and F has at most 2p+3 matches there. If G=1, only D1 is available and F has at most 2p matches. Consequently

    2p <= CA_3(f,g) <= 2p+3.

Choose two distinct alpha,beta outside the plane union. This is possible in E, since the union has p³+p²−p elements. Define F=f+alpha*g and G=f+beta*g. Each individual agreement is ≤2p+3; common agreement is unchanged by this invertible source transformation. For t≠−1, the line F+tG is the nonzero scalar multiple of f+z g with z=(alpha+t beta)/(1+t). All M high labels are transported to distinct nonzero finite t, as alpha,beta were chosen outside the plane union.

At t=−1 the word is (alpha−beta)g. The constant zero matches N−|D1|=7p²+2 coordinates, and the constant alpha−beta matches |D1|=2(p²−1) coordinates. Every other quadratic matches at at most four coordinates.

IMPORTANT: Thus this endpoint transformation does NOT preserve singleton lists at its projective-infinity label. At t=−1 there are exactly TWO threshold witnesses, the constants zero and alpha−beta, since both blocks have >4p points. All other quadratics have at most four matches. There are exactly M+1 nonzero qualifying labels after transformation; M singleton lists and one two-element list. This does not affect the population or both-source separation claims. Do not assert all transformed lists are singleton.

The source-to-threshold agreement gap is at least 2p−3. Exact source agreement or exact common agreement beyond the interval above is not asserted.

## First-order and Johnson comparison

K=3 and N=9p². Johnson is sqrt(2N)=sqrt(18)*p>4p. The usual low-rate first-order bound gives

    N*a1(3/N) <= sqrt(13.5)*p + (13.5)^(1/4)*sqrt(p)/sqrt(2).

The right side is less than 4p for every p≥19. The low branch applies. At p=11 the exact low-branch equation does not give the claimed inequality, so the original p≥11 onset cannot be used without modifying N. Thus p≥19 is a safe fully proved statement.

The resulting line has N=9p², characteristic p>K−1, M+1=Theta(p³)=Theta(N^(3/2)) exceptional labels, both sources and common agreement ≤2p+3, and threshold 4p strictly above first order and below Johnson. Its domain/challenge field is F_(p⁴); its rate vanishes. It improves the characteristic-versus-length scale relative to the existing projective quadratic line, not the Theta(sqrt N) agreement-gap scale. The one projective-infinity label has two witnesses, as explicitly noted.
