# Independent proof: projective locator seed and quadratic pullback

Let p be an odd prime, B=F_(p^5), and theta lie in an extension with degree at least three over B. Put

    n=p^4+p^3+p²+p+1, N=2n, D=mu_(2n) in B*,
    F_j(T)=T^[2(p^j-1)/(p-1)],
    f=F_4+theta F_3+theta² F_2, g=F_2.

The code consists of degree-at-most-two polynomials (dimension K=3), so p exceeds its degree cap. Since 2n divides p^5-1, the domain is defined over B. Squaring is two-to-one from D onto mu_n. The map X -> X^(p-1) from B* onto mu_n has fibers of size p-1.

For each three-dimensional F_p-subspace W of B, write its monic locator

    L_W=X^(p³)+a X^(p²)+b X^p+cX, c nonzero.

It gives the label and quadratic witness

    z_W=b^p-a^(p+1)+theta*a-theta²,
    h_W=(a^p b-c^p-theta b)T²+a^p c-theta c.

Projectivizing the original locator identity and pulling back by T² gives exact agreement

    A=2(p²+p+1).

Distinct W give distinct labels by the original coefficient/intersection argument. None is zero, since theta² is independent of 1,theta. Their population is

    M=[5 choose2]_p=p^6+p^5+2p^4+2p³+2p²+p+1
      =Theta(N^(3/2)).

## All witnesses above common agreement are classified

This is a direct proof, not an assumption that fresh quadratic witnesses are even.

Suppose f+zg agrees with h, deg h<=2, on more than C=2p+2 coordinates. The four evaluation columns 1,T,T²,g have rank four on that support. Otherwise g would agree with a quadratic on more than deg g=C distinct points, impossible. Choose four independent rows and solve for h's coefficients and z. All belong to the B-span of 1,theta,theta², even if the original ambient field is larger.

Projecting onto theta² gives (1+z_2)g=h_2 on more than C points, whence z_2=-1 and h_2=0. Thus

    z=z_0+theta*z_1-theta², h=h_0+theta*h_1,

with z_i in B and h_i quadratic over B. On the support,

    F_4+z_0 F_2=h_0, F_3+z_1 F_2=h_1.

Using F_4=T² F_3^p and F_3=T² F_2^p gives

    (z_0+z_1^(p+1))F_2=h_0-T² h_1^p+z_1^p h_1.

Both sides have degree at most C, so this is a polynomial identity. For odd p, its T^(p+2) coefficient forces the odd coefficient of h_1 to be zero. Its T coefficient then forces the odd coefficient of h_0 to be zero. Write h_1=uT²+v. Coefficient comparison yields

    z_0=-u^p-z_1^(p+1),
    h_0=(v^p-z_1^p u)T²-z_1^p v.

The entire word and witness are even; their full match set on D is invariant under T -> -T. More than 2p+2 matches therefore means at least 2p+4 matches. Lifting through T²=X^(p-1), the equation F_3+z_1F_2=h_1 supplies at least

    (p+2)(p-1)=p²+p-2 > p²

nonzero roots in B of the linearized polynomial

    L=X^(p³)+z_1 X^(p²)-u X^p-vX.

Its B-root space consequently has dimension three: dimensions are integers, and the degree bounds the root count by p³. It is separable (otherwise it has at most p² distinct roots). Hence it is precisely L_W for a unique three-space W. The coefficient identities recover exactly the displayed z_W and h_W.

Therefore the labels with agreement strictly greater than C are EXACTLY the M canonical labels. Each has one qualifying quadratic witness and exact maximum agreement A. Every other label has maximum agreement at most C. This also proves that no new odd quadratic witness contributes at any advertised threshold above C.

## Exact source agreement

The degree bound gives agr(g)<=C. Simultaneous explanations on every two-dimensional subspace of B, followed by the same projectivization and pullback, attain C=2(p+1) for both sources. For f, interpolation on three points places any quadratic witness in the span of 1,theta,theta²; projection onto theta² bounds its agreement by deg g=C. Thus

    agr(f)=agr(g)=CA(f,g)=2(p+1).

## Below-Johnson first-order threshold

Advertise A0=2p²+p. It satisfies

    2N-A0²=3p²+4p+4>0,

so it is strictly below the degree-two Johnson threshold. For every p>=5 it is strictly above the low-rate first-order curve at rho=3/N. Here is an exact algebraic certificate.

Set J=18 A0 N+9N-4A0³. The low-rate criterion is A0²>3N/2 together with 216N³>J² when J>0. The first inequality follows from

    2A0²-3N=2p^4+2p³-4p²-6p-6>0 (p>=5).

After substituting p=x+5, all coefficients of 216N³-J² are positive. In descending order they are

    128,8064,230928,3973680,45732396,370490616,
    2163218684,9152246304,27757264296,58562494200,
    80947664016,64932476400,22269823004.

The advertised integer A0 fails the first-order test at p=3; the uniform claim starts at p=5. For every p>=5, A0>C and A0<A, so the exact classification applies below Johnson as well.

This improves the large-characteristic vanishing-rate population exponent from 6/5 to 3/2. It does not give fixed rate, fixed absolute gap, or a prime-field alphabet/domain. The domain lies in F_(p^5), and the challenge field must contain theta of degree at least three over it.
