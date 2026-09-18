# Two-row character supports: exact low-degree correction, but no common line

Bounded characteristic-ladder assessment, September 18, 2026. No scan and no general obstruction to two-row constructions.

Let p be odd, E=F_(p²), omega^p=-omega with omega nonzero, h=(p-1)/2, and D=F_p+omega union F_p-omega. Thus n=2p, K=h<p. For a in F_p set

    S_a={u+omega*chi(u-a): u in F_p, u!=a}.

The two factors below have exactly the prescribed h roots on their respective rows:

    U=(X-a-omega)^h, V=(X-a+omega)^h,
    L_a=(U-1)(V+1)
       =[((X-a)^2-omega^2)^h-1] - [V-U].

Consequently L_a=H_a-P_a, where P_a=V-U has degree at most h-1. The witness degree is already correct for strict message dimension K=h; its characteristic guard is harmless. The support size is p-1. For a!=b, the quadratic-character correlation gives |S_a intersect S_b|=(p-3)/2=h-1, consistent with this small witness degree but not establishing a common source line.

The failure is the high-degree part of H_a. Since h=-1/2 in E, its first two coefficients after the monic leading coefficient are a and a²+omega²/2. Any affine line in high-coefficient space therefore contains at most two such heads for p>=7. Low-degree witnesses cannot alter these coefficients. This is exactly the failed stage; the support and locator identities themselves remain useful.

## Allowing a second quadratic/norm parameter does not fix this construction

Here is a stronger, still narrowly scoped, gate. For p>=11 let

    Q_(s,t)=X²+sX+t,
    head(s,t)=[Q_(s,t)^h] in E[X] / E[X]_(degree<h).

Every affine line contains at most THREE distinct heads of this form. In particular allowing ((X-a)²-c)^h with freely varying c does not supply a growing bank on one received line. This enlarges the possible heads beyond those currently known to give supports in D, so the obstruction applies to that two-parameter proposal a fortiori.

Proof. Denote the first four coefficients below the leading coefficient by c1,...,c4. They survive the quotient because 2h-4>=h for p>=11. Direct expansion gives

    c1=h*s,
    c2=h*t + h(h-1)*s²/2,
    c3=h(h-1)*s*t + h(h-1)(h-2)*s³/6.

If s is nonconstant on the proposed affine line, use s as its affine parameter. Its second coordinate is affine in s, so

    t=alpha+beta*s-(h-1)*s²/2.

Substituting in c3 leaves a cubic with leading coefficient

    h(h-1)(1-2h)/6 = 1/4 in E.

The third coordinate of a line is affine in s. Equality therefore has at most three solutions, over the algebraic closure as well as E.

If s is constant, c2 is affine with nonzero slope in t. For fixed s, c4 is a quadratic in t with leading coefficient

    binom(h,2)=3/8 !=0.

Thus a line contains at most two different t values. If c2 is constant too, there is just one head. This proves the assertion, including all degeneracies of the chosen line.

The statement also handles nonzero scalar multiples of these monic locator heads: if residuals on an affine source line have varying leading coefficient, projectivize their high-coefficient vectors and normalize the leading coordinate to one. A projective line's intersection with this chart is an affine line. Zero leading coefficient is outside the degree-(p-1) locator family, not an extra member of it.

## Scope and decision

This gate applies when the common received line has degree at most p-1 and its residuals, after subtracting strict-degree<h witnesses, have heads given by scalar multiples of a quadratic raised to h. Subtracting a constant such as -1 does not change the head. It does not cover rational or higher-degree heads, supports with a genuinely different locator, a changed evaluation code, or additional multiples of the full domain locator at larger ambient degree. On D the full locator has degree 2p, so no such evaluation ambiguity occurs within the stated degree range.

The simple support family is quantitatively attractive: n=2p, K=(p-1)/2, A=p-1 approaches the Johnson scale and p>K. Nevertheless this specific one- or two-parameter quadratic-power head cannot give Omega(p²) exceptional labels: even the enlarged two-parameter family supplies at most three on any line. Further work must change the head algebra, not merely add a translation or norm constant. No claim is made about all character/norm support families.
