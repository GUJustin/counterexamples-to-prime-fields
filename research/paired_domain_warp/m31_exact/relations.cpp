// Exhaustive ternary relation test in F_p(additive) x F_p^*.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <vector>
#include <chrono>
static constexpr uint32_t P=2147483647;
static std::array<uint32_t,30>a,R,S;
static uint32_t mul(uint32_t x,uint32_t y){uint64_t z=uint64_t(x)*y,t=(z&P)+(z>>31);return t>=P?t-P:t;}
static uint32_t power(uint32_t x,uint32_t e){uint32_t y=1;while(e){if(e&1)y=mul(y,x);x=mul(x,x);e>>=1;}return y;}
static void fill(int i,int end,uint32_t sum,uint32_t prod,std::vector<uint64_t>&out){
 if(i==end){out.push_back((uint64_t(sum)<<31)|prod);return;}
 fill(i+1,end,sum,prod,out);
 uint32_t plus=uint64_t(sum)+a[i]>=P?sum+a[i]-P:sum+a[i];
 uint32_t minus=sum>=a[i]?sum-a[i]:P-(a[i]-sum);
 fill(i+1,end,plus,mul(prod,R[i]),out);
 fill(i+1,end,minus,mul(prod,S[i]),out);
}
int main(){
 auto start=std::chrono::steady_clock::now();
 for(int i=0;i<30;i++){std::cin>>a[i];assert(std::cin && a[i]>1 && a[i]<=(P-1)/2);for(int j=0;j<i;j++)assert(a[i]!=a[j]);uint32_t num=P+1-a[i],den=1+a[i];R[i]=mul(num,power(den,P-2));S[i]=mul(den,power(num,P-2));assert(mul(R[i],S[i])==1);}
 std::vector<uint64_t>left,right;left.reserve(14348907);right.reserve(14348907);
 fill(0,15,0,1,left);fill(15,30,0,1,right);assert(left.size()==14348907 && right.size()==14348907);
 std::sort(left.begin(),left.end());std::sort(right.begin(),right.end());
 size_t i=0,j=0;uint64_t matches=0,nonempty=0,first=0;
 while(i<left.size() && j<right.size()){
  if(left[i]<right[j]){i++;continue;}if(left[i]>right[j]){j++;continue;}
  uint64_t key=left[i];size_t ni=i,nj=j;while(ni<left.size() && left[ni]==key)ni++;while(nj<right.size() && right[nj]==key)nj++;
  uint64_t count=uint64_t(ni-i)*(nj-j);matches+=count;uint64_t bad=count-(key==1?1:0);if(bad && !nonempty)first=key;nonempty+=bad;i=ni;j=nj;
 }
 double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
 printf("{\"half_assignments\":14348907,\"matching_pairs\":%llu,\"nonempty_zero_relations\":%llu,\"first_nonempty_key\":%llu,\"seconds\":%.6f}\n",(unsigned long long)matches,(unsigned long long)nonempty,(unsigned long long)first,seconds);
}
