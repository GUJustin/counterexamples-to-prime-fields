# Bounded remote cyclic search receipts

All four manifests were executed on the task-owned Vast instance51382288. Other user instances were untouched. Each job has a90-second limit;16 jobs run concurrently. The quote was $0.055185185 per hour. A local watchdog bounds the rental duration; its authoritative state is tmp/proximity_vast_state.json.

Batch001 has177 receipts, including six q23 timeouts. Those cases are incomplete. Its exact source is batch_001_search.cpp. Batches002,003,004 use search.cpp, SHA256 a19c2b6f030aebcb16393f2b94422ffe33e8bb1064ccb30372b634ec6283e301. The latter three archives were downloaded, checked against every manifest job and source hash, and every receipt reports successful exhaustive completion for its stated finite-field search.

- Batch002:152 jobs,24 hits, all at q5 orq7 (positive regression families). Includes full profile-pruned q23 searches, small composite q9/15/21 and Singer q63.
- Batch003:1208 jobs, no hits. Together with72 earlier jobs, covers all80 normalized q127 difference-set first supports at16 stated split primes.
- Batch004:1728 jobs, no hits. Covers576 additional doubling-invariant q127 first supports at three primes509,2287,5081.

These finite-prime scans alone give no characteristic-zero exclusion and no universal list-size bound. Separate exact modular unit-leading certificates prove the scoped characteristic-zero exclusions; see MODULAR_ALL_PROFILE_EXCLUSION.md and SMALL_Q_COMPLETE_MODULAR_EXCLUSION.md. The latter new batch is awaiting independent audit. No better.codes improvement or new positive list larger than seven follows from these searches.
