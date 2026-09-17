# A far point with almost all other parameters nearby

September 17, 2026. New simplification of averaged padding; proof below.
Not yet integrated into the manuscript at this checkpoint.

Keep the core hypotheses of AVERAGED_PADDING.md: w has degree A-1,
P_1,...,P_L are distinct degree<K<A polynomials, each has exactly A-1
agreements with w on N old coordinates. Let q<=p-N, n=N+q. There is
NO restriction K-1+q<A and NO direction union-bound condition.
Put R=p-N, T=d*binom(L,2)-pairs(L*(A-1),N), and
M=L^2*R/(L*R+2*T), as before.

Choose q available points with largest evaluation-image sizes s_x.
Every P_i-w has degree exactly A-1, all of whose roots already occur
on the core. Hence P_i(x)-w(x) is NONZERO at every available point.
The difference images S_x={P_i(x)-w(x)} are subsets of F_p^*, with
size s_x and mean at least M. In particular M<=p-1.

Set f(x)=w(x) on the ENTIRE new domain. Set g=0 on the core and
choose g_j independently uniformly in F_p^* on the padding. Each
selected candidate becomes nearby at parameters

    z=(P_i(x_j)-w(x_j))/g_j,

which are always nonzero. For each fixed z!=0, independent random
multiplicative shifts hit it at coordinate j with probability s_x/(p-1).
Therefore the expected union has size

    (p-1)*(1-product_j(1-s_x/(p-1)))
      >= (p-1)*(1-(1-M/(p-1))^q).

Some choice of g attains the ceiling. This proves a nearby-label lower
bound analogous to the additive-offset version, with p replaced by p-1.

At z=0, f=w agrees with any degree<K polynomial on at most A-1
coordinates by the root bound. Selected P_i attain A-1 agreements,
so this word has distance EXACTLY (n-A+1)/n, one coordinate beyond
the nearby radius (n-A)/n. Also no pair F,G can have A joint agreements
with f,g, because even F alone cannot agree with f at A coordinates.
Thus the far-point and no-correlated-agreement assertions are automatic.
The received line is nonconstant because g is nonzero on the padding.

Both dense asymptotic theorems survive with identical leading constants:
p-1~p and the same image estimates apply. The direction-condition proof
becomes unnecessary. The near-unit theorem still needs c>H_2(rho) for
strict Elias; it no longer needs it to construct a suitable direction.
The family now genuinely has a farther point, unlike the previous
additive-offset argument, which did not assert one.

Finite replay must use the new p-1 union formula, not silently reuse
p-based rounded counts. The change in the unrounded count is at most
one, but an integer or eighth-decimal endpoint can change. Recheck all
displayed density bounds before modifying the manuscript. Prior additive
construction certificates remain independently valid.
