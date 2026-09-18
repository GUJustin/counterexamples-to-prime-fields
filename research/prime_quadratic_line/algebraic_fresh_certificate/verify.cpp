// Independent structured replay: direct core products, batch inverses,
// affine label forms, reversed bank order, and completed-bank owner updates.
#include <cstdint>
#include <iostream>
#include <vector>
#include <map>
#include <chrono>
#include "verify_input.h"
using namespace std;using U=uint64_t;
U modpow(U a,U b){U z=1;while(b){if(b%2)z=z*a%P;a=a*a%P;b/=2;}return z;}
int main(){auto start=chrono::steady_clock::now();
 vector<int>a(L),square(L),slope(L);vector<uint8_t>core(P);
 for(int i=0;i<L;i++){a[i]=modpow(G,2*Q*i+(U)i*i%Q);square[i]=(U)a[i]*a[i]%P;slope[i]=modpow(square[i],P-2);}
 int nc=0;for(int i=0;i<L;i++)for(int j=i+1;j<L;j++){
  int z=(U)a[i]*a[j]%P;if(core[z]||core[P-z])return 2;
  core[z]=core[P-z]=1;nc+=2;
 }
 vector<int>x,h;U dh=1469598103934665603ULL;int deleted=0,candidates=0;
 for(int u=1;u<=LAST;u++)if(!core[u]){
  candidates++;int u2=(U)u*u%P,u3=(U)u2*u%P;
  U v=0;for(int j=13;j>=0;j--)v=(v*u+HC[j])%P;
  bool forbidden=false;
  for(int i=L-1;i>=0;i--){int z=((U)slope[i]*u2+square[i])%P;if(v==(U)z||(v+u3)%P==(U)z){forbidden=true;break;}}
  if(forbidden){deleted++;continue;}
  x.push_back(u);h.push_back(v);dh^=u;dh*=1099511628211ULL;
 }
 if(x.size()!=TCOUNT||x.back()!=LAST||nc!=L*(L-1))return 3;
 size_t t=x.size();vector<int>prefix(t+1),c1(t),c2(t),c0(t);prefix[0]=1;
 for(size_t j=0;j<t;j++)prefix[j+1]=(U)prefix[j]*x[j]%P;
 U inv=modpow(prefix[t],P-2);
 for(size_t j=t;j-->0;){U z=inv*prefix[j]%P;inv=inv*x[j]%P;c1[j]=z;c2[j]=z*z%P*z%P;c0[j]=(P-(U)h[j]*c2[j]%P)%P;}
 vector<uint8_t>multiplicity(P);vector<uint16_t>owner(P);vector<int>touched;touched.reserve(t);
 vector<U>hit_hist(14);hit_hist[0]=(U)L*P;
 for(int i=L;i-->0;){
  touched.clear();
  for(size_t j=0;j<t;j++){
   int label=((U)c1[j]*slope[i]+(U)c2[j]*square[i]+c0[j])%P;
   if(!multiplicity[label])touched.push_back(label);
   if(++multiplicity[label]>13)return 4;
  }
  for(int label:touched){int z=multiplicity[label];hit_hist[0]--;hit_hist[z]++;if(z>=GAP)owner[label]++;multiplicity[label]=0;}
 }
 map<int,U>oh;U singles=0,bad=0;for(int j=0;j<P;j++){oh[owner[j]]++;singles+=owner[j]==1;bad+=owner[j]>0;}
 if(owner[0]||owner[1])return 5;
 cout<<"{\"canonical_singleton_labels\":"<<singles<<",\"canonical_bad_labels\":"<<bad<<",\"candidates_examined\":"<<candidates<<",\"deleted\":"<<deleted<<",\"domain_fnv64\":\""<<dh<<"\",\"owner_histogram\":{";
 bool first=true;for(auto z:oh){if(!first)cout<<",";first=false;cout<<"\""<<z.first<<"\":"<<z.second;}cout<<"},\"bank_fresh_hit_histogram\":[";
 for(int j=0;j<14;j++){if(j)cout<<",";cout<<hit_hist[j];}
 cout<<"],\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"}\n";
}
