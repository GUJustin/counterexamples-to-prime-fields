# Independent review of the quadratic-extension reduction

PASS for the stated two-block, dimension-three model. The root agent checked
the saved FP2_PARTITIONED_TWO_BLOCK_REDUCTION.md algebra directly.

For a non-even quadratic the Frobenius elimination has degree at most four.
Its identical vanishing forces N(A)=1, B^(2p-2)=A^(-3), and zero discriminant.
Applying these necessary conditions to both normalized blocks gives N(c)=1;
if c is norm one but not one, the two discriminants force lambda=0, and the
two leading-coefficient identities then force c^4=c^3, a contradiction.
Thus the asserted U+4 bound outside the even canonical family is valid.

The even constant equations give

    d(1-c)=lambda+a c lambda^p.

With z=(lambda/(1-c))^p, this is exactly d=z^p-a z. The second-block
direction is eta times the first when c=eta^(1-p), as stated. Each coordinate
away from x^2=z determines one norm-one coefficient a, while each coordinate
with x^2=z matches all p+1 coefficients. This proves the incidence identity
n+p e_z, including its overlap accounting. It does not prove any rich center.

The common-agreement estimate follows because a nonconstant quadratic
explaining the indicator word can match its zero and one values on at most
four coordinates, whereas constant explanations attain each block maximum.
The affine square-lift count p-chi_E(u) follows from the nonsingular quadratic
norm character sum on a nonzero affine fiber. The separate zero-fiber counts
are correct and cannot be replaced by the quartic theorem's doubled plane.

Finally, on a base-field domain, both block restrictions are quadratics, so
all received words have agreement at least n/2. For n>8 this exceeds sqrt(2n).
This rules out the desired far endpoints for this model on such a domain;
it is not an impossibility statement for arbitrary received words or codes
over F_(p^2). The short-domain rich-center target remains unconstructed.
