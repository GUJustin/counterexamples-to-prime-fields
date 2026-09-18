# Five-tag exchange amplification: independent audit

September18,2026. PASS for the root's component cap. A stronger aggregate count below bounds all collisions obtainable by whole-mu4-packet compositions, including overlapping translates. No five-tag scan was repeated and no large component search was launched.

The54 verified modular exchanges are real finite-field identities. Their signed support differences are constant on each of the64 mu4 packets in mu256. Every sum of such differences retains this property. Thus, on the136-subsets of mu256 minus1, any chain of legal exchanges fixes every partially occupied packet. Overlap and order of application do not alter this invariant.

## Individual component cap

Use the ambient sector determined by these fixed partial patterns. Let r count all pure nonidentity packets, including ones that might never actually toggle in the chosen move graph. Let c be the number of points in the fixed partial packets. Then

    c=4q,  k=34-q,  c<=3(64-r),  q<=63-r.

The distinguished packet cannot be full because1 was omitted. An r-packet selection J with k full packets can be enlarged by any fixed q nonidentity tags outside this pool, giving an injection into34-subsets of the63 nonidentity tags. A full packet of tag a has product -a, so this injection preserves the product key up to a fixed multiplier. Consequently each component is bounded by the largest product class of these34-subsets, even before enforcing the tag-sum constraint.

An independent character calculation gives that maximum explicitly. Put N63=C(63,34)=759510004936100355. For product exponent s modulo64, the class size is

    [N63 -265182525*c2(s) +6435*c4(s) +35*c8(s)
          +3*c16(s) -c32(s) +c64(s)]/64,

where c_d is the Ramanujan sum for order d. This follows by taking the x^34 coefficient in (1-(-x)^d)^(64/d)/(1+x). Every odd s attains the maximum

    [C(63,34)+C(31,17)]/64 =11867343831270045.

Every even class is smaller. All64 values independently match the root's DP file. The required274980728111395088 witnesses therefore need at least24 distinct partial-pattern sectors. The existing moves cannot connect those sectors.

## Exact ceiling on aggregate packet amplification

There is also a small exact bound on the total number of pairs that packet compositions could certify. Relax the graph maximally: allow ANY size-preserving exchange of whole mu4 packets and discard every moment and product requirement. Two136-subsets are in the same relaxed sector exactly when their difference is constant on all packets.

For an ordered pair (U,V), let h be the number of packets full in U and empty in V; cardinality forces the same number in the reverse direction. Both kinds avoid the distinguished packet. Choose the two disjoint tag sets in

    C(63,h)*C(63-h,h)

ways, then choose their common136-4h roots in C(255-8h,136-4h) ways. This decomposition is unique. Hence the exact number of all same-sector ordered pairs is

    B = sum_(h=0)^29 C(63,h)*C(63-h,h)*C(255-8h,136-4h)
      =414319865818322878759515521387490230478570450041439785658992436327353246660877.

Writing N=C(255,136),

    B/N =252.20911707958686.

Thus even the complete transitive closure of every possible whole-packet move, with all signature restrictions optimistically removed, supplies at most this average number of certified partners. Its ordered-pair count is only about2^(-49.95363) of the sufficient second-moment target N*(274980728111395088-1)+1. This counts across ALL partial-pattern sectors, so summing separate components does not evade the aggregate ceiling.

This is a bound on packet-generated pairs, not on the full modular signature collision count. The latter already has a far larger lower bound by pigeonhole and necessarily involves many distinct partial patterns. One cannot add the relaxed bound to the generic Cauchy-Schwarz estimate as if the pairs were disjoint. An improvement would need a new relation or theorem that actually couples different partial patterns sharing the full signature; translations, overlapping applications, and integer combinations of this mu4 relation cannot do that alone.

## Verification

`verify_amplification_audit.py` / `amplification_audit.json` independently check all54 saved signed exchange vectors, replay all64 product-class counts by the character formula, and exhaust small sector partitions to validate the new ordered-pair identity. The structural proof and arithmetic cover arbitrary compositions; no heuristic connectivity claim or independence assumption is used.
