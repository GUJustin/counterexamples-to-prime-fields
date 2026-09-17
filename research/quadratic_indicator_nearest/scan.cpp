#include <algorithm>
#include <cassert>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>
int power(int a,int e,int p){int z=1;for(;e;e>>=1,a=a*a%p)if(e&1)z=z*a%p;return z;}
int main(int argc,char**argv){
 assert(argc==2);int p=std::stoi(argv[1]);assert(p==17||p==41);int k=(p-1)/4;
 std::vector<int>sq,ns;for(int x=1;x<p;x++)(power(x,2*k,p)==1?sq:ns).push_back(x);
 assert(sq.size()==2*k&&ns.size()==2*k);
 std::set<std::vector<int>>bank;std::vector<int>zero(k+1),one(k+1);one[0]=1;bank.insert(zero);bank.insert(one);
 std::vector<int>s(k);std::iota(s.begin(),s.end(),0);long long count=0;
 do{
  std::vector<int>H(1,1);for(int j:s){std::vector<int>a(H.size()+1);for(size_t t=0;t<H.size();t++){a[t]=(a[t]+(p-ns[j])*H[t])%p;a[t+1]=(a[t+1]+H[t])%p;}H=a;}
  std::vector<int>hist(p);for(int x:sq){int v=0;for(int j=k;j>=0;j--)v=(v*x+H[j])%p;hist[v]++;}assert(hist[0]==0);
  for(int v=1;v<p;v++)if(hist[v]>=k){assert(hist[v]==k);int c=power(v,p-2,p);auto P=H;for(int &a:P)a=a*c%p;bank.insert(P);}
  count++;int j=k-1;while(j>=0&&s[j]==k+j)j--;if(j<0)break;s[j]++;for(int t=j+1;t<k;t++)s[t]=s[t-1]+1;
 }while(true);
 std::cout<<"{\"p\":"<<p<<",\"length\":"<<p-1<<",\"dimension\":"<<k+1<<",\"maximum_agreement\":"<<2*k<<",\"root_subsets\":"<<count<<",\"bank_size\":"<<bank.size()<<",\"complete\":true,\"coefficients\":[";
 bool first=true;for(const auto&P:bank){std::cout<<(first?"":",")<<"[";first=false;for(size_t j=0;j<P.size();j++)std::cout<<(j?",":"")<<P[j];std::cout<<"]";}std::cout<<"]}\n";
}
