# Extra-head odd-characteristic compiler: identity, subsequently closed

The fixed-domain recurrence in `EXTRA_HEAD_FIXED_DOMAIN_FACTOR_RECURRENCE.md` proves that the displayed parameter family has at most five split locators. The algebra below remains valid, but it is not a viable growing-bank construction. This is a compiler, not a constructed split-support family. It replaces the impossible two-variable-high-head candidate. Work over an odd-characteristic field and take integers 1 <= B < K. Put u=X^K and

L=u^4+c u^3+a u^2+b u+V,  V(0)=0, deg(V)=B,

with V monic. Define F=u^8+theta*u^4 and

Q=u^4-c u^3+(c^2-a)u^2+(-c^3+2ca-b)u
  +c^4-3c^2a+a^2+2cb-V+theta.

Direct polynomial multiplication gives F-LQ=R3*u^3+R2*u^2+R1*u+R0, where

R3=2cV-c^5+4c^3a-3ca^2-3c^2b+2ab-c*theta,
R2=(2a-c^2)V-ac^4+3c^2a^2-a^3+bc^3-4abc+b^2-a*theta,
R1=(c^3-2ca+2b)V-bc^4+3bc^2a-ba^2-2cb^2-b*theta,
R0=V^2-(c^4-3c^2a+a^2+2cb+theta)V.

Consequently R has leading possible term 2c X^(3K+B), and all remaining terms have smaller degree. Since V(0)=0, R is divisible by X. Set strict RS dimension J=3K+B-1, received word f=F/X, and direction g=X^J. On every nonzero root of L, f-2c*g agrees with a polynomial of degree <J. A simply split L therefore supplies 4K-1 agreements, provided all its nonzero roots lie in the evaluation domain.

The degree convention matters: the code is degree STRICTLY LESS THAN J. The direction g has degree exactly J, hence agreement exactly J with this code on any domain of at least J nodes. Ordinary common agreement of (f,g) is also exactly J: g supplies the upper bound and simultaneous interpolation on any J nodes supplies the lower bound. No individual upper bound on agreement(f) is asserted.

## A genuine parameter window, but no support existence theorem

Take K=20*l, B=l, J=61*l-1, n=108*l, T=80*l-1. At the limiting rate rho=61/108 and agreement fraction a=20/27,

[a(8-rho)-3rho]^2-4rho(5-rho)(2-rho)=675323/4251528 > 0,
rho-a^2=47/2916 > 0.

The first bracket is positive. Thus the full first-order agreement curve lies strictly below a, and a lies strictly below Johnson. These strict inequalities persist for all sufficiently large l after the displayed integer corrections (Johnson uses (J-1)/n). The agreement loss T-J=19*l is a constant fraction of the capacity margin T-J; in particular there is no vanishing-loss defect relative to that margin. This sentence concerns ordinary common agreement and the far direction, not two individually far sources.

Unlike the previous locator family, distinct L now differ in degree at most 3K. Two 4K-root supports can fit in n=5.4K without violating their intersection bound. The ordinary Johnson constant-list obstruction for degree-<=(3K) locator differences only forces bounded population when n<16K/3; here n=5.4K>16K/3.

Moreover, if two locators have the same c, their difference has degree at most 2K, whereas their nonzero supports intersect in at least 2(4K-1)-n > 2K for sufficiently large l. Thus c is injective on any such split bank. Because V is monic and characteristic is odd, the labels 2c are automatically distinct. This proves label injection conditional on support existence; it does not manufacture a large bank. A prime alphabet must be large enough to accommodate the desired number of distinct c values.

## Remaining constructive target

Find more than n simply split polynomials of the displayed form, with monic low tail of degree l, all their nonzero roots in one 108*l-point prime-field domain. Even n log n would meet the current population objective. No such family is supplied here. Generic splitting, arbitrary coefficient choices, binary support-tree descriptions, or extension-field linearized constructions do not establish this target. The extra-head compiler only removes the immediate support-intersection and Johnson barriers that invalidated the preceding sparse candidate.
