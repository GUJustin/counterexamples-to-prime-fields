#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
using i64 = int64_t;
i64 power(i64 x,i64 e,i64 p){i64 v=1;for(;e;e>>=1,x=x*x%p)if(e&1)v=v*x%p;return v;}
i64 choose(int n,int k){i64 v=1;for(int j=1;j<=k;j++)v=v*(n-j+1)/j;return v;}
int main(int argc,char**argv){
 assert(argc==3 || argc==4);int r=std::stoi(argv[1]);i64 p=std::stoll(argv[2]);int n=4*r;
 bool puncture=argc==4;assert(!puncture || std::string(argv[3])=="three-cosets");
 assert(r>=1 && r<=10 && p>n && p<100000000 && (p-1)%n==0);
 for(i64 q=2;q*q<=p;q++)assert(p%q);
 i64 root=0;for(i64 g=2;g<p;g++){i64 x=power(g,(p-1)/n,p);bool ok=power(x,n,p)==1;
 for(int j=1;j<n;j++)if(n%j==0&&power(x,j,p)==1)ok=false;if(ok){root=x;break;}}
 assert(root);std::vector<i64>x(n);x[0]=1;
 for(int j=1;j<n;j++)x[j]=x[j-1]*root%p;
 if(puncture){x.erase(std::remove_if(x.begin(),x.end(),[&](i64 a){return power(a,r,p)==1;}),x.end());n=x.size();assert(n==3*r);}
 std::vector<i64>w(n);
 for(int j=0;j<n;j++)w[j]=((1+power(x[j],2*r,p))*((p+1)/2)-power(x[j],r,p)+p)%p;
 std::vector<std::vector<i64>> inv(n,std::vector<i64>(n));
 for(int a=0;a<n;a++)for(int b=0;b<n;b++)if(a!=b)inv[a][b]=power((x[a]-x[b]+p)%p,p-2,p);
 std::vector<int>s(r);for(int j=0;j<r;j++)s[j]=j;
 i64 subsets=0,best_subsets=0;int best=0;std::set<std::vector<i64>> maximizers;
 do{
  std::vector<i64> c(r);for(int j=0;j<r;j++)c[j]=w[s[j]];
  for(int j=1;j<r;j++)for(int i=r-1;i>=j;i--)c[i]=(c[i]-c[i-1]+p)*inv[s[i]][s[i-j]]%p;
  int agreements=0;for(int j=0;j<n;j++){i64 v=c[r-1];for(int i=r-2;i>=0;i--)v=(v*((x[j]-x[s[i]]+p)%p)+c[i])%p;agreements+=v==w[j];}
  subsets++;if(agreements>best){best=agreements;best_subsets=1;maximizers.clear();}else if(agreements==best)best_subsets++;
  if(puncture && agreements==best){std::vector<i64>a={c[r-1]};for(int i=r-2;i>=0;i--){std::vector<i64>b(a.size()+1);for(size_t j=0;j<a.size();j++){b[j]=(b[j]+(p-x[s[i]])*a[j])%p;b[j+1]=(b[j+1]+a[j])%p;}b[0]=(b[0]+c[i])%p;a=b;}maximizers.insert(a);}
  int i=r-1;while(i>=0&&s[i]==n-r+i)i--;if(i<0)break;s[i]++;for(int j=i+1;j<r;j++)s[j]=s[j-1]+1;
 }while(true);
 assert(subsets==choose(n,r));assert(best_subsets%choose(best,r)==0);
 std::cout<<"{\"r\":"<<r<<",\"p\":"<<p<<",\"n\":"<<n<<",\"primitive_root\":"<<root
 <<",\"interpolation_subsets\":"<<subsets<<",\"maximum_agreement\":"<<best
 <<",\"maximizing_polynomials\":"<<best_subsets/choose(best,r)<<",\"three_cosets\":"<<(puncture?"true":"false")<<",\"complete\":true";
 if(puncture){assert((i64)maximizers.size()==best_subsets/choose(best,r));auto array=[](const std::vector<i64>& a){std::cout<<"[";for(size_t j=0;j<a.size();j++){if(j)std::cout<<",";std::cout<<a[j];}std::cout<<"]";};std::cout<<",\"domain\":";array(x);std::cout<<",\"witnesses\":[";bool first=true;for(const auto&a:maximizers){if(!first)std::cout<<",";first=false;array(a);}std::cout<<"]";}
 std::cout<<"}\n";
}
