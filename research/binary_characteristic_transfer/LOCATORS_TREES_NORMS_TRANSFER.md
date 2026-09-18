# Additive locators, support trees, norm compilers: characteristic transfer

## Scope and matched baseline

Read-only review of `/Users/jthaler/Documents/binary_field_counterexamples`, in particular `AGENTS.md`, `docs/current-status.md`, `docs/research-strategy.md`, `sections/preliminaries.tex`, `sections/constructions/additive-support-trees.tex`, `sections/constructions/quadratic-near-johnson.tex`, and `sections/constructions/half-rate-norms.tex`. No files in that repository were modified.

The binary manuscript ALREADY extends its general locator compiler to every FIXED characteristic p (Remark `rem:fixed-characteristic-all-rates`). Reproving that is not a new result. The useful extraction below is explicit dependence on growing p, together with an odd-characteristic norm identity and the precise prime-field degeneration. These are weaker, shrinking-gap statements, not a fixed-gap prime-field counterexample or a claimed improvement over DKT.

## 1. Uniform version of the existing locator compiler

Let D be F_p-linear of size N=p^d in a challenge field of size q. Choose a subspace H of size n=N/p^r, and codimension-s subspaces W of H, where s>=2 and d-r>=s+2. Put

    t=n/p^s, K0=t/p^2.

Their locators have p-power exponents. The already-proved triangular elimination uses p-power Frobenius and subtraction (not the binary plus sign) and leaves one affine label coefficient at X^(t/p). The second source before padding is X^(p K0-1), and the strict witness is -R_W/X with degree at most K0-1. The label functions are distinct affine functions of the s-1 compiler parameters.

For completeness, the recovery does not lose uniformity in p: the label coefficients recover the top s locator coefficients. The difference of two locators with those coefficients equal has degree at most n/p^(2s+1), whereas W intersection W' has at least n/p^(2s) elements. Root counting forces equality. Frobenius powers are bijective over the coefficient field, and there is no factorial division.

The population is exactly

    M=[d-r choose s]_p >= p^(s(d-r-s))
                         =N^s/p^(s(s+r)).            (1)

The inequality follows directly from the Gaussian product: each factor (1-p^(i-(d-r)))/(1-p^(i-s)) is at least one. Collision averaging over the compiler parameters gives at least

    ceil(q M/(q+M-1))

distinct labels. In particular M>(q-1)^2 gives ALL q labels by integer rounding.

Let J=floor(rho N), and pad outside H with a locator of degree

    wpad=J-p K0+1.

Provided 0<=wpad<=N-n, the new direction is monic of degree exactly J, the witness degree is at most J-(p-1)K0<J, and

    T >= J+(p^2-p)K0
      = J+N*(p-1)/p^(s+r+1),
    CA_J=agr_J(g)=J.                                (2)

These are exact integer formulas. The first source is not asserted individually far: when all labels are bad, label zero necessarily makes it close. For fixed rho in (0,1) and sufficiently large p, r=1 satisfies the padding inequalities.

If p<=N^gamma and q<=N^a, r=1 gives M>=N^(s-gamma*s*(s+1)). Thus

    s-gamma*s*(s+1)>2a

is a sufficient asymptotic all-label condition. The certified fractional gap is of order p^(-s-1), not a uniform positive constant. The seed-dimension/integrality condition must also be retained.

### Concrete growing-characteristic consequence

For every sufficiently large prime p and any fixed rho in (0,1), take

    native field/domain F_(p^10), N=p^10,
    n=p^9, s=4, K0=p^3, J=floor(rho N).

Here M=[9 choose4]_p>=p^20=N^2>(N-1)^2. Consequently one fixed pair has EVERY native challenge exceptional at

    T >= J+p^5-p^4,   CA_J=J.

Absorbing the monic degree-J direction into the witnesses gives at least N distinct nearby codewords in the code of dimension J+1, at the same agreement. Their degree-J coefficients are the distinct negatives of the labels.

