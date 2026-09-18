#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <random>
#include <set>
using namespace std;
int p;vector<int> invv,rt;
int m(long long x){x%=p;return x<0?x+p:x;}
int main(){mt19937 gen(20260918);ofstream hit("research/prime_line_strengthening/four_word_one_pole/transversal_search/hits.jsonl");
for(int prime:{97,113}){p=prime;invv.assign(p,0);rt.assign(p,-1);for(int x=1;x<p;x++){for(int y=1;y<p;y++)if(x*y%p==1){invv[x]=y;break;}rt[x*x%p]=x;}long long seeds=0,admiss=0,cores=0,patterns=0,hits=0;
for(int trial=0;trial<100000 && cores<1000;trial++){seeds++;array<int,4>a;for(int&i:a)i=1+gen()%(p-1);set<int> sq;for(int x:a)sq.insert(x*x%p);if(sq.size()!=4)continue;
int e1=0,e3=0,e4=1;for(int x:a){e1=m(e1+x);e4=m(e4*x);}for(int i=0;i<4;i++){int z=1;for(int j=0;j<4;j++)if(i!=j)z=m(z*a[j]);e3=m(e3+z);}if(!e3)continue;int pole=m(e1*e4*invv[e3]);
vector<int>ys,ws;set<int>seen;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++){int x=m(a[i]*a[j]),v=m(a[i]*a[i]+a[j]*a[j]);for(int y:{x,m(-x)}){ys.push_back(y);ws.push_back(m((y-pole)*v));seen.insert(y);}}if(seen.size()!=12||seen.count(pole))continue;admiss++;
for(int c=0;c<p&&cores<1000;c++){if(rt[m(pole-c)]<0)continue;vector<int>roots;bool ok=true;for(int y:ys){int r=rt[m(y-c)];if(r<0){ok=false;break;}roots.push_back(r);}if(!ok)continue;cores++;
vector<int> fullY=ys,fullW=ws,fullR=roots;
for(int omit=0;omit<12;omit+=2){
ys={pole};ws={0};roots={rt[m(pole-c)]};
for(int j=0;j<12;j++)if(j!=omit){ys.push_back(fullY[j]);ws.push_back(fullW[j]);roots.push_back(fullR[j]);}
for(int mask=0;mask<128;mask++){patterns++;array<int,8>ts,weights;for(int i=0;i<8;i++)ts[i]=(i==0||!(mask&(1<<(i-1))))?roots[i]:m(-roots[i]);int ell=0;for(int i=0;i<8;i++){int den=1;for(int j=0;j<8;j++)if(i!=j)den=m(den*(ts[i]-ts[j]));weights[i]=invv[den];ell=m(ell+ws[i]*weights[i]);}if(!ell)continue;
array<array<int,2>,4>bs;for(int j=8;j<12;j++)for(int s=0;s<2;s++){int t=s?m(-roots[j]):roots[j],den=0;for(int i=0;i<8;i++)den=m(den+weights[i]*m(ws[i]-ws[j])*invv[m(t-ts[i])]);bs[j-8][s]=den?m(t-ell*invv[den]):-1;}
for(int sg=0;sg<2;sg++){int b=bs[0][sg];if(b<0)continue;array<int,4>sign;sign[0]=sg;bool yes=true;for(int j=1;j<4;j++){if(bs[j][0]==b)sign[j]=0;else if(bs[j][1]==b)sign[j]=1;else{yes=false;break;}}if(!yes)continue;int by=m(b*b+c);if(by==pole||seen.count(by))continue;
// Since ell!=0 and b is off all interpolation nodes, N(b)=-ell*L8(b)!=0.
hits++;hit<<"{\"p\":"<<p<<",\"a\":[";for(int i=0;i<4;i++)hit<<(i?",":"")<<a[i];hit<<"],\"first_pole\":"<<pole<<",\"critical\":"<<c<<",\"new_pole\":"<<b<<",\"nodes\":[";for(int i=0;i<12;i++){int t=i<8?ts[i]:(sign[i-8]?m(-roots[i]):roots[i]);hit<<(i?",":"")<<t;}hit<<"],\"base_nodes\":[";for(int i=0;i<12;i++)hit<<(i?",":"")<<ys[i];hit<<"],\"values\":[";for(int i=0;i<12;i++)hit<<(i?",":"")<<ws[i];hit<<"]}\n";hit.flush();if(hits>=8)goto done;
}
}
}
ys=fullY;ws=fullW;roots=fullR;
}
}
done:cout<<"{\"p\":"<<p<<",\"sampled_seeds\":"<<seeds<<",\"admissible_seeds\":"<<admiss<<",\"fully_split_cores\":"<<cores<<",\"first_sign_patterns\":"<<patterns<<",\"proper_hits\":"<<hits<<"}"<<endl;
}
}
