"""Sequential checks for the newly integrated finite coding certificates."""
from pathlib import Path
import json, os, subprocess, sys, time

ROOT = Path(__file__).resolve().parent
DATA = ROOT/'certificates'


def main():
    started=time.monotonic()
    env=os.environ.copy()
    for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS',
                'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
        env[key]='1'
    commands=[
        ['clang++','-O3','-UNDEBUG','-std=c++17','exact_distribution.cpp','-o','exact_distribution'],
        ['clang++','-O3','-UNDEBUG','-std=c++17','central_quadratic_histogram.cpp','-o','central_quadratic_histogram'],
        [sys.executable,'verify_exact_distribution.py'],
        [sys.executable,'verify_radial_projection_moments14.py'],
        [sys.executable,'verify_radial3d_projection_moments14.py'],
        [sys.executable,'verify_tilted_radial_boundary.py','--dimension','4'],
        [sys.executable,'verify_tilted_radial_boundary.py','--dimension','3'],
        [sys.executable,'verify_exact_support_incidences.py','--n','82','--t','12','--q','486'],
        [sys.executable,'verify_saved_scalar.py'],
        [sys.executable,'certify_circle_product_dyadic.py'],
        [sys.executable,'verify_circle_product_orbits.py'],
        [sys.executable,'verify_circle_product_dyadic_output.py'],
    ]
    completed=[]
    for index,command in enumerate(commands):
        print('Checking',command,flush=True)
        report=f'replay_{index:02d}_resources.json'
        guarded=[sys.executable,'run_bounded.py','--rss-mib','384',
                 '--seconds','900','--report',report,'--',*command]
        subprocess.run(guarded,cwd=DATA,env=env,check=True)
        completed.append(dict(command=command,resources=json.loads((DATA/report).read_text())))
    result=dict(status='passed',steps=completed,seconds=time.monotonic()-started,
        scope='New finite-certificate integration. Includes n64 complementary enumeration, saved projection identities and raw moments, both displaced weights, n82 coordinate recount and exact dual replay, and native-circle arithmetic. Does not rerun the full original projection subset counts or the pre-existing paper suite.')
    (ROOT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print('All new finite-certificate checks passed.',flush=True)


if __name__=='__main__':
    main()