This is an explicit shrinking-gap lower bound as characteristic grows: additive gap is asymptotic to sqrt(N), fractional gap to N^(-1/2). It does not contradict fixed-positive-gap large-characteristic results. The all-label criterion cannot work in a smaller fixed native extension degree by this population exponent alone: with r=1, max_s s(d-1-s)=floor((d-1)^2/4), which first reaches 2d at d=10. This is a limitation of the stated sufficient count, not an impossibility theorem for other constructions.

### Prime-field endpoint

Inside F_p an F_p-linear domain has dimension at most one. The compiler requires d-r>=s+2 and a nontrivial codimension-s subspace family, so it has no genuine prime-field endpoint. Passing to an extension and then treating its elements as tuples is not an F_p-affine received line and does not repair this obstruction.

## 2. What survives from support trees, and what does not

For an affine F_p-flat of size u=p^k, its monic locator has leading term X^u and all other terms of degree at most u/p. Thus its degree gap is (1-1/p)u. A disjoint union of M such equal-size flats has locator

    X^(Mu)+lower terms of degree <=Mu-(1-1/p)u.

The product argument is characteristic-independent. Padding by a fixed disjoint set of size (1-1/p)u then gives the same head/correction compiler, with additive agreement gain (1-1/p)u. No derivative or factorial argument is needed for this part.

The binary population count is NOT characteristic-independent. Its proof uses squarefree Boolean coordinates x_i^2=x_i, exterior highest forms, and the recovery of a branching direction from a wedge annihilator. For p>2 the associated graded algebra is the truncated symmetric algebra with x_i^p=0, not the exterior algebra. A p-way slice indicator is 1-(z-c)^(p-1), of degree p-1; simply replacing two children by p children does not preserve the old top-form recovery proof. Full polarization across degrees reaching p also loses invertible factorials. A new template-injectivity proof would be required before claiming the binary Gaussian population exponent.

Even granting a growing family, the bare locator-gap resource degenerates with p. Every proper F_p-flat in D has size at most N/p, so its available gap is at most (1-1/p)N/p. A union whose variable coefficients are controlled only by that affine-flat head gap certifies at most O(N/p) extra agreement after this padding. At fixed rate the resulting fractional gain tends to zero. This is a limitation of the head-gap certificate, not of arbitrary unions or all possible cancellations.

In F_p itself proper F_p-flats are singletons. Their locator gap is1, so the analogous elementary compiler is a near-capacity, constant-additive-gap construction.

## 3. Norm identities survive odd characteristic

Let b=p^h>=3, N=b^e with e>=2, B=F_N, and use challenge field F_(N^2). Write

    s=N/b, d=(N-1)/(b-1), r=(s-1)/(b-1),
    Lambda=X^N-X, K=N-2s, T=N-d.

Choose alpha,beta in F_b^* with alpha+beta=1. For ordered distinct t,u in B, set

    G=alpha*(X+t)^d+beta*(X+u)^d,
    F=alpha*(X+t)^r+beta*(X+u)^r.

Both are monic. The norm-fiber equation for G has exactly d distinct native roots: under y=(x+t)/(x+u), it is y^d=-beta/alpha, a nonzero F_b value different from1. Since d-1=br and d=1 in characteristic p,

    G'=F^b,
    G^b-G=Lambda*F^b.

Let Jloc=Lambda/G and P=F*Jloc. Then

    P^b=Lambda^(b-1)-Jloc^(b-1).                    (3)

The polynomial P is monic of degree N-s and has exactly T native roots. In (3), the two terms of degree (b-2)N+1 cancel: the coefficient in Lambda^(b-1) is -(b-1)=1 in characteristic p, and Jloc is monic. All remaining terms below the leading term have degree at most (b-2)N. Taking the inverse Frobenius proves

    P=X^(N-s)+C,  deg C<=K.

Thus pole reduction gives strict degree-less-than-K witnesses and exact common agreement K.

