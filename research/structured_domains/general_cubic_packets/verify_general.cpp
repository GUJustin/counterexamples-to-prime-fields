#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>
using U=uint64_t;
U p;
U mul(U a,U b){return a*b%p;}
U sub(U a,U b){return a>=b?a-b:a+p-b;}
U power(U a,U e){U r=1;for(;e;e>>=1,a=mul(a,a))if(e&1)r=mul(r,a);return r;}
U key(U a,U b){return (a<<32)|b;}
U hash64(U x){x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;return x^(x>>31);}
struct Point{uint32_t e1,e2;int i,j,k;};
struct Pair{uint32_t a,b;};
struct Slot{U key=0;uint32_t stamp=0;uint8_t flag=0;};
int main(int argc,char**argv){
 assert(argc==4 || argc==6);p=std::stoull(argv[1]);int n=std::stoi(argv[2]),bucket=std::stoi(argv[3]);
 assert(n>=8&&(n&(n-1))==0&&bucket>=4&&(bucket&(bucket-1))==0&&n%bucket==0&&(p-1)%n==0&&p<2147483648ULL);
 U gen=0;for(U a=2;!gen;++a){U g=power(a,(p-1)/n);if(power(g,n/2)!=1)gen=g;}
 std::vector<U>d(n);d[0]=1;for(int i=1;i<n;++i)d[i]=mul(d[i-1],gen);
 int inv3=1;while((3*inv3)%n!=1)++inv3;
 std::vector<Point>base;
 for(int i=0;i<n;++i)for(int j=i+1;j<n;++j){int k=(2*n-i-j)%n;if(k<=j)continue;
  U e1=(d[i]+d[j]+d[k])%p,e2=(mul(d[i],d[j])+mul((d[i]+d[j])%p,d[k]))%p;
  base.push_back({uint32_t(e1),uint32_t(e2),i,j,k});}
 assert(base.size()==U(n-1)*(n-2)/6);
 std::unordered_map<U,int>lookup;lookup.reserve(base.size()*2);
 for(int i=0;i<int(base.size());++i)assert(lookup.emplace(key(base[i].e1,base[i].e2),i).second);
 struct Level{U inverse;std::vector<Pair>points;};
 std::vector<Level>levels;
 for(int j=1;j<bucket;++j){int exponent=j*n/bucket;U scale=d[(exponent*inv3)%n];U inv=power(sub(d[exponent],1),p-2);
  U f1=mul(scale,inv),f2=mul(mul(scale,scale),inv);Level level;level.inverse=inv;
  for(auto a:base)level.points.push_back({uint32_t(mul(a.e1,f1)),uint32_t(mul(a.e2,f2))});levels.push_back(std::move(level));}
 size_t capacity=1;while(capacity<2*base.size()*(bucket-1))capacity<<=1;std::vector<Slot>slots(capacity);
 std::vector<U>unscale(n),unscale2(n);for(int e=0;e<n;++e){int j=(e*inv3)%n;unscale[e]=d[(n-j)%n];unscale2[e]=mul(unscale[e],unscale[e]);}
 int best=0,bestanchor=-1;U bests1=0,bests2=0,candidate_lines=0,degenerate_lines=0,pairs=0;
 auto degenerate=[&](const Point&a,U s1,U s2){for(int i:{a.i,a.j,a.k})if((mul(s1,mul(d[i],d[i]))+1)%p==mul(s2,d[i]))return true;return false;};
 auto count=[&](int index,U s1,U s2){auto a=base[index];int count=0;for(int e=0;e<n;++e){U delta=sub(d[e],1);
   U a1=(a.e1+mul(s1,delta))%p,a2=(a.e2+mul(s2,delta))%p;
   count+=lookup.count(key(mul(a1,unscale[e]),mul(a2,unscale2[e])));}
  if(count>best){best=count;bestanchor=index;bests1=s1;bests2=s2;}return count;};
 int start=argc==6?std::stoi(argv[4]):0,end=argc==6?std::stoi(argv[5]):int(base.size());assert(start>=0&&end<=int(base.size())&&start<end);
 auto began=std::chrono::steady_clock::now();
 for(int i=start;i<end;++i){auto a=base[i];uint32_t stamp=i+1;
  for(const auto&level:levels){U offset1=mul(a.e1,level.inverse),offset2=mul(a.e2,level.inverse);
   for(auto q:level.points){++pairs;U s1=sub(q.a,offset1),s2=sub(q.b,offset2),k=key(s1,s2);size_t at=hash64(k)&(capacity-1);
    while(slots[at].stamp==stamp&&slots[at].key!=k)at=(at+1)&(capacity-1);
    auto &slot=slots[at];if(slot.stamp!=stamp){slot.stamp=stamp;slot.key=k;slot.flag=1;
     if(best==0&&!degenerate(a,s1,s2))count(i,s1,s2);
    }else if(slot.flag==1){if(degenerate(a,s1,s2)){slot.flag=2;++degenerate_lines;}
     else{slot.flag=3;++candidate_lines;assert(count(i,s1,s2)>=3);}}
   }
  }
  if((i+1)%512==0){double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-began).count();
   std::cerr<<"anchors "<<i+1<<"/"<<end<<", nondegenerate candidates "<<candidate_lines<<", best "<<best<<", seconds "<<seconds<<"\n";}
 }
 bool complete=start==0&&end==int(base.size());
 std::cout<<"{\"p\":"<<p<<",\"n\":"<<n<<",\"bucket_size\":"<<bucket<<",\"generator\":"<<gen
 <<",\"normalized_triples\":"<<base.size()<<",\"anchor_start\":"<<start<<",\"anchor_end\":"<<end
 <<",\"complete_scan\":"<<(complete?"true":"false")<<",\"pairs_examined\":"<<pairs
 <<",\"nondegenerate_candidates\":"<<candidate_lines<<",\"degenerate_candidates\":"<<degenerate_lines
 <<",\"maximum_examined_full_fibers\":"<<best<<",\"nonconstant_product_upper_bound\":"<<std::max(2*n/bucket,best)
 <<",\"hash_capacity\":"<<capacity<<",\"witness_anchor\":["<<base[bestanchor].e1<<","<<base[bestanchor].e2
 <<"],\"witness_slopes\":["<<bests1<<","<<bests2<<"]}\n";
}
