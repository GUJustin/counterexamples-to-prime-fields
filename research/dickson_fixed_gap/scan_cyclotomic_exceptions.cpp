#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using ll=long long;
int power(int a,int e,int p){ll v=1,b=a;while(e){if(e&1)v=v*b%p;b=b*b%p;e>>=1;}return v;}
bool prime(int p){if(p<2)return false;for(int d=2;ll(d)*d<=p;d++)if(p%d==0)return false;return true;}
int generator(int p){std::vector<int>f;int n=p-1;for(int d=2;ll(d)*d<=n;d++)if(n%d==0){f.push_back(d);while(n%d==0)n/=d;}if(n>1)f.push_back(n);for(int g=2;g<p;g++){bool ok=true;for(int d:f)if(power(g,(p-1)/d,p)==1)ok=false;if(ok)return g;}return 0;}
int ranker(const std::vector<std::vector<int>>& sets,int n,int k,int p,int z){
 std::vector<int>xs(n),iv(n),ivd(n);xs[0]=iv[0]=1;int zi=power(z,p-2,p);
 for(int j=1;j<n;j++){xs[j]=ll(xs[j-1])*z%p;iv[j]=ll(iv[j-1])*zi%p;ivd[j]=power((xs[j]+p-1)%p,p-2,p);}
 std::vector<std::vector<int>> inverse(n,std::vector<int>(n));
 for(int x=0;x<n;x++)for(int y=0;y<n;y++)if(x!=y)inverse[x][y]=ll(iv[y])*ivd[(x-y+n)%n]%p;
 std::vector<std::vector<int>> basis(n);int rank=0;
 for(const auto&S:sets){
  std::vector<int>den(k,1);
  for(int a=0;a<k;a++)for(int b=0;b<k;b++)if(a!=b)den[a]=ll(den[a])*inverse[S[a]][S[b]]%p;
  for(int i=k;i<(int)S.size();i++){
   int x=S[i];std::vector<int>row(n);row[x]=1;ll pr=1;
   for(int j=0;j<k;j++)pr=pr*(xs[x]-xs[S[j]]+p)%p;
   for(int j=0;j<k;j++)row[S[j]]=(p-pr*inverse[x][S[j]]%p*den[j]%p)%p;
   for(int col=0;col<n;col++)if(row[col]){
    int v=row[col];
    if(!basis[col].empty())for(int j=col;j<n;j++){ll t=(ll)row[j]-ll(v)*basis[col][j]%p;row[j]=(t+p)%p;}
    else{int inv=power(v,p-2,p);for(int j=col;j<n;j++)row[j]=ll(row[j])*inv%p;basis[col]=std::move(row);rank++;break;}
   }
   assert(rank<=n-k);if(rank==n-k)return rank;
  }
 }
 return rank;
}
int main(int argc,char**argv){assert(argc==2);std::ifstream in(argv[1]);int cases;in>>cases;std::cout<<"[";
 for(int ca=0;ca<cases;ca++){
  int seed,n,k,L,limit;in>>seed>>n>>k>>L>>limit;std::vector<std::vector<int>>sets(L);
  for(auto&S:sets){int t;in>>t;S.resize(t);for(auto&x:S)in>>x;}
  int primes=0,embeddings=0,native_hits=0;bool first=true;
  if(ca)std::cout<<",";
  std::cout<<"{\"seed_prime\":"<<seed<<",\"n\":"<<n<<",\"K\":"<<k<<",\"limit\":"<<limit<<",\"exceptions\":[";
  for(int p=n+1;p<=limit;p+=n)if(prime(p)){
   primes++;int z=power(generator(p),(p-1)/n,p);
   for(int a=1;a<n;a++)if(std::gcd(a,n)==1){
    embeddings++;int root=power(z,a,p);int r=ranker(sets,n,k,p,root);
    if(r<n-k){if(p==seed)native_hits++;if(!first)std::cout<<",";first=false;std::cout<<"{\"p\":"<<p<<",\"root\":"<<root<<",\"embedding\":"<<a<<",\"rank\":"<<r<<"}";}
   }
  }
  assert(native_hits>0);
  std::cout<<"],\"primes\":"<<primes<<",\"embeddings\":"<<embeddings<<",\"native_hits\":"<<native_hits<<"}";std::cout.flush();
 }
 std::cout<<"]\n";
}
