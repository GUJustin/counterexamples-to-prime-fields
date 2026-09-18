# Exact NTT contact compression to 48 maximal profiles

September 18, 2026. Algebraic compression of the EXISTING monomial-word rank test, preserving every original cap. Subsequent exact audit settles its proposed injectivity test NEGATIVELY: the maximal profiles have more columns than the original one-point image dimension 182580, so they necessarily have kernels. No contact matrix was allocated or global rank computed. This proves special-word kernel existence, not a uniform source repair or benchmark improvement. The endpoint-domination and local-rank observations are from the root review and independently verified here.

## Frozen source and scope

Work over the Koala prime field, p=2130706433, on mu_n, with

    n=262144, w=131071, a=181275, m=115,
    W=20846625, Q=159, s=35, L=274277.

The original monomials satisfy d+w*i+(w-1)*j<W, j<=s, i+j<=Q, and i+j+z<=L. Their exact number is

    sum_(i+j<=159,j<=35) [W-w(i+j)+j] [L-(i+j)+1]
      =13123663101701085.

Specialize the received pair to f(x)=x^a, g(x)=0. Because g=0, contact constraints do not mix powers of Z. Therefore the full capped map is injective if and only if its Z-free full-Q source is injective: each other Z coefficient belongs to a subspace of that source, and Z^0 contains the entire source.

An injective SPECIAL received word could falsify a uniform nonzero-kernel assertion. This particular word cannot do so: the rank ceiling proved below forces kernels. Its kernels do not prove a universal source repair or move the benchmark. The separate final ledger deficit remains 21042194961366305.

## Coordinate identity, including the caps

In the localization X!=0 set

    q=X^n, y=X^(-a)Y, r=X^(1-a)R, t=q-1.

For S=X^n-1, the exact order-two Hermite coordinate is

    H=Y-X^a+(S/n)(aX^a-XR)
     =X^a [y-1-(t/n)(r-a)].

Indeed X/n is the inverse of S' modulo S, and a<n. The all-m contact-ideal theorem consequently identifies the normalized ideal with

    J_m=(t^max(m-2b,0) h^b : 0<=b<=ceil(m/2)),
    h=y-1-(t/n)(r-a).                         (1)

The cyclic action (X,Y,R)->(zeta X,zeta^a Y,zeta^(a-1)R) preserves both source and contact ideal. Since n is invertible, its character spaces split. For character chi in {0,...,n-1}, write

    X^d Y^i R^j = X^chi q^k y^i r^j,
    d+a(i+j)-j=chi+nk.

The original caps translate EXACTLY to

    0<=j<=35, i>=0, i+j<=159,
    ceil([a(i+j)-j-chi]/n) <= k
      <= floor([W-1+(a-w)(i+j)-chi]/n).        (2)

Empty intervals are omitted. No free cap is placed on transformed coefficients. Every listed monomial recovers an admissible original monomial, and conversely. In particular 0<=k<=109. Multiplication by X^chi is a unit on the domain. Descent of membership from the localization is exact: (1) contains (q-1)^m, so q is already a unit modulo it. Thus no q-torsion or missing boundary condition is introduced.

## One fixed short-exponent map

All characters now use the SAME linear map; only their monomial subsets differ:

    Phi(q^k y^i r^j)
      =(1+t)^k [1+(t/n)(r-a)+h]^i r^j
        modulo monomials t^ell h^b with ell+2b>=115.     (3)

Its coefficient of t^ell h^b r^v is

    binom(i,b) sum_u binom(i-b,u) n^(-u)
       * binom(k,ell-u) binom(u,v-j) (-a)^(u-v+j),      (4)

where out-of-range binomial terms are zero and u>=v-j. The retained rows have ell+2b<115 and 0<=v<=159-b. This is at most 474875 explicit coefficient rows, with k<=109 and i<=159; the old degree-d binomials had d approaching twenty million.

Formula (3), rather than a naked dimension count, is the exact discriminating map. Its polynomial degree bounds do not make a dense computation small: maximal profiles still have about 182600 columns.

## Endpoint reduction and exact finite counts

There are 5130 pairs (i,j). As chi increases, a lower endpoint in (2) drops once, adding a monomial, at residue (a(i+j)-j) mod n. An upper endpoint drops once, removing a monomial, at residue

    e_t=(W+(a-w)t) mod n,  t=i+j=0,...,159.

