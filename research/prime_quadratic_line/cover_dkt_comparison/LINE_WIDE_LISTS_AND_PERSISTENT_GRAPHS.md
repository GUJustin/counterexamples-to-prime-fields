# Line-wide lists, codewide lists, and a valid persistent-graph refinement

This note separates three different quantities. No main-manuscript changes.

## Positive-density cover: small lists along the one constructed line

For each canonical label lambda≠0,1, the total bank–fiber hit count S_lambda is a sum of independent Bernoulli variables with mean≤2 for sufficiently large L. Thus
Pr(S_lambda≥r)≤(2e/r)^r.
Taking r=ceil(3logp/loglogp) and union-bounding over all p labels gives failure probabilityo(1). This event can be imposed simultaneously with the nonbank-good event and the positive singleton population: excluding failed samples costs onlyo(p) in the expected singleton count.

Every bank's agreement is A+s·h, where h is its number of fresh fiber hits. Every nonbank has agreement≤A on the good event. Therefore at EVERY point on this ONE line, and at EVERY integer threshold R with A<R≤T=A+s, the list has size≤r. At any of the counted singleton labels, the list remains the same singleton throughout this entire threshold interval. The final infinity word has singleton list{0}, since nonzero degree≤2s polynomials match it at at most5s<A coordinates.

This is uniform along the constructed line; it is NOT a codewide list-size bound over all received words. The argument here is for the positive-density p~L³ realization. For an off-density realization, a failure probability merelyo(1) is insufficient when subtracting it from an expected counto(p); a stronger tail must be chosen.

Root's separate deterministic greedy/full-fiber construction may improve this to line-wide list size1 over sufficiently large fields. That strengthens the distinction below but is not needed for this probabilistic note.

## The same code has a list of size at least L at the TARGET threshold

Choose one distinct fresh base fiber for each of the L bank members (there are t≥L). Define another received word W to equal the common intersection word on the core, and to equal Q_i on the dedicated fiber assigned to i. Fill all other coordinates arbitrarily.

Every Q_i then has at least A+s=T matches with W. Consequently the codewide maximum list size is at leastL already at threshold T, and hence at every lower threshold. This is stronger than merely observing a large list at T/2. The received word W need not belong to the constructed line.

## Exact DKT interface

The local 2026/2056 text states:
- Lemma5.6/Eq55 and Theorem5.8 bound exceptional challenges from geometric joint degree J and reduced generic-fiber degree F_reg. They have no input parameter representing an attained list size.
- Lemma5.11 explicitly bounds the list of EVERY received word and therefore supplies a codewide bound. Its Lambda cannot be replaced by a line-wide value without a different theorem.
- The ell in curve-indexed geometric formulas is received-curve degree, not list size.

A small number of close candidates at each finite-field specialization does not bound the degree of the algebraic candidate cover: different persistent components may be close at disjoint challenge values. Our bank has L such components even when each line point has at most one close candidate.

Thus the positive-density examples, for0<b<1, rule out a boundO(n Lambda_line^q) with no other growing factors for any fixed q, since M/n is polynomial while Lambda_line is polylogarithmic. They do NOT rule out a theorem using the codewide maximum list size, or one retaining appropriate rate, normalized-gap, or geometric-degree factors.

## Concrete valid algebraic refinement: an affine persistent-graph cover

Suppose every threshold candidate, except a separately counted exceptional set, belongs to one of m fixed graphs
P_i(z)=U_i+zV_i,
where U_i,V_i lie in the message space. Let C_i be the simultaneous agreement count of U_i,V_i with the source pair F,G, and assume C_i≤A<T.

At each of the n−C_i remaining coordinates, agreement of P_i(z) with F+zG holds for at most one challenge (or none). A challenge with T agreements therefore consumes at least T−C_i such accidental-coordinate incidences. Hence the graph contributes at most
(n−C_i)/(T−C_i)≤(n−A)/(T−A)
qualifying labels. Summing gives the valid upper bound
m(n−A)/(T−A),
plus the separately counted exceptions. This uses the actual number of persistent graphs m, not an attained list size.

For the canonical conic bank, the nonbank-good event supplies exactly such a cover with m=L. The bound isO(L³), instead of the generic finite-DKT O(n²). In fact only fresh coordinates can contribute accidental matches; their number is st, and each qualifying challenge requires at leasts of them. Thus the sharper construction-specific bound isLt. It matches the positive-density lower bound's order and the large-field distinct-label construction exactly.

This is a genuine algebraic direction for improving an upper bound: certify a small affine persistent-graph cover, or a comparably simple finite component structure, then charge source-gap incidences. It is not justified merely by knowing all actual nearby lists are singleton. No general reduction from the DKT first-order candidate surface to such a cover has been proved here.
