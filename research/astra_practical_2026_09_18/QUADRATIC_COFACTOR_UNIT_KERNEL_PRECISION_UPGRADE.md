# A large valid bank forces a unit kernel at the full fifteen-coefficient prefix

Let E=F_(p^6), p>3. Let W(U)=a+Ub modulo Z^15, with a(0)=1 and b(0)=0, and W'(V)=a^sigma+V b^sigma. Suppose a set S of distinct tau in E has genuine reversed quadratic cofactors q_tau with q_tau(0)=1, and genuine base-field packet prefixes V_tau, such that

W(tau)=V_tau*q_tau modulo Z^15.

Then W(tau)*q_tau^sigma=W'(tau^p)*q_tau modulo Z^15. If

|S|>3p+2,

the same equation has a GENERIC unit solution: there are polynomials P,Q in E(U,V)[Z], deg P,deg Q<=2, with P(0)=Q(0)=1 and

W(U)*P=W'(V)*Q modulo Z^15.

No labels need be discarded. This conclusion does not assume the earlier all-maximal-minors test; it implies that test.

## Exact augmented-rank argument

Write P=1+x1 Z+x2 Z^2 and Q=1+y1 Z+y2 Z^2. The constant equation is automatic. The remaining fourteen equations are

N x=d,

with four columns N=[ZW,Z^2W,-ZW',-Z^2W'] and d=W'-W, using coefficients of Z^1,...,Z^14. Entries in the first two columns are affine in U, entries in the next two are affine in V, and d is affine jointly in U,V.

Let r be the rank of N over E(U,V). All (r+1)-minors of N are identically zero, so no specialization can have rank greater than r. If the augmented system were generically inconsistent, [N|d] would have rank r+1. Choose a nonzero (r+1)-minor D. It necessarily includes d, since N alone has rank r.

At every valid specialization (tau,tau^p), the system is consistent. Its augmented rank is therefore at most r, even if the rank of N drops. Thus D(tau,tau^p)=0 for EVERY tau in S.

There are at most two U-only columns and two V-only columns. Expanding the d column into its constant, U and V parts shows that every monomial U^i V^j of D has i<=3,j<=3 and i+j<=5; more precisely its support is contained in the union of the rectangles (i<=3,j<=2) and (i<=2,j<=3). Since p>3, substitution V=U^p sends distinct monomials to distinct powers. Therefore D(U,U^p) is nonzero, of degree at most3p+2. It cannot have more than3p+2 roots, a contradiction.

## Full-precision classification

Use the proof in `QUADRATIC_COFACTOR_IDENTITY_COMMON_FACTOR_REDUCTION.md`, starting with this unit relation instead of dividing a Z-valued kernel. Every rational approximation and interpolation is now valid modulo Z^15. All cross-product degrees in that proof are at most eight, so every step remains valid with the higher precision.

Consequently a genuine large bank has, modulo Z^15, the following classification. If b is nonzero, reduce b/a=B/A with coprime polynomials, A(0)=1,B(0)=0, and t=max(deg A,deg B)<=2.

* t=2: a=H A,b=H B with H over Fp modulo Z^15.
* t=1: a=H_base F A,b=H_base F B, where H_base is over Fp modulo Z^15 and F=product_{i=0}^{j-1}(1-u^(p^i)Z) for some0<=j<=5.
* b=0 modulo Z^15: the fifteen-coefficient product prefix is fixed (fourteen nonconstant coefficients); no fixed packet prefix is inferred when q varies.

The same normalized rational-function and Frobenius-norm arguments establish these statements. In the linear branch, the sixfold norm has numerator and denominator degree at most six, again strictly below the available precision.

For the practical prime p=2130706433 the exceptional upper bound is

3p+2=6392119301,

far below the required274980728111395088 distinct labels. Thus a proposed practical bank necessarily falls into the FULL fifteen-coefficient-prefix classification, not merely its thirteen-coefficient truncation (twelve nonconstant heads).

This recovers two coefficients in the structural reduction. It does not by itself prove a numerical packet-fiber upper bound, a fixed packet head in every branch, root-free cofactors, or a successful denominator remainder construction. Those remain separate arithmetic requirements. In particular no factor-p loss or factor-four improvement follows solely from the classification.

## Primitive quadratic branch: fixed packet prefix outside at most 2p+1 labels

In the t=2 branch write W_tau=H P_tau modulo Z^15, with H over Fp, P_tau=A+tau B, gcd(A,B)=1, A(0)=1,B(0)=0 and generic degree2. For each actual factorization W_tau=V_tau q_tau, the rational function P_tau/q_tau agrees modulo Z^15 with the base-field series V_tau/H. Its Frobenius cross-difference has degree at most four and vanishes to order15; consequently P_tau/q_tau lies exactly in Fp(Z).

There are at most p parameters for which P_tau has an Fp root: each r in Fp allows at most one tau, since A(r),B(r) cannot both vanish. There are at most p parameters for which the entire normalized P_tau belongs to Fp[Z]: choose any nonzero coefficient of B, whose corresponding coefficient A_i+tau B_i determines tau from a value in Fp. Finally, there is at most one parameter where the generic quadratic degree drops.

Outside this union of at most2p+1 parameters, P_tau has degree2 and no nonconstant divisor in Fp[Z]. Indeed such a divisor would either be linear, giving an Fp root, or quadratic, making normalized P_tau itself a base-field polynomial.

