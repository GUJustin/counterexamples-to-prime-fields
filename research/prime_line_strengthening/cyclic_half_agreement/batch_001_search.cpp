#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using I=long long;
int p;
int add(int a,int b){return (I(a)+b)%p;}
int mul(int a,int b){return I(a)*b%p;}
int pw(int a,int n){int b=1;for(;n;n>>=1,a=mul(a,a))if(n&1)b=mul(b,a);return b;}
int ev(const std::vector<int>&a,int x){int y=0;for(auto i=a.rbegin();i!=a.rend();++i)y=add(mul(y,x),*i);return y;}
int main(int argc,char**argv){
 if(argc<3)return 2;int q=std::atoi(argv[1]);p=std::atoi(argv[2]);int limit=argc>3?std::atoi(argv[3]):20;
 bool fixed=argc>4;std::vector<int>fixedS;if(fixed){std::stringstream ss(argv[4]);std::string s;while(std::getline(ss,s,','))fixedS.push_back(std::stoi(s));std::sort(fixedS.begin(),fixedS.end());}
 if(p<2||q<3||q>257||(!fixed&&q>23)||(q%2)==0||(p-1)%q)return 3;
 if(fixed&&((int)fixedS.size()!=(q+1)/2||fixedS.front()<0||fixedS.back()>=q||std::adjacent_find(fixedS.begin(),fixedS.end())!=fixedS.end()))return 6;
 for(int d=2;I(d)*d<=p;++d)if(p%d==0)return 4;
 for(int d=2;d*d<=q;++d)if(q%d==0)return 5;
 int z=1;for(int g=2;g<p&&z==1;++g)z=pw(g,(p-1)/q);
 std::vector<int> roots(q,1);for(int i=1;i<q;++i)roots[i]=mul(roots[i-1],z);
 std::vector<bool> seen(p);std::vector<int> reps;for(int a=1;a<p;++a)if(!seen[a]){reps.push_back(a);for(int x:roots)seen[mul(a,x)]=true;}
 int r=(q-1)/2,hits=0;uint32_t full=fixed?0:(uint32_t(1)<<q)-1;I supports=0,tests=0;
 auto start=std::chrono::steady_clock::now();bool stopped=false;
 for(uint32_t mask=0;mask<=full&&!stopped;++mask){
  std::vector<int>S=fixedS;
  if(!fixed){if(__builtin_popcount(mask)!=r+1)continue;
   uint32_t rot=mask;bool canonical=true;for(int j=1;j<q;++j){rot=((rot<<1)&full)|(rot>>(q-1));if(rot<mask){canonical=false;break;}}
   if(!canonical)continue;for(int j=0;j<q;++j)if(mask&(1u<<j))S.push_back(j);
  }++supports;
  std::vector<std::vector<int>>basis;
  for(int s:S){std::vector<int>b(1,1);int den=1;for(int t:S)if(t!=s){std::vector<int>c(b.size()+1);for(int j=0;j<(int)b.size();++j){c[j]=add(c[j],mul(b[j],p-roots[t]));c[j+1]=add(c[j+1],b[j]);}b=c;den=mul(den,add(roots[s],p-roots[t]));}int inv=pw(den,p-2);for(int&x:b)x=mul(x,inv);basis.push_back(b);}
  for(int h=r+1;h<q&&!stopped;++h){
   std::vector<int>P(r+1);for(int j=0;j<(int)S.size();++j)for(int d=0;d<=r;++d)P[d]=add(P[d],mul(roots[(h*S[j])%q],basis[j][d]));
   int first=0;for(int s=0;s<q;++s)first+=ev(P,roots[s])==roots[(h*s)%q];if(first!=r+1)continue;
   for(int a:reps){if(a==1)continue;++tests;std::vector<int>vals;for(int s=0;s<q;++s)vals.push_back(mul(ev(P,mul(a,roots[s])),roots[(q-(h*s)%q)%q]));auto sorted=vals;std::sort(sorted.begin(),sorted.end());
    for(int j=0;j<q;){int k=j+1;while(k<q&&sorted[k]==sorted[j])++k;if(k-j>=r){
     ++hits;std::cout<<"{\"q\":"<<q<<",\"p\":"<<p<<",\"zeta\":"<<z<<",\"h\":"<<h<<",\"mask\":"<<mask<<",\"alpha\":"<<a<<",\"value\":"<<sorted[j]<<",\"multiplicity\":"<<k-j<<",\"S\":[";for(int d=0;d<(int)S.size();++d)std::cout<<(d?",":"")<<S[d];std::cout<<"],\"P\":[";for(int d=0;d<=r;++d)std::cout<<(d?",":"")<<P[d];std::cout<<"]}\n";
     std::cout.flush();if(limit>0&&hits>=limit){stopped=true;break;}
    }j=k;}if(stopped)break;
   }
  }
 }
 std::cerr<<"{\"q\":"<<q<<",\"p\":"<<p<<",\"supports\":"<<supports<<",\"tests\":"<<tests<<",\"hits\":"<<hits<<",\"exhaustive\":"<<(stopped?"false":"true")<<",\"seconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"}\n";
}
