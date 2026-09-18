# Independent audit: general fixed support down to c>sqrt(2)

Verdict: PASS. Independently derived the original support sums and read the complete `NORM_ONE_GENERAL_FIXED_SUPPORT_2026_09_18.md`, including its finite onset rather than just its asymptotic leading terms. Primary references remain Proposition 5.10, Eq. (60)–(63), and Lemma 5.6, Eq. (54),(56), in `tmp/eprint-2056/paper.txt`. No main-paper edits.

## Counts with the actual message degree

Set D=2,m=2h, derivative cap s>=h, B=hT. The strict source-weight cutoff is x+2i+j<2B. For B>=s, summing first over total jet degree t at fixed j gives

 sum_(t=j)^B (2B−2t+j)=B(B−j+1),

hence G=(s+1)B(B+1−s/2). This uses D=2 and derivative weight one; replacing D by dimension three would be wrong.

For local index a, count the overlap of [0,a] and [t−s,t]. Expressing min(2h−a,overlap) as a sum of level indicators gives q=min(2h−a,a+1,s+1) levels, with level j supported on a+s−2j+3 possible t. Thus the row sum is q(a+s+2−q). With s>=h, q=a+1 for a<h and q=2h−a thereafter. Summation proves

 R=h(h+1)(6s+2h+7)/6.

The finite condition B>=2h+s guarantees both the total-t cap and the strict cutoff a+t<2B are inactive in every nonzero block. Merely stating B>s for arbitrary s>=h would not suffice without an extra argument; the current source note correctly uses the stronger condition. For the particular large-s choices, the weaker condition could be enough, but is unnecessary.

Independently replayed original Eq. (61),(62) sums for (h,s)=(1,1),(2,2),(2,5),(3,3),(3,8),(8,8),(5,21), at B=s+2h. Every formula agrees. This is a bounded arithmetic check of the derived identities, not a word or rank scan.

## Critical constant and explicit choices

The ratio 2R/((s+1)h²) simplifies exactly to

 ccrit²=2+2/h+(h+1)(2h+1)/(3h(s+1)).

For delta=c²−2 in (0,2), h=ceil(8/delta), s=ceil(8h/delta) give 2/h<=delta/4. Also (h+1)(2h+1)/(3h)<=2h for h>=1, so the last term is <=delta/4. Therefore ccrit²<=2+delta/2<c².

The primary support explicitly allows derivative cap s>m/2. Counting requires p>max(D,s), not p>B or p>mT. Thus allowing large fixed s is legitimate and is precisely why the critical constant can approach two rather than the s=h limit 8/3.

## Finite onset, including ceilings

The note chooses kappa=ceil(4c²/delta), H=kappa B. Its definitions g2,g1,a2,a1,a0 are correct. The polynomial G(T) is increasing for hT>=2h+s; evaluating it at the real value T=cp is therefore a valid lower bound despite T=ceil(cp). In particular no extra negative constant from rounding is needed:

 G>=g2 p²−g1 p.

The stated a2 satisfies a2/((s+1)h²)>=kappa delta/2−c²>=c²>0. The other two coefficients are nonnegative. For

 p>max{s,3/(c−1),(2h+s)/(hc),1,(a1+a0)/a2},

all cap conditions and characteristic guards hold, and

 (kappa−1)G−kappa NR>=a2 p²−a1 p−a0>0.

This implies G>NR and the full graded surplus B[(kappa−1)G−kappa NR]+(G−NR)>0. Hence the use of the finite certificate is fully quantified, not only a favorable asymptotic dimension ratio. Arbitrarily large primes beyond this fixed real bound exist; the norm construction uses F_{p³}, so no extra splitting-prime condition is needed.

## Counting and exact lower list

With B>=2h+s, Eq. (54) has u=B,v=s+1 and gives

 Freg=(2s+1)B−s(s+1), S=(2s−1)B−s².

For C=h(2s+1), d0=2C−s(s+1), the note's exact rewritten counting bound

 C N+d0 lambda+h(2s−1)T−2C−s²

is correct. The onset ensures lambda=(N−2)/(T−2)<=2p, while c<2 implies ceil(cp)<=2p. Taking Kcorr=2max(d0,0)+2h(2s−1) bounds the correction by Kcorr*p. The additional requirement p>=Kcorr/2 gives list<=(C+1)N. This is a uniform all-word bound, not just a property of the constructed received word. Because h=O(delta^−1) and s=O(delta^−2), C+1=O(delta^−3).

The exact norm-one list remains N/2: the onset guarantees p+1<T<=2p, inside the already proved complete-list interval p+1<T<=2p+2. No new algebraic witness or list decoding assertion is needed.

## Scientific scope

The result proves maximum list size Theta_c(N) for every fixed sqrt(2)<c<2, with an explicit finite onset and coefficient depending on c. This is a valid new CONSEQUENCE of the existing finite first-order support formulas, not a revision of the published rate-only asymptotic curve. Only c>sqrt(3) is eventually above N*a1(3/N); for sqrt(2)<c<=sqrt(3), the useful certificate is a sharper finite-degree application of the same machinery. The construction still has K=3, vanishing rate, and an extension-field alphabet. No prime-alphabet, fixed-rate, or MCA-count conclusion is implied.
