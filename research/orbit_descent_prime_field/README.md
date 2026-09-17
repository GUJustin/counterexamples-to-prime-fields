# Orbit descent and the remaining prime-field ratio

September 17, 2026. The complete descent argument and its quantitative
prime-field implication are in ../ordinary_ca_superlinear/PROOF.md.

A nearest orbit of size r for the full Dickson word descends to a true
nearest list of size r on mu_(4r), over the SAME F_p. Thus r->infinity
and r/p->0 would suffice for superlinear full-support MCA counts over
prime fields at exact rate1/8 and gap1/16. Only unbounded r is currently
proved. The ratio condition is not a consequence of orbit descent.

The scanner checks every degree-determining subset for13 small proper
quotients, using the previously audited quotient_scan.cpp. The r3 andr4
cases use220 and1,820 subsets; r5 uses15,504; r6 uses134,596; each r8
case uses10,518,300. Every listed maximum is strictly below3r/2.
The complete rows are in scan.json. These results exclude these particular
quotients as descents of a full-word nearest candidate, whose normalized
agreement is at least3/8. They do not rule out larger quotient degrees,
other primes, or different received words.

This investigation did yield the unconditional quadratic ordinary-CA
result over F_(p^2): descent makes the true nearest list linear relative
to its own length, irrespective of p/r. The prime-field obstruction is
now precisely the missing short-domain ratio for this route.

Reproduce by compiling ../dickson_fixed_gap/quotient_scan.cpp to the
existing tmp/dickson-quotient-scan path and running scan.py under the
repository resource guard. No source modification or new compiler was
used for these runs.
