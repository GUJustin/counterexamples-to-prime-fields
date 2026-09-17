# The natural cyclotomic lift does not preserve the full seed lists

September 17. Exact finite rank certificates, not a general impossibility
claim for moving domains or alternative support families.

For a seed prime p0, put n=p0-1 and K=n/4. Choose a primitive element g
of F_p0 and identify the original node g^j with a primitive nth root
zeta^j in characteristic zero. Keep every Dickson agreement support,
but allow an entirely new received word and new degree-<K witnesses.

For each support, interpolate its witness from K anchor nodes. Each
remaining node gives a homogeneous Lagrange interpolation equation on
the received-word values. All global degree-<K words lie in the kernel,
so its rank is at most n-K. A rank of n-K proves that these are the only
received words; every witness then coincides with that global codeword.

The equations are defined over Q(zeta_n). Reduce at a split auxiliary
prime q=1 mod n, using a primitive nth root in F_q. Distinct-node
interpolation denominators remain nonzero. A full-rank modular minor
therefore certifies full rank in characteristic zero. It also excludes
the fixed pattern in all but finitely many new characteristics, although
this audit does not compute the exceptional primes.

| seed p0 | n | K | auxiliary q | native rank | lifted rank |
|---:|---:|---:|---:|---:|---:|
|17|16|4|65537|11|12|
|41|40|10|65761|29|30|
|97|96|24|65761|71|72|
|193|192|48|67777|143|144|

Only prefixes of7,11,11,15 seed supports, respectively, already force
full lifted rank. The native ranks are n-K-1, retaining the expected
non-codeword direction in the original characteristic.

`check_cyclotomic_lift.py` independently constructs primitive roots,
Lagrange constraints, and modular echelon bases. It checks distinctness
of all new nodes and the global-codeword rank upper bound. The proof
permits arbitrary new received words; it does not merely substitute the
old word polynomial into a new field.

## Keeping only one complete multiplicative orbit

The seed parameters a modulo sign split according to chi(a)=+1 or-1.
For either orbit, remove unused columns before interpreting the kernel;
otherwise free values at untouched coordinates could create a spurious
non-codeword direction.

`check_cyclotomic_orbits.py` checks both orbits at p0=17,41,97,193,257,337.
Every orbit uses all n coordinates in these fixtures. For every p0>=41
in that set, both lifted ranks are exactly n-K. Thus retaining just one
full orbit does not rescue these natural lifts. At p0=17 each four-support
system has eight independent rows and an eight-dimensional kernel;
this small underconstrained case is not excluded. No growing-family
conclusion follows from it, and a deficient modular rank alone would
not ordinarily prove a characteristic-zero rank deficiency.

## What remains possible

This excludes neither different moving domains, other selected sublists,
nor exceptional new characteristics annihilating all relevant maximal
minors. A potential next search is for such exceptional primes at which
these fixed cyclotomic patterns regain a nontrivial kernel. For a prime
q=1 mod n, different primitive nth roots can give different specializations;
a search of just one embedding would not cover all possibilities.
No new fixed-gap short-domain list or benchmark improvement is claimed.

The follow-up `CYCLOTOMIC_EXCEPTION_AUDIT.md` records a23392-embedding
bounded scan and a complete integral certificate for n16: only the
original characteristic17 can realize the full support pattern on the
natural cyclotomic domain. Larger-seed conclusions remain bounded.
