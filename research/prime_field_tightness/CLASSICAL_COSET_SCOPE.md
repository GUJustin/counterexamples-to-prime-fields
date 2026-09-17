# Classical coset construction: parameter check

Primary source: Atri Rudra, *List Decoding and Property Testing of Error
Correcting Codes* (2007), Section6.4.3, Theorems6.10 and6.13, printed
pages106–108; attribution to Guruswami–Rudra is in Section6.5.
https://cse.buffalo.edu/faculty/atri/papers/coding/thesis-chaps/chap6.pdf

The displayed family has n=p=ah+1, dimension k=(b-1)h+1,
agreement A=bh, and binom(a,b) candidates. Thus eta=(h-1)/p and

    log2 binom(a,b) <= a < 1/eta.

This bounds the displayed bank, not the complete decoding list. It does
not furnish growing fixed-gap lists. The main manuscript now credits
this earlier multiplicative-orbit mechanism explicitly. This targeted
check is not an exhaustive survey of lower bounds.
