# Five-tag result: one genuine modular exchange orbit

September18,2026. Parent-authorized bounded follow-up only. Enumeration of all C(63,5)=7,028,847 supports completed in0.81seconds with111280KiB sampled RSS, under the512MiB/120second watchdog. No larger search launched.

Files: `gate5.cpp`, `result5.json`, `resources5.json`; independent replay `verify5.py`, `verified5.json`; optional exact norm calculation `modular_relation5.json`.

## Positive arithmetic result

There are173304 unordered signature collisions. Exactly54 are disjoint and genuinely modular; all remaining collisions lift to characteristic zero. The54 modular exchanges form ONE rotation orbit. A canonical tag representative, allowing tag0 before imposing the omitted-packet condition, is

    A={0,1,5,43,44}, B={6,25,29,37,60}.

With zeta=1548376985 of order64 modulo p=2130706433,

    sum_(a in A) zeta^a = sum_(b in B) zeta^b,
    sum A = sum B mod64.

There are64 rotations, ten of which put0 in the union of the two disjoint five-tag sets. The other54 are exactly the admissible pairs recorded by the exhaustive enumeration. For an admissible explicit example use

    A={24,25,45,46,50}, B={6,10,18,41,51}.

Each tag j corresponds to the four underlying mu256 exponents j,j+64,j+128,j+192. Thus these are disjoint20-root exchanges. The independent Python verifier expands ALL54 pairs into their40 roots, verifies every moment1 through6 and the root product directly in Fp, and verifies nonvanishing modulo Phi64 over the integers. It does not merely repeat the reduced sum/product key.

The canonical signed relation reduced modulo X32+1 is

    F=1+X+2X5-X6-X11-X12-X25+X28-X29.

This polynomial is nonzero over Q(zeta64). Its exact cyclotomic norm is

    resultant(F,X32+1)=127654883813896
                         =2130706433 * 59912.

The benchmark prime occurs exactly once. This supplies explicit arithmetic evidence for a genuinely characteristic-specific relation rather than a disguised lifted packet identity.

## Counting consequence: currently negligible

The54 admissible unordered exchanges give108 ordered exchanges in E20. Their exact completion weight is

    108*C(215,116).

Relative to the sufficient collision target C(255,136)*(274980728111395088-1)+1 this is approximately2^(-91.2056). After division by C(255,136), the contribution to the second-moment lower bound on the largest fiber is only9.6312e-11. Hence this is a modular building block, **not an improved family count or benchmark certificate**.

The maximum signature fiber in this five-tag family remains15. The new exchange orbit does not itself make a large fiber. Any use of it would need a proof that compatible compositions or interaction with the ambient136-subset family produces vastly more collisions; independence and disjointness cannot be assumed. No such amplification theorem is claimed here, and no additional scale was searched.
