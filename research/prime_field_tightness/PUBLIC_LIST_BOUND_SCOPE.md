# Additional public theorem comparison, checked September 17

Brakensiek, Chen, Putterman, Zhang, and Zheng,
*Algorithmic List Decoding of Reed–Solomon Codes up to Capacity*,
[arXiv:2609.08005v1](https://arxiv.org/html/2609.08005v1), is a distinct
paper from the user's Dao–Kominers–Thaler draft.

Its formal Theorem4.1 and Corollary5.1 bound both running time and list
size by powers of the FIELD SIZE q. The informal Corollary1.2 instead
states a power of block length n. The displayed proof of Corollary5.1
concludes with the q-dependent bound. Thus that proof alone should not
be used as a field-size-independent list bound in our superpolynomial-
field compiler. This is a scope discrepancy, not a claim that the
stronger statement is false or that the underlying algorithm is invalid.

Our existing polynomial-pool dependency remains the separately stated
field-independent Theorem1.1 of Jeronimo, ECCC TR26-169. Neither full
external proof has been independently audited in this research turn.
