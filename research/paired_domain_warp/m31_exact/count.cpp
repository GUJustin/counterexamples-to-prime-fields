// Exact subset-product image count; pure coding-theory certificate.
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <chrono>
static constexpr uint32_t P=2147483647;
static uint32_t mul(uint32_t a,uint32_t b){uint64_t z=uint64_t(a)*b;uint64_t t=(z&P)+(z>>31);return t>=P?t-P:t;}
static uint64_t state=0x7072696d65706731ULL;
static uint64_t next(){state+=0x9e3779b97f4a7c15ULL;uint64_t z=state;z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;return z^(z>>31);}
int main(int argc,char **argv){
 int m=argc>1?std::atoi(argv[1]):30,D=argc>2?std::atoi(argv[2]):16;assert(m>=4 && m<=38 && D>0 && D<m);
 auto start=std::chrono::steady_clock::now();
 std::vector<uint32_t>a(m),v(m);
 for(int i=0;i<m;i++){
  while(true){uint32_t x=2+next()%((P-1)/2-1);bool used=false;for(int j=0;j<i;j++)if(a[j]==x)used=true;if(!used){a[i]=x;break;}}
  uint32_t sq=mul(a[i],a[i]);v[i]=sq<=1?1-sq:P+1-sq;assert(v[i]!=0);
 }
 int l=m/2,h=m-l;std::vector<std::vector<uint32_t>>left(l+1),right(h+1);
 for(int half=0;half<2;half++){
  auto &groups=half?right:left;int size=half?h:l,offset=half?l:0;std::vector<uint32_t>vals(1<<size,1);
  for(uint32_t mask=0;mask<(1u<<size);mask++){
   if(mask){uint32_t bit=__builtin_ctz(mask);vals[mask]=mul(vals[mask&(mask-1)],v[offset+bit]);}
   groups[__builtin_popcount(mask)].push_back(vals[mask]);
  }
 }
 std::vector<uint64_t>bits((uint64_t(P)+63)/64,0);uint64_t supports=0;
 for(int k=0;k<=l;k++){
  int j=D-k;if(j<0 || j>h)continue;
  for(uint32_t x:left[k])for(uint32_t y:right[j]){uint32_t z=mul(x,y);bits[z>>6]|=uint64_t(1)<<(z&63);supports++;}
 }
 uint64_t count=0,hash=1469598103934665603ULL;
 for(uint64_t word:bits){count+=__builtin_popcountll(word);hash=(hash^word)*1099511628211ULL;}
 assert(!(bits[0]&1));
 double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
 printf("{\"p\":%u,\"n\":%d,\"K\":%d,\"D\":%d,\"supports\":%llu,\"distinct_products\":%llu,\"bitmap_word_fingerprint\":\"%016llx\",\"seconds\":%.6f,\"core_representatives\":[",P,2*(m+1),2*D-1,D,(unsigned long long)supports,(unsigned long long)count,(unsigned long long)hash,seconds);
 for(int i=0;i<m;i++)printf("%s%u",i?",":"",a[i]);puts("]}");
}
