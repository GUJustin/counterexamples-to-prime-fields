# Finite-characteristic scope audit of the universal max-seven proof

Current conclusion: characteristic zero and all sufficiently large
characteristics are certified. The present certificate does not certify
all odd characteristics or every prime field.

The final geometric conditions are clean. In Q(w), w^3+2w^2-w-1=0,
independent Fraction arithmetic gives

    Norm(6w^2-2w-2)=8,
    Norm(486-390w-270w^2)=216,
    Norm(42w^2+81w-30)=-189.

Thus the amplitude rank witness, fifth-point eighth-cubic obstruction,
and alternative leading interpolation coefficient require only the
possible exceptions2,3,7. The preliminary orbit exclusions and explicit
branch-II contradiction also have only powers of2 as their guarded scalar
constants.

However, the tracked rational Buchberger DAG uses many additional
intermediate denominators, including17,19,23,43,61,89,227 and larger
integers. They may be algorithmic artifacts, but cannot simply be ignored
when reducing that particular certificate modulo primes. A finite set of
exceptions exists, as already claimed, but it has not been reduced to2,3,7.

A bounded attempt to reverse-expand each desired final identity as a
polynomial combination of the original integer generators is recorded in
orbit7_expand_certificate.py/log/resources.json. It reached the60-second
limit at292496KiB RSS before producing any final expanded identity. This
is not a successful certificate and supports no strengthened claim.

A possible next method is a cleaner low-degree integer identity, or two
independently expanded certificates whose cleared-denominator gcd removes
artificial primes. That step remains open. The current positive-construction
scope is stronger and independent: the compact Paley bank works in every
characteristic outside2,3,7 containing mu7. In characteristic3 its second
bucket vanishes and actually gives eight cubics over a suitable extension,
so at least one odd-characteristic exception is genuine.
