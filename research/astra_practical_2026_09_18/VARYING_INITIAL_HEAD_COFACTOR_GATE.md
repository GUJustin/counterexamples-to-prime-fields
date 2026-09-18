# Varying initial heads: coarse linear rigidity and a quadratic discriminator

September 18, 2026. Bounded algebraic audit of the remaining external-
cofactor case. No better practical certificate, root-subset search, or
manuscript edit is obtained.

There is a new obstruction for a coarse linear cofactor, even when the
first packet head is allowed to vary. A coarse quadratic cofactor has
a separate, explicit necessary determinant test. Passing that test is
not a construction, and the exceptional determinant-identity case is
not classified here.

## 1. Practical identity and available coefficients

Use the exact Koala6 parameters

    p=2130706433, E=F_(p^6), B=512, J=131072,
    h=272, c=518, A=hB+c=139782,
    required labels L*=274980728111395088.

Let R be a fixed monic c-point domain locator, and V_gamma a monic
degree-h packet polynomial over Fp. Consider the common identity

    F0+gamma F1-T P_gamma
       =lambda_gamma R V_gamma(X^B) q_gamma(X^B),
    deg(P_gamma)<J, lambda_gamma!=0,

where q_gamma is monic of coarse degree s=1 or2 and has no roots over
the packet labels. Write e=sB and suppose

    deg(T)<=e+2B+7=e+1031.

The common denominator is nonzero on the evaluation domain. The high
band above the code contribution has length at least

    A+e-(J-1+deg(T)) >=7680=15B.

After division by the fixed reversed R-series, the first fifteen
coefficients of the reversed monic product W_gamma=V_gamma*q_gamma
are available. Their values are fractional linear functions of gamma
with one common denominator, namely the leading error normalization.
A fractional linear change of parameter therefore writes them as

    W_tau(Z)=a(Z)+tau*b(Z) modulo Z^15,

where Z=1/Y, W denotes the reversed monic polynomial, and the new
parameter tau is injective on the original bank. This normalization
does not assume shared coefficients of V.

## 2. Three-head rigidity for a coarse linear cofactor

**Lemma.** Suppose p>2, V is monic over Fp, and q(Y)=Y+u is monic
over E. Suppose the first three normalized heads of W=V*q range on
one projective affine pencil as above. For a bank with more than 2p
distinct labels, one of the following holds:

1. The first head of V is fixed after discarding at most p labels.
2. Every cofactor q in the bank has coefficients in Fp.

The alternatives need not be disjoint. They exhaust this coarse-linear
case; there is no genericity hypothesis on the pencil.

Write the first three packet heads as x,y,z in Fp. Then

    w1=x+u,  w2=y+u*x,  w3=z+u*y.                    (1)

First suppose w1 is nonconstant on the pencil. Use t=w1 as parameter,
and write w2=a*t+b, w3=d*t+e with fixed E-coefficients. Eliminating
u gives

    (a-x)t=y-x²-b,
    z=(d-y)t+x*y+e.                                 (2)

If a is outside Fp, fix x and substitute the first equation into the
second. The coefficient of y² is -1/(a-x), which is outside Fp.
A polynomial of degree at most two with an E-coefficient outside Fp
can take Fp values at at most two Fp inputs unless all its coefficients
are in Fp: apply an Fp-linear functional E->Fp that kills Fp but not
that coefficient. Consequently there are at most two labels per x,
and at most 2p labels in total.

Now let a be in Fp. If b is also in Fp, every t outside Fp in (2)
forces x=a and y=a²+b. There are only p exceptional values t in Fp,
which gives alternative 1.

If b is outside Fp, x=a is impossible. For x!=a, the second equation
becomes

    z=[-y²+(d+b+a*x)y-d(x²+b)+e(a-x)]/(a-x).          (3)

If d+b is outside Fp, the non-base linear coefficient allows at most
one y for each x. If d+b is in Fp, then d is outside Fp and the
y-dependent terms are all in Fp. The constant condition in (3) is
that -d*x²-e*x+(a*e-d*b) lie in Fp. Its non-base leading coefficient
allows at most two x values, each with at most p choices of y.
Either way the bank has at most 2p labels.

It remains to consider constant w1=v. If w2=t is nonconstant and
w3=d*t+e, then

    t=v*x+y-x²,
    z=e+d*v*x-d*x²+(d-v+x)y.                         (4)

For v in Fp, t is in Fp and there are at most p labels. For v outside
Fp, either d-v is outside Fp, allowing at most one y per x, or d-v
is in Fp, in which case the constant polynomial in x has the non-base
leading coefficient -d and allows at most two x values. This again
gives at most 2p labels.

Finally, if w1=v and w2 are both constant, v outside Fp makes x
unique in the equation w2=y+v*x-x². This gives alternative 1 without
discarding labels. If v is in Fp, every valid factorization has
u=v-x in Fp, giving alternative 2. This proves the lemma.

