#include <algorithm>
#include <chrono>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>
using namespace std;
long long pw(long long a,int e,int p){long long r=1;for(;e;e>>=1,a=a*a%p)if(e&1)r=r*a%p;return r;}
bool prime(int x){if(x<2)return false;for(int d=2;(long long)d*d<=x;d++)if(x%d==0)return false;return true;}
int main(int argc,char**argv){int L=argc>1?stoi(argv[1]):25,p=argc>2?stoi(argv[2]):20011,steps=argc>3?stoi(argv[3]):200000;unsigned seed=argc>4?stoul(argv[4]):123;string out=argc>5?argv[5]:"swap.json";if(!prime(p))return 2;int t=L*(L-1)+1;vector<int>a;for(int i=2;a.size()<L;i++)if(prime(i))a.push_back(i);if(p<=2LL*a.back()*a.back())return 3;vector<int>inv(L);for(int i=0;i<L;i++)inv[i]=pw(a[i]*a[i],p-2,p);vector<unsigned char>bad(p),selected(p);bad[0]=1;for(int i=0;i<L;i++)for(int j=0;j<i;j++){int v=1LL*a[i]*a[j]%p;bad[v]=bad[p-v]=1;}
auto labels=[&](int x,vector<int>&v){v.resize(L);long long ix=pw(x,p-2,p),ix3=ix*ix%p*ix%p;for(int i=0;i<L;i++){v[i]=(a[i]*a[i]*ix3+inv[i]*ix-x)%p;if(v[i]<0)v[i]+=p;if(v[i]<2)return false;}return true;};
mt19937 rng(seed);vector<int>nodes,hist(p),v;vector<vector<int>> cache;int score=0;auto change=[&](int z,int d){score-=hist[z]==1;hist[z]+=d;score+=hist[z]==1;};while(nodes.size()<t){int x=1+rng()%(p-1);if(bad[x]||selected[x]||!labels(x,v))continue;selected[x]=1;nodes.push_back(x);cache.push_back(v);for(int z:v)change(z,1);}int initial=score,accept=0;auto start=chrono::steady_clock::now();for(int k=0;k<steps;k++){int x=1+rng()%(p-1);if(bad[x]||selected[x]||!labels(x,v))continue;int at=rng()%t,old=score;for(int z:cache[at])change(z,-1);for(int z:v)change(z,1);if(score>=old){selected[nodes[at]]=0;selected[x]=1;nodes[at]=x;cache[at]=v;accept++;}else{for(int z:v)change(z,-1);for(int z:cache[at])change(z,1);}}
ofstream f(out);f<<"{\"L\":"<<L<<",\"p\":"<<p<<",\"steps\":"<<steps<<",\"seed\":"<<seed<<",\"initial\":"<<initial<<",\"singletons\":"<<score<<",\"accepted\":"<<accept<<",\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<",\"nodes\":[";for(int i=0;i<t;i++)f<<(i?",":"")<<nodes[i];f<<"]}\n";cout<<initial<<" -> "<<score<<" density "<<double(score)/p<<"\n";}
