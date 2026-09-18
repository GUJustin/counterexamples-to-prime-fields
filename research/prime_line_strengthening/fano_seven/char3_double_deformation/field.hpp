#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std; using E=uint32_t;
const int B=729; const E BS=531441,Q=387420489;
vector<uint16_t> ad(B*B),mu(B*B);int ng[B],pw3[7]={1,3,9,27,81,243,729};
int ba(int a,int b){return ad[a*B+b];} int bm(int a,int b){return mu[a*B+b];}
E add(E a,E b){return ba(a%B,b%B)+B*ba(a/B%B,b/B%B)+BS*ba(a/BS,b/BS);}
E neg(E a){return ng[a%B]+B*ng[a/B%B]+BS*ng[a/BS];}
E sub(E a,E b){return add(a,neg(b));}
E mul(E a,E b){if(!a||!b)return 0;int x[3]={(int)(a%B),(int)(a/B%B),(int)(a/BS)},y[3]={(int)(b%B),(int)(b/B%B),(int)(b/BS)},c[5]={};for(int i=0;i<3;i++)for(int j=0;j<3;j++)c[i+j]=ba(c[i+j],bm(x[i],y[j])); // theta^3=theta+zeta
c[1]=ba(c[1],bm(3,c[4]));c[2]=ba(c[2],c[4]);c[0]=ba(c[0],bm(3,c[3]));c[1]=ba(c[1],c[3]);return c[0]+B*c[1]+BS*c[2];}
E power(E a,uint32_t n){E z=1;for(;n;n>>=1,a=mul(a,a))if(n&1)z=mul(z,a);return z;}
E inv(E a){assert(a);E v=power(a,Q-2);assert(mul(a,v)==1);return v;}
void init(){int ds[B][6];for(int a=0;a<B;a++)for(int i=0;i<6;i++)ds[a][i]=a/pw3[i]%3;for(int a=0;a<B;a++){ng[a]=0;for(int i=0;i<6;i++)ng[a]+=(3-ds[a][i])%3*pw3[i];for(int b=0;b<B;b++){int s=0,c[11]={};for(int i=0;i<6;i++){s+=(ds[a][i]+ds[b][i])%3*pw3[i];for(int j=0;j<6;j++)c[i+j]+=ds[a][i]*ds[b][j];}ad[a*B+b]=s;for(int k=10;k>=6;k--){int t=c[k]%3;for(int j=0;j<6;j++)c[k-6+j]+=2*t;}int z=0;for(int i=0;i<6;i++)z+=c[i]%3*pw3[i];mu[a*B+b]=z;}}assert(power(3,7)==1&&3!=1);assert(sub(power(B,3),B)==3);assert(power(B,Q)==B);}
