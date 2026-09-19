# Prime-power norm-one lists, trace-dual subplanes, and a field descent gate

September 19, 2026. Bounded follow-up to the existing dimension-three
[norm-one construction](norm_one_direct_list.tex). No manuscript changes.
The geometry below is the classical projective-plane design; no novelty
claim is made for that design or for odd-characteristic constructions generally.

**Result.** Replacing the prime base by any odd prime power is valid. A
trace-dual subplane gives a concrete proper coordinate restriction preserving
a complete, Johnson-saturating nearest list. Its parameters are exactly those
of the smaller-base family, so this gives no improved rate/list/loss tradeoff.
For a fixed characteristic, the extension degree is accounted for explicitly.
Moreover, in the field-degree regime described in Section 4, even projective
coordinate changes cannot descend a rich restricted list into the target
field: a subset of at least seven coordinates has either maximum quadratic
agreement at most four or is itself a quadratic codeword.

## 1. Prime-power base: the precise parameters

Let ell be an odd prime, r≥1, Q=ell^r, and E=F_(Q^3)=F_(ell^(3r)). Put

    L_Q=Q²+Q+1,  N_Q=2L_Q,
    G_Q=ker Norm_(E/F_Q),
    D_Q={x∈E*: x²∈G_Q}={x∈E*: Norm(x)∈{1,−1}},
    f_Q(x)=x^(2Q+2).

The group G_Q has odd order L_Q, so all its elements are squares in E and
|D_Q|=N_Q. The dimension-three Reed--Solomon code on D_Q has L_Q distinct
quadratics

    P_a(X)=aX²−a^(Q²+1),   Norm(a)=−1,

each agreeing with f_Q at exactly A_Q=2Q+2 points. These constitute the
complete nearest list, and A_Q is the maximum agreement.

The existing proof works with Q-Frobenius throughout. Explicitly, substituting
y=a^(Q²)z in y^(Q+1)=ay−a^(Q²+1) gives

    z^(Q+1)−z+1=0,   z^Q=1−1/z.

The fractional linear map on the right has order three, so all roots are
in E. The polynomial is squarefree because its derivative is z^Q−1;
here the derivative uses the actual characteristic ell dividing Q.
Its Q+1 roots have norm −1; hence the corresponding y have norm one,
and each has two square roots in D_Q. Distinct a give distinct polynomials.
The ordinary Johnson count is exact:

    M ≤ N_Q(A_Q−2)/(A_Q²−2N_Q)=L_Q.

Thus the displayed list is complete. The polynomial f_Q−P has degree A_Q
for every quadratic P, also proving the maximum agreement directly.

The full two-bank classification in the existing proof transfers as well:
there are 2L_Q distinct further quadratics

    (uX−u^(Q²+1))²,   Norm(u)∈{1,−1},

each with Q+1 matches; every remaining quadratic has at most four. The
semilinear matrix identity uses the three iterates of Q-Frobenius, and the
quartic/sign argument uses only odd characteristic. No step requires Q
itself to be prime. For Q≥5 the stated two-bank threshold ranges separate
the second bank from the at-most-four remainder.

At Q≥53 and T=ceil(19Q/10), the displayed word therefore has exactly N_Q/2
threshold-T witnesses. The characteristic-free shortening bound already
proved in the source gives

    N_Q/2 ≤ L_max(T) ≤ 4N_Q/3.

More generally the same upper-to-exhibited asymptotic ratio
4/(c²−2) holds at T=ceil(cQ), sqrt(2)<c<2. This changes neither the
dimension-three rate 3/N_Q nor the list size N_Q/2 nor the comparison loss.
The native alphabet still has size Q³=Theta(N_Q^(3/2)). Fixed ell and
growing r give a fixed-characteristic family, with growing prime-field
extension degree **3r**. Large Q never means large characteristic: any
separate interpolation theorem's characteristic condition must be checked
against ell, not Q. The shortening comparison above needs no such condition.

For orientation, Q=81 gives N_Q=13286 over F_(3^12), and Q=125 gives
N_Q=31502 over F_(5^9). These are dimension-three examples, not high-rate
instances. At a fixed large characteristic ell, Q≥ell forces
N_Q≥2(ell²+ell+1).

## 2. A concrete trace identity and proper subplane restriction

Let q=ell^s with s dividing r, so F_q⊂F_Q. For u,d∈E*, set

    y(u)=u^(Q−1),
    R_d(X)=−d^(Q−Q²)X²−d^(1−Q²).

Negative exponents denote inverses in E*. The map u mod F_Q* ↦ y(u)
is a bijection from the projective points of E/F_Q to G_Q. Likewise
R_d is unchanged by scaling d by F_Q*, and different such classes give
different polynomials. Indeed the kernel of d↦d^(Q−Q²) is F_Q*.
The leading coefficient a=−d^(Q−Q²) has norm −1, and
a^(Q²+1)=d^(1−Q²), so R_d belongs to the native first bank.

