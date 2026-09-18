#include <algorithm>
#include <array>
#include <chrono>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
int pw(int x,int e,int p){int r=1;for(;e;e>>=1,x=1LL*x*x%p)if(e&1)r=1LL*r*x%p;return r;}
int main(){const int p=4801,n=4096;for(int d=2;d*d<=p;d++)if(p%d==0)return 2;
int g=2;for(;g<p;g++)if(pw(g,2400,p)!=1&&pw(g,1600,p)!=1&&pw(g,960,p)!=1)break;
auto subgroup=[&](int k){vector<int> h;int a=1,z=pw(g,4800/k,p);for(int i=0;i<k;i++){h.push_back(a);a=1LL*a*z%p;}if(a!=1)return vector<int>();return h;};
auto h16=subgroup(16),h64=subgroup(64);vector<vector<array<int,3>>> banks(3);
for(int a=0;a<16;a++)for(int b=0;b<16;b++)for(int c=0;c<16;c++){banks[0].push_back({a,b,c});banks[1].push_back({h16[a],h16[b],h16[c]});}
for(int u:h64)for(int v:h64)banks[2].push_back({u,v,u*v%p});
auto start=chrono::steady_clock::now();cout<<"{\"p\":"<<p<<",\"n\":"<<n<<",\"primitive_root\":"<<g<<",\"necessary_incidence\":323584,\"banks\":[";
for(int z=0;z<3;z++){vector<int> maxima(p),hist(p);for(int x=0;x<p;x++){fill(hist.begin(),hist.end(),0);int x2=x*x%p;for(auto q:banks[z])hist[(1LL*q[0]*x2+q[1]*x+q[2])%p]++;maxima[x]=*max_element(hist.begin(),hist.end());}sort(maxima.rbegin(),maxima.rend());long long cap=accumulate(maxima.begin(),maxima.begin()+n,0LL);if(z)cout<<",";cout<<"{\"model\":"<<z<<",\"bank_size\":"<<banks[z].size()<<",\"capacity\":"<<cap<<",\"maximum_bucket\":"<<maxima[0]<<",\"cutoff_bucket\":"<<maxima[n-1]<<",\"bucket_histogram\":{";bool first=1;for(int i=0;i<p;){int j=i;while(j<p&&maxima[j]==maxima[i])j++;if(!first)cout<<",";first=0;cout<<"\""<<maxima[i]<<"\":"<<j-i;i=j;}cout<<"}}";}
cout<<"],\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"}\n";
}
