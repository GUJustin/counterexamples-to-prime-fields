# A numerator-only limit for redistributing the B1024 core

For a>=1, put c=1024a−1 and h=137−a. A degree-c core and h whole packets have maximum agreement140287. At target139782 their selected overlap may be at most505. Six common leading coefficients plus product still give witness degree at most c+1024(h−9)=131071 after the two-factor quotient, whenever that degree calculation applies.

There is no need to optimize the overlap pattern merely to test the elementary pigeonhole guarantee. Even granting that EVERY h-subset of all256 packet tags qualifies, the numerator is at most C(256,128). This is only3.5115582636181446 times the archived C(255,136) numerator. Exact integer arithmetic gives

    ceil(C(256,128)/(256*p^6)) =240820351691620212
                                  <274980728111395088.

Thus changing core size, distributing its roots across more packets, or choosing a different h cannot alone produce the needed guarantee while keeping the same six-coefficient and256-class product denominator. This is an upper bound on that uniform-pigeonhole GUARANTEE, not an upper bound on an actual largest fiber. A smaller attainable signature image or genuine modular concentration would be additional mathematics outside this count. No weighted-tail scan or rental is justified solely for enlarging this numerator.