For x²=y(u), the key exact identity is

    f_Q(x)=R_d(x)  iff  Tr_(E/F_Q)(du)=0.                 (1)

To verify it, substitute y=u^(Q−1) into
y^(Q+1)+d^(Q−Q²)y+d^(1−Q²)=0 and multiply by d^(Q²−1)u.
The result is

    d^(Q²−1)u^(Q²)+d^(Q−1)u^Q+u=0,

which is d^(-1)Tr(du)=0.

Choose any F_Q-basis e_1,e_2,e_3 of E and its trace-dual basis
e_1*,e_2*,e_3*, with Tr(e_i e_j*)=delta_ij. This exists also when
ell=3: the finite-field trace pairing is nondegenerate, although Tr(1)=0.
Define the three-dimensional F_q spaces

    U={sum_i c_i e_i : c_i∈F_q},
    V={sum_i d_i e_i* : d_i∈F_q}.

Select one representative from each nonzero F_q-projective class of U
and V. Their images as F_Q-projective classes are injective: if two
coefficient triples in F_q³ are proportional over F_Q, comparing any
nonzero coordinate shows the proportionality constant lies in F_q.

Retain the two roots x of x²=u^(Q−1) for each selected u, and retain
R_d for each selected d. This gives

    n=2(q²+q+1),  number of witnesses=q²+q+1=n/2,
    agreement of every witness=2q+2.                    (2)

Indeed (1) becomes the ordinary dot product sum_i c_i d_i=0 over F_q.
Every projective line has q+1 points, every point is on q+1 lines,
and distinct lines meet in one point; the square-root lift doubles all
coordinate incidences. Each coordinate is in q+1 supports, and every
pair of witness supports meets in two coordinates.

This is a **complete nearest list**, not merely a retained sublist.
The Johnson bound at n=2(q²+q+1), A=2q+2 is exactly n/2, already
attained by the distinct displayed polynomials. An additional quadratic
with at least A matches would violate that bound. In fact any outsider
has at most 2q matches: counting its intersections with all bank supports
gives (q+1)agr≤2(q²+q+1), hence agr≤2q for q≥3.

When q<Q this is a proper subset of D_Q preserving a rich bank. It works
even when the subfield F_(q³) lies inside F_Q and the naive map
u∈F_(q³) ↦ u^(Q−1) would collapse. The trace-dual vector spaces are the
essential replacement for that naive subfield restriction.

The parameters in (2) equal those of the native q-base construction.
The ambient E used here can be larger, not smaller. For q≥53, universal
shortening still gives n/2≤L_max(ceil(19q/10))≤4n/3, but the exact native
two-bank profile is **not** claimed after this puncture: the outsider
bound 2q need not exclude outsiders at ceil(19q/10). All retained
witnesses remain in the two-dimensional span of 1 and X². This does not
escape a fixed-span restriction in a separate far-word/line compiler.

## 3. Exact native field intersections

Place all fields in a common algebraic closure, and let K=F_(ell^m).
Write d=gcd(r,m), g=gcd(3r,m). Since E∩K=F_(ell^g), cyclicity gives

    |G_Q∩K|=gcd(Q²+Q+1, ell^g−1),
    |D_Q∩K|=gcd(2(Q²+Q+1), ell^g−1).                    (3)

These formulas simplify completely using the exponent of 3 in an integer:

* If v_3(m)≤v_3(r), then g=d divides r, and

      |G_Q∩K|=gcd(3,ell^d−1),
      |D_Q∩K|=gcd(6,ell^d−1)≤6.

  This follows from Q≡1 modulo ell^d−1.

* If v_3(m)>v_3(r), then g=3d and 3 does not divide r/d. With q_0=ell^d,

      |G_Q∩K|=q_0²+q_0+1,
      |D_Q∩K|=2(q_0²+q_0+1).

  Modulo q_0³−1, Q is q_0 or q_0², so Q²+Q+1 is congruent to
  q_0²+q_0+1. Since q_0 is odd, 2(q_0²+q_0+1) divides q_0³−1.

In particular every m not divisible by 3, including **m=1,2,4,5**,
has at most six native coordinates, for every r. This conclusion does
not assume that the whole field E embeds in K. For m=6, if 3 divides r
there are again at most six; otherwise d is 1 or 2 and the sizes are
2(ell²+ell+1) or 2(ell^4+ell²+1). Increasing r cannot obtain a shorter
native family in that target field.

## 4. Affine and projective changes do not preserve a rich descended list

Assume v_3(m)≤v_3(r), so the common field F_(ell^g) lies inside F_Q.
The following claims concern coordinate changes and the ordinary
degree-two Reed--Solomon action. They do not concern arbitrary unrelated
GRS column multipliers, nonlinear coordinate maps, or new received words.

