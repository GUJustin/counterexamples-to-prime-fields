# Can505 spare agreements fund same-domain padding?

The B=1024,M=256,H=137 candidate has140287 agreements,505 above the
139782 target, but its guaranteed family count is about4.01 times too
small. A single-word list with this size and agreement would indeed be
interesting input to a coordinate-padding/diversity construction.
The available family is not such a list.

## Actual geometry of the counted bank

Put Y=X^1024. With R the fixed degree1023 core locator, V0 a reference,
Delta_U=V0-V_U, and alpha the selected pole, the witnesses are

    gamma_U=Delta_U(alpha)/alpha,
    P_U=R[Delta_U(Y)-gamma_U Y]/[Y(Y-alpha)].

They match different members of the received line

    f0=R V0(Y)/[Y(Y-alpha)],  f1=-R/(Y-alpha),
    f0+gamma_U f1.

The guaranteed near-polynomial bank of size68579341025511059 is
therefore a bank of label/witness pairs. It is not a list about f0 or
any other established single received word. Applying a single-word
compiler directly would drop the gamma_U f1 term incorrectly.

## The direction cannot be absorbed on the retained coordinates

After repurposing at most506 coordinates, at least261638 coordinates
remain. If f1 agreed with a polynomial P of degree<131072 at all those
points, then

    R+(Y-alpha)P

would have at least261638 roots and degree at most132095. It would
vanish identically. This is impossible: at any root of Y-alpha in an
algebraic closure, R is nonzero because alpha is outside the packet
labels and R's roots are in the original domain. Thus a codeword shift
cannot turn this line into a direction-zero line on the retained core.

Nor can one reuse the same witness at a different challenge parameter
on its original agreement set: f1 is nonzero away from the1023 core
roots. Any such coordinate forces the new parameter to equal gamma_U.
This is a restriction on reusing the established agreements; accidental
additional agreements elsewhere are not ruled out.

## A genuine single-word version pays another coefficient

The natural fixed-word version deletes the pole correction and uses

    W=R V0(Y)/Y,  P_U=R Delta_U(Y)/Y.

With only six common top coefficients, Delta_U has degree at most129,
so P_U has degree at most132095, exceeding the code's131071 maximum.
Fixing a seventh coefficient lowers the bound to131071. Its guaranteed
list count becomes

    ceil(binomial(255,136)/(256*p^7))=32186199.

Even granting506 perfectly disjoint label sets, each as large as this
entire certified list, yields only16286216694 labels, far below
274980728111395088. This comparison excludes obtaining the target from
this guaranteed list and the elementary t*L compiler bound; it is not
an upper bound on the true largest coefficient fiber or on every list
about W.

## Benchmark condition

The pinned upper target requires many winning labels for an input with
no simultaneous correlated witness satisfying the selected linear
constraints, throughout an unsafe-radius suffix. With zero constraints,
the existing rational-line proof uses that f1 is far to ensure this.
A full-support MCA count alone would not replace that condition. A
proper single-word list can instead use the established nonzero-constraint
list reduction, but the prerequisite single-word list is missing here.

These conclusions use the restored construction and benchmark-scope
notes. They do not claim a fresh Lean verification or a new score.
