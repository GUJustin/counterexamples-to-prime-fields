# Unique witnesses with nearly full gap separation

`orbit.tex` extends the paired powers-of-two construction to prime-order orbits. For any fixed separation fraction below one, suitable infinitely many prime fields have lines violating the c2=1 numerical prescription, with exactly one efficiently recoverable codeword at every nearby point. The far point is one coordinate short of maximum RS distance.

This is a sparse-bank theorem. It does not combine uniqueness with complete nonzero coverage.

Run, sequentially:

```
python3 verify_parameters.py
python3 check_small.py
python3 verify.py
```

The saved roots in `roots.json` are independently checked. `instances.json` gives compact exact domains and representative witness polynomials. See `PROOF_AUDIT.md` for the dependencies, qualifications, and replay scope.
