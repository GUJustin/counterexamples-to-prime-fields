"""Exact DP for two candidate cosets, using subgroup-invariant domains/words."""
import argparse
from array import array
from collections import Counter
from math import comb,isqrt
from pathlib import Path
import json,time


def prime(p): return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def generator(p):
    fac=[];m=p-1;d=2
    while d*d<=m:
        if m%d==0:
            fac.append(d)
            while m%d==0: m//=d
        d+=1
    if m>1: fac.append(m)
    return next(g for g in range(2,p) if all(pow(g,(p-1)//d,p)!=1 for d in fac))

def evaluate(c,x,p):
    y=0
    for a in reversed(c):y=(y*x+a)%p
    return y


def solve(r,k,j,H,shift,c=4):
    started=time.monotonic();p=2*r*k+1
    assert prime(p) and k%H==0 and 0<shift<k//H and c*k<=p-1
    g=generator(p);e=r*k+j
    coeff=[comb(e,r*i+j)%p for i in range(k+1)]
    assert coeff[-1]==1 and coeff[1]
    C=(p-1)//H
    sub=[pow(g,C*i,p) for i in range(H)]
    cosets=[[pow(g,t,p)*h%p for h in sub] for t in range(C)]
    hist=[Counter(evaluate(coeff,x,p) for x in xs) for xs in cosets]
    offset=(p-1)//k*shift
    actions=[]
    for t in range(C):
        left,right=hist[t],hist[(t+offset)%C]
        vectors={}
        for v in left.keys()|right.keys():
            ab=(left[v],right[v]); vectors[ab]=min(v,vectors.get(ab,p))
        frontier=[]
        for (a,b),v in vectors.items():
            if not any(aa>=a and bb>=b and (aa>a or bb>b) for aa,bb in vectors):
                frontier.append((a,b,v))
        actions.append(sorted(frontier))
    q=c*k//H;n=c*k;width=n+1;size=(q+1)*width
    dp=array('h',[-1])*size;dp[0]=0
    history=[]
    for t,opts in enumerate(actions):
        nxt=dp[:];choice=array('h',[-1])*size
        for used in range(min(q-1,t)+1):
            base=used*width;newbase=base+width
            for first in range(used*H+1):
                second=dp[base+first]
                if second<0:continue
                for option,(a,b,v) in enumerate(opts):
                    idx=newbase+first+a
                    value=second+b
                    if value>nxt[idx]:
                        nxt[idx]=value;choice[idx]=option
        history.append(choice);dp=nxt
    first=max(range(n+1),key=lambda a:min(a,dp[q*width+a]))
    second=dp[q*width+first];A=min(first,second)
    selected=[];used=q;current=first
    for t in range(C-1,-1,-1):
        option=history[t][used*width+current]
        if option>=0:
            a,b,v=actions[t][option]
            selected.append((t,v,a,b));used-=1;current-=a
    assert used==0 and current==0 and len(selected)==q
    domain=[x for t,v,a,b in selected for x in cosets[t]]
    word={x:(v-pow(x,k,p))%p for t,v,a,b in selected for x in cosets[t]}
    candidates=sub+[pow(g,offset,p)*h%p for h in sub]
    assert len(set(candidates))==2*H and len(set(domain))==n
    counts=[sum((evaluate(coeff,h*x%p,p)-pow(x,k,p))%p==word[x] for x in domain) for h in candidates]
    assert min(counts)==A
    assert len(set(counts[:H]))==len(set(counts[H:]))==1
    elias=A>k and n**n*(p-1)**(n-A)<(n-A)**(n-A)*A**A*p**(n-k)
    return dict(r=r,k=k,section=j,H=H,shift=shift,p=p,generator=g,n=n,L=2*H,
                A=A,group_agreements=[counts[0],counts[-1]],positive_gap=A>k,
                below_elias=elias,selected_cosets=selected,seconds=time.monotonic()-started,
                scope='Optimal among unions of H-cosets with a constant normalized word on each coset; only the selected two candidate cosets.')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    if args.pilot:
        cases=[(33,32,0,8,1),(33,32,0,8,2),(5,64,0,16,1),(5,64,1,16,1),(6,64,0,16,1),(6,64,1,16,1),(3,128,0,32,1),(3,128,1,32,1),(13,128,0,32,1),(13,128,1,32,1)]
    else:
        cases=[(r,k,j,k//4,1) for k in (32,64,128) for r in range(2,49)
               if prime(2*r*k+1) for j in sorted({0,1,r//2,r-1})]
    rows=[]
    for case in cases:
        row=solve(*case);rows.append(row)
        args.output.write_text(json.dumps(dict(status='running',completed=len(rows),total=len(cases),rows=rows),indent=2)+'\n')
        print(json.dumps({key:row[key] for key in ('r','k','section','H','shift','p','L','A','positive_gap','below_elias','seconds')}),flush=True)
    args.output.write_text(json.dumps(dict(status='complete',completed=len(rows),total=len(cases),rows=rows),indent=2)+'\n')

if __name__=='__main__':main()
