# Complete one-pole test on the positive seven-cubic bank

The exact number-field affine bank was tested on all C(14,7)=3432 supports.
There is no proper N(X)/(X-b), degree N at most4, with b outside the domain,
agreeing on seven nodes. There is also no degree-four polynomial agreeing
on seven nodes (the corresponding pole-at-infinity case for an O(3)
section). The conclusion holds after any extension of the cubic coefficient
field, not only for poles already in that field.

For completeness, fix the first five nodes of a proposed support. Let W be
their degree-at-most-four interpolant, L their monic degree-five locator,
and ell the leading coefficient of W. Every degree-at-most-four numerator
with pole b matching these five values has exactly the form

    N(X)=(X-b)W(X)-ell L(X).

If ell=0 this is an improper polynomial. Otherwise a sixth node x with
received value y forces

    b=x-ell L(x)/(W(x)-y).

The denominator cannot vanish, since L(x) is nonzero. Thus the two remaining
support nodes must prescribe the same pole, necessarily in the original
coefficient field. The program tests that equality exactly and rejects
poles on the domain; any retained numerator must satisfy N(b) nonzero.
For the infinity case, the same W must match both remaining nodes and have
nonzero degree-four coefficient. All cases failed.

The implementation groups supports by their first five nodes (792 groups),
uses independently implemented Fraction arithmetic in Q(w), and reports
3432 supports,67 degree-at-most-three interpolants, zero finite proper
witnesses, and zero quartic-at-infinity supports. Files:
`orbit7_one_pole.py/json/log/resources.json`. The watchdog run completed in
2.15 seconds with less than13 MiB RSS.

This blocks the immediate one-pole extension of this particular bank. It
is not an obstruction to other seven-word banks or other extension
operations, and it does not weaken the certified positive seven-word result.
