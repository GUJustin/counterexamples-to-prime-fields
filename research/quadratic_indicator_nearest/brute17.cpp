#include <array>
#include <cassert>
#include <iostream>
int main(){
 constexpr int p=17,k=4,total=1419857;
 std::array<int,17>w{};for(int x=1;x<p;x++){int v=1;for(int j=0;j<8;j++)v=v*x%p;w[x]=(1+v)*9%p;}
 std::array<long long,17>hist{};int found=0;
 std::cout<<"{\"p\":17,\"degree_bound\":4,\"total\":"<<total<<",\"threshold\":7,\"coefficients\":[";
 for(int code=0;code<total;code++){
  std::array<int,5>c{};int z=code;for(int&v:c){v=z%p;z/=p;}assert(z==0);
  int a=0;for(int x=1;x<p;x++){int v=0;for(int j=k;j>=0;j--)v=(v*x+c[j])%p;a+=v==w[x];}hist[a]++;
  if(a>=7){std::cout<<(found++?",":"")<<"[";for(int j=0;j<=k;j++)std::cout<<(j?",":"")<<c[j];std::cout<<"]";}
 }
 std::cout<<"],\"histogram\":[";for(int j=0;j<=16;j++)std::cout<<(j?",":"")<<hist[j];std::cout<<"],\"bank_size\":"<<found<<"}\n";
 assert(found==6&&hist[7]==0&&hist[8]==6);
}
