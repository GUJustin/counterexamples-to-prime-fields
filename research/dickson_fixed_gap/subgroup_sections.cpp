#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
using ll=long long;
ll power(ll a,int e,int p){ll v=1;while(e){if(e&1)v=v*a%p;a=a*a%p;e>>=1;}return v;}
bool prime(int p){if(p<2)return false;for(int d=2;ll(d)*d<=p;++d)if(p%d==0)return false;return true;}
int generator(int p){std::vector<int>f;int q=p-1;for(int d=2;ll(d)*d<=q;++d)if(q%d==0){f.push_back(d);while(q%d==0)q/=d;}if(q>1)f.push_back(q);for(int g=2;g<p;++g){bool good=true;for(int d:f)if(power(g,(p-1)/d,p)==1)good=false;if(good)return g;}return 0;}
struct Coset{int index,mode,value,word;};
int main(){
 std::cout<<"[";bool first=true;
 for(int k:{16,32,64,128})for(int r=2;r<=48;++r){
  int p=2*r*k+1;if(!prime(p))continue;int g=generator(p);
  for(int section=0;section<r;++section){
   int e=r*k+section;std::vector<int>inv(e+1),coeff(k+1);inv[1]=1;
   for(int j=2;j<=e;++j)inv[j]=p-ll(p/j)*inv[p%j]%p;
   ll bin=1;for(int j=0;j<=e;++j){if(j%r==section)coeff[(j-section)/r]=bin;if(j<e)bin=bin*(e-j)%p*inv[j+1]%p;}
   assert(coeff[k]==1 && coeff[1]!=0);
   std::vector<int>values(p);for(int x=1;x<p;++x){ll v=0;for(int j=k;j>=0;--j)v=(v*x+coeff[j])%p;values[x]=v;}
   for(int L=4;L<=k;L*=2){
    int cosets=(p-1)/L,h=power(g,cosets,p),start=1;
    std::vector<Coset>rows;std::vector<int>counts(p),touched;
    for(int c=0;c<cosets;++c){int x=start,best=0,vbest=0;
     for(int i=0;i<L;++i){int v=values[x];if(!counts[v])touched.push_back(v);++counts[v];if(counts[v]>best || (counts[v]==best && v<vbest)){best=counts[v];vbest=v;}x=ll(x)*h%p;}
     assert(x==start);rows.push_back({c,best,vbest,int((vbest-power(start,k,p)+p)%p)});
     for(int v:touched)counts[v]=0;touched.clear();start=ll(start)*g%p;
    }
    std::sort(rows.begin(),rows.end(),[](const Coset&a,const Coset&b){return a.mode!=b.mode?a.mode>b.mode:a.index<b.index;});
    if(!first)std::cout<<",";first=false;
    std::cout<<"{\"r\":"<<r<<",\"section\":"<<section<<",\"k\":"<<k<<",\"L\":"<<L<<",\"p\":"<<p<<",\"generator\":"<<g<<",\"agreements\":[";
    bool sep=false;for(int c:{4,8,16,32})if(c*k<=p-1){int A=0;for(int i=0;i<c*k/L;++i)A+=rows[i].mode;if(sep)std::cout<<",";sep=true;std::cout<<"["<<c<<","<<A<<"]";}
    std::cout<<"]}";
   }
  }
 }
 std::cout<<"]\n";
}
