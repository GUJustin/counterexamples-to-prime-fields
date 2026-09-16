#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using U=uint64_t;
U p;
U mul(U a,U b){return a*b%p;}
U sub(U a,U b){return (a+p-b)%p;}
U power(U a,U e){U r=1;for(;e;e>>=1,a=mul(a,a))if(e&1)r=mul(r,a);return r;}
struct Point {U e1,e2;int i,j,k;};
int main(int argc,char**argv){
 assert(argc==3);p=std::stoull(argv[1]);int n=std::stoi(argv[2]);
 assert(n>=4 && (n&(n-1))==0 && (p-1)%n==0 && p<2147483648ULL);
 U gen=0;for(U a=2;!gen;++a){U g=power(a,(p-1)/n);if(power(g,n/2)!=1)gen=g;}
 std::vector<U>d(n);d[0]=1;for(int i=1;i<n;++i)d[i]=mul(d[i-1],gen);
 std::vector<U>keys;keys.reserve(U(n)*(n-1)*(n-2)/6);
 std::vector<Point>pts;
 for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)for(int k=j+1;k<n;++k){
  U e1=(d[i]+d[j]+d[k])%p;
  U e2=(mul(d[i],d[j])+mul((d[i]+d[j])%p,d[k]))%p;
  keys.push_back(e1*p+e2);
  if((i+j+k)%n==0)pts.push_back({e1,e2,i,j,k});
 }
 std::sort(keys.begin(),keys.end());std::map<int,U>hist;int polymax=0;U polykey=0;
 for(size_t i=0;i<keys.size();){size_t j=i+1;while(j<keys.size()&&keys[j]==keys[i])++j;
  int size=int(j-i);++hist[size];if(size>polymax){polymax=size;polykey=keys[i];}i=j;}
 std::vector<U>().swap(keys);
 std::sort(pts.begin(),pts.end(),[](const Point&a,const Point&b){return a.e1<b.e1 || (a.e1==b.e1&&a.e2<b.e2);});
 for(size_t i=1;i<pts.size();++i)assert(pts[i].e1!=pts[i-1].e1 || pts[i].e2!=pts[i-1].e2);
 int best=0,bestdegenerate=0;bool bestvertical=false;U bestslope=0,bestintercept=0;
 std::vector<int>ids;std::vector<U>prefix;std::vector<std::pair<U,int>>slopes;
 U pairs=0;
 for(int i=0;i<int(pts.size());++i){
  ids.clear();prefix.clear();slopes.clear();prefix.push_back(1);int vertical=1;
  for(int j=i+1;j<int(pts.size());++j){++pairs;U dx=sub(pts[j].e1,pts[i].e1);
   if(!dx){++vertical;continue;}ids.push_back(j);prefix.push_back(mul(prefix.back(),dx));}
  if(vertical>best){best=vertical;bestvertical=true;bestintercept=pts[i].e1;}
  U inv=power(prefix.back(),p-2);
  for(int a=int(ids.size())-1;a>=0;--a){int j=ids[a];U dx=sub(pts[j].e1,pts[i].e1);
   U invdx=mul(inv,prefix[a]);inv=mul(inv,dx);
   slopes.emplace_back(mul(sub(pts[j].e2,pts[i].e2),invdx),j);}
  std::sort(slopes.begin(),slopes.end());
  for(size_t a=0;a<slopes.size();){size_t b=a+1;while(b<slopes.size()&&slopes[b].first==slopes[a].first)++b;
   int size=1+int(b-a);U s=slopes[a].first;
   U val=sub((mul(mul(s,s),s)+mul(pts[i].e2,s))%p,(mul(pts[i].e1,mul(s,s))+1)%p);
   if(val==0)bestdegenerate=std::max(bestdegenerate,size);
   else if(size>best){best=size;bestvertical=false;bestslope=s;bestintercept=sub(pts[i].e2,mul(s,pts[i].e1));}
   a=b;
  }
 }
 std::cout<<"{\"p\":"<<p<<",\"n\":"<<n<<",\"generator\":"<<gen
 <<",\"polynomial_max_complete_fibers\":"<<polymax<<",\"polynomial_witness\":["<<polykey/p<<","<<polykey%p
 <<"],\"polynomial_fiber_histogram\":{";
 bool first=true;for(auto [a,b]:hist){if(!first)std::cout<<",";first=false;std::cout<<"\""<<a<<"\":"<<b;}
 std::cout<<"},\"constant_product_points\":"<<pts.size()<<",\"pairs_examined\":"<<pairs
 <<",\"constant_product_max_complete_fibers\":"<<best<<",\"maximum_degenerate_line_size\":"<<bestdegenerate
 <<",\"line_vertical\":"<<(bestvertical?"true":"false")<<",\"line_slope\":"<<bestslope
 <<",\"line_intercept\":"<<bestintercept<<",\"line_witness\":[";
 first=true;for(auto q:pts){bool on=bestvertical?q.e1==bestintercept:sub(q.e2,mul(bestslope,q.e1))==bestintercept;
  if(on){if(!first)std::cout<<",";first=false;std::cout<<"["<<q.i<<","<<q.j<<","<<q.k<<"]";}}
 std::cout<<"]}\n";
}
