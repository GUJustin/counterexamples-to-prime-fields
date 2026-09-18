"""Independent direct counts and necessary routing gates for profile108."""
import json
from pathlib import Path
N=262144; W=131071; A=181275; P=2130706433
m,B,s,U,k,n0,L=108,41,19,146,4,7,2557

C=M=0
caps=[]
for h in range(s+1):
    reserve=h if h<n0 else k
    cutoff=m*A-reserve*(A-(W-2))
    caps.append((cutoff+B-1)//W)
    for j in range(B-2*h+1):
        for i in range(U-h-j+1):
            count=max(0,cutoff-W*i-(W-1)*j-(W-2)*h)
            C+=count; M+=(i+j+h)*count
R=T=0
for r in range(m):
    for h in range(s+1):
        for i in range(r+1):
            for j in range(B-2*h+1):
                if i+j+h<=U:
                    R+=1;T+=i+j+h
        q=max((m-r+1)//2,max(0,m-r-max(0,s-h)))
        if q<=r and m-r+2*h<=B:
            for i in range(r-q+1):
                for j in range(B-2*h-q+1):
                    if i+j+h+q<=U:
                        R-=1;T-=i+j+h+q
assert (C,M,R,T)==(496877347482,30748718496757,1887186,96199851)

def mixed(p,q,r):
    a,b,c=p;d,e,f=q;g,h,i=r
    return (c*f*i+a*f*i+d*c*i+g*c*f+b*f*i+e*c*i+h*c*f
            +c*e*h+f*b*h+i*b*e+a*e*i+a*h*f+d*b*i+d*h*c+g*b*f+g*e*c)

def slack(flag,a,b,s,agreement=A):
    # Arguments a,b,s are shifted nonnegative variables.
    a+=2;b+=1;s+=1
    normal=mixed(flag,(262144*a,1+262144*(b+1),262144*(s+1)),
                 (131074*a,131074*b+2,131074*s+3))
    ident=(flag[0]*(393219+262146*s)+flag[1]*(786438+524292*s)
           +flag[2]*(1048586+262146*a+524292*b+524292*s))
    return (agreement-W)*normal-(N-W)*(N-agreement+1)*ident

assert slack((1,0,0),0,0,0,181353)==3426347998358554
slacks={}
for label,flag in [('z',(1,0,0)),('yz',(0,1,0)),('all',(0,0,1))]:
    f0=slack(flag,0,0,0)
    coefficients={'1':f0}
    units=[(1,0,0),(0,1,0),(0,0,1)]
    names=['a','b','s']
    for e,name in zip(units,names):
        f1=slack(flag,*e);f2=slack(flag,*(2*x for x in e))
        square=(f2-2*f1+f0)//2
        coefficients[name]=f1-f0-square;coefficients[name+'^2']=square
    for i in range(3):
        for j in range(i+1,3):
            e=tuple(units[i][h]+units[j][h] for h in range(3))
            coefficients[names[i]+names[j]]=(slack(flag,*e)-slack(flag,*units[i])
                                             -slack(flag,*units[j])+f0)
    assert min(coefficients.values())>=0
    slacks[label]=coefficients

def gates(r,y,t):
    helper=(B+s*(r-1),U+s*(y-1),L+s*(t-1))
    def pair(R,Y,T):return [r*T+t*R,y*T+t*Y,y*R+r*Y]
    reduced=(1+(W+1)*(2*y-2))*r+y*(2*r-2)*(W+1)
    identity=(1+W*(2*y-2))*r+y*(2*r-1)*W
    return dict(r=r,y=y,t=t,helper_caps=helper,helper_mixed=pair(*helper),
                coefficient_mixed=pair(B,U,L),retained_reduced_mixed=reduced,
                retained_identity_mixed=identity,
                retained_characteristic_pass=max(reduced,identity)<P,
                helper_characteristic_pass=max(pair(*helper)+pair(B,U,L))<P)

source=(L+1)*C-M;rank=(L+1)*R-T
assert source-N*rank==2092909271
out=dict(profile=[m,B,s,U,k,n0,L],agreement=A,source_count=source,
         local_rank_upper=rank,kernel_lower=source-N*rank,
         scalar_counts=dict(C=C,M=M,R=R,T=T),cutoff_caps=caps,
         source_hypotheses=dict(two_s_le_B=2*s<=B,B_le_m=B<=m,m_plus_s_le_U=m+s<=U,
          m_plus_B_plus_s_le_L=m+B+s<=L,all_cutoff_caps_cover_U=min(caps)>=U,
          k_lt_m=k<m,k_le_s=k<=s,k_plus_one_le_n0=k+1<=n0,
          retained_flag_nonnegative=2*(n0-k-1)<=B,L_lt_3261=L<3261),
         identity_target_slack_coefficients=slacks,
         characteristic_gates=[gates(12,55,3261),gates(30,136,6917),gates(36,163,9678)],
         scope='Independent integer audit of source and explicit target routing gates; no Lean build or full receipt.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
