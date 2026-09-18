# Uniform finite certificate for the projective quadratic line

For every prime p>=5, put

    n=1+p+p²+p³+p⁴, N=2n, K=3, D=2,
    A0=2p²+p, B=2A0=4p²+2p.

Take the derivative-weighted DKT Eq. (60) support with m=4, derivative cap2 and total jet cap B. Its exact coefficient count and local rank bound are

    G=3B², R=3+6+8+6=23.

The coefficient formula follows by summing 4A0-2q+v over v=0,1,2 and v<=q<=B. Every required local cutoff holds. Moreover

    5G-116N
      =8(p-5)^4+168(p-5)^3+1148(p-5)^2+2648(p-5)+308>0.

Thus G>(116/5)N>23N. The challenge cap H=116B passes the graded row test, since

    (H-B+1)G>(115B+1)(116/5)N>(116B+1)23N.

The interpolation proposition is characteristic-free. The reconstruction guard is p>max(D,2), satisfied for every p>=5.

For an explicit budget, B>=110, B<N, and B²<8N (the last inequality is exactly A0²<2N). At incidence thresholds L=L0=floor(A0/2)=(B-2)/4,

    lambda=(N-2)/(A0-2)<=3N/B,
    (N-L+1)/(A0-L+1)<=4N/B,
    (N-2)/(L-2)<=5N/B.

In DKT Eq. (54), tau=1, u=B, v=3, and therefore

    Freg=5B-6<=5B, S=3B-4<=3B,
    Hs=3H=348B,
    J1=H(16B-21)+10B-12<=1866B².

The list budget is <=lambda Freg+S<=18N.

The two regular MCA terms are at most 22392N² and25N². Since Psi_2(S)<=8S<=24B, the ordinary tail is bounded by

    16716N+33411NB <=50127N².

Hence the full MCA bound is <=72544N²<75000N², and in particular <=300000N². All these are uniform constants along the vanishing-rate family, not O_rho notation.

For p>=7 one can instead use the smaller H=48B because G>(47/2)N, but this improvement is unnecessary for the all-p>=5 statement.
