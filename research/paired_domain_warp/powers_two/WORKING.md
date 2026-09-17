# Deterministic unique banks with efficient decoding — development notes

Promoted after audit to `deterministic.tex`; see `../UNIQUE_PROOF_AUDIT.md`.
The final theorem and exact two-level refinement have independent arithmetic
and exhaustive small-instance checks.

Take a_i=2^i, 1<=i<=m, padding±1, and D-subsets as before. Suppose
p>2^[D(2m-D+1)], with1<=D<m. This bounds every positive product
T_I=prod(4^i-1), |I|=D, strictly belowp. It also impliesp>2^(m+1),
so no nonzero ternary sum of thea_i vanishes modulo p: the largest
power exceeds the sum of all smaller powers. The signed-relation
criterion thus classifies EVERY nearby codeword as a paired locator.

Subset products are injective by an elementary real inequality, no
factorization theorem needed. Write T_I=4^s U_I, s=sumI. Always
2/3<U_I<=1, because prod(1-x_i)>=1-sumx_i andsum_i4^-i=1/3.
For nonemptyI, T_I has exactly2s binary digits, hence determines s.
After earlier choices have been removed, at indexi:
- ifi is selected, U_remaining<=1-4^-i;
- ifi is not selected, U_remaining>=prod_{j>i}(1-4^-j)
  >1-sum_{j>i}4^-j=1-(1/3)4^-i>1-4^-i.
This determines membership recursively and proves injectivity.

Exact integer decoder: lift (-1)^(D+1)z modp to t in[0,p).
Rejectt=0 orodd bitlength (exceptt=1 handled byemptysetcheck).
Set s=bitlength(t)/2 for t>1. At eachi, compare
 t*4^i <= (4^i-1)*4^s.
Ifyes, require divisibility by4^i-1, divide t, subtracti froms, and
recordi. Finally requiret=1,s=0,andexactlyD selectedindices, and
verify the product. No false positives pass this final check; everybank
parameter is recovered. All integers haveO(logp)bits onvalid inputs.
The unique nearest polynomial is reference locator minus the decoded
locator, with optionalXfactor forparity.

Thus this gives deterministic exactrate primefieldcounterexamples with
EVERY nearby point uniquely decodable, efficient near/far decision and
witness recovery, andfar pointonecoordinatebelowmaxdistance. Choose
n=Theta_rho(sqrt(logp)), eta3/n; logJ=nHrho/2+O(logn), so c2<3/2
isdefeatedbyanexponentialfactor. Elias holds withamplemargin.
Needfinite/exhaustivetests, parityaudit, andformalproofintegration.