For the actual target, 2p=4261412866 is far below L*. In alternative 1,
the remaining bank is still much larger than p, and its fixed first
head supplies exactly the initialization required by
`EXTERNAL_COFACTOR_REMAINDER_GATE.md`. Thus the existing fifteen-head
gate for deg(T)<=e+1030, or its fourteen-head-plus-remainder gate at
e+1031 with the stated pole geometry, applies to that large subbank.
Merely varying the first head with a genuinely extension-valued coarse
linear factor does not bypass it.

## 3. Base-field cofactors preserve the dimension deficit

This part covers both s=1 and s=2, without any shared-head hypothesis.
Suppose q_gamma lies in Fp[Y]. The entire monic product W=V*q then
lies in Fp[Y], of degree h+s. Apply the fixed-partial-locator quotient
dimension argument from `PARTIAL_PACKET_DENOMINATOR_CODIMENSION.md`
to W instead of V. It permits every common denominator that is
nonzero on the domain, regardless of degree or pole shape.

Its kernel dimension is at most

    kappa=floor((J-1-c)/B)+1=255.

The monic product coefficient vectors therefore occupy an E-affine
space of dimension at most kappa+1=256. Intersection with base-field
coefficient vectors has Fp-affine dimension at most 256. Thus the
product W has at least 17 affine coefficient conditions for s=1,
and at least 18 for s=2.

Allowing the cofactor to vary does not restore a lost dimension of
the packet-factor variety. Multiplication of two monic polynomials
of prescribed degrees is a finite algebraic map: a factor is selected
from the finitely many root-multiplicity allocations of their product.
For s=1 this is especially explicit: the cofactor root is integral
over the W-coefficients because it satisfies W, and polynomial division
then determines V. The inverse image of the above product space has
dimension at most 256, and projection to the 272 packet coefficients
cannot increase dimension. The packet factors therefore lie in an
algebraic locus of codimension at least 16, for either cofactor degree.

This locus need not be affine in the coefficients of V. This is a
dimension obstruction to gaining a free parameter, NOT an upper bound
on the number of root-subset polynomials in a special fiber. It does
not justify a numerical factor-p loss without a distribution theorem.
The practical concentration question remains separate.

## 4. A finite symbolic gate for coarse quadratic cofactors

Let s=2. Use the normalized fifteen-coefficient reversed pencil from
Section 1, and let superscript sigma raise coefficients to their p-th
powers while fixing Z. Since V has Fp coefficients, every valid label
satisfies

    W_tau*q_tau^sigma = W_tau^sigma*q_tau.

Form the 15-by-6 truncated convolution matrix with columns

    W, ZW, Z²W, W^sigma, ZW^sigma, Z²W^sigma,

using coefficients of Z^0 through Z^14. It has rank at most 5 at every
valid label. Therefore every one of its binom(15,6)=5005 maximal
minors vanishes at every bank label.

This is an exact small symbolic test. Introduce independent variables
U,V and replace the two series by a(Z)+U*b(Z) and
a^sigma(Z)+V*b^sigma(Z). Each minor is a polynomial D(U,V) of
bidegree at most(3,3). At a valid label it obeys D(tau,tau^p)=0.
If a minor is nonzero, so is this one-variable polynomial: p>3 makes
the exponents i+p*j distinct for 0<=i,j<=3. Its degree is at most

    3(p+1)=6392119302.

Hence one nonzero minor caps the entire bank at 6392119302 labels,
far below L*. Any candidate reaching L* must make all 5005 minors
identically zero in the two independent variables. The field degree 6
does not invalidate this root bound.

The test is necessary, not sufficient. Identical vanishing need not
produce the required Frobenius-related cofactors, root-free external
factors, denominator remainder identities, useful distinct supports,
or far received words. Fixed packet heads and base-field constant
product pencils already give degenerate cases, so one cannot declare
all identity pencils successful or all of them impossible. A claimed
new varying-two-head construction must first exhibit its actual
fifteen-coefficient pencil and pass this test outside those already
controlled cases. No such pencil is supplied here.

The same rank principle applies to a general external X-cofactor of
degree e: use e+1 shifts of the normalized error prefix and e+1 shifts
of its coefficient-Frobenius conjugate. A nonzero maximal minor gives
the cap (e+1)(p+1), provided enough high coefficients are available.
For e<=1024 the 7680-coefficient high band is long enough, and this
cap is still far below L*. That matrix is much larger; the coarse
quadratic version is the useful bounded discriminator, not a proposal
to run the general matrix computation.

## Outcome

No seven-agreement improvement has been constructed. The previously
uninitialized coarse-linear case reduces to an existing fixed-head
gate, up to p exceptional labels, or to a base-field factor variety
with the same sixteen-condition dimension deficit. For coarse degree
two, a candidate must satisfy the explicit all-minors identity test;
the surviving exceptional pencils still need classification and a
root-subset counting theorem. These are precise model statements,
not a general impossibility result for the prescribed NTT benchmark.
