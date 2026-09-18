# Off-density correlated covers: restricted-family order sharpness

## Statement

Fix real constants `r>3` and `0<b<=1`. For infinitely many prime/divisor pairs, let

- `L=floor(p^(1/r))`, `s=Theta(L^b)`, `s<=L/100`, and `2s | p-1`;
- `k=2s+1`, `t=L^2-L+1`;
- `n=s(2L^2-2L+1)`, `A=2s(L-1)`, `T=s(2L-1)`.

There is a correlated-cover line with both final sources having individual and common agreement exactly `A`, and with `(1-o(1))Lt ~ L^3` nonzero parameters having singleton lists at threshold `T`. All finite bad parameters in the original normalization are witnessed by its specified conic bank. Their total number is at most `Lt`, and after the source change there is at most one additional parameter. Thus both the total exceptional count and its singleton subcount are asymptotic to `L^3`.

The thresholds satisfy exactly `(k-1)n-T^2=s^2>0`, and eventually `T>n a_1(k/n)`. Here `p~L^r`, so the ambient parameter space is strictly larger in order than the exceptional count.

## Prime/divisor choice

For arbitrarily large `X`, apply Bombieri–Vinogradov to moduli `2s` with `s` in `[eta X^(b/r),2eta X^(b/r)]`, and count primes in `[X,2X]` congruent to 1. The sum of main terms is at least a positive constant times `X/log X`, while the summed absolute errors at both endpoints are `O(X/log^2 X)`. Since `b/r<1/2`, these moduli lie within the classical level of distribution. A sufficiently small fixed `eta` ensures `s<=L/100` when `b=1`; for `b<1` the condition eventually holds automatically. This proves infinitely many pairs, not existence for every prime or every prescribed divisor.

The subgroup `H=(F_p^*)^s` has even order and `|H|~L^(r-b)>>L^2`. In particular it contains the Sidon core and all fresh base nodes required in `correlated_cover_line.tex`. Use precisely that construction, including its blacklist and full fibers. All its deterministic core, source, common-agreement, and parameter-change arguments are unchanged.

## Global nonbank failure is small enough

Let `epsilon_L` denote the probability that some nonbank degree-at-most-`2s` polynomial has more than `A` matches at any original parameter. As in the original proof,

    epsilon_L <= p^(2s+2) binom(t,L-1) (s/(p-2L))^(L-1).

Using `log p=(r+o(1))log L` and `log s=(b+o(1))log L`,

    log epsilon_L <= [2rs+(b+1-r+o(1))L]log L.

For `b<1`, `s=o(L)`, and `b+1-r<0`. For `b=1`, the displayed coefficient is at most `[r/50+2-r+o(1)]L`, also negative for every `r>3`. Hence

    epsilon_L <= exp(-c L log L) = o(L^3/p)

for some fixed positive `c` and all sufficiently large `L`. This is the stronger error estimate needed here: merely `epsilon_L=o(1)` would not suffice when the expected singleton fraction tends to zero.

## Rare singleton probability, with relative error

Fix an original parameter `lambda` other than 0 or 1. Let `S_lambda` be the number of bank–fresh-fiber hits. At a fresh base point all bank target values are distinct, so its contribution is Bernoulli. These contributions are independent over fresh fibers. Each bank loses at most `6L` possible nodes to the blacklist, uniformly in `lambda`. Consequently

    mu_lambda = E S_lambda = (Lt/p)(1+O(1/L+L/p)).

In particular `mu_lambda~L^3/p -> 0`, uniformly. For a sum `S` of independent Bernoulli variables,

    E[S(S-1)] <= (E S)^2,
    E S - E[S(S-1)] <= Pr(S=1) <= E S.

The lower inequality follows pointwise from `1[S=1] >= S-S(S-1)`. Thus

    Pr(S_lambda=1) = (1+o(1))Lt/p

with relative error tending to zero. Summing over the `p-2` eligible parameters yields expected isolated-hit count `(1+o(1))Lt`.

Subtracting at most `p epsilon_L=o(Lt)` for the event of any nonbank improvement proves that some nonbank-good realization has `(1-o(1))Lt` singleton bad parameters. On that event, every finite threshold witness is a bank polynomial. Each bank needs at least one fresh fiber and each bank–fiber incidence determines one parameter. Hence there are at most `Lt` finite bad parameters, deterministically. This also establishes the asserted asymptotic total count.

The blacklist ensures both original labels 0 and 1 have exact agreement `A`. The invertible source change `(f,g)->(f,f+g)` preserves common agreement and transports all counted labels to nonzero finite parameters. The omitted projective parameter gives `-g` and has the single witness zero; it changes the count by only one.

## Restricted upper-bound comparison and scope

Apply the previously audited conic-bank inequality in the ORIGINAL normalization, where the witnesses really are the fixed bank

    Q_theta(X)=theta+theta^(-1)X^(2s).

It gives

    # bank-witnessed labels <= 2n(n-1)/[(T-k+1)(T-A)] ~ 4L^3.

The new lower bound is `~L^3`, while `p/L^3->infinity`. Thus the restricted witness-family upper bound has the correct order for reasons not explained by the trivial ambient-field cap. After changing the sources, the qualifying polynomials are parameter-dependent scalar multiples of the bank; the comparison is transported through the parameter bijection, rather than asserting that this final family is the same fixed bank.

In length notation, the source gap is `Theta(n^(b/(b+2)))`, the exception count is `Theta(n^(3/(b+2)))`, and the field size is `Theta(n^(r/(b+2)))`. For `b<1` the exception count is superlinear. Rate is asymptotic to `L^-2`, relative source gap is exactly `1/(2L^2-2L+1)`, and the bad-parameter fraction tends to zero. This is restricted conic-bank order sharpness, not a universal optimality theorem, fixed-rate construction, or constant bad probability.

The prime-selection input and its primary-source verification are recorded in `CORRELATED_COVER_INDEPENDENT_AUDIT.md`; the conic-bank inequality is independently audited in `../astra_strategy_2026_09_18/CONIC_BANK_UPPER_BOUND_INDEPENDENT_AUDIT.md`.