Write the reduced rational function P_tau/q_tau as R/S with coprime R,S in Fp[Z]. From P_tau S=q_tau R and coprimality, R divides P_tau. The absence of a nonconstant base-field divisor forces R to be constant. Therefore P_tau divides q_tau. Both have degree at most two, P_tau has degree two, and both have constant coefficient1, so q_tau=P_tau. It follows that

V_tau=H modulo Z^15.

Thus the packet prefix modulo Z^15 is fixed, namely its constant coefficient1 and FOURTEEN nonconstant heads on a subbank losing at most2p+1 labels. This is a genuine reduction to a fixed-prefix packet family. It is still not a numerical bound on that family's finite root-subset fiber; any use of a separate fixed-head or denominator-remainder gate must check that gate's own hypotheses.

## Primitive linear branch: remaining factor allocation

Choose the partial-orbit representation with F=1 when H/H^sigma=1. Otherwise let d<=6 be the orbit length of u and choose 1<=j<d, so F contains a proper consecutive segment of j distinct conjugates. In particular F has no nonconstant divisor in Fp[Z]. Write W_tau=H_base F P_tau, where P_tau=A+tau B is a primitive normalized linear pencil.

The actual factorization implies F P_tau/q_tau is in Fp(Z): the Frobenius cross-product degree is at most (j+1)+2<=8, less than15. Exclude at most p parameters where P_tau belongs to Fp[Z], at most one degree-drop parameter, and at most d<=6 parameters where its root belongs to the full orbit underlying F. Each root condition determines at most one parameter by coprimality of A,B.

For every remaining valid parameter, P_tau must divide q_tau. Otherwise its root survives in the reduced numerator of the base-field rational function F P_tau/q_tau. All Frobenius conjugates of that root must then also survive, but none occurs in F, and P_tau has only one root. This contradicts P_tau being non-base-field. Write q_tau=P_tau q0, with deg q0<=1 and q0(0)=1. Now F/q0 lies in Fp(Z).

If j>=2, write F/q0=R/S in reduced base-field form. Since R divides F and F has no nonconstant base-field divisor, R is constant and F divides q0, impossible. Thus this branch has at most p+7 valid labels.

If j=1, the same argument gives q0=F and V_tau=H_base modulo Z^15: the packet prefix modulo Z^15 (fourteen nonconstant heads) is fixed outside at most p+7 labels.

If j=0, q0 itself is a base-field polynomial of degree at most one. Consequently V_tau*q0=H_base modulo Z^15. This last case has a varying base-field linear cofactor; it is not a fixed-head conclusion for V_tau alone. It is exactly the arithmetic residual case that must be checked against the existing base-field-cofactor quotient/dimension analysis, without converting a dimension statement into a fiber-count bound.

For GENUINE NONCONSTANT prefix pencils (b!=0 modulo Z^15), the primitive quadratic and linear branches reduce to a fixed packet prefix modulo Z^15, or to such a fixed prefix after multiplication by a base-field linear cofactor, apart from explicitly O(p) exceptional labels. Each prefix consists of the normalization coefficient and fourteen nonconstant heads. The b=0 case remains a SEPARATE constant-product-prefix branch: W is fixed modulo Z^15, but V need not be fixed when the quadratic cofactor varies. In particular a constant base-field W prefix can allow varying base-field quadratic cofactors; this branch is not absorbed into the preceding two conclusions. No root-subset cardinality improvement follows automatically.

## Constant product-prefix branch: base-field factors of degree at most two

When b=0 modulo Z^15, choose one actual factorization a=V_* q_* modulo Z^15. Normalize all factors at Z=0. Let B_* be the maximal divisor of q_* in Fp[Z], and write q_*=F_* B_*. Such a maximal divisor exists: on each Frobenius orbit of irreducible factors, retain the minimum multiplicity. Every base-field divisor of q_* divides B_*.

For any other actual factorization a=V_tau q_tau, the quotient q_*/q_tau agrees with the base-field series V_tau/V_* modulo Z^15. Its Frobenius cross-difference has degree at most four, so the quotient is exactly in Fp(Z). Write q_*/q_tau=R/S in reduced normalized base-field form. Then R divides q_*, hence R divides B_*, and

q_tau=F_* (B_*/R)S=F_* B_tau,

where B_tau is over Fp and has degree at most 2−deg F_*. Cancelling the unit F_* gives

V_tau B_tau=V_* B_* modulo Z^15.

The right-hand side is one fixed base-field prefix. This reduction loses no labels. It permits a base-field quadratic cofactor when deg F_*=0, a base-field linear cofactor when deg F_*=1, and a fixed packet prefix when deg F_*=2. In particular, it does not turn a constant product prefix into a fixed packet prefix without checking its factor allocation.

## Indexing and final scope

Modulo Z^15 means coefficients0 through14. Coefficient0 is the monic normalization1, so this is FOURTEEN nonconstant heads, not fifteen. Recovering the unit kernel restores the two coefficients lost by the abstract modulo-Z^13 argument; it does not manufacture the coefficient of Z^15. At the practical boundary deg(T)=e+1031, any application must use the fourteen-head-plus-remainder gate and verify its additional hypotheses. The fifteen-nonconstant-head gate requires the separately available coefficient at Z^15. Constant product-prefix pencils have the separate base-field factor reduction above; a quadratic residual is allowed. None of these statements supplies a numerical finite-fiber count.
