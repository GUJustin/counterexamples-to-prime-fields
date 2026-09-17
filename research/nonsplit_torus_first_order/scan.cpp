#include <algorithm>
#include <cassert>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
int power(int a,int e,int p){int z=1;for(;e;e>>=1,a=a*a%p)if(e&1)z=z*a%p;return z;}
int main(int argc,char**argv){
 assert(argc==4);int p=std::stoi(argv[1]),D=std::stoi(argv[2]),smax=std::stoi(argv[3]);
 assert(p<256&&D>0&&D%2==0&&D<p&&smax<=D);int n=p+1,m=n/2;
 int nu=2;while(power(nu,(p-1)/2,p)!=p-1)nu++;
 std::vector<int>perm(n),order;int ga=-1,gb=-1;
 for(int a=0;a<p&&ga<0;a++)for(int b=1;b<p;b++)if((a*a-nu*b*b%p+p*p)%p==1){
  for(int x=0;x<=p;x++){
   int u=x==p?a:(a*x+nu*b)%p,v=x==p?b:(b*x+a)%p;
   perm[x]=v?u*power(v,p-2,p)%p:p;
  }
  int len=1,x=perm[0];while(x!=0&&len<=n){x=perm[x];len++;}
  if(len==m){ga=a;gb=b;break;}
 }
 assert(ga>=0);std::vector<int>seen(n);
 for(int start=0;start<n;start++)if(!seen[start]){int x=start,ct=0;do{assert(!seen[x]);seen[x]=1;order.push_back(x);x=perm[x];ct++;}while(x!=start);assert(ct==m);}
 assert(order.size()==n);
 std::vector<std::vector<int>>basis(D,std::vector<int>(n));
 for(int i=0;i<n;i++)if(order[i]!=p){int x=order[i],q=(x*x-nu+p)%p;assert(q);int z=power(power(q,D/2,p),p-2,p);for(int j=0;j<D;j++){basis[j][i]=z;z=z*x%p;}}
 std::vector<int>div;for(int d=1;d<=m;d++)if(m%d==0)div.push_back(d);
 struct Row{long long count=0,above=0;int best=-1;std::vector<int>coeff;};std::map<int,Row>rows;
 std::vector<int>exps,cs,values(n);long long total=0;
 auto test=[&](){
  int M=0;
  for(int c=0;c<2;c++){int hist[256]={},mx=0;for(int t=0;t<m;t++){int i=c*m+t,v=0;for(size_t j=0;j<exps.size();j++)v+=cs[j]*basis[exps[j]][i];v%=p;values[i]=v;mx=std::max(mx,++hist[v]);}M+=mx;}
  int L=m;for(int d:div){bool ok=true;for(int c=0;c<2&&ok;c++)for(int t=d;t<m;t++)if(values[c*m+t]!=values[c*m+t%d]){ok=false;break;}if(ok){L=d;break;}}
  auto&r=rows[L];r.count++;total++;long long F=1LL*(8*n-D-1)*M*M-6LL*(D+1)*M*n+1LL*(D+1)*(4*(D+1)-5*n)*n;if(F>0)r.above++;
  if(M>r.best){r.best=M;r.coeff.assign(D+1,0);for(size_t j=0;j<exps.size();j++)r.coeff[exps[j]]=cs[j];}
 };
 std::function<void(int)> coefficients=[&](int at){if(at==int(cs.size())-1){cs[at]=1;test();return;}for(int c=1;c<p;c++){cs[at]=c;coefficients(at+1);}};
 std::function<void(int,int)> supports=[&](int next,int remaining){if(!remaining){cs.resize(exps.size());coefficients(0);return;}for(int j=next;j<=D-remaining;j++){exps.push_back(j);supports(j+1,remaining-1);exps.pop_back();}};
 for(int s=1;s<=smax;s++)supports(0,s);
 std::cout<<"{\"p\":"<<p<<",\"D\":"<<D<<",\"length\":"<<n<<",\"dimension\":"<<D+1<<",\"nu\":"<<nu<<",\"torus_a\":"<<ga<<",\"torus_b\":"<<gb<<",\"max_terms\":"<<smax<<",\"cases\":"<<total<<",\"rows\":[";
 bool first=true;for(auto&[L,r]:rows){std::cout<<(first?"":",")<<"{\"orbit\":"<<L<<",\"count\":"<<r.count<<",\"above_curve\":"<<r.above<<",\"maximum_agreement\":"<<r.best<<",\"coefficients\":[";first=false;for(size_t j=0;j<r.coeff.size();j++)std::cout<<(j?",":"")<<r.coeff[j];std::cout<<"]}";}std::cout<<"]}\n";
}
