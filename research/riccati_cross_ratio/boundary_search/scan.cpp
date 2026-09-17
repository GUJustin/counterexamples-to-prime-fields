// Exact exploration of polynomial Riccati solution counts; no protocol code.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using Poly=std::vector<int>;
int p;
int mod(int a){a%=p;return a<0?a+p:a;}
int inv(int a){for(int b=1;b<p;b++)if(a*b%p==1)return b;assert(false);return 0;}
void trim(Poly& a){while(a.size()>1&&!a.back())a.pop_back();}
bool zero(const Poly&a){return a.size()==1&&a[0]==0;}
Poly sub(Poly a,const Poly&b){a.resize(std::max(a.size(),b.size()));for(size_t i=0;i<b.size();i++)a[i]=mod(a[i]-b[i]);trim(a);return a;}
Poly mul(const Poly&a,const Poly&b){Poly c(a.size()+b.size()-1);for(size_t i=0;i<a.size();i++)for(size_t j=0;j<b.size();j++)c[i+j]=(c[i+j]+a[i]*b[j])%p;trim(c);return c;}
Poly deriv(const Poly&a){Poly c(std::max(size_t(1),a.size()-1));for(size_t i=1;i<a.size();i++)c[i-1]=a[i]*i%p;trim(c);return c;}
Poly rem(Poly a,const Poly&b){int v=inv(b.back());while(!zero(a)&&a.size()>=b.size()){int q=a.back()*v%p;size_t s=a.size()-b.size();for(size_t i=0;i<b.size();i++)a[i+s]=mod(a[i+s]-q*b[i]);trim(a);}return a;}
Poly gcd(Poly a,Poly b){while(!zero(b)){Poly r=rem(a,b);a=b;b=r;}int v=inv(a.back());for(auto&x:a)x=x*v%p;return a;}
Poly divide(Poly a,const Poly&b){Poly q(std::max(size_t(1),a.size()-b.size()+1));int v=inv(b.back());while(!zero(a)&&a.size()>=b.size()){size_t s=a.size()-b.size();int z=a.back()*v%p;q[s]=z;for(size_t i=0;i<b.size();i++)a[i+s]=mod(a[i+s]-z*b[i]);trim(a);}assert(zero(a));trim(q);return q;}
std::string ratio(Poly a,Poly b){Poly g=gcd(a,b);a=divide(a,g);b=divide(b,g);int v=inv(b.back());std::string key;key.push_back(char(a.size()));for(int x:a)key.push_back(char(x*v%p));key.push_back(char(b.size()));for(int x:b)key.push_back(char(x*v%p));return key;}
Poly decode(int z,int D){Poly a(D+1);for(auto&x:a){x=z%p;z/=p;}trim(a);return a;}
void print(const Poly&a){std::cout<<'[';for(size_t i=0;i<a.size();i++){if(i)std::cout<<',';std::cout<<a[i];}std::cout<<']';}
int main(int argc,char**argv){
 assert(argc==3);p=std::stoi(argv[1]);int D=std::stoi(argv[2]);assert(p>D&&D>=1);
 int q=1;for(int j=0;j<=D;j++)q*=p;
 std::vector<Poly> polynomials,derivatives;
 for(int z=0;z<q;z++){polynomials.push_back(decode(z,D));derivatives.push_back(deriv(polynomials.back()));}
 int best=0,centers=0;long long examined=0;Poly bestU;std::vector<int> bestV;
 auto started=std::chrono::steady_clock::now();
 for(int u=1;u<q;u++){
  const Poly&U=polynomials[u];if(U.back()!=1)continue;centers++;
  std::unordered_map<std::string,std::vector<int>> groups;
  for(int v=1;v<q;v++){
   if(u==v)continue;const Poly&V=polynomials[v];examined++;
   Poly N=sub(mul(derivatives[v],U),mul(derivatives[u],V));if(zero(N))continue;
   Poly denominator=mul(mul(U,V),sub(V,U));
   auto&bucket=groups[ratio(N,denominator)];bucket.push_back(v);
   if(int(bucket.size())+2>best){best=int(bucket.size())+2;bestU=U;bestV=bucket;}
  }
  if(centers%100==0)std::cerr<<"centers "<<centers<<" maximum "<<best<<'\n';
 }
 std::cout<<"{\"p\":"<<p<<",\"D\":"<<D<<",\"complete\":true,\"monic_centers\":"<<centers<<",\"pairs_examined\":"<<examined<<",\"maximum_solutions\":"<<best<<",\"witness\":[[0],";print(bestU);for(int v:bestV){std::cout<<',';print(polynomials[v]);}std::cout<<"],\"seconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count()<<"}\n";
}
