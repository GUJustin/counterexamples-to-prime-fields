# Point-free proper degree-five Pfaffian fibers: a sufficient geometric criterion

September 18, 2026. This note supplies a criterion for the d=5 native-label investigation. It does not analyze the theta,z equations, prove those fibers proper, or assert their surjectivity. No main or binary-workspace files were edited.

**Proposition.** Let C be a geometrically connected projective curve over a finite field Fq. Suppose C is geometrically Cohen--Macaulay and pure of dimension one, has degree five in its given projective embedding, and has arithmetic genus one. Then C(Fq) is empty if and only if C over the algebraic closure is a reduced union of five lines whose incidence graph is a five-cycle and Frobenius acts transitively on the lines.

In particular the proposition applies to a scheme-theoretically proper P4 linear section of Gr(2,5), or to a degree-five Pfaffian model whose homogeneous Pfaffian ideal has height three. No lower bound on q is required. Nonreduced fibers under these hypotheses always have an Fq point.

## 1. Literature and precise hypotheses

Fisher--Sadek, [On genus one curves of degree 5 with square-free discriminant](https://arxiv.org/pdf/1406.6953), Lemma 5.3, proves a useful properness test: independence of the five Pfaffians together with absence of a plane in the geometric support forces a curve. The height-three Pfaffian resolution then supplies the degree and genus. Their lemma is not a classification of point-free finite-field fibers. Fisher's [Minimisation and reduction of 5-coverings of elliptic curves](https://arxiv.org/pdf/1112.5131), Lemmas 7.8--7.10, studies related geometric degenerations; its local minimality hypotheses should not be silently transferred to the present family.

The closely related tangent and pentagon criteria already appear in Shunqi Lu's [Completing the classification of maximum scattered linear sets in PG(1,q^5)](https://shunqilu.github.io/publications/classification_maximum_scattered_linear_sets_PG1q5.pdf), version dated September 1, 2026, Lemmas 3.1--3.3. Those statements have explicit height-three, smooth-orbit, and, for the pentagon converse, line-disjointness hypotheses. Their local proofs check independently; the full new preprint's classification is not assumed here. The argument below separately treats all component orbits and nonreduced fibers, so it does not require a distinguished smooth orbit of spanning points. No novelty claim is made for this finite-field geometry.

For a height-three Pfaffian ideal in R=Fq[x0,...,x4], the Buchsbaum--Eisenbud complex is exact:

    0 -> R(-5) -> R(-3)^5 -> R(-2)^5 -> R -> R/I -> 0.

Its Hilbert series is (1+3t+t^2)/(1-t)^2, hence its Hilbert polynomial is 5m. The ring is Cohen--Macaulay and Gorenstein. Sheafifying the resolution and using the intermediate cohomology vanishing of line bundles on P4 gives H^0(C_bar,O)=Fq_bar. Thus C is geometrically connected and has all the proposition's hypotheses, including absence of embedded or isolated components. The same conclusions follow for a proper P4 section of Gr(2,5): expected dimension one gives height three for the restricted Pfaffian ideal. These assertions survive base change.

The remaining proof is a component, degree, and intersection argument.

## 2. Every nonreduced case has a rational point

Work over the algebraic closure, with Frobenius permuting geometric irreducible components. For a component orbit let l be its length, d the degree of each component, and m its common generic multiplicity. That orbit contributes l*m*d to degree five.

Cohen--Macaulayness excludes embedded associated points. Therefore a nonreduced curve must have a component of generic multiplicity m>=2: otherwise a nonzero nilradical would have an embedded associated point. For such a component orbit there are only two possibilities:

* l=1. The Frobenius-fixed component has degree d<=2 and descends to a geometrically integral Fq line or conic. It has an Fq point.
* l=2. Necessarily m=2 and d=1; this consumes degree four. The remaining degree-one component is a Frobenius-fixed line, also giving an Fq point.

No larger orbit fits into degree five. A geometrically integral conic over a finite field has a rational point, including in characteristic two. Thus a point-free curve in the proposition must be geometrically reduced.

## 3. A fixed geometric component also gives a rational point

Now suppose C is geometrically reduced. Let r be the number of geometric components, g_i their normalization genera, and delta_P the lengths of the normalization quotients at geometric singular points. Geometric connectedness and the normalization sequence give

    1=p_a(C)=sum_i g_i + sum_P delta_P-r+1.

Connectedness implies sum_P delta_P>=r-1: identifying the r normalized components into one connected curve requires at least r-1 independent branch identifications. Equivalently, delta_P is at least the number of branches at P minus one, and the incidence graph is connected. Therefore sum_i g_i<=1.

If a component is Frobenius-fixed, it descends to a geometrically integral Fq curve. Its normalization is a smooth projective curve over the perfect field Fq and has genus zero or one. The Hasse--Weil lower bound

    #normalization(Fq)>=q+1-2g*sqrt(q)>0

holds for every finite q>=2 when g<=1. Its rational point maps to C(Fq). Hence a point-free C has no Frobenius-fixed geometric component.

## 4. The only orbit partitions are five lines or two plus three lines

Every nontrivial component orbit contributes at least its length to degree five. With no fixed component, the only possible weighted-degree partitions are 5 or 2+3. In both cases all components have degree one and multiplicity one. Thus the support consists of five distinct lines, and their normalizations have genus zero. The normalization identity specializes to

    sum_P delta_P=5.

First consider two conjugate lines A0,A1 and three conjugate lines B0,B1,B2. Connectedness requires an A--B intersection. Frobenius acts transitively on the six cross-pairs, so all six cross-pairs intersect. The resulting intersection points form one orbit of length dividing six.

If this orbit has length one, there is an Fq point. If it has length two, all three B-lines pass through both distinct points, impossible for distinct projective lines. If it has length three, both A-lines pass through the same three distinct points, again impossible. More explicitly, label cross-pairs by t in Z/6 via (A_(t mod 2),B_(t mod 3)); an equivariant identification into two or three points is reduction modulo two or three, respectively. If the orbit has length six, there are at least six distinct singular points, each with delta>=1, contradicting sum delta=5. Therefore the 2+3 orbit pattern cannot be point-free.

## 5. Five conjugate lines force exactly the nonsplit pentagon

The remaining case is one Frobenius orbit of five lines. Any intersection point is fixed by the fifth power of Frobenius, since each pair of distinct projective lines has at most one intersection. If an intersection point is Frobenius-fixed, it is already rational.

Suppose there is no rational point. A point incident with at least three lines would then have five distinct conjugates. Each uses at least three unordered pairs of lines; no line pair can occur at two distinct intersection points. This would require at least fifteen distinct pairs, although five lines have only ten pairs. Thus every intersection involves exactly two lines.

Two distinct projective lines have distinct tangent directions at their intersection, so these two-branch singularities are ordinary nodes with delta=1. The curve consequently has exactly five nodes. Its connected incidence graph has five vertices and five edges, is simple, and admits a transitive cyclic permutation of the five vertices. All vertices have equal valency, necessarily two. Hence the graph is a five-cycle.

Conversely, on a reduced five-cycle with Frobenius transitive on the lines, a smooth rational point would force its unique component to be fixed. A rational node would force its incident pair of lines to be invariant under a five-cycle, also impossible. Thus the curve has no Fq point. This completes the proposition.

## 6. A usable sufficient test for the d=5 fibers

For a given label, first prove height three or establish a rational point by another argument. A mere assertion that five hyperplanes were imposed does not prove properness. Once height three is known, point-freeness is equivalent to the transitive pentagon above; every nonreduced fiber already has a point.

One convenient way to exclude a pentagon is to exhibit a geometric smooth point P and show that its projective tangent line is not contained in C. A smooth point on a pentagon lies on exactly one line, which is its tangent line. For a curve defined by quadrics, if the tangent line is spanned by P and v, the containment check reduces to evaluating the defining quadrics at v: their values at P and their polar terms already vanish. Any nonzero evaluation therefore proves C(Fq)!=empty, provided the height-three hypothesis has been established.

This last implication is a sufficient test, not a claim that one tangent calculation resolves every singular label. For improper fibers the proposition is inapplicable. Lu's Lemma 2.3 gives an independently checkable primal--dual point-count equality without properness assumptions, but it is not itself an existence theorem. The explicit d=5 parameter family must still account for dimension jumps and exclude all remaining nonsplit-pentagon fibers before an all-native-label conclusion is justified.
