# Arbitrary-word list bound for weighted monic-cubic polynomial first integrals

**Later strengthening:** the final list theorem uses `p>max(3,2D)`; see `TWO_D_RADICAL_BUDGET.md`, its independent audit, and `general_cubic_list.tex`. The stronger characteristic assumptions in this earlier argument remain valid sufficient conditions.

Status: independently checked combination of REPEATED_H_MULTIPLICITY_BUDGET.md and CRITICAL_COMPONENT_CONSTANT_VALUE.md, using the separately audited three-label cubic-cover lemma. This strengthens the root-domain conclusion to every evaluation domain and every received word.

## Statement

Let k be a field of characteristic zero, or characteristic p>max(3,6D). Let 0≤D<n, let H in k[X] be nonzero, and let

    F(X,u)=u³+a2(X)u²+a1(X)u+a0(X),
    deg a2≤D, deg a1≤2D, deg a0≤3D.

Let B consist of all degree-at-most-D polynomial sections P satisfying

    F(X,P)=cH,  c in k.

On any n distinct evaluation coordinates, for any received word, the number L of candidates with at least D+eta*n agreements is at most

    floor(9+(3+108D/n)/eta),                    (1)

for every eta>0. Extending the symbol field causes no problem: extend constants to an algebraic closure of a field containing the coordinates and received symbols. The statement concerns this first-integral section family, not all Reed–Solomon candidates or arbitrary first-order equations.

## Proof

If D=0, candidates are distinct constants, so each coordinate matches at most one and L*eta*n≤n. Assume D≥1.

Each label has at most three polynomial sections. If no selected section has a nonzero label, L≤3. Otherwise N=deg H≤3D, as required by both component arguments.

Extend constants algebraically. If the original critical ideal (F_u,H F_X−H′F) has a positive-dimensional component, the constant-value and cubic-cover arguments give either at most eight sections in total or an affine family of degree-at-most-D polynomials. In the latter case the direct agreement bound is L(a−D)≤n, where a is the minimum candidate agreement. Thus both alternatives satisfy (1).

It remains to treat a zero-dimensional critical ideal (including the unit ideal). Let r be the number of evaluation coordinates that are roots of H, and r_H the number of all distinct roots of H, so r≤r_H. At any evaluation coordinate with H(x)≠0, the received value w(x) fixes the section label:

    c=F(x,w(x))/H(x).

Therefore at most three selected candidates match there. At a root of H, at most L match. Summing all candidate agreements gives

    L a ≤ L r + 3(n−r) ≤ L r_H+3n,
    r_H ≥ a−3n/L.                              (2)

If L≤max(9,3/eta), the claimed bound is immediate. Otherwise, a≥D+eta*n and (2) give

    r_H−D ≥ eta*n−3n/L>0.

The repeated-H total-bank theorem is now applicable, even though the evaluation domain was not restricted to roots of H:

    L ≤ 9+108D/(r_H−D)
      ≤ 9+108D/(eta*n−3n/L).

Since L>9, multiplication by the positive denominator yields

    (L−9)(eta−3/L)≤108D/n,
    eta*L≤9eta+3+108D/n−27/L
          <9eta+3+108D/n.

This implies (1). The displayed floor is safe even when the real upper bound is an integer; the strict inequality could improve that endpoint by one, but no endpoint refinement is needed.

## Scope and interpretation

Repeated roots, arbitrary received values, and positive-dimensional original critical loci are all included after combining the two cases. The coefficient degree caps and characteristic bound remain essential hypotheses of the proved route. No classification of general rational cubic first integrals is asserted; here the denominator H is independent of u and F is monic with the displayed weighted degree budget.

The arbitrary-domain step uses only the fact that a received value away from H=0 determines the constant fiber label. It does not assume the received word satisfies the differential equation or lies on a selected branch.
