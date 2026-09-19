# Quadratic-cofactor identity case: common-factor reduction

This is an exact necessary structural classification of the truncated identity case. It does not give a numerical bound on packet-subset fibers.

Let k be the coefficient field, let a,a',b,b' be series modulo Z^15, and suppose a+U b and a'+V b' are units for generic independent U,V. Suppose all maximal minors of

[W, ZW, Z^2W, W', ZW', Z^2W']

vanish identically in U,V, where W=a+Ub and W'=a'+Vb'. Then, over an infinite scalar extension of k, there exist a unit series H modulo Z^13 and four polynomials A,B,C,D of degree at most two such that

a=H A, b=H B, a'=H C, b'=H D modulo Z^13.

Conversely, this representation implies the analogous rank defect modulo Z^13. No converse modulo Z^15 is claimed. In the practical application a'=a^sigma and b'=b^sigma. The assertion over an infinite scalar extension avoids silently assuming rational-point descent; the necessary low-degree rational-function certificates below can still be tested directly on the original field coefficients.

## 1. From the rank defect to rational functions

A kernel vector gives P W+Q W'=0 with deg P,deg Q<=2 over k(U,V). Neither P nor Q is zero, since multiplication by a unit is injective on degree-<=2 polynomials modulo Z^15. Their Z-valuations agree, because W,W' are units. Divide by their common Z-power, at most two. Thus W/W' has a rational approximation with unit numerator and denominator of degrees at most two, valid modulo Z^13.

Use the following elementary precision fact repeatedly: two rational functions with unit denominators, of numerator/denominator degrees at most (d1,e1) and (d2,e2), which agree modulo Z^N, are exactly equal whenever N>max(d1+e2,d2+e1). All comparisons below have this maximum at most eight, strictly less than13.

## 2. Fixed denominator for an affine rational pencil

Fix a generic V=v0 and write S=W'(v0). Two generic U specializations give rational functions of type (2,2) for W(U)/S. Their affine interpolation in U is a rational function of type at most (4,4), with one fixed denominator. The generic type-(2,2) approximation agrees with it to order13, so the precision fact makes the equality exact.

Reduce the interpolated rational pencil to its minimal fixed denominator Q. A factor of Q can cancel for generic U only if it divides both coefficient numerators, in which case it was not minimal. Hence its generic reduced denominator is Q, and deg Q<=2. The generic numerator degree is the maximum of the two coefficient-numerator degrees, so both are <=2. We have

W(U)=H0 P_U modulo Z^13,

where H0=S/Q is a unit series and P_U is an affine polynomial pencil of degree<=2. Constant pencils are allowed.

Now fix a generic U=u0. The ratio W'(V)/H0 equals P_u0 times the inverse of a type-(2,2) approximation. It therefore has generic rational type at most (4,2). Interpolating two V values gives type at most (6,4), and comparison to the generic (4,2) approximation is exact because the cross-product degree is at most eight. Minimal-denominator reduction yields

W'(V)/H0=T_V/D0,

where D0 is fixed of degree<=2, T_V is affine in V of degree<=4, and gcd(D0,T_V)=1 generically.

## 3. Independent parameters force the degree-two common factor

The exact rational function P_U D0/T_V agrees with the generic type-(2,2) approximation to W(U)/W'(V). Its cross-product comparison has degree at most six, so it is itself of reduced type (2,2).

Because U,V are independent, any generic common factor of P_U and T_V divides both coefficient polynomials of each pencil. Let this fixed gcd be G. The factor D0 is generically coprime to T_V by minimality. Write P_U=G P'_U and T_V=G T'_V. The reduced ratio is P'_U D0/T'_V; hence

deg(P'_U D0)<=2, deg T'_V<=2.

All denominators and G have nonzero constant coefficient, since the generic original series are units. Setting H=H0 G/D0 proves

W(U)=H[D0 P'_U], W'(V)=H T'_V modulo Z^13,

with both bracketed polynomial pencils of degree<=2, as claimed.

## Consequences and unresolved arithmetic

Assuming additionally a(0)!=0, b/a must admit a type-(2,2) rational representation modulo Z^13, and so must a^sigma/a in the practical Frobenius case. This extra assumption holds in the normalized practical application a(0)=1. A candidate whose normalized pencil direction fails either finite Padé test cannot lie in the all-minors identity case. The simultaneous common-factor condition is stronger than these separate necessary tests.

The surviving prefixes are therefore a fixed unit series times quadratic polynomial pencils; they are not arbitrary fifteen-head pencils. This recovers a concrete exceptional-family interface, but not a root-subset construction. One must still enforce the two additional coefficients at Z^13 and Z^14, the Frobenius relation on the actual cofactor, base-field packet coefficients, root-free cofactor conditions, the denominator remainder identity, and the required number of distinct packet subsets.

In particular, this initial common-factor reduction alone does not prove that H has base-field coefficients, that the first two packet heads are fixed, or that the finite packet fiber loses a factor p. The sharper normalized Frobenius statements below add further structure; no numerical factor-p saving follows merely from this classification or from dimension. The better.codes factor-four concentration deficit remains unresolved.

## Sharper Frobenius classification (normalized genuine pencils)

Assume now k=F_(p^6), a(0)=1,b(0)=0, sigma is coefficient Frobenius, and b is nonzero modulo Z^13. There is a unique reduced rational function b/a of type (2,2) modulo Z^13. Uniqueness follows from the cross-product bound4<13; existence over a scalar extension therefore descends to k (equivalently solve the Padé linear equations over k and normalize the unit denominator). Write it B/A with coprime A,B in k[Z], A(0)=1, B(0)=0, and let t=max(deg A,deg B). Thus t is1 or2. Put H=a/A, a unit k-series.

The generic cross-ratio becomes

(H/H^sigma)*(A+U B)/(A^sigma+V B^sigma).

The ratio H/H^sigma initially has a rational representation of type at most (4,4), obtained from a/a^sigma and A^sigma/A. Its product above has type at most (6,6), and comparison to the generic type-(2,2) approximation is exact because the cross-product degree is at most8<13. Since A,B are coprime, the generic polynomial A+U B has no fixed nonconstant factor; likewise for its independent conjugate pencil. Neither can cancel a fixed numerator or denominator of H/H^sigma, and the two independent polynomial pencils are generically coprime. It follows that H/H^sigma has reduced numerator and denominator degrees at most 2-t.

* If t=2, H/H^sigma is constant. Its constant coefficient is1, so H=H^sigma modulo Z^13. Therefore H has Fp coefficients: the entire exceptional prefix is a fixed base-field series times a primitive quadratic pencil.
* If t=1, H/H^sigma is type (1,1). Its sixfold Frobenius norm equals1 modulo Z^13; the numerator and denominator of that norm have degree<=6, so the equality is exact. If the ratio is nonconstant, it is (1-uZ)/(1-vZ), with u,v nonzero and the same Frobenius orbit, hence v=u^(p^j) for some1<=j<=5. Consequently

  H=H_base * product_{i=0}^{j-1}(1-u^(p^i)Z) modulo Z^13,

  where H_base has Fp coefficients. If the ratio is constant use the empty product.

Thus the remaining identity pencils have an explicit interface: either a base-field common series times a primitive quadratic pencil, or a base-field common series times a fixed partial Frobenius orbit of at most five linear factors and a primitive linear pencil. This is a prefix classification, not a count of valid packet factors. Requiring W=Vpacket*q with Vpacket over Fp and q quadratic remains an additional arithmetic factor-allocation problem, as do the two omitted coefficients and the actual prescribed root-subset condition.

## Coefficient indexing

Modulo Z^13 retains coefficients0..12 (twelve nonconstant heads after normalization), and modulo Z^15 retains coefficients0..14 (fourteen nonconstant heads). See the unit-kernel upgrade receipt for the large-bank upgrade and the separate b=0 constant-product-prefix branch. No fixed packet-prefix conclusion is asserted for that constant-product-prefix branch merely from the product being fixed.
