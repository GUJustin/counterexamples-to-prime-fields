// Independent complementary-support histogram, sixteen 16-bit-counter passes.
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <vector>
#include <chrono>
static constexpr uint64_t P=2147483647;
static std::array<uint64_t,30>inv;
static std::vector<uint16_t>count;
static uint32_t bucket;
static uint64_t visited;
static uint64_t power(uint64_t x,uint64_t e){uint64_t y=1;while(e){if(e&1)y=y*x%P;x=x*x%P;e>>=1;}return y;}
static void visit(int from,int need,uint64_t value){
 if(!need){if((value>>27)==bucket){auto &x=count[value&((1u<<27)-1)];assert(x<65535);x++;visited++;}return;}
 for(int i=from;i<=30-need;i++)visit(i+1,need-1,value*inv[i]%P);
}
int main(){
 auto start=std::chrono::steady_clock::now();uint64_t totalprod=1;
 for(int i=0;i<30;i++){uint64_t a;std::cin>>a;assert(std::cin && a>1 && a<=(P-1)/2);uint64_t v=(P+1-a*a%P)%P;inv[i]=power(v,P-2);assert(inv[i]*v%P==1);totalprod=totalprod*v%P;}
 count.resize(1u<<27);std::array<uint64_t,65536>hist{};
 for(bucket=0;bucket<16;bucket++){
  std::fill(count.begin(),count.end(),0);visit(0,14,totalprod);
  uint32_t size=bucket==15?(1u<<27)-1:1u<<27;
  for(uint32_t i=0;i<size;i++)hist[count[i]]++;
 }
 uint64_t mass=0,total=0,near=0;int maximum=0;
 for(int i=0;i<65536;i++){total+=hist[i];mass+=uint64_t(i)*hist[i];if(i){near+=hist[i];if(hist[i])maximum=i;}}
 assert(total==P && mass==145422675 && visited==mass && near==140916078);
 printf("{\"supports\":%llu,\"nearby_parameters\":%llu,\"unique_parameters\":%llu,\"maximum_list_size_on_line\":%d,\"histogram_including_zero_parameter\":[",(unsigned long long)mass,(unsigned long long)near,(unsigned long long)hist[1],maximum);
 for(int i=0;i<=maximum;i++)printf("%s%llu",i?",":"",(unsigned long long)hist[i]);printf("],\"seconds\":%.6f}\n",std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count());
}
