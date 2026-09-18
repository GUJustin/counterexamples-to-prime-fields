#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
using Block=array<unsigned char,7>;vector<array<int,3>>tr;vector<array<int,3>>pa;vector<Block>all;int degs[7]={},pc[21]={};Block chosen;int pi[7][7];uint64_t pow3[21];
uint64_t code(Block a){uint64_t x=0;for(int t:a)x=x*35+t;return x;}
uint64_t pairs(Block a){uint64_t x=0;for(int t:a)for(int p:pa[t])x+=pow3[p];return x;}
void rec(int depth,int lo){if(depth==7){for(int d:degs)if(d!=3)return;all.push_back(chosen);return;}int left=7-depth;for(int i=0;i<7;i++)if(degs[i]+left<3)return;for(int t=lo;t<35;t++){bool ok=true;for(int v:tr[t])if(degs[v]>=3)ok=false;for(int p:pa[t])if(pc[p]>=2)ok=false;if(!ok)continue;for(int v:tr[t])degs[v]++;for(int p:pa[t])pc[p]++;chosen[depth]=t;rec(depth+1,t);for(int v:tr[t])degs[v]--;for(int p:pa[t])pc[p]--;}}
int main(){int q=0;for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)pi[i][j]=pi[j][i]=q++;uint64_t full=0,z=1;for(int i=0;i<21;i++){pow3[i]=z;full+=2*z;z*=3;}int id[128];for(int i=0;i<128;i++)id[i]=-1;for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)for(int k=j+1;k<7;k++){id[(1<<i)|(1<<j)|(1<<k)]=tr.size();tr.push_back({i,j,k});pa.push_back({pi[i][j],pi[i][k],pi[j][k]});}rec(0,0);
vector<array<unsigned char,35>>pm;array<int,7>perm={0,1,2,3,4,5,6};do{array<unsigned char,35>v;for(int i=0;i<35;i++)v[i]=id[(1<<perm[tr[i][0]])|(1<<perm[tr[i][1]])|(1<<perm[tr[i][2]])];pm.push_back(v);}while(next_permutation(perm.begin(),perm.end()));
auto trans=[&](Block b,int p){for(auto &x:b)x=pm[p][x];sort(b.begin(),b.end());return b;};unordered_map<uint64_t,vector<int>>by;for(int i=0;i<(int)all.size();i++)by[pairs(all[i])].push_back(i);unordered_set<uint64_t>covered;vector<Block>reps;long long ordered=0;for(auto a:all){auto it=by.find(full-pairs(a));if(it!=by.end())ordered+=it->second.size();if(covered.count(code(a)))continue;Block best=a;for(int p=0;p<5040;p++){auto b=trans(a,p);covered.insert(code(b));if(b<best)best=b;}reps.push_back(best);}sort(reps.begin(),reps.end());
ofstream out("research/prime_line_strengthening/fano_seven/design_orbits.jsonl");int total=0,validtypes=0;for(int r=0;r<(int)reps.size();r++){auto T=reps[r];auto it=by.find(full-pairs(T));if(it==by.end())continue;validtypes++;vector<int>stab;for(int p=0;p<5040;p++)if(trans(T,p)==T)stab.push_back(p);set<Block>Creps;for(int ix:it->second){auto C=all[ix],best=C;for(int p:stab){auto b=trans(C,p);if(b<best)best=b;}Creps.insert(best);}for(auto C:Creps){out<<"{\"orbit\":"<<total++<<",\"T_type\":"<<r<<",\"T_stabilizer\":"<<stab.size()<<",\"T\":[";for(int i=0;i<7;i++){if(i)out<<",";auto b=tr[T[i]];out<<"["<<b[0]+1<<","<<b[1]+1<<","<<b[2]+1<<"]";}out<<"],\"C\":[";for(int i=0;i<7;i++){if(i)out<<",";auto b=tr[C[i]];out<<"["<<b[0]+1<<","<<b[1]+1<<","<<b[2]+1<<"]";}out<<"]}\n";}}
cout<<"{\"regular_halves\":"<<all.size()<<",\"half_orbits\":"<<reps.size()<<",\"compatible_half_orbits\":"<<validtypes<<",\"ordered_labelled_designs\":"<<ordered<<",\"ordered_simultaneous_S7_orbits\":"<<total<<"}"<<endl;}
