#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
using u64=uint64_t;
u64 power(u64 x,u64 e,u64 p){u64 y=1;while(e){if(e&1)y=y*x%p;x=x*x%p;e>>=1;}return y;}
bool prime(int x){if(x<2)return false;for(int d=2;d*(long long)d<=x;d++)if(x%d==0)return false;return true;}
u64 rng(u64 &s){s^=s<<13;s^=s>>7;s^=s<<17;return s;}
int main(int argc,char**argv){
 int L=argc>1?atoi(argv[1]):293,p=argc>2?atoi(argv[2]):1000003,d=argc>3?atoi(argv[3]):2;
 u64 seed=argc>4?strtoull(argv[4],nullptr,10):20260918,rs=seed;
 const int D=13,A=2*L-2,T=A+d; long long n=1LL*T*T/2+1,n0=1LL*L*(L-1),t=n-n0,N=t+2LL*L*D;
 if(!prime(p)||D>L-2||N+n0>=p){cerr<<"invalid parameters\n";return 2;}
 auto start=chrono::steady_clock::now();
 int q=L;while(!prime(q))q++;
 vector<int>factors;int v=p-1;for(int z=2;1LL*z*z<=v;z++)if(v%z==0){factors.push_back(z);while(v%z==0)v/=z;}if(v>1)factors.push_back(v);
 int generator=2;for(;;generator++){bool ok=true;for(int z:factors)if(power(generator,(p-1)/z,p)==1)ok=false;if(ok)break;}
 vector<int>aa(L),ia(L);vector<unsigned char>core(p,0);int core_count=0;
 vector<int>exponents(L);for(int i=0;i<L;i++){exponents[i]=2*q*i+(1LL*i*i%q);int a=power(generator,exponents[i],p);aa[i]=1LL*a*a%p;ia[i]=power(aa[i],p-2,p);}
 for(int i=0;i<L;i++)for(int j=0;j<i;j++){int z=power(generator,exponents[i]+exponents[j],p);for(int x:{z,p-z}){if(core[x]){cerr<<"core collision\n";return 3;}core[x]=1;core_count++;}}
 if(core_count!=n0){cerr<<"core size\n";return 4;}
 vector<int>h(D+1);for(int i=0;i<D;i++)h[i]=rng(rs)%p;h[D]=1;
 vector<int>inverse(p);inverse[1]=1;for(int i=2;i<p;i++)inverse[i]=p-1LL*(p/i)*inverse[p%i]%p;
 vector<int>xs,x2s,hs,ig;xs.reserve(t);x2s.reserve(t);hs.reserve(t);ig.reserve(t);
 long long candidates=0,deleted=0;u64 hash=1469598103934665603ULL;
 int last=0;
 for(int x=1;x<p&&xs.size()<(size_t)t;x++){
  if(core[x])continue;if(++candidates>N){cerr<<"candidate exhaustion\n";return 5;}
  int x2=1LL*x*x%p,g=1LL*x2*x%p,z=1;
  for(int j=D-1;j>=0;j--)z=(1LL*z*x+h[j])%p;
  bool forbidden=false;for(int i=0;i<L;i++){int y=(1LL*x2*ia[i]+aa[i])%p;if(z==y||z==(y-g+p)%p){forbidden=true;break;}}
  if(forbidden){deleted++;continue;}
  xs.push_back(x);x2s.push_back(x2);hs.push_back(z);ig.push_back(1LL*inverse[x]*inverse[x]%p*inverse[x]%p);last=x;
  hash^=(u64)x;hash*=1099511628211ULL;
 }
 if(xs.size()!=(size_t)t){cerr<<"insufficient nodes\n";return 6;}
 double setup=chrono::duration<double>(chrono::steady_clock::now()-start).count();
 vector<unsigned char>hits(p);vector<uint16_t>owners(p);vector<u64>hit_hist(D+1,0);hit_hist[0]=1ULL*L*p;int max_hits=0;
 for(int i=0;i<L;i++){
  fill(hits.begin(),hits.end(),0);
  for(size_t j=0;j<xs.size();j++){
   int y=(1LL*x2s[j]*ia[i]+aa[i])%p;
   int label=1LL*(y-hs[j]+p)*ig[j]%p;
   int c=++hits[label];if(c==d)owners[label]++;
   if(c>D){cerr<<"degree cap exceeded\n";return 7;}
   hit_hist[c-1]--;hit_hist[c]++;max_hits=max(max_hits,c);
  }
 }
 map<int,u64>owner_hist;u64 bad=0,single=0;for(int label=0;label<p;label++){owner_hist[owners[label]]++;if(owners[label])bad++;if(owners[label]==1)single++;}
 if(owners[0]||owners[1]){cerr<<"blacklist failed\n";return 8;}
 double total=chrono::duration<double>(chrono::steady_clock::now()-start).count();
 cout<<"{\n\"schema\":1,\"L\":"<<L<<",\"p\":"<<p<<",\"d\":"<<d<<",\"D\":"<<D<<",\"A\":"<<A<<",\"T\":"<<T<<",\"n\":"<<n<<",\"n0\":"<<n0<<",\"t\":"<<t<<",\"candidate_limit\":"<<N<<",\n";
 cout<<"\"q\":"<<q<<",\"primitive_root\":"<<generator<<",\"seed\":"<<seed<<",\"h_coefficients_ascending\":[";for(int i=0;i<=D;i++){if(i)cout<<",";cout<<h[i];}cout<<"],\n";
 cout<<"\"domain_rule\":\"Increasing integers x in [1,p-1], excluding core ±gamma^(b_i+b_j), then blacklist h(x)=P_i(x) or P_i(x)-x^3, retaining first t survivors; b_i=2qi+(i^2 mod q), i=0..L-1\",\n";
 cout<<"\"candidates_examined\":"<<candidates<<",\"deleted\":"<<deleted<<",\"last_fresh_node\":"<<last<<",\"domain_fnv64\":\""<<hash<<"\",\n";
 cout<<"\"canonical_bad_labels\":"<<bad<<",\"canonical_singleton_labels\":"<<single<<",\"transformed_bad_labels\":"<<bad+1<<",\"transformed_singleton_labels\":"<<single+1<<",\"owner_histogram\":{";bool first=true;for(auto z:owner_hist){if(!first)cout<<",";first=false;cout<<"\""<<z.first<<"\":"<<z.second;}cout<<"},\n";
 cout<<"\"bank_fresh_hit_histogram\":[";for(int j=0;j<=D;j++){if(j)cout<<",";cout<<hit_hist[j];}cout<<"],\"max_bank_fresh_hits\":"<<max_hits<<",\"nonbank_agreement_upper\":"<<L+D<<",\"setup_seconds\":"<<setup<<",\"total_seconds\":"<<total<<"\n}\n";
}
