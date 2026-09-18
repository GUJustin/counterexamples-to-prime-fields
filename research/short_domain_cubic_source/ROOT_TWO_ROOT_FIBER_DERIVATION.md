# Root derivation: arbitrary two-root constant fibers

Status: independent audit PASS; integrated as Lemma R.10 and Theorem R.11. See TWO_ROOT_FIBER_INDEPENDENT_AUDIT.md and TWO_ROOT_INTEGRATION.md.

Work over algebraically closed constants of characteristic zero or p>b. Suppose a monic degree-b family satisfies

    F(X,u)-c0 H(X)=(u-R(X))^r (u-S(X))^s,
    r,s>=1, r+s=b, deg R,deg S<=D, H nonzero.

If R!=S, set Y=(P-R)/(R-S), q=H/(R-S)^b. Sections satisfy

    Y^r(Y+1)^s=lambda q, lambda=c-c0.

If q is constant, every Y is constant and the section bank is an affine pencil. If R=S, one noncritical section likewise puts every section in an affine pencil. Agreement D+eta*n then bounds its list by floor(1/eta).

Assume q nonconstant. Put d=gcd(r,s), r0=r/d, s0=s/d, b0=r0+s0. Choose one nonzero-label section Y*. With h0(y)=y^r0(y+1)^s0 and q0=h0(Y*), q is a constant multiple of q0^d. Every other nonzero-label section satisfies h0(Y)=mu q0 for a nonzero constant mu. The rational function q0 is nonconstant.

## Monodromy for coprime exponents

The polynomial h0 has just two distinct roots with coprime multiplicities. It is indecomposable. Indeed, if h0=A(B) with both degrees greater than one, and A has at least two distinct roots, the two corresponding fibers of B must each consist of a single one of the roots 0,-1. Thus B-alpha and B-beta are constant multiples of y^m and (y+1)^m. Their difference cannot be constant: their leading coefficients must agree, and their degree-(m-1) coefficient differs by a nonzero multiple of m. If A has one distinct root, its degree divides both r0 and s0, also impossible.

Indecomposability gives primitive monodromy: a nontrivial block system would give an intermediate function field, and Luroth plus the unique point over infinity turns that intermediate map into a polynomial decomposition. The derivative of h0 has one simple critical point away from 0,-1, at -r0/b0. Its inertia is a transposition. A primitive permutation group containing a transposition is the full symmetric group: the graph of conjugate transposition edges has components forming a block system, so it is connected, and its edge transpositions generate the symmetric group.

## Three covers have positive genus

For three distinct nonzero mu_i, the covers h0(y_i)=mu_i*t each have a unique nonzero finite branch point, different from those of the other two covers. Its inertia in the joint Galois closure is a transposition in one factor and identity in the others. Conjugating by the joint group, whose projections are surjective, gives the whole symmetric group in each factor. Thus the product monodromy is S_b0^3 and the degree-b0^3 fiber product is connected.

Write r=r0,s=s0,b=b0 for this calculation. At infinity the number of inertia orbits is b^2. At zero the simultaneous (r)(s) permutation has r^2+s^2+3r+3s orbits on the product: the all-r and all-s tuples contribute r^2 and s^2, and the two mixed types contribute 3s and 3r because gcd(r,s)=1. Each of the three separate simple branch points has index b^2. Riemann-Hurwitz therefore gives

    2g-2=2b^2-r^2-s^2-3b=b^2+2rs-3b >=0.

The last inequality holds for b=2 (equality) and for b>=3 because rs>=b-1. Hence g>=1. Three rational solutions with t=q0(X) would embed this positive-genus function field in k(X), impossible by Luroth, even if q0 is inseparable.

There are therefore at most two nonzero mu values. Each admits at most b0 rational solutions Y. The original zero fiber contributes only R,S, yielding at most 2b0+2 sections in total. This is a bound for the entire rational-section bank in the nonconstant-q case, not merely for a received-word list.

This closes two-distinct-root constant fibers only. It does not classify repeated fibers with three or more distinct roots, arbitrary first-order equations, or intrinsic prime-field proximity gaps.
