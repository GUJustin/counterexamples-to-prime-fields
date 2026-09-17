// Independent enumeration: complementary supports, inverse factors,
// recursive traversal, ordinary modular reduction, and 32-bit bitmap words.
#include <array>
#include <cstdlib>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <vector>
#include <chrono>
static constexpr uint64_t P=2147483647;
static std::array<uint64_t,38>inv;
static int m=30,D=16;
static std::vector<uint32_t>bits;
static uint64_t supports=0,distinct=0;
static uint64_t power(uint64_t x,uint64_t e){uint64_t a=1;while(e){if(e&1)a=a*x%P;x=x*x%P;e>>=1;}return a;}
static void visit(int from,int need,uint64_t value){
 if(!need){uint32_t mask=uint32_t(1)<<(value%32);uint32_t &w=bits[value/32];if(!(w&mask)){w|=mask;distinct++;}supports++;return;}
 for(int i=from;i<=m-need;i++)visit(i+1,need-1,value*inv[i]%P);
}
int main(int argc,char **argv){
 if(argc>1)m=std::atoi(argv[1]);if(argc>2)D=std::atoi(argv[2]);assert(m>=4 && m<=38 && D>0 && D<m);
 auto start=std::chrono::steady_clock::now();uint64_t total=1;std::array<uint64_t,38>a;
 for(int i=0;i<m;i++){std::cin>>a[i];assert(std::cin && a[i]>1 && a[i]<=(P-1)/2);for(int j=0;j<i;j++)assert(a[i]!=a[j]);uint64_t v=(P+1-a[i]*a[i]%P)%P;assert(v);total=total*v%P;inv[i]=power(v,P-2);assert(inv[i]*v%P==1);}
 bits.resize((P+31)/32);visit(0,m-D,total);
 uint64_t pop=0,hash=1469598103934665603ULL;
 for(size_t i=0;i<bits.size();i+=2){uint64_t word=bits[i];if(i+1<bits.size())word|=uint64_t(bits[i+1])<<32;pop+=__builtin_popcountll(word);hash=(hash^word)*1099511628211ULL;}
 assert(pop==distinct && !(bits[0]&1));
 double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
 printf("{\"supports\":%llu,\"distinct_products\":%llu,\"bitmap_word_fingerprint\":\"%016llx\",\"seconds\":%.6f}\n",(unsigned long long)supports,(unsigned long long)distinct,(unsigned long long)hash,seconds);
}
