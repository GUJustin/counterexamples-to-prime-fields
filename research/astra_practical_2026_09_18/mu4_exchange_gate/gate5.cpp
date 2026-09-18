#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
using U=uint64_t;
const U p=2130706433;
U power(U a,U b){U r=1;for(;b;b>>=1,a=a*a%p)if(b&1)r=r*a%p;return r;}
struct R{U key,mask;};
bool lifted(U a,U b){for(int j=0;j<32;j++)if(int(a>>j&1)-int(b>>j&1)!=int(a>>(j+32)&1)-int(b>>(j+32)&1))return false;return true;}
void array(U a){std::cout<<"[";bool comma=false;for(int i=1;i<64;i++)if(a>>i&1){if(comma)std::cout<<",";std::cout<<i;comma=true;}std::cout<<"]";}
int main(){U g=2;while(power(g,(p-1)/2)==1||power(g,(p-1)/127)==1)g++;U z=power(g,(p-1)/64),v[64];v[0]=1;for(int i=1;i<64;i++)v[i]=v[i-1]*z%p;
std::vector<R>r;r.reserve(7028847);for(int a=1;a<60;a++)for(int b=a+1;b<61;b++)for(int c=b+1;c<62;c++)for(int d=c+1;d<63;d++)for(int e=d+1;e<64;e++)r.push_back({(((v[a]+v[b]+v[c]+v[d]+v[e])%p)<<6)|U((a+b+c+d+e)%64),(U(1)<<a)|(U(1)<<b)|(U(1)<<c)|(U(1)<<d)|(U(1)<<e)});
std::sort(r.begin(),r.end(),[](R a,R b){return a.key<b.key;});U pairs=0,disjoint=0,fresh=0,allfresh=0,maxfiber=0,ex[2]={};
std::cout<<"{\"p\":"<<p<<",\"primitive_generator\":"<<g<<",\"tag_root\":"<<z<<",\"supports\":"<<r.size()<<",\"genuine_disjoint_examples\":[";bool comma=false;
for(size_t l=0;l<r.size();){size_t h=l+1;while(h<r.size()&&r[h].key==r[l].key)h++;maxfiber=std::max(maxfiber,U(h-l));for(size_t i=l;i<h;i++)for(size_t j=i+1;j<h;j++){pairs++;bool modular=!lifted(r[i].mask,r[j].mask);if(modular)allfresh++;if(!(r[i].mask&r[j].mask)){disjoint++;if(modular){fresh++;if(fresh<=1000){if(comma)std::cout<<",";std::cout<<"[";array(r[i].mask);std::cout<<",";array(r[j].mask);std::cout<<"]";comma=true;}}}}l=h;}
std::cout<<"],\"unordered_equal_signature_pairs\":"<<pairs<<",\"unordered_disjoint_pairs\":"<<disjoint<<",\"genuine_pairs\":"<<allfresh<<",\"genuine_disjoint_pairs\":"<<fresh<<",\"maximum_signature_fiber\":"<<maxfiber<<"}\n";}
