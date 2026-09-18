// Independent verifier: reconstructs all finite-field polynomials from supports.
// Flat input: q, domain_count, pair_count, row_count; domains(size,indices);
// pairs(source_domain,target_domain); rows(id,pair,h,p,zeta,claimed_pass).
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <tuple>
#include <vector>
using namespace std;
using Poly=vector<int>;
static int modp;
int norm(long long x){x%=modp;if(x<0)x+=modp;return int(x);}
int mulm(int a,int b){return int((int64_t)a*b%modp);}
int pw(int a,int n){int v=1;for(;n;n>>=1,a=mulm(a,a))if(n&1)v=mulm(v,a);return v;}
void trim(Poly& a){while(!a.empty()&&!a.back())a.pop_back();}
Poly add(Poly a,const Poly&b,int sign=1){a.resize(max(a.size(),b.size()));for(size_t i=0;i<b.size();++i)a[i]=norm((long long)a[i]+sign*b[i]);trim(a);return a;}
Poly times(const Poly&a,const Poly&b){if(a.empty()||b.empty())return {};Poly c(a.size()+b.size()-1);for(size_t i=0;i<a.size();++i)for(size_t j=0;j<b.size();++j)c[i+j]=norm((long long)c[i+j]+mulm(a[i],b[j]));trim(c);return c;}
Poly scale(Poly a,int c){for(int&x:a)x=mulm(x,c);trim(a);return a;}
pair<Poly,Poly> divide(Poly a,const Poly&b){assert(!b.empty());if(a.size()<b.size())return {{},a};Poly q(a.size()-b.size()+1);int inv=pw(b.back(),modp-2);while(!a.empty()&&a.size()>=b.size()){int shift=int(a.size()-b.size()),c=mulm(a.back(),inv);q[shift]=c;for(size_t j=0;j<b.size();++j)a[j+shift]=norm((long long)a[j+shift]-mulm(c,b[j]));trim(a);}trim(q);return {q,a};}
Poly gcd_cert(const Poly&a,const Poly&b){Poly r0=a,r1=b,s0{1},s1{},t0{},t1{1};while(!r1.empty()){auto qr=divide(r0,r1);Poly ns=add(s0,times(qr.first,s1),-1),nt=add(t0,times(qr.first,t1),-1);r0=r1;r1=qr.second;s0=s1;s1=ns;t0=t1;t1=nt;}if(r0.empty())return {};int u=pw(r0.back(),modp-2);r0=scale(r0,u);s0=scale(s0,u);t0=scale(t0,u);assert(add(times(s0,a),times(t0,b))==r0);return r0;}
bool prime(int n){if(n<2)return false;for(int d=2;(int64_t)d*d<=n;++d)if(n%d==0)return false;return true;}
struct DomainData{Poly modulus;vector<Poly> powers;};
struct PairData{int s,t;vector<int> shifts;};
int main(int argc,char**argv){assert(argc==3);ifstream in(argv[1]);ofstream out(argv[2]);int q,nd,np,nr;in>>q>>nd>>np>>nr;assert(in&&q>=3&&q%2==1);int r=(q-1)/2;vector<vector<int>>domains(nd);for(auto&d:domains){int n;in>>n;d.resize(n);for(int&x:d)in>>x;auto t=d;sort(t.begin(),t.end());assert(unique(t.begin(),t.end())==t.end());for(int x:d)assert(0<=x&&x<q);}
 vector<PairData>pairs(np);for(auto&x:pairs){in>>x.s>>x.t;assert(int(domains[x.s].size())==r+1&&int(domains[x.t].size())==r);vector<bool>S(q);for(int t:domains[x.s])S[t]=true;for(int shift=0;shift<q;++shift){bool ok=true;for(int t:domains[x.t])if(!S[(t+shift)%q]){ok=false;break;}if(ok)x.shifts.push_back(shift);}}
 map<tuple<int,int,int>,DomainData>cache;map<int,bool>primes;
 auto getdata=[&](int id,int zeta)->DomainData&{auto key=make_tuple(id,modp,zeta);auto it=cache.find(key);if(it!=cache.end())return it->second;DomainData d;d.modulus={1};for(int j:domains[id])d.modulus=times(d.modulus,{norm(-pw(zeta,j)),1});int n=domains[id].size();assert(int(d.modulus.size())==n+1&&d.modulus.back()==1);d.powers.assign(q,Poly(n));d.powers[0][0]=1;for(int h=1;h<q;++h){int lead=d.powers[h-1][n-1];d.powers[h][0]=norm(-mulm(lead,d.modulus[0]));for(int j=1;j<n;++j)d.powers[h][j]=norm((long long)d.powers[h-1][j-1]-mulm(lead,d.modulus[j]));}return cache.emplace(key,move(d)).first->second;};
 int passes=0,claimed=0;for(int row=0;row<nr;++row){int id,pairid,h,p,zeta,claim;in>>id>>pairid>>h>>p>>zeta>>claim;assert(in&&p>2&&p<2147483647&&0<=pairid&&pairid<np&&r<h&&h<q);modp=p;if(!primes.count(p))primes[p]=prime(p);assert(primes[p]&&pw(zeta,q)==1&&zeta!=1&&zeta>0&&zeta<p);for(int ell=2;ell<=q;++ell)if(q%ell==0&&prime(ell))assert(pw(zeta,q/ell)!=1);auto pair=pairs[pairid];const auto&S=getdata(pair.s,zeta);const auto&T=getdata(pair.t,zeta);const Poly&P=S.powers[h],&v=T.powers[h];int pivot=0;while(pivot<r&&!v[pivot])++pivot;assert(pivot<r);Poly H{1};for(int shift:pair.shifts)H=times(H,{norm(-pw(zeta,shift)),1});int bound=r-int(pair.shifts.size());assert(bound>=0);vector<Poly>E;int witness=-1;for(int j=0;j<r;++j){if(j==pivot)continue;Poly e(r+1);for(int k=0;k<=r;++k)e[k]=mulm(P[k],norm((long long)mulm(v[pivot],T.powers[k][j])-mulm(v[j],T.powers[k][pivot])));trim(e);auto quotient=divide(e,H);assert(quotient.second.empty());e=quotient.first;assert(int(e.size())<=bound+1);if(int(e.size())==bound+1)witness=j;E.push_back(e);}Poly g;for(const auto&e:E){g=gcd_cert(g,e);if(g.size()==1)break;}bool pass=witness>=0&&g.size()==1;if(claim){++claimed;assert(pass);}passes+=pass;out<<id<<' '<<pass<<' '<<witness<<' '<<bound<<' '<<int(g.size())-1<<' '<<pair.shifts.size()<<'\n';}
 cout<<"rows="<<nr<<" passes="<<passes<<" claimed="<<claimed<<" domains="<<nd<<" cached="<<cache.size()<<"\n";
}
