#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <set>
#include <vector>

using namespace std;using V=vector<int>;int p;
int norm(long long a){a%=p;return a<0?a+p:a;}int powm(int a,int n){int b=1;while(n){if(n&1)b=(long long)b*a%p;a=(long long)a*a%p;n>>=1;}return b;}void cut(V&a){while(a.size()&&!a.back())a.pop_back();}
V rem(V a,const V&b){int inv=powm(b.back(),p-2);for(int k=(int)a.size()-(int)b.size();k>=0;--k){int c=(long long)a[k+b.size()-1]*inv%p;for(int j=0;j<(int)b.size();++j)a[k+j]=norm(a[k+j]-(long long)c*b[j]);}cut(a);return a;}
V quotient(V a,const V&b){V out(max(0,(int)a.size()-(int)b.size()+1));for(int k=(int)out.size()-1;k>=0;--k){int c=a[k+b.size()-1];out[k]=c;for(int j=0;j<(int)b.size();++j)a[k+j]=norm(a[k+j]-(long long)c*b[j]);}cut(a);assert(a.empty());cut(out);return out;}
V gcdp(V a,V b){while(b.size()){V c=rem(a,b);a=b;b=c;}return a;}
V mulroot(V a,int x){V b(a.size()+1);for(int j=0;j<(int)a.size();++j){b[j]=norm(b[j]-(long long)x*a[j]);b[j+1]=norm(b[j+1]+a[j]);}return b;}
struct Data{V poly;vector<V> powers;};struct Pair{int s,t,sc,rt;V shifts;};
int main(int argc,char**argv){ifstream in(argv[1]);ofstream out(argv[2]);int q,nd,np;in>>q>>nd>>np;int r=(q-1)/2;vector<V> dom(nd);for(auto&d:dom){int n;in>>n;d.resize(n);for(int&x:d)in>>x;}vector<Pair> pairs(np);for(auto&a:pairs){in>>a.s>>a.t>>a.sc>>a.rt;set<int>S(dom[a.s].begin(),dom[a.s].end());for(int b=0;b<q;++b){bool good=true;for(int t:dom[a.t])if(!S.count((t+b)%q)){good=false;break;}if(good)a.shifts.push_back(b);}}
 vector<int> primes;for(int n=q+1;primes.size()<4;n+=q){bool prime=n>1;for(int d=2;d*d<=n;++d)if(n%d==0){prime=false;break;}if(prime)primes.push_back(n);}vector<vector<bool>>done(np,vector<bool>(q));int count=0;for(int prime:primes){p=prime;int z=2;while(true){bool full=powm(z,q)==1;for(int d=1;d<q;++d)if(q%d==0&&powm(z,d)==1)full=false;if(full)break;++z;}vector<Data> data(nd);for(int i=0;i<nd;++i){auto&d=data[i];d.poly={1};for(int x:dom[i])d.poly=mulroot(d.poly,powm(z,x));int n=dom[i].size();d.powers.resize(q);d.powers[0]={1};for(int h=1;h<q;++h){V x=d.powers[h-1];x.insert(x.begin(),0);d.powers[h]=rem(x,d.poly);}for(auto&x:d.powers)x.resize(n);}
 for(int id=0;id<np;++id){auto&a=pairs[id];auto&S=data[a.s];auto&T=data[a.t];V H{1};for(int sh:a.shifts)H=mulroot(H,powm(z,sh));int bound=r-(int)a.shifts.size();for(int h=r+1;h<q;++h){if(done[id][h])continue;auto&P=S.powers[h];auto&v=T.powers[h];int pivot=0;while(pivot<r&&!v[pivot])++pivot;assert(pivot<r);V g;bool degree=false;for(int j=0;j<r;++j){if(j==pivot)continue;V e(r+1);e[j]=norm(e[j]+(long long)v[pivot]*P[j]);e[pivot]=norm(e[pivot]-(long long)v[j]*P[pivot]);e[r]=norm((long long)P[r]*((long long)v[j]*T.poly[pivot]-(long long)v[pivot]*T.poly[j]));cut(e);e=quotient(e,H);if((int)e.size()==bound+1)degree=true;if(g.size()!=1)g=gcdp(g,e);if(degree&&g.size()==1)break;}
 bool pass=degree&&g.size()==1;if(pass){done[id][h]=true;++count;}if(pass||prime==primes.back())out<<"{\"source_class\":"<<a.sc<<",\"relative_target\":"<<a.rt<<",\"pair_id\":"<<id<<",\"h\":"<<h<<",\"p\":"<<p<<",\"zeta\":"<<z<<",\"accepted\":"<<(pass?"true":"false")<<"}\n";
 }}cerr<<"prime "<<p<<" accepted "<<count<<" / "<<np*(q-r-1)<<"\n";}
}
