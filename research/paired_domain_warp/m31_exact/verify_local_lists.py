"""Check exact local lists after excluding every unpaired nearby locator."""
from pathlib import Path
import json,os,subprocess,tempfile,time
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();a=json.loads((BASE/'count.json').read_text());inp=' '.join(map(str,a['core_representatives']))
 assert (a['p'],a['n'],a['K'])==(2**31-1,62,31)
 assert len(set(a['core_representatives']))==30 and all(1<x<=(a['p']-1)//2 for x in a['core_representatives'])
 results={}
 with tempfile.TemporaryDirectory(prefix='paired-m31-lists-') as temp:
  for name in ['relations','relations_replay','histogram','histogram_replay']:
   exe=Path(temp)/name
   subprocess.run([os.environ.get('CXX','c++'),'-O3','-UNDEBUG','-std=c++17',str(BASE/(name+'.cpp')),'-o',str(exe)],check=True)
   results[name]=json.loads(subprocess.check_output([str(exe)],input=inp,text=True))
   print('PASS '+name,flush=True)
 assert results['relations']['nonempty_zero_relations']==0 and results['relations']['matching_pairs']==1
 assert results['relations_replay']['only_trivial_relation']
 h=results['histogram']['histogram_including_zero_parameter'];assert h==results['histogram_replay']['histogram_including_zero_parameter']
 assert sum(h)==a['p'] and sum(i*v for i,v in enumerate(h))==a['supports']
 assert sum(h[1:])==a['distinct_products'] and h[1]**3>62**3*2**62
 assert h==[2006567569,136494714,4337028,83442,891,3]
 out=dict(status='passed',p=a['p'],n=62,K=31,histogram=h,exact_nearby_parameters=sum(h[1:]),
  uniquely_nearby_parameters=h[1],maximum_list_size_on_this_line=len(h)-1,seconds=time.monotonic()-start,
  scope='Exact lists on this one line at distance28/62. The no-signed-relation lemma excludes all nonpaired witnesses. This is not a global list-size bound for the code.',replays=results)
 (BASE/'local_lists_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
