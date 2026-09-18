# Primary-literature check: linearized trinomials and rank-metric lists

September 18, 2026. Primary papers read:

* Paolo Santonastaso and Ferdinando Zullo, *Linearized trinomials with maximum kernel*, arXiv:2012.14861v2, Theorem 1.3. https://arxiv.org/html/2012.14861v2
* Rocco Trombetti and Ferdinando Zullo, *On the list decodability of Rank Metric codes*, arXiv:1907.01289v2, Theorem 14, Corollary 15, and Theorem 16. https://arxiv.org/html/1907.01289v2

## Exact facts used from the papers

Santonastaso–Zullo Theorem 1.3(a) excludes kernel dimension r for ax+bx^sigma-x^(sigma^r) when r≥3, d≤r(r-1), and r does not divide d; sigma may be any generator of Gal(F_(q^d)/F_q). Part (b) allows only the binomial case when r divides d in that range. Part (c) characterizes the d=r(r-1)+1 case, including the requirement that r-1 be a power of the characteristic.

Trombetti–Zullo Theorem 14 and Corollary 15 use the McGuire–Mueller family at d=r(r-1)+1. It has (q^d-1)/(q-1) monic trinomials X^(q^r)-bX^q-aX, each with a kernel of dimension r, under that characteristic-power condition. Their Theorem 16 turns these into rank-metric list lower bounds for codes containing a two-dimensional Gabidulin subcode. Rank-metric length is d; it is not the full-domain Hamming length q^d.

## The proposed p^7 quartic locator is already excluded

The proposed shape is

    L=X^(p^4)+aX^(p³)+vX over B=F_(p^7), v≠0.

Apply Frobenius^(-4) to its output and set sigma=Frobenius^(-1). Its kernel is unchanged, and its terms have sigma-degrees 0,1,4. Divide by the nonzero coefficient of the sigma-degree-four term and adjust signs. The result is precisely the family in Theorem 1.3(a), with d=7,r=4. Since 7≤12 and 4 does not divide 7, it cannot have a four-dimensional kernel. This is an existing all-characteristic theorem, not a new obstruction to rediscover computationally. If v=0, the original polynomial has inseparable degree reduction and cannot have p^4 distinct roots either.

## More general first-order consequence (our parameter translation)

Consider either endpoint-adjacent trinomial shape

    X^(p^r)+aX^p+bX,
    X^(p^r)+aX^(p^(r-1))+bX,

with maximum kernel r in F_(p^d), r≥3 and d>r. The second shape reduces to the first using the inverse Frobenius generator as above. Take full-domain length N=p^d and message dimension K=p. Even allowing every kernel point as an agreement gives at most p^r matches.

In this low-rate regime, the DKT first-order curve satisfies

    N*a1(K/N)>sqrt(Np/2)=p^((d+1)/2)/sqrt(2).

For p≥3, if d≥2r then p^r is below this lower bound. Therefore crossing first order requires d≤2r-1. But then

    r<d<2r,  d≤r(r-1),  r does not divide d.

The cited theorem excludes the needed maximum kernel. Thus these endpoint-adjacent maximum-kernel trinomials cannot supply the desired K=p first-order construction in any proper full-domain extension, not just d=7,r=4. This derived comparison is restricted to the stated shapes, ordinary degree, and full domain; it is not a theorem about all sparse linearized polynomials.

## Translating the cited rank-metric positive family

Set q=p to preserve characteristic p greater than message degree p-1. Dividing each source trinomial by X gives the ordinary received word and witnesses

    f=X^(p^r-1),   h_(a,b)=bX^(p-1)+a,
    N=p^d, K=p, A=p^r-1, d=r(r-1)+1.

The nonzero constant term a of the locator ensures that zero is not an agreement, so A is exact. Distinct locator pairs yield distinct witnesses. The supplied population is M=(p^d-1)/(p-1)~N/p, not a superlinear count in this Hamming length.

For r≥3,

    (d+1)/2-r=(r-1)(r-2)/2>0.

Consequently this family's agreement lies below first order, by an exponentially large factor in r in the natural p-exponents. The characteristic-power restriction additionally forces r to grow when varying p with r-1 a nontrivial p-power. The degenerate small parameter r=2,d=3 can exceed the first-order threshold, but the provided population is only about p²=N^(2/3), not an improvement on the p^5 line's N^(6/5) exceptional population.

There is a separate correlated-agreement obstruction to the naive transfer. Both variable terms in h_(a,b) are already in the degree-<p code. If one turns b or a into a scalar challenge, the direction is X^(p-1) or 1, hence itself a codeword. For any such direction g, CA(f,g)=agr(f): a witness for f combines with the exact witness g on the same support. Therefore simply relabeling this ordinary list does not give bad correlated-agreement challenges. A new out-of-code direction/compiler would be required even if the threshold mismatch were repaired.

## Research decision

Neither cited family provides a new large-characteristic K=p line counterexample beyond N^(6/5). The proposed quartic trinomial route is already closed by the primary literature. The rank-metric construction gives a useful source of ordinary lists, but its full-domain Hamming threshold, population, and codeword-direction issue prevent the requested transfer. More general middle-exponent trinomials or four-term locators are not excluded by this note; pursuing them would require an explicit single-line identity and a first-order parameter advantage before launching a search.
