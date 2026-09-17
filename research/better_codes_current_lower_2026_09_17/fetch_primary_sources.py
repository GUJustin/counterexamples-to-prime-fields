"""Restore public pinned Lean inputs, verifying each saved SHA256."""
import hashlib,json,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]
manifest=json.loads((ROOT/'source_inputs.json').read_text())
for item in manifest['files']:
    target=REPO/item['path']
    if target.exists():
        data=target.read_bytes()
        assert hashlib.sha256(data).hexdigest()==item['sha256'],f'Changed input: {target}'
        continue
    data=urllib.request.urlopen(item['url'],timeout=30).read()
    assert hashlib.sha256(data).hexdigest()==item['sha256'],f'Checksum mismatch: {target}'
    target.parent.mkdir(parents=True,exist_ok=True)
    temporary=target.with_name(target.name+'.download')
    temporary.write_bytes(data)
    temporary.replace(target)
print(f"Verified {len(manifest['files'])} pinned inputs.")
