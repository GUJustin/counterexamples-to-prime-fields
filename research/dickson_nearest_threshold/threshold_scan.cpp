#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
int mul(int a,int b){return a*b%41;}
int power(int a,int e){int v=1;for(;e;e>>=1,a=mul(a,a))if(e&1)v=mul(v,a);return v;}
int main(int argc,char**argv){
 assert(argc==2);int coset=std::stoi(argv[1]);assert(coset>=0&&coset<4);
 int g=2;while(power(g,20)==1||power(g,8)==1)g++;assert(power(g,40)==1);
 std::array<int,40>x,w;for(int j=0;j<40;j++){x[j]=power(g,j);w[j]=((1+power(x[j],20))*21-power(x[j],10)+41)%41;}
 int val=w[coset];std::vector<int> masks;
 for(int m=0;m<1024;m++)if(__builtin_popcount((unsigned)m)==4){int lo=m,rot=m;for(int j=1;j<10;j++){rot=((rot<<1)&1023)|(rot>>9);lo=std::min(lo,rot);}if(lo==m)masks.push_back(m);}
 assert(masks.size()==22);
 uint64_t count=0;int observed=0;
 for(int mask:masks){
  std::vector<int> outside,extra;std::array<int,40>Z{};
  for(int j=0;j<40;j++){
   int z=1;for(int h=0;h<10;h++)if(mask>>h&1)z=mul(z,(x[j]-x[coset+4*h]+41)%41);Z[j]=z;
   if(j%4!=coset)outside.push_back(j);else if(z)extra.push_back(j);
  }
  assert(outside.size()==30&&extra.size()==6);
  std::array<int,30> y;int inv[30][30];
  for(int i=0;i<30;i++){
   y[i]=mul((w[outside[i]]-val+41)%41,power(Z[outside[i]],39));
   for(int j=0;j<30;j++)if(i!=j)inv[i][j]=power((x[outside[i]]-x[outside[j]]+41)%41,39);
  }
  std::array<int,6>s={0,1,2,3,4,5};
  do{
   int c[6];for(int j=0;j<6;j++)c[j]=y[s[j]];
   for(int h=1;h<6;h++)for(int j=5;j>=h;j--)c[j]=mul((c[j]-c[j-1]+41)%41,inv[s[j]][s[j-h]]);
   auto eval=[&](int xi){int v=c[5];for(int j=4;j>=0;j--)v=(mul(v,(xi-x[outside[s[j]]]+41)%41)+c[j])%41;return v;};
   int a=10;for(int j:extra)a+=(val+mul(Z[j],eval(x[j])))%41==w[j];
   int remaining=24;
   for(int j=0;j<30;j++){
    if(std::find(s.begin(),s.end(),j)!=s.end())continue;
    a+=eval(x[outside[j]])==y[j];remaining--;
    if(a+remaining<16)break;
   }
   count++;observed=std::max(observed,a);
   if(a>=16){
    std::cout<<"{\"p\":41,\"coset\":"<<coset<<",\"found\":true,\"agreements\":"<<a<<",\"values\":[";
    int truea=0;for(int j=0;j<40;j++){int v=(val+mul(Z[j],eval(x[j])))%41;truea+=v==w[j];std::cout<<(j?",":"")<<v;}assert(truea==a);
    std::cout<<"],\"primitive_root\":"<<g<<",\"supports_checked\":"<<count<<"}\n";return 0;
   }
   int j=5;while(j>=0&&s[j]==24+j)j--;if(j<0)break;s[j]++;for(int h=j+1;h<6;h++)s[h]=s[h-1]+1;
  }while(true);
 }
 assert(count==22ULL*593775);
 std::cout<<"{\"p\":41,\"coset\":"<<coset<<",\"found\":false,\"anchor_orbits\":22,\"supports_checked\":"<<count<<",\"primitive_root\":"<<g<<",\"complete\":true}\n";
}
