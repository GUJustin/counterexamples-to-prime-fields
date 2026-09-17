# Lines between majority words: a genuine linear bad-label construction

The majority words do yield actual bad labels on a nonconstant prime-field line. For a single Dickson candidate, flipping the tie rule gives an exact construction with **(p−1)/4 distinct full-support bad labels**. It also shows why this particular interpolation cannot turn majority list gain into a macroscopic line-distance gain: away from the endpoints, each fixed Dickson candidate gains at most one coordinate beyond its persistent support.

This is a linear label construction on a domain of size p−1, not a superlinear prime-field counterexample or a better.codes improvement.

## 1. Parameters and the tie-flip line

Let p≡1 mod8, n=p−1=4k, and use RS polynomials of degree at most k−1 on F_p^*. Fix a≠0 and the bank member `P_a=G_a−X^k`.

The exact Dickson bucket identities give:

- On nonsquare x, G_a(x)=0 at exactly k coordinates.
- On square x, G_a(x)∈{+1,−1} at exactly k coordinates in total.
- On the remaining k square coordinates, forming a set T, G_a(x) is nonzero, is not ±1, and `G_a(x)^2=a²/x`.

The endpoints x=a² lie in the shared ±1 buckets, so no endpoint correction is missing from T. These identities are in `../quartic_singular_route/DICKSON_SHARP_LIST_THRESHOLD.md`.

For square x=s², form the one-candidate sign sum `S(s)=χ(s+a)+χ(s−a)`. Define two shifted words W_+,W_- by:

- both are zero on nonsquares;
- on squares with S(s)≠0, both equal sign S(s);
- on ties S(s)=0, set W_+=+1 and W_-=-1.

Because χ(−1)=1, these definitions do not depend on the square root s. The tie set is exactly T. Let

`f=W_+−X^k`, `g=W_-−W_+`, `f_z=f+zg`.

Then g=−2 on T and zero elsewhere, so the line is nonconstant. Its shifted value on T is `1−2z`.

## 2. Exact agreements and full-support badness

The candidate P_a agrees persistently at exactly 2k coordinates S: k nonsquares with G_a=0 and k squares with G_a=±1. It has no other persistent agreements.

For each x∈T put

`z_x=(1−G_a(x))/2`.

The k labels z_x are distinct: equality of G_a values implies equality of their squares, and `G_a(x)^2=a²/x` determines x. None of these labels is 0,1, or1/2. At z_x the full agreement support of P_a is exactly `S∪{x}`, of size **2k+1**. At every other label it is exactly S.

At any z_x, a degree-at-most-(k−1) direction polynomial agreeing with g on the full support would vanish on all 2k points of S, hence be zero. But g(x)=−2≠0 at the extra coordinate. Therefore each z_x is a genuine full-support bad label.

This gives bad-label probability `k/p=(p−1)/(4p)` at agreement `(2k+1)/n=1/2+1/n`. The agreement surplus above the code rate is `1/4+1/n`, bounded away from zero.

## 3. Ordinary common-agreement distinction

At the exact threshold A=2k+1, the line also has **no affine codeword pencil with A persistent agreements**. Indeed, suppose degree-at-most-(k−1) polynomials F,G agree coefficientwise with f,g on at least2k+1 coordinates. At most k of these lie in T, so G vanishes on at least k+1 coordinates and must be zero. Their common support must therefore lie outside T.

Outside T there are3k coordinates, and P_a agrees with f on2k of them. If F agreed with f on at least2k+1 of those3k coordinates, F and P_a would coincide at at least k+1 points, so F=P_a. This contradicts P_a having only2k such agreements. Thus no ordinary common support of size2k+1 exists.

At any threshold A≤2k, however, the persistent pencil `(F,G)=(P_a,0)` supplies A common agreements. Consequently this example does **not** give a fixed positive separation between the near-label agreement and the best common agreement: their difference is one coordinate. It also does not establish exact nearest-codeword distances of the endpoints or of a far line point. Other codewords have not been excluded from individual lists.

The distinction matters: the construction gives real full-support bad labels and a one-coordinate ordinary-common-agreement obstruction, but cannot be advertised as a macroscopic line-distance gap merely because its agreement exceeds the rate by a constant.

## 4. General majority endpoints have the same one-coordinate bottleneck

Let W_0,W_1 be any two majority words on the same square/nonsquare partition: both are zero on nonsquares and ±1 on squares. This includes changing the selected parameter bank or translating its parameters a_i. After the common shift −X^k, their line direction is supported on

`T={x square:W_0(x)≠W_1(x)}`.

Fix any nonzero candidate P_a in the original Dickson bank. At a label z not equal to0 or1, a match on T must lie in a singleton bucket, since the line value is `W_0(x)(1−2z)` and is not ±1. At z=1/2 it is zero and there are no such matches. Otherwise a match forces

`x=a²/(1−2z)²`.

Hence every candidate has at most **one nonpersistent agreement** at every nonendpoint label, uniformly in how the two majority banks were chosen. The sign W_0(x) does not affect the squared equation. All other matches lie in its fixed persistent support.

Thus, if a candidate's persistent support is at least two coordinates short of a chosen threshold, it cannot become nearby at an interior label. A fixed positive normalized deficit cannot be bridged by this line interpolation. If A>(3/8+ε)n, each candidate capable of reaching A belongs to an endpoint list at threshold A−1. The sharp Dickson list theorem bounds the number of these candidates by a constant depending on ε (when n is sufficiently large), but this list fact is not needed for the one-coordinate obstruction itself.

This argument covers arbitrary endpoint majority rules and parameter translations on the **same coordinate partition**. It does not claim to cover coordinate-translated banks with different square partitions and challenge-dependent polynomial corrections, nor arbitrary codewords outside the Dickson bank.

## 5. What a stronger construction would require

A majority-derived line that gains a positive fraction of coordinates at many labels would need to escape the singleton-bucket equation above. Possibilities include changing the underlying candidate family or arranging genuine challenge-dependent candidate polynomials whose new agreement buckets are not pinned to one x by a²/(1−2z)². Merely interpolating between two same-partition majority words cannot do so.

The full-characteristic bank also has degree k−1≈p/4. Any nontrivial restriction of its evaluation domain retaining these polynomials at bounded rate has length Ω(p), so its p available labels remain O(n). A superlinear-in-n prime-field construction needs a different degree/domain regime as well as different line geometry; this note supplies neither and makes no such claim.
