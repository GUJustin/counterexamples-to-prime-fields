# Sharp degrees of positive-dimensional actual solution components

Appendix J extends the actual-component argument to every fixed
differential order d. With tau=max(0,2(D-d)-1), b=1+tau(B-1),
T=b+tau*H, K=H+B*T, q=B+H, it proves

    J_j <= q*K^(d+1-j)*T^(j-1),  1<=j<=d+1.

Here J_j sums projective degrees of actual regular joint solution
components of dimension j. Thus every positive-dimensional stratum has
degree O(D^d). At a fixed challenge, its positive-dimensional components
have degree O(D^(d-1)); isolated fiber points are explicitly excluded.

Together with Appendix I, all four powers are sharp. The examples have
jet and challenge degrees bounded in terms of d alone:

| Actual locus | Isolated points | Positive-dimensional degree |
|---|---:|---:|
| Joint polynomial--challenge locus | D^(d+1) | D^d |
| Fixed challenge | D^d | D^(d-1) |

The degree-D=re power family is defined by

    Wr(e P phi_1'-P' phi_1, ..., e P phi_r'-P' phi_r)=0,
    phi_j=X^j (j<r), phi_r=X^r+z.

For p>D+r-1, its actual regular closure consists exactly of powers
P=c H^e, with projective degree-<=r coefficients satisfying h0=z*h_r,
including the zero vertex in the closure. It is irreducible of dimension
r+1, has degree at least e^r, and each fixed-label fiber has degree e^(r-1).
Lower-degree H must have H(0)=0; they are included in the classification.
The exact joint degree is not asserted.

A challenge-independent Wronskian equation has exactly binom(D+d+1,d)
isolated solutions P=R H'/H with deg H<=d and roots supported on R.
Adjoining a free challenge gives that many degree-one affine codeword
graphs. This shows why isolated generic-fiber points cannot be included
in the smaller positive-dimensional fiber bound.

## MCA scope

Nonaffine actual curves have O(n^d) nearby-pair counts at a fixed gap.
The component bounds alone do not prove that bound for full MCA:
isolated points and affine graph curves remain separate obstacles.

The logarithmic-derivative family has O(n) full-support bad labels at
any fixed positive gap, even allowing a candidate to recur at many
challenges. Its proof counts rational triples, with horizontal graph
lines controlled by the at-most-n bad labels of a fixed candidate.
The power family is covered by Appendix G in that theorem's sufficiently
large characteristic regime. No quadratic MCA lower bound is claimed.

## Checks

Run sequentially from the repository root:

```sh
python3 research/actual_higher_order_components/verify.py
python3 research/actual_higher_order_components/verify_fixed_fiber.py
```

The standard-library power-family checker exhausts 36,140 polynomials
covering 252,730 polynomial--label pairs, checks 45 separants through
order five, and verifies 40 reduced degree sections with 1,574 points
in total. A characteristic-three control produces 30 extra pairs;
a boundary fixture outside the sufficient strict cutoff still passes.
The fixed-equation checker exhausts 7,203 polynomials and checks 16
separants through order four, 12,236 rational triples, and a four-label
bad-support example reusing the zero candidate.

These checks supplement the geometric proofs; they cannot establish
the generic-projection argument. Proofs were twice self-reviewed,
without independent coauthor review or a novelty assertion. Numerical
jobs run sequentially under a 384 MiB watchdog; reported RSS is sampled
process-group usage, not exact high-water memory.
