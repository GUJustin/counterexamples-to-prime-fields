// Exact product-fiber histogram with eight bounded-memory passes.
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <vector>
#include <chrono>
static constexpr uint32_t P=2147483647;
static uint32_t mul(uint32_t x,uint32_t y){uint64_t z=uint64_t(x)*y,t=(z&P)+(z>>31);return t>=P?t-P:t;}
int main(){
 auto start=std::chrono::steady_clock::now();std::array<uint32_t,30>v;
 for(int i=0;i<30;i++){uint64_t a;std::cin>>a;assert(std::cin && a>1 && a<=(P-1)/2);v[i]=(P+1-a*a%P)%P;assert(v[i]);}
 std::array<std::vector<uint32_t>,16>L,R;
 for(int half=0;half<2;half++){
  std::vector<uint32_t>value(1<<15,1);auto &out=half?R:L;
  for(unsigned mask=0;mask<(1u<<15);mask++){if(mask)value[mask]=mul(value[mask&(mask-1)],v[15*half+__builtin_ctz(mask)]);out[__builtin_popcount(mask)].push_back(value[mask]);}
 }
 constexpr uint32_t chunk=1u<<28;std::vector<uint8_t>counts(chunk);std::array<uint64_t,256>hist{};uint64_t scanned=0;
 for(uint32_t bucket=0;bucket<8;bucket++){
  std::fill(counts.begin(),counts.end(),0);uint32_t lo=bucket*chunk;
  for(int k=1;k<=15;k++)for(uint32_t x:L[k])for(uint32_t y:R[16-k]){
   uint32_t value=mul(x,y);if((value>>28)==bucket){uint8_t &c=counts[value-lo];assert(c<255);c++;scanned++;}
  }
  uint32_t size=bucket==7?chunk-1:chunk;
  for(uint32_t i=0;i<size;i++)hist[counts[i]]++;
 }
 assert(scanned==145422675);uint64_t total=0,mass=0,near=0;int maximum=0;
 for(int i=0;i<256;i++){total+=hist[i];mass+=uint64_t(i)*hist[i];if(i){near+=hist[i];if(hist[i])maximum=i;}}
 assert(total==P && mass==scanned && near==140916078);
 double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
 printf("{\"p\":%u,\"supports\":%llu,\"nearby_parameters\":%llu,\"unique_parameters\":%llu,\"maximum_list_size_on_line\":%d,\"histogram_including_zero_parameter\":[",P,(unsigned long long)mass,(unsigned long long)near,(unsigned long long)hist[1],maximum);
 for(int i=0;i<=maximum;i++)printf("%s%llu",i?",":"",(unsigned long long)hist[i]);printf("],\"seconds\":%.6f}\n",seconds);
}
