#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>

int modpow(int a,int e,int p){int r=1;while(e){if(e&1)r=r*a%p;a=a*a%p;e>>=1;}return r;}

int main(int argc,char**argv){
  assert(argc==2);int p=std::stoi(argv[1]);assert(p<=449 && (p-1)%32==0);
  int root=2;while(!(modpow(root,32,p)==1 && modpow(root,16,p)!=1))++root;
  int bits=0;while((1u<<bits)<unsigned(p))++bits;
  assert(7*bits<=63);
  std::array<std::array<int,7>,32> powers{};
  int x=1;
  for(int i=0;i<32;++i){int v=x;for(int j=0;j<7;++j){powers[i][j]=v;v=v*x%p;}x=x*root%p;}
  std::vector<uint64_t> keys;keys.reserve(10518300);
  std::array<int,7> sums{};
  auto visit=[&](auto&&self,int start,int left)->void{
    if(!left){uint64_t key=0;for(int j=0;j<7;++j)key=(key<<bits)|unsigned(sums[j]);keys.push_back(key);return;}
    for(int i=start;i<=32-left;++i){
      for(int j=0;j<7;++j){sums[j]+=powers[i][j];if(sums[j]>=p)sums[j]-=p;}
      self(self,i+1,left-1);
      for(int j=0;j<7;++j){sums[j]-=powers[i][j];if(sums[j]<0)sums[j]+=p;}
    }
  };
  visit(visit,0,8);assert(keys.size()==10518300);
  std::sort(keys.begin(),keys.end());
  std::cout<<"{\"p\":"<<p<<",\"root\":"<<root<<",\"subsets\":"<<keys.size()<<",\"rows\":[";
  for(int s=1;s<=7;++s){
    int shift=(7-s)*bits;uint64_t previous=keys[0]>>shift,best_key=previous;
    uint64_t run=0,best=0,zero=0,classes=0;
    auto flush=[&](){++classes;if(run>best){best=run;best_key=previous;}if(previous==0)zero=run;};
    for(uint64_t key:keys){uint64_t prefix=key>>shift;if(prefix!=previous){flush();run=0;previous=prefix;}++run;}
    flush();
    if(s>1)std::cout<<",";
    std::cout<<"{\"s\":"<<s<<",\"maximum_list\":"<<best<<",\"zero_moment_list\":"<<zero<<",\"classes\":"<<classes<<",\"maximizing_moments\":[";
    for(int j=0;j<s;++j){if(j)std::cout<<",";std::cout<<((best_key>>((s-1-j)*bits))&((1u<<bits)-1));}
    std::cout<<"]}";
  }
  std::cout<<"]}\n";
}
