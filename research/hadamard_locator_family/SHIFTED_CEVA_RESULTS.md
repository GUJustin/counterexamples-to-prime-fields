# General shifted finite-pole Ceva family

This extends the inversion chart without treating translation of Y=T² as a permissible change of the base T. No characteristic-zero nonexistence result is claimed.

Write the six edges as h+(1,b,c,q/c,q/b,q), in order 01,02,03,12,13,23. Assume they are nonzero and distinct. Put

 beta=(0,q-bc,q-c,q-b),
 N=bc+bq+cq+q, J=bc+b+c+q,
 M=b²c²-b²cq+b²c-b²q-bc²q+bc²+bq²-bq-c²q+cq²-cq+q²,
 W=-b²c²q+2b²c²-b²q-c²q+q³,
 Delta=(q-b²)(q-c²)(q-1), Mh=qM+hW, Nh=N+hJ.

With a0=1, the internal complement and all-plus conditions give

 t=-Nh/Mh,
 ai=1+t beta_i(sum(beta)-2 beta_i),
 p=-(2hN+(h²+q)J)/Nh,
 k=sigma*tau=Delta/Mh.

The all-plus factor is T²-sigma T+p. Scripts `shifted_internal.py` and `shifted_parameters.py` verify these rational identities symbolically. The elimination of the all-plus equations gives the linear factor Nh*P+hN+qJ, with P=p+h.

## Exceptional denominators

The exact identity q*M*J-N*W=2bc*Delta excludes simultaneous Mh=Nh=0 under the distinct-edge guards in characteristic not2. Mh=0 alone is inconsistent with the complement equations; Nh=0 alone forces t=0 and coincident leading coefficients. These are not omitted feasible charts.

Do not discard p+edge=0. Dividing a polynomial numerator by Y+p can conceal an edge condition there. Actual equality of the interpolated B values restores it: for edge e=eij=-p, the missing equation is

 -ai Ci'(e)+aj Cj'(e)+k*p*(beta_i-beta_j)=0.

Here Ci(Y) is the product of the three edge factors incident to i. The derivative identity follows directly from the exact quotient expression for B and the Ceva beta relation. The final search includes these cases and checks the restored equation.

## Bounded finite-field gates

`shifted_search.cpp` solves the six cross-remainder equations by a common univariate gcd in z=sigma², for all guarded b,c,q,h in the stated prime field. It retains nonconstant gcds irrespective of whether they split. Every retained gcd in these two runs was linear.

| Field | Retained candidates | Degree of gcd(K,K') and counts | Valid squarefree K |
|---|---:|---|---:|
| F29 | 3024 | 12:2664; 14:336; 16:24 | 0 |
| F43 | 8328 | 12:7992; 14:336 | 0 |

K is the full degree28 domain locator, including six edge quadratics and all four cross quadratics and their reversals. Thus collisions are geometric, not merely failure to split over the prime field.

`verify_shifted_candidates.py` independently reconstructs the eight sextics with FLINT, checks exact polynomial division, all six edge B equalities, all-plus and cross divisibility, distinct signed leading coefficients, and the full locator gcd for all11352 records. The replay passed in1.09 seconds with34MiB peak RSS. Receipts and examples are in `verify_shifted_candidates.json` and its resources file.

The generator coverage concerns shapes over F29 or F43 only. It does not exclude shapes over extension fields or characteristic zero. No new bank, lifting certificate, or parameterically growing construction has been obtained from this chart.
