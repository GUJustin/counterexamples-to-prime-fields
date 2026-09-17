# Targeting the actual singleton bottleneck

The repaired target pipeline's binding prefix can be traced exactly:

1. Phase 32 at `(r,v,z)=(17,45,4526)` uses phase 6.
2. Phase 6 at `(13,43,3749)` uses phase 5.
3. Phase 5 at `(12,43,3206)` uses the base envelope.
4. The active base sheet has slope zero and a single Bellman component
   `(12,43)`. There is no packing decomposition loss at this contact.

The singleton allowance is 288191873412750740, attained at `z=3206`, total
degree 3261. Root group 11 (zero-indexed) is the cheapest available bound.
Several other root groups are within 0.06%. This is precisely one coordinate
before source 00 becomes routeable at `z=3207`.

The baseline control explains the inflation: at incumbent agreement 181284,
the same singleton allowance was 253053344381670839. Its source 06 threshold
was 2505, versus 3376 after repairing the target source. The loss of early
routing is therefore important; the change is not just the increased
auxiliary source total-degree caps.

## Bounded source searches

Four bounded searches tested 1464 shapes in total, with some overlap. All
source dimension counts, thin-band route checks, and singleton envelope
objectives use exact integers. `fast_firstjet_count.py` sums the cubic
coefficient-count polynomial separately between residue crossings; its
saturation hypothesis is `L >= floor((D+s-1)/w)`.

The best source satisfying the entire enlarged phase box's characteristic
gates was `(m,L,s,Y)=(84000,5880000,26014,116174)`. It moves the critical
threshold from 3207 to 3193 and lowers this singleton allowance to
286984958181367914. These are local envelope improvements; a full pipeline
improvement has not been claimed.

A context-local singleton source can legitimately use the actual factor
degrees in the characteristic gates. For example, at `r=12,y=55`, the gate
is `55 L + t Y < p`, rather than the global-box requirement
`163 L + t Y < p`. The generic thin split theorem applies to the singleton
factor set; all power stages have smaller right-hand caps. An explicit
local singleton adapter is needed because the existing `PhaseSourceSound`
wrapper quantifies over the entire box.

The best tested local source was
`(m,L,s,Y)=(120000,8400000,37168,165963)`, with kernel dimension lower bound
1633475068169425859609748. Its exact helper affine majorant is
`5467424339886*z + 7731591903795957`. The threshold is 3191 and the singleton
allowance becomes 286812541719741796, a local gain of 1379331693008944.
All three mixed characteristic costs at total 9678 are below the prime:
`(460511904,2068189914,4035796)`.

The distinct high-`L/m` branch did not produce a better tested source.
At fixed `(m,s)=(28000,8529)`, the exact normalized gate margin is affine
and decreasing in `L` in the saturated regime. Increasing `L/m` from 130
to 260 and 520 changes it from approximately−0.000395 to−0.000628 and
−0.001094. The analytic agent's exact-degree correction note establishes
a rigorous exclusion for that fixed shape and large-L interval; it is
not a global obstruction for all interpolation sources.

## Exact contact-degree sharpener

The generic thin-band theorem permits actual source contact budget
`D=m*A`, instead of the shape-derived upper bound `w*(Y+1)-s`. This is a
proof-preserving refinement after adding D to the numeric route interface.
The factor contact bound remains unchanged.

At the critical singleton, the eight source thresholds change as follows:

| Source | Rounded contact cap | Exact D |
|---|---:|---:|
|00|3207|3207|
|01|3222|3222|
|02|3217|3216|
|03|3229|3229|
|04|3269|3268|
|05|4041|4032|
|06|3376|3374|
|New 350|5872|5860|

Thus this sharpener leaves the current singleton maximum at 3206 unchanged.
It is useful for future candidates but does not explain away the complete
target pipeline's approximately 7.65% deficit.

The corresponding scripts/results are `trace_binding_prefix.py`,
`trace_singleton_contacts.py`, `search_early_phase.py`,
`search_alternate_phase.py`, `search_char_limited_phase.py`,
`search_local_singleton_source.py`, and `exact_contact_thresholds.py`.
All numerical jobs have bounded resource reports. No new leaderboard score
or completed formal certificate is asserted.