Residue zero means that no drop occurs inside 0<=chi<n. Between upper-drop events the support only grows. Hence injectivity at chi=e_t-1 for every positive e_t, and at chi=n-1, implies injectivity for every character. This leaves 161 candidates. Comparing the 5130 integer intervals componentwise then removes contained or duplicate supports.

Exact arithmetic gives 5289 consecutive constant-profile intervals before domination and precisely 48 inclusion-maximal profiles afterwards. Their character representatives are

    3468, 9176, 14592, 20300, 25716, 31424, 37132, 42548,
    48256, 53672, 59380, 64796, 70504, 75920, 81628, 87336,
    92752, 98460, 103876, 109584, 115000, 120708, 126124, 131832,
    137248, 137540, 142956, 148664, 154080, 159788, 165204, 170912,
    176328, 182036, 187452, 193160, 198868, 204284, 209992, 215408,
    221116, 226532, 232240, 237656, 243364, 249072, 254488, 260196.

The 48 source dimensions range from 182584 to 182687. The largest is at chi=154080. Across ALL characters, dimensions range from 182472 to 182687, and sum to 47859086760, agreeing with the direct Z-free column count. The 5129 nonzero lower events and 160 upper events share exactly one residue, 137249, giving 5288 events and 5289 profiles.

Reproduction requires only integer interval arithmetic: form the 161 endpoints above; for each form the 5130 intervals in (2); discard profile A if every nonempty interval of A is contained in the corresponding interval of another profile B, breaking equal-support ties by index. No field or matrix operations enter. The full-profile count was independently checked by an endpoint sweep adding +1 at each lower event and -1 for each upper event, with their multiplicities; integrate the running column count over the interval lengths to obtain 47859086760.

## Exact local rank settles the proposed injectivity test

Translate one original domain point and its received value to zero. Source translation preserves all caps. Every X prefix has length at least6336, exceeding115, so each allowed Y/R monomial has every coefficient in A=F_p[t]/(t^115) available. At fixed total Y/R degree q, put lo=max(0,q-35). A basis over A is

    Y^lo (Y-tR)^k R^(q-lo-k),  0<=k<=min(q,35).

This is an invertible triangular basis change within the derivative cap: its expansion never has R-degree above q-lo<=35. Substituting Y=tR+t^2E gives

    t^(lo+2k) (R+tE)^lo E^k R^(q-lo-k).

Multiplication by the common monic factor (R+tE)^lo is injective over A, and the remaining E/R monomials are independent. The exact one-point image dimension is therefore

    R0=sum_(q=0)^159 sum_(k=0)^min(q,35)
         max(115-max(0,q-35)-2k,0) =182580.       (5)

Every ORIGINAL character source is a subspace of this one-point source. Its normalized map (3) differs from its original one-point map only by invertible local coordinate changes and multiplication by the truncated unit X^(-chi). Thus its rank is at most182580. The unit transformation can depend on chi; no claim that the union of all normalized source profiles has a common182580-dimensional image is needed.

Each of the48 maximal profiles has at least182584 columns, so each has a kernel of dimension at least4; the largest has dimension at least107. The proposed all-profile injectivity lemma is FALSE by this exact dimension argument. No Birkhoff, Padé, or strong-Lefschetz theorem can certify it.

The same endpoint sweep gives98642 characters with column count greater than182580 and

    dim(kernel on Z-free source) >= sum_chi max(C_chi-182580,0)
                                  =2568270.

Multiplying every Z-free helper by Z^z for 0<=z<=L-Q gives274119 independent copies within all challenge caps. Hence the full source has kernel dimension at least704011604130 for this SPECIAL received pair. The root's independent arithmetic receipt is `verify_ntt_contact_rank_ceiling.py/.json` in this directory.

Equation (5) is not a new uniform row saving: summing the corresponding prefix ranks over the original Z cap and all n points reproduces13125118926520320, exactly the existing frozen row allowance. What creates the special-word kernels is cyclic imbalance among character column counts, not a reduction of that local accounting.

## Decision

The exact compression is valid, but this monomial word is closed as an injectivity counterinstance to the uniform kernel gate. Its many helpers do not supply the universal received-pair theorem or an adapter paying the final7.65-percent charge deficit. No further rank computation on these48 profiles is justified. The primary gate for arbitrary received pairs remains unresolved, and the benchmark score is unchanged.