The label multiplicity proof is also uniform. At an exterior pole zeta, put v=alpha*(zeta+t)^d and w=beta*(zeta+u)^d. Their relative norms each lie in F_b^*. For a fixed gamma=v+w, each of the (b-1)^2 ordered norm choices gives a nonzero quadratic equation for v, hence at most two possibilities. Each v determines t uniquely, since all d-th roots of unity lie in B; likewise w determines u. Finally a fixed P(zeta) determines at most b-1 values of gamma by (3). Therefore a value occurs for at most

    2(b-1)^3

ordered pairs, and there are at least ceil(N(N-1)/(2(b-1)^3)) distinct labels. A source shift makes them nonzero because the set has size less than N^2.

For growing b>=p, the count is of order N^2/b^3, but the rate is 1-2/b and the agreement gap above it is asymptotic to1/b. This transfer does not retain a fixed rate or a fixed positive gap as p grows. The regression `verify_odd_norm.py/json` checks every ordered pair for b=3,N=9, challenge field81, including all identities, exact supports, strict degrees, and multiplicity bounds. It uses less than one second and no large arrays.

### Native norm family and its prime degeneration

For c^(b-1)=1, the native polynomials

    P_c=X^r*(X^N-X)/(X^d-c)

have T roots and leading degree N-s. For e>=2, the next unshifted degree is strictly below K. Translation gives leading terms

    X^(N-s)-t^s X^(N-2s),

because binom(b-1,1)=-1 and s is a p-power. The coefficient map -t^s permutes B, so every native label is exceptional. This is the sign-correct analogue of the binary norm hierarchy.

At the genuine prime endpoint N=b=p, the strict unshifted degree inequality changes (d=s=1); handle it directly instead. Let K=p-2, f=X^(p-1), g=X^(p-2). For every c in F_p,

    h_c=f+c*g-(X^p-X)/(X-c)

has degree at most p-3 and agrees with f+c*g at exactly p-1 points. The quotient takes value -1 at c, so the last point does not agree. The monic degree-K direction gives exact common agreement K. This yields all p labels, and equivalently a complete p-word ordinary list at dimension p-1 and agreement p-1. It is the elementary codimension-two MDS example: rate tends to1 and the line's common-agreement gap is only1/p. It should not be presented as fixed-gap prime-field progress.

## 4. Why a naive Kummer replacement does not preserve the additive gain

A multiplicative coset locator X^m-a has a large gap, but in F_p^* there is a unique subgroup of each order m. For a fixed quotient size (p-1)/m there are only constantly many cosets and constantly many unions of a fixed number of them. Varying the quotient size to obtain a growing selection space makes m/(p-1) small. Translating such a locator creates the term -mt X^(m-1), with m nonzero mod p, so the additive-flat translation-stable head gap disappears. These facts close the direct substitution of multiplicative cosets into the same tree proof; they do not exclude more elaborate Kummer covers or arbitrary prime-field constructions.

## 5. Smooth characteristic lifting: a separate baseline

For L degree-at-most-D codewords, N variable nodes, N variable received values, and LA selected incidence equations, there are L(D+1)+2N raw variables. A full-row-rank Jacobian would require

    A-D-1 <= 2N/L.

Thus an unstructured smooth-lifting certificate with a growing list forces the normalized gap above dimension to be at most2/L. Gauge directions can only strengthen this necessary dimension count. It is NOT an impossibility theorem for structured characteristic-zero realizations: identities among incidence equations can leave a rank-deficient but unobstructed family. A meaningful lift of a binary tensor family would have to preserve such dependencies explicitly, rather than merely delete enough equations to achieve full row rank.

## Assessment

The strongest immediate positive extraction is the uniform growing-characteristic locator consequence over F_(p^10), with all labels and a sqrt(N)-scale additive gap. The cleanest algebraic transfer is the general-b norm compiler with its explicit b^-3 population loss. Neither reaches fixed-gap prime fields. The decisive missing ingredient is a growing support population with a translation-stable high-degree gap when the base additive dimension has collapsed to one, or a structured incidence lift preserving its equation dependencies. No broad search or new binary manuscript addition is justified by the results above alone.
