# An exact resource profile survives at linear multiplicities13--16

September 19, 2026. This is a limitation of the explicitly tested necessary
resources, not a globally realizable polynomial, a large-list construction,
or a better.codes counterexample.

Use the exact binding shape and rank function from
LINEAR17_OWN_SYSTEM_EXCLUSION.md. For each e=13,14,15,16 put h=43-e and
write A=(Y-P)^e H, deg_Y H=h. The following profile has no bad nodes:

| Coordinate type | Contact | Count |
|---|---:|---:|
| Nongraph | h | 60000 |
| Graph | 42 | 71073 |
| Graph | 43 | 131071 |

The total is262144. There are202144 graph coordinates, fewer than211941,
so the established agreement-overlap test does not route all candidates.

The rank sums and their surplus over the required6802316684344 are:

| e | h | Rank sum | Surplus |
|---:|---:|---:|---:|
|13|30|7028330928619|226014244275|
|14|29|6967610268619|165293584275|
|15|28|6909411348619|107094664275|
|16|27|6853734948619|51418264275|

Every centered coefficient degree budget also passes simultaneously.
For H_j, put k=h-j and nu(s)=max(0,ceil(s/2),s-12). Its forced order sum
on the graph coordinates is

    71073 nu(k-1)+131071 nu(k) <= k w+12.

The exact checker verifies this for every coefficient of all four shapes;
the smallest slack is12. Thus these resources do not force any centered
coefficient to vanish, even if all such coefficients are nonzero.

The local Newton conditions are compatible as well. At a graph coordinate
of contact a=42 or43, take H_h=1 and choose each lower centered coefficient
H_j=t^nu(a-e-j). Then A=Y^e H has

    min_(t^u Y^k in A) [u+k+min(u,12)] = a.

At a nongraph coordinate take received value1, graph P=0, and
A=Y^e(Y-1)^h. After translating the received value its contact expression
has the required minimum h. These are local coefficient models, not
global polynomials satisfying all the degree constraints together.

The explicit graph-power locator helper also fails throughout its own
permitted exponent range. For power q=0,...,55 its weight bound is

    q w+60000h+71073 max(42-q,0)+131071 max(43-q,0).

Because131071=w, powers42 and43 tie for the minimum; every other power
costs more. The minimum is43w+60000h, exceeding the own-system cap55w
by respectively227148,167148,107148,47148 for e=13,14,15,16.

The exact profile checks are included in
linear17_own_system_certificate.py/json. No optimizer is required to
verify them. They show precisely why extending the same inequalities
and graph-power family cannot finish these cases. A further global
compatibility condition, another helper, or a different geometric
inequality would be needed; no such claim is supplied by this profile.

The later [squarefree residual discriminant check](LINEAR13_16_SQUAREFREE_RESIDUAL_LIMIT.md)
adds a resource absent from the calculations above. It rejects these
specific e=13,14 profiles when Disc(H) is nonzero, but explicit shifts
of graph contact43 nodes to contact42 restore all tested budgets.
The e=15,16 profiles already pass that additional budget. Non-squarefree
H remains outside the discriminant argument.
