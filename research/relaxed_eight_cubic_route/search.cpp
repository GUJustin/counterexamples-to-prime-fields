// Exact bounded RS[16,4]/F17 received-word search, followed by incidence rank.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <chrono>
#include <algorithm>
#include <cstdint>
using namespace std;
constexpr int p=17,n=16,codes=83521;
uint64_t state=202609182711ULL;
uint64_t rng(){state^=state<<13;state^=state>>7;state^=state<<17;return state;}
int mod(int x){x%=p;return x<0?x+p:x;}
int inv(int x){for(int y=1;y<p;y++)if(x*y%p==1)return y;abort();}
array<int,4> coeff(int k){array<int,4>a;for(auto &z:a){z=k%p;k/=p;}return a;}
int rank_matrix(vector<array<int,64>> A,vector<int>&piv){int r=0;for(int j=0;j<64&&r<(int)A.size();j++){int k=r;while(k<(int)A.size()&&!A[k][j])k++;if(k==(int)A.size())continue;swap(A[k],A[r]);int vi=inv(A[r][j]);for(int c=j;c<64;c++)A[r][c]=A[r][c]*vi%p;for(k=r+1;k<(int)A.size();k++)if(A[k][j]){int z=A[k][j];for(int c=j;c<64;c++)A[k][c]=mod(A[k][c]-z*A[r][c]);}piv.push_back(j);r++;}return r;}
void arr(ostream&o,const vector<int>&v){o<<'[';for(int i=0;i<(int)v.size();i++){if(i)o<<',';o<<v[i];}o<<']';}
int main(){auto begin=chrono::steady_clock::now();vector<array<uint8_t,n>> E(codes);for(int k=0;k<codes;k++){auto a=coeff(k);for(int j=0;j<n;j++){int x=j+1;E[k][j]=mod(((a[3]*x+a[2])*x+a[1])*x+a[0]);}}
long words=0,hits=0;int best=0,best_rank=0;long histogram[30]={0};bool success=false;vector<int>savedword,savedcodes,pivots;vector<vector<int>>support;
for(;words<100000;words++){if(words%16==0&&chrono::duration<double>(chrono::steady_clock::now()-begin).count()>50)break;array<uint8_t,n>w;for(auto&z:w)z=rng()%p;vector<int>list;for(int k=0;k<codes;k++){int a=0;for(int j=0;j<n;j++)a+=(E[k][j]==w[j]);if(a>=7)list.push_back(k);}int count=list.size();histogram[min(count,29)]++;best=max(best,count);if(count<8)continue;hits++;
for(int trial=0;trial<min(32,1+count*2);trial++){if(trial)for(int i=count-1;i;i--)swap(list[i],list[rng()%(i+1)]);vector<array<int,64>>M;vector<vector<int>>S;
 for(int i=0;i<8;i++){int k=list[i];auto a=coeff(k);vector<int>matches;for(int j=0;j<n;j++)if(E[k][j]==w[j])matches.push_back(j);if(trial)for(int j=matches.size()-1;j;j--)swap(matches[j],matches[rng()%(j+1)]);matches.resize(7);sort(matches.begin(),matches.end());S.push_back(matches);for(int j:matches){array<int,64>row{};int x=j+1,powx=1;for(int e=0;e<4;e++){row[4*i+e]=powx;powx=powx*x%p;}row[32+j]=mod(a[1]+2*a[2]*x+3*a[3]*x*x);row[48+j]=p-1;M.push_back(row);}}
 vector<int>pv;int r=rank_matrix(M,pv);best_rank=max(best_rank,r);if(r==56){success=true;savedword.assign(w.begin(),w.end());savedcodes.assign(list.begin(),list.begin()+8);support=S;pivots=pv;break;}}
if(success){words++;break;}}
ofstream o("research/relaxed_eight_cubic_route/search.json");o<<"{\"p\":17,\"n\":16,\"degree\":3,\"agreement\":7,\"list_target\":8,\"seed\":202609182711,\"words\":"<<words<<",\"hits\":"<<hits<<",\"best_list\":"<<best<<",\"best_jacobian_rank\":"<<best_rank<<",\"smooth_hit\":"<<(success?"true":"false")<<",\"histogram\":[";for(int i=0;i<30;i++){if(i)o<<',';o<<histogram[i];}o<<"],\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-begin).count();if(success){o<<",\"nodes\":[";for(int j=0;j<n;j++){if(j)o<<',';o<<j+1;}o<<"],\"word\":";arr(o,savedword);o<<",\"polynomials\":[";for(int i=0;i<8;i++){if(i)o<<',';auto a=coeff(savedcodes[i]);arr(o,vector<int>(a.begin(),a.end()));}o<<"],\"selected_supports\":[";for(int i=0;i<8;i++){if(i)o<<',';arr(o,support[i]);}o<<"],\"pivot_columns\":";arr(o,pivots);}o<<"}\n";o.close();cout<<"words="<<words<<" hits="<<hits<<" best_list="<<best<<" best_rank="<<best_rank<<" smooth="<<success<<endl;}
