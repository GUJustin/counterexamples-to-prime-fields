# Arbitrary-word barrier for symmetrized elliptic translations

This strengthens the archived `SYMMETRIZED_TRANSLATIONS.md`: no isogeny received word, torsion domain, or dense-domain assumption is needed. It also permits arbitrary parameter-dependent nonzero scalar and constant normalizations. It does not exclude higher-degree elliptic functions with shared poles.

Let E:y²=x³+Ax+B be nonsingular in characteristic zero or characteristic p>5. Choose L>=4 distinct x-coordinates t_i of non-two-torsion points. Put

    R_t(X)=x(P+T)+x(P-T)
          =2[tX²+(t²+A)X+At+2B]/(X-t)²,
    D0(X)=product_i(X-t_i)².

Allow arbitrary scalars c_i!=0 and b_i, and an arbitrary common polynomial H. The candidate bank is

    P_i(X)=D0(X)(c_i R_(t_i)(X)+b_i)-H(X).

The numerator of R_t at X=t is4(t³+At+B)!=0, so it has a genuine double pole. Hence candidates are distinct.

## Exact degree cost after the normalizations

Write the Laurent expansion

    R_t(X)=2t + (6t²+2A)/X + (10t³+6At+4B)/X² + O(X^-3).

Let D=max_(i,j) deg(P_i-P_j), the minimum possible maximum candidate degree after common polynomial subtraction. We claim D>=2L-2.

If instead D<=2L-3, the rational functions c_iR_(t_i)+b_i have identical coefficients of X^0,X^-1,X^-2. The common X^-1 coefficient cannot be zero, since then every t_i is a root of6t²+2A, impossible for L>=4. Dividing the common X^-2 coefficient by it gives a scalar lambda such that every t_i satisfies

    10t_i³+6At_i+4B = lambda(6t_i²+2A).

This nonzero cubic has at most3 distinct roots, a contradiction. Thus even arbitrary label-dependent c_i,b_i cannot lower the degree cost below2L-2. Without such normalizations the degree is2L; with scalar-only leading normalization it is at least2L-1.

## Agreement bound for every word and every domain

Take any N distinct affine domain points and any received word; let every candidate have at least A_agree matches. At a pole coordinate t_i, all L-1 other candidates take the common value -H(t_i), while P_i does not. There are at most L such coordinates, contributing at most L(L-1) total incidences.

Outside those poles, any pair of candidates has at most4 equal-value coordinates: after cancelling D0, the difference of their normalized rational functions has denominator (X-t_i)²(X-t_j)² and numerator degree at most4. It is not identically zero because of its distinct genuine poles.

Let M be the number of nonpole domain coordinates, and let S be the total candidate/word incidences there. Counting pairs of candidates agreeing with the word gives

    sum_x binom(k_x,2) <=4 binom(L,2),
    S² <= M(S+4L(L-1)),
    S <= M+2L sqrt(M).

Therefore

    A_agree <= L-1+M/L+2sqrt(M).

With a=A_agree/N, rho=(D+1)/N, and the nontrivial-code assumption D<N,

    a-rho <= 1/L+2/sqrt(N)-rho/2
           <= 1/L+2/sqrt(2L-1).

The right side tends to zero as L grows. Since the first-order threshold is at least capacity, this model cannot produce a growing list with a FIXED POSITIVE first-order margin, on any domain and for any word. This closes the sparse-domain loophole of the archived isogeny-word argument. For the unnormalized family one also gets the stronger direct bound a<=rho/2+2/L+O(1/N), since for fixed X the function t->R_t(X) is a nonconstant degree-two map. The pair-count proof is more robust because it allows completely arbitrary c_i,b_i.

## Pullbacks and common zeros do not rescue this model

After a degree-e pullback and multiplication by a common polynomial of degree z, pair-difference degree is at least e(2L-2)+z. There are at most eL inherited pole nodes and at most z new common-zero nodes. Outside these, pairwise equality occurs at at most4e nodes. The same incidence argument gives

    A_agree <= e(L-1)+z+M/L+2sqrt(eM),
    (A_agree-D)/N <= 1/L+2sqrt(e/N)
                     <= 1/L+2/sqrt(2L-2).

This remains valid under arbitrary domain restriction; discarded pole fibers only lower their allowed contribution. More generally, interleaved polynomial pullbacks and common-zero multiplications combine into one total pullback and one common factor, so the same accounting applies. Extra padding coordinates are already included in arbitrary M and the arbitrary received word.

## What must change for an elliptic route to remain promising

Translations by torsion points do not improve this bound: torsion only selects the t_i and changes none of the divisor or pair-incidence counts. Composing R_t with a multiplication/Lattes map is precisely a rational-cover version of the same growing disjoint-pole cost, rather than a new collision source. A viable elliptic construction must therefore use a new common-pole identity (so the degree cost is sublinear in the number of independently moving poles), or higher-degree functions whose pairwise residual intersections grow enough to defeat the displayed pair budget. Neither is supplied by symmetrized translations, scalar/constant normalizations, or ordinary multiplication maps.

No numerical torsion scan is warranted for this family. The statement is not an exclusion of all elliptic, Lattes, or higher-degree singular-first-integral constructions.
