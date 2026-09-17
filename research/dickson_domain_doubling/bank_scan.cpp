#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <vector>
#include <set>
int A[289][289],M[289][289],N[289],I[289];
int power(int a,int e){int z=1;for(;e;e>>=1,a=M[a][a])if(e&1)z=M[z][a];return z;}
int sub(int a,int b){return A[a][N[b]];}
int main(){
 for(int a=0;a<289;a++){N[a]=(17-a%17)%17+17*((17-a/17)%17);for(int b=0;b<289;b++){A[a][b]=(a%17+b%17)%17+17*((a/17+b/17)%17);M[a][b]=(a%17*(b%17)+3*(a/17)*(b/17))%17+17*((a%17*(b/17)+(a/17)*(b%17))%17);}}
 for(int a=1;a<289;a++){I[a]=power(a,287);assert(M[a][I[a]]==1);}
 int g=0;for(int a=2;a<289;a++){int v=power(a,9);if(power(v,16)!=1&&power(v,32)==1){g=v;break;}}assert(g);
 std::array<int,32>x,w;for(int j=0;j<32;j++){x[j]=power(g,j);w[j]=sub(M[9][A[1][power(x[j],16)]],power(x[j],8));}
 int lower=0;for(int j=0;j<32;j++){int v=9;v=A[v][M[16][power(x[j],2)]];v=A[v][M[7][power(x[j],4)]];v=A[v][M[2][power(x[j],6)]];lower+=v==w[j];}assert(lower==12);
 std::vector<int>masks;for(int mask=0;mask<256;mask++)if(__builtin_popcount((unsigned)mask)==3){int z=mask,lo=mask;for(int i=1;i<8;i++){z=((z<<1)&255)|(z>>7);lo=std::min(lo,z);}if(lo==mask)masks.push_back(mask);}assert(masks.size()==7);
 long long count=0,hits=0;int best=12;std::set<std::array<int,32>> bank;
 for(int c0=0;c0<4;c0++)for(int mask:masks){
  int val=w[c0];std::array<int,32>Z;std::vector<int>out,extra;
  for(int j=0;j<32;j++){int z=1;for(int h=0;h<8;h++)if(mask>>h&1)z=M[z][sub(x[j],x[c0+4*h])];Z[j]=z;if(j%4!=c0)out.push_back(j);else if(z)extra.push_back(j);}
  assert(out.size()==24&&extra.size()==5);int y[24],inv[24][24];
  for(int i=0;i<24;i++){y[i]=M[sub(w[out[i]],val)][I[Z[out[i]]]];for(int j=0;j<24;j++)if(i!=j)inv[i][j]=I[sub(x[out[i]],x[out[j]])];}
  std::array<int,5>s={0,1,2,3,4};
  do{
   int q[5];for(int j=0;j<5;j++)q[j]=y[s[j]];
   for(int h=1;h<5;h++)for(int j=4;j>=h;j--)q[j]=M[sub(q[j],q[j-1])][inv[s[j]][s[j-h]]];
   auto eval=[&](int v){int z=q[4];for(int j=3;j>=0;j--)z=A[M[z][sub(v,x[out[s[j]]])]][q[j]];return z;};
   int agreement=8;for(int j:extra)agreement+=A[val][M[Z[j]][eval(x[j])]]==w[j];int rem=19;
   for(int j=0;j<24;j++){if(std::find(s.begin(),s.end(),j)!=s.end())continue;agreement+=eval(x[out[j]])==y[j];rem--;if(agreement+rem<12)break;}
   if(agreement>=12){hits++;int check=0;std::array<int,32>v;for(int j=0;j<32;j++){v[j]=A[val][M[Z[j]][eval(x[j])]];check+=v[j]==w[j];}assert(check==agreement);best=std::max(best,agreement);for(int t=0;t<8;t++){std::array<int,32>rot;for(int j=0;j<32;j++)rot[j]=v[(j+4*t)%32];bank.insert(rot);}}
   count++;int j=4;while(j>=0&&s[j]==19+j)j--;if(j<0)break;s[j]++;for(int h=j+1;h<5;h++)s[h]=s[h-1]+1;
  }while(true);
 }
 assert(count==1190112);
 std::cout<<"{\"characteristic\":17,\"extension_degree\":2,\"modulus\":\"T^2-3\",\"domain_generator\":"<<g<<",\"length\":32,\"dimension\":8,\"threshold_scanned\":12,\"maximum_agreement\":"<<best<<",\"supports\":"<<count<<",\"successful_supports\":"<<hits<<",\"complete\":true,\"bank_size\":"<<bank.size()<<",\"values\":[";
 bool first=true;for(const auto&v:bank){std::cout<<(first?"":",")<<"[";first=false;for(int j=0;j<32;j++)std::cout<<(j?",":"")<<v[j];std::cout<<"]";}std::cout<<"]}\n";
}
