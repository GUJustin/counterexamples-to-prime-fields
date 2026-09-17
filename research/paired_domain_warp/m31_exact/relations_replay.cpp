// Independent iterative ternary expansion with ordinary modular arithmetic.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <iterator>
#include <vector>
#include <chrono>
static constexpr uint64_t P=2147483647;
static uint64_t power(uint64_t x,uint64_t e){uint64_t y=1;while(e){if(e&1)y=y*x%P;x=x*x%P;e>>=1;}return y;}
static std::vector<uint64_t>build(const std::vector<uint64_t>&a,int start,int end){
 std::vector<uint64_t>v;v.reserve(14348907);v.push_back(1);
 for(int i=end-1;i>=start;i--){
  uint64_t r=(P+1-a[i])*power(1+a[i],P-2)%P,s=power(r,P-2);assert(r*s%P==1);
  size_t old=v.size();v.resize(3*old);
  for(size_t j=0;j<old;j++){
   uint64_t x=v[j]>>31,y=v[j]&P;
   v[old+j]=(((x+a[i])%P)<<31)|(y*r%P);
   v[2*old+j]=(((x+P-a[i])%P)<<31)|(y*s%P);
  }
 }
 assert(v.size()==14348907);std::sort(v.begin(),v.end());return v;
}
int main(){
 auto begin=std::chrono::steady_clock::now();std::vector<uint64_t>a(30);
 for(auto &x:a){std::cin>>x;assert(std::cin && x>1 && x<=(P-1)/2);}
 auto L=build(a,0,15),R=build(a,15,30);std::vector<uint64_t>intersection;
 std::set_intersection(L.begin(),L.end(),R.begin(),R.end(),std::back_inserter(intersection));
 bool ok=intersection.size()==1 && intersection[0]==1 && std::count(L.begin(),L.end(),1)==1 && std::count(R.begin(),R.end(),1)==1;
 assert(ok);
 printf("{\"status\":\"passed\",\"only_trivial_relation\":true,\"half_assignments\":14348907,\"seconds\":%.6f}\n",std::chrono::duration<double>(std::chrono::steady_clock::now()-begin).count());
}