**Affine gate.** Any affine image of a subset of D_Q that lies in K has
at most six points. To see this even for an affine map with coefficients
in the algebraic closure, normalize two distinct source points and their
two target points to 0 and 1. The resulting common parameters lie in
E∩K. Thus the source points have the form a t+b with a,b∈E, a≠0,
t∈F_(ell^g)⊂F_Q. Membership in D_Q implies

    Norm_(E/F_Q)(a t+b)²−1=0.

This is a degree-six polynomial in t with nonzero leading coefficient
Norm(a)², so it has at most six roots.

**Projective gate.** Suppose S⊂D_Q has at least seven points and a
fractional linear map over the algebraic closure sends S into P¹(K).
Then the restriction f_Q|S either is the restriction of one polynomial
of degree at most two, or every quadratic has at most four agreements
on S. Consequently S cannot retain two distinct quadratics each with
at least five agreements. In particular it cannot retain the subplane
nearest bank from (2).

Here is the proof, including the projective point at infinity. Normalize
three distinct source points to 0,1,infinity by a map T_E∈PGL_2(E),
and normalize the three corresponding target points by T_K∈PGL_2(K).
The maps T_E and T_K composed with the proposed descent map agree at
three points, hence are equal. All normalized parameters for S therefore
belong to P¹(E)∩P¹(K)=P¹(F_(ell^g)). Write the inverse source map as

    phi(t)=(a t+b)/(c t+d),  a,b,c,d∈E,  ad−bc≠0.

At each selected projective parameter, phi(t) is a finite nonzero
element of D_Q. In homogeneous variables U,V the degree-six polynomial

    [prod_(i=0..2)(a^(Q^i)U+b^(Q^i)V)]²
      −[prod_(i=0..2)(c^(Q^i)U+d^(Q^i)V)]²             (4)

vanishes. More than six projective roots force (4) to vanish identically.
Odd characteristic then implies that the two norm cubics are equal up
to sign. Neither a nor c can be zero: otherwise their root multisets
would force both numerator and denominator to be constant multiples
of V, contradicting ad−bc≠0. Write

    phi(t)=kappa(t−u)/(t−v).

Equality of the norm cubics says Norm(kappa)∈{1,−1} and that u,v have
the same three-element Frobenius root multiset. Because u≠v, u is of
degree three over F_Q, and precisely two cases remain:

    v=u^Q,  or  v=u^(Q²).                              (5)

All parameters t in the common field are fixed by Q-Frobenius. To
transport the degree-two code, multiply the received word and every
evaluation of a quadratic by (ct+d)². This is exactly the usual
degree-two action, giving a bijection of binary quadratic forms.
Let C=c² kappa^(2Q+2), a nonzero constant.

For v=u^Q, the transported received word is

    C (t−u)²(t−u^Q)²/(t−u^(Q²))².                    (6)

Subtracting any quadratic H(t) and clearing the denominator gives a
polynomial of degree at most four. It is nonzero because its value at
t=u^(Q²) is C(u^(Q²)−u)²(u^(Q²)−u^Q)²≠0. Homogenizing gives a nonzero
binary quartic, so the at-most-four agreement bound includes infinity.
The denominator has no zero on P¹ of the common field.

For v=u^(Q²), the transported word instead simplifies to

    C(t−u^Q)²,                                       (7)

which is a quadratic codeword. Both identities hold at infinity as
degree-two sections: the value there is the leading coefficient C.
Transporting back preserves equality at every selected point. Thus (6)
proves the four-agreement case, while (7) gives an actual original
quadratic agreeing everywhere on S. In the latter case every other
quadratic has at most two agreements. This proves the projective gate.

## 5. Verification and scope

The standard-library fixture
[verify_norm_one_prime_power_subplane.py](verify_norm_one_prime_power_subplane.py)
uses Q=9, E=F_(3^6), with the explicitly checked irreducible polynomial
T^6+T+2. It verifies a native domain of size 182 with 91 bank members
at agreement 20; a trace-dual q=3 subplane with 26 coordinates and
13 distinct witnesses at agreement 8; all 169 trace incidences,
coordinate multiplicity 4 and pair intersection 2; both projective
orientations, including infinity; and 576 exact integer checks of (3)
and its closed forms. The [receipt](verify_norm_one_prime_power_subplane.json)
records the checks. The process completed under a 60-second/384-MiB
[guard](verify_norm_one_prime_power_subplane.resources.json).
No quadratic census or parameter search is used as a substitute for proof.

This supplies a valid structured restriction and a precise obstruction to
direct or projective descent into the stated smaller extensions. It does
not give a better.codes upper-bound improvement, a high-rate family,
a prime-alphabet rich bank, an exceptional-line construction, or a new
far-source statement. No manuscript is changed by this note.
