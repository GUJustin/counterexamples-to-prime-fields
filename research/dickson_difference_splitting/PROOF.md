# Splitting of pairwise Dickson differences

September 17, 2026. The finite pattern now has the following algebraic
proof. No novelty claim. This improves the extension-field construction;
it does not transfer the construction to prime ambient fields.

Let p=1 mod4, k=(p-1)/4 and e=(p+1)/2. For nonzero a in F_p define

    G_a(X)=sum_{j=0}^k binom(e,2j+1) a^(e-2j-1) X^j.

For a^2 != b^2, every root of G_a-G_b belongs to F_p. Consequently this
nonzero degree-(k-1) polynomial splits completely over F_p. For p=5 the
same statement includes the possible constant difference.

Proof. Let alpha be a root in an algebraic closure, choose t with
alpha=t^2, and write y=G_a(alpha)=G_b(alpha). If t=0 the conclusion
is immediate. Otherwise, for c=a,b put

    U_c=(c+t)^e, V_c=(c-t)^e.

The binomial identity gives U_c-V_c=2ty. Since 2e=p+1 and c^p=c,

    U_c^2-V_c^2=2c(t+t^p),
    U_c^2+V_c^2=2c^2+2t^(p+1).

If y=0, the first identity gives t^p=-t, hence alpha^p=alpha.
If y!=0, set H=(t+t^p)/(ty). Then U_c+V_c=cH, so

    c^2 H^2 + 4t^2 y^2 = 4c^2 + 4t^(p+1).

Subtract the equations for a and b. Since a^2!=b^2, H^2=4.
Substitution gives t^2 y^2=t^(p+1). Therefore

    (t+t^p)^2=4t^(p+1), i.e. (t^p-t)^2=0.

Thus t^p=t and again alpha^p=alpha. Finally the leading coefficient
of G_a-G_b is -(a^2-b^2)/8, so its degree is k-1.

## Sharper quadratic exception count

Use the full Dickson bank with p=1 mod8, N=p-1, k=N/4, A=3N/8,
L=N/2. Any nonsquare anchor x is incident to exactly ell=N/4 candidates.
Indeed sum_a chi(a^2-x)=-1, no summand is zero, and the a=0 summand is
-1. Thus N/2 nonzero parameters satisfy chi(a^2-x)=1, giving N/4
candidates modulo sign.
Their distinct quotients Q_i=(P_i-w(anchor))/(X-anchor) have pairwise
differences with every root in F_p by the splitting lemma.

At every padding point in F_(p^2) minus F_p, all ell evaluations are
therefore distinct. There are p^2-p >= p=N+1 available such points.
Choose any p distinct points and independently translate their value
sets. The expected union size is exactly

    p^2 [1-(1-ell/p^2)^p].

The standard full-support MCA argument applies: each label has at least
A-1>=k old zero-direction agreements and a new direction-one agreement.
Any degree-<k direction witness is forced to vanish, a contradiction.
No nearest-list completeness or ordinary-CA conclusion is needed.

For a clean uniform bound, write h(u)=1-exp(-u/4), a concave function
with h(0)=0. Monotonicity in ell and 1-v<=exp(-v) give

    expected union >= p^2 h(N/p) >= Np h(1) >= N^2 h(1).

Moreover h(1)>=1/4-(1/4)^2/2=7/32>1/5. At output length n=2N,
there are consequently at least ceil(n^2/20) full-support exceptions.
The sharper uniform coefficient is (1-exp(-1/4))/4, about0.05530.
The previous elementary compiler bound was3/100. The rate remains1/8
and the capacity gap1/16; the ambient field remains F_(p^2).
