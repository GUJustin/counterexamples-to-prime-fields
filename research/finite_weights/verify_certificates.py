"""Check all saved candidate weights exactly against the verified moments."""
from pathlib import Path
from math import prod
from hashlib import sha256
import json

ROOT = Path(__file__).parent
saved = json.loads((ROOT/'moments40.json').read_text())
assert (saved['n'],saved['t'],saved['q'],saved['center'],saved['degree']) == (64,34,1071,22138,40)
assert len(saved['raw_moments']) == len(saved['centered_moments']) == saved['degree']+1
verified = []
for path in sorted(ROOT.glob('*_certificates.json')):
    for cert in json.loads(path.read_text()):
        coeff = cert['coefficients_ascending']
        assert isinstance(cert['degree'],int) and 0 <= cert['degree'] <= saved['degree']
        assert len(coeff) == cert['degree']+1
        assert (cert['center'],cert['low'],cert['high']) == (saved['center'],17969,26129)
        assert all(isinstance(a,int) for a in coeff) and coeff[-1] != 0
        if 'roots' in cert:
            assert len(cert['roots']) == cert['degree']
            assert all(isinstance(r,int) for r in cert['roots'])
        def evaluate(x):
            out = 0
            for a in reversed(coeff):
                out = out*x+a
            return out
        numerator = sum(a*m for a,m in zip(coeff,saved['centered_moments']))
        denominator = 0
        for x in range(-4169,3992):
            value = evaluate(x)
            if 'roots' in cert:
                assert value == coeff[-1]*prod(x-r for r in cert['roots'])
            denominator += max(0,value)
        assert numerator == cert['numerator'] > 0
        assert denominator == cert['denominator'] > 0
        bound = (numerator+denominator-1)//denominator
        assert bound == cert['list_lower_bound']
        verified.append(dict(file=path.name,degree=cert['degree'],list_lower_bound=bound))
result = dict(status='passed',moments_sha256=sha256((ROOT/'moments40.json').read_bytes()).hexdigest(),
    certificates=verified,best_list_lower_bound=max(c['list_lower_bound'] for c in verified))
(ROOT/'certificates_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
