# Reproduce the all-multiplicity certificate

From the repository root, with a C++17 compiler and Python 3:

```sh
c++ -O2 -std=c++17 research/better_codes_primary_nonrectangular/all_m_slope.cpp -o /tmp/primary_all_m_slope
mkdir -p research/better_codes_primary_nonrectangular/all_m_certificates
/tmp/primary_all_m_slope 1 64 research/better_codes_primary_nonrectangular/all_m_certificates
/tmp/primary_all_m_slope 65 128 research/better_codes_primary_nonrectangular/all_m_certificates
/tmp/primary_all_m_slope 129 194 research/better_codes_primary_nonrectangular/all_m_certificates
python3 research/better_codes_primary_nonrectangular/verify_all_m.py 1 64
python3 research/better_codes_primary_nonrectangular/verify_all_m.py 65 128
python3 research/better_codes_primary_nonrectangular/verify_all_m.py 129 194
```

Every maximum slope must be zero. Generation took approximately 16 seconds,
verification 9 seconds on the recorded machine. Parameterwise JSON receipts,
three verification summaries, resource reports, and `flow_manifest.json`
are retained. The large `.flowbin.gz` payloads remain local; regenerate them
from the source rather than committing them. Raw files are portable
little-endian records on the recorded platform. Compare their SHA-256
hashes to `sha256_raw` in the manifest. The verifier also reads gzip files.

On macOS with an SDK-only compiler installation, compilation may additionally
require `-isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX15.4.sdk`.

## Partial-prefix frozen-m115 gate

```sh
c++ -O2 -std=c++17 research/better_codes_primary_nonrectangular/partial_prefix.cpp -o /tmp/partial_prefix
/tmp/partial_prefix research/better_codes_primary_nonrectangular/partial_prefix
python3 research/better_codes_primary_nonrectangular/verify_partial_prefix.py
```

Expected: maximum slope zero, flow=cut47859086760, 600647 nodes and2011395
original directed edges. The generator used about217MiB and17seconds;
verification used about48MiB and2seconds. The same optional macOS SDK flag
applies. `partial_prefix.flow_manifest.json` records the raw flow hash.
