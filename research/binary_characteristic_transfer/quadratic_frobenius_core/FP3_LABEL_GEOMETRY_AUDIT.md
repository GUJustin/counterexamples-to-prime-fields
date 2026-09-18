# Exact F_(p³) label geometry, separated from square-lift supports

Independent audit, September 18, 2026. **PASS** for the label statement. This note does not assert a coding construction or match count.

Let E=F_(p³), W,V two-dimensional F_p subspaces, and index `J_[u]=u^(-1)V` by projective directions [u] in W. This is independent of the representative because V is F_p-linear.

For nonzero lambda, the directions whose J contains lambda are precisely the projective points of `W intersect lambda^(-1)V`. Dimension is at least one, hence each lambda belongs to either one J or all p+1 of them. The latter case is exactly `lambda W=V`.

The multiplicative stabilizer of W is F_p*. Indeed the set `{a in E:aW subset W}` is a subfield: it is closed under addition and multiplication, and a nonzero a acts injectively on finite W, so its inverse also preserves W. E has prime extension degree three, so this subfield is either F_p or E; E is impossible for a proper nonzero subspace W. Thus each scalar orbit of planes has size `(p³-1)/(p-1)=p²+p+1`, equal to the total number of planes. The scalar action is transitive, and exactly p-1 scalars take W to V.

## Zero-coordinate exclusions when V=span(1,eta)

Assume eta is outside F_p and write `lambda=(b+eta c)/u`, with b,c in F_p. Define

    A={1/w:w in W*},  B=eta A.

These are exactly the label sets allowing c=0 and b=0, respectively. Both have p²-1 elements. Their intersection corresponds, under inversion, to `W intersect eta^(-1)W`, which is one-dimensional: equality of the two planes would put eta in the stabilizer F_p*. Hence

    |A intersect B|=p-1,
    |A union B|=2p²-p-1.

More precisely, `A intersect B` IS the exceptional set `{lambda:lambda W=V}`: membership says both 1 and eta belong to lambda W, so their span equals lambda W.

Consequently:

- Exactly `p(p-1)²` nonzero labels have one representing projective direction and both b,c nonzero.
- Each of the p-1 exceptional labels has p+1 representing directions: one with b=0, one with c=0, and p-1 with both nonzero.
- The number of labels having at least one both-nonzero representation is therefore `p(p-1)²+(p-1)`. The exceptional labels are multiple representations, not singleton labels.

As a consistency check, the total both-nonzero incidence count is `(p+1)(p-1)²`, equal to `p(p-1)²+(p-1)²`. The labels in the symmetric difference A△B each have only their unique zero-coordinate representation.

## Conditional square-lift obstruction and exact scope

This label geometry alone supplies no root supports, distinct evaluation domain, or codeword agreement. In particular the earlier doubled square-lift count over F_(p⁴) cannot be transferred to E=F_(p³).

For odd p, the quadratic character of E restricted to F_p* is the ordinary quadratic character of F_p, because `(p³-1)/(p-1)=p²+p+1` is odd. Thus on EACH one-dimensional F_p subspace of E, exactly half of its nonzero elements are squares in E. A two-dimensional W contains p+1 such directions, so W* has exactly `(p²-1)/2` squares. Therefore

    |{x in E:x² in W*}|=p²-1,

rather than `2(p²-1)`. The same holds for any nonzero scalar multiple of W. A construction demanding two square roots for EVERY nonzero element of W fails in E itself.

This does not exclude choosing partial square fibers, a different map, or a larger field. Agreement along affine subspaces and intersections of scaled lifted domains still need their own proof; the label-plane calculation must not be substituted for those calculations. No prime-field or F_(p³) coding theorem is claimed here.
