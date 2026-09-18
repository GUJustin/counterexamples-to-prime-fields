# What exact product coverage alone cannot improve at the benchmark

September 18, 2026. This is a limitation of the current quotient compiler,
not an upper bound on arbitrary proximity-gap counterexamples.

At the recorded better.codes target, n=262144, J=131072, a qualifying
agreement threshold is T*=139782, and the required number of distinct
challenge labels is L*=274980728111395088. Consider the exact compiler
with n=(s+1)m, J-1=(r-2)m+w, and certified agreement T=J+2m-1.

Since m divides n, m is a power of two. Reaching T* requires
2m-1>=8710, hence m>=8192. Thus s<=31. For any such m dividing J,
w=m-1 and r=J/m+1=(s+3)/2. At m=8192 this gives s=31,r=17,
and only binom(31,17)=265182525 candidate subsets. For larger m,
even the total number 2^s of all subsets is smaller. Therefore the
number of labels certified by these witnesses is at most 265182525,
far below L*, regardless of any improvement in product coverage.

Conversely m=4096 gives T=139263, already 519 agreements short of
the chosen threshold; smaller m gives still fewer agreements.

This argument even permits a freely chosen union of fibers and an
arbitrary challenge field. It explains why the new all-product theorem
does not by itself improve the benchmark. To do so requires a different
degree/agreement tradeoff or witnesses beyond this compiler. It makes
no claim that these candidate witnesses exhaust all possible nearby
polynomials of its received words, and no global security upper bound.
