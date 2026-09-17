#include <algorithm>
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>
#include <map>
using ll=long long;
int power(int a,int e,int p){int v=1;for(;e;e>>=1,a=a*a%p)if(e&1)v=v*a%p;return v;}
struct Row{int best=-1;ll count=0,ties=0;std::vector<int> ex,coeff,mode,freq;};
int main(int argc,char**argv){
 assert(argc==2);int p=std::stoi(argv[1]);assert(p>5&&p<10000&&p%4==1);for(int j=2;j*j<=p;j++)assert(p%j);
 int n=p-1,k=n/4,g=2;for(;;g++){bool ok=true;for(int j=1;j<n;j++)if(n%j==0&&power(g,j,p)==1)ok=false;if(ok)break;}
 std::vector<int> xs(n);std::vector<std::vector<int>> pw(n,std::vector<int>(k));
 for(int j=0;j<n;j++){xs[j]=power(g,j,p);pw[j][0]=1;for(int e=1;e<k;e++)pw[j][e]=pw[j][e-1]*xs[j]%p;}
 std::map<int,Row> rows;ll total=0;
 auto inspect=[&](std::vector<int> ex,std::vector<int> coeff){
  int h=k;for(int e:ex)h=std::gcd(h,e);int orbit=k/h;
  std::vector<int> freq(4),mode(4),hist(p);int M=0;
  for(int c=0;c<4;c++){
   std::fill(hist.begin(),hist.end(),0);for(int j=c;j<n;j+=4){int v=0;for(size_t t=0;t<ex.size();t++)v+=coeff[t]*pw[j][ex[t]];v%=p;hist[v]++;}
   mode[c]=std::max_element(hist.begin(),hist.end())-hist.begin();freq[c]=hist[mode[c]];M+=freq[c];
  }
  auto &r=rows[orbit];r.count++;total++;
  if(M>r.best){r.best=M;r.ties=1;r.ex=ex;r.coeff=coeff;r.mode=mode;r.freq=freq;}else if(M==r.best)r.ties++;
 };
 for(int a=1;a<k;a++){
  inspect({a},{1});
  for(int b=a+1;b<k;b++)for(int ca=1;ca<p;ca++)inspect({a,b},{ca,1});
  for(int b=a+1;b<k;b++)for(int c=b+1;c<k;c++)for(int ca=1;ca<p;ca++)for(int cb=1;cb<p;cb++)inspect({a,b,c},{ca,cb,1});
 }
 auto arr=[](const std::vector<int>&v){std::cout<<"[";for(size_t i=0;i<v.size();i++)std::cout<<(i?",":"")<<v[i];std::cout<<"]";};
 std::cout<<"{\"p\":"<<p<<",\"n\":"<<n<<",\"k\":"<<k<<",\"primitive_root\":"<<g<<",\"polynomials\":"<<total<<",\"rows\":[";
 bool first=true;for(auto &[orbit,r]:rows){std::cout<<(first?"":",")<<"{\"orbit\":"<<orbit<<",\"maximum_agreement\":"<<r.best<<",\"above_quarter_rate_first_order_curve\":"<<((31LL*r.best*r.best-6LL*r.best*n-4LL*n*n>0)?"true":"false")<<",\"cases\":"<<r.count<<",\"ties\":"<<r.ties<<",\"exponents\":";arr(r.ex);std::cout<<",\"coefficients\":";arr(r.coeff);std::cout<<",\"coset_modes\":";arr(r.mode);std::cout<<",\"coset_frequencies\":";arr(r.freq);std::cout<<"}";first=false;}
 std::cout<<"],\"complete_for_at_most_three_nonconstant_terms\":true}\n";
}
