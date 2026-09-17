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


## Broader short-domain census (September 17)

`short_domain_scan.py` completes 246 determining-support censuses for
r=2,...,8, with 4r dividing p-1 and p>8r. The prime bound is 2,000
for r<=6 and 500 for r=7,8. Thus every domain leaves enough unused
prime-field coordinates for the exact-halving compiler.

| r | Number of primes | Maximum-agreement distribution |
|---|---:|---|
| 2 | 68 | 2 agreements: 67 primes, 3 agreements: 1 primes |
| 3 | 69 | 4 agreements: 69 primes |
| 4 | 33 | 4 agreements: 14 primes, 5 agreements: 19 primes |
| 5 | 35 | 5 agreements: 1 primes, 6 agreements: 30 primes, 7 agreements: 4 primes |
| 6 | 30 | 8 agreements: 30 primes |
| 7 | 6 | 9 agreements: 5 primes, 10 agreements: 1 primes |
| 8 | 5 | 10 agreements: 3 primes, 11 agreements: 2 primes |

Only r=2,p=17 reaches agreement fraction 3/8: maximum3 on8 points,
with2 nearest polynomials. No new qualifying example was found. This
is evidence about this finite cyclic-word search only, and does not
exclude longer domains, other characteristics, or other received words.
These negative search results are retained here rather than added to the
main paper. The full rows are in `short_domain_scan.json`; both bounded
runs finished successfully, using less than22MiB measured process-group RSS.
