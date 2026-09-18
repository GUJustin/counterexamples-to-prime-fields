#include <array>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <chrono>
using namespace std;
const int p=1009; int mt[p][p],iv[p],xs[36],wordv[36]; long long countp=0,limitp=0;set<array<int,36>> bank;
int sub(int a,int b){int c=a-b;return c<0?c+p:c;} int add(int a,int b){int c=a+b;return c>=p?c-p:c;} int pw(int a,int n){int r=1;for(;n;n>>=1,a=mt[a][a])if(n&1)r=mt[r][a];return r;}
vector<vector<int>> combs(vector<int> v,int k){vector<vector<int>> out;vector<int>s;auto rec=[&](auto&&self,int j)->void{if((int)s.size()==k){out.push_back(s);return;}for(int i=j;i<=(int)v.size()-(k-(int)s.size());i++){s.push_back(v[i]);self(self,i+1);s.pop_back();}};rec(rec,0);return out;}
vector<vector<int>> patterns(int m){vector<int> v;for(int i=0;i<9;i++)v.push_back(i);set<vector<int>> out;for(auto s:combs(v,m)){auto best=s;for(int t=1;t<9;t++){vector<int>a;for(int x:s)a.push_back((x+t)%9);sort(a.begin(),a.end());best=min(best,a);}out.insert(best);}return {out.begin(),out.end()};}
// Simultaneous Newton interpolation evaluations and locator on all 36 nodes.
void interp(const vector<int>& s,const int*y,int*r,int*l){fill(r,r+36,0);fill(l,l+36,1);for(int j:s){int c=mt[sub(y[j],r[j])][iv[l[j]]];for(int x=0;x<36;x++){r[x]=add(r[x],mt[c][l[x]]);l[x]=mt[l[x]][sub(xs[x],xs[j])];}}}
void record(const int*v){array<int,36>a;int hits=0;for(int i=0;i<36;i++){a[i]=v[i];hits+=v[i]==wordv[i];}if(hits<12){cerr<<"BAD HIT\n";exit(2);}auto best=a;for(int t=1;t<9;t++){array<int,36>b;for(int i=0;i<36;i++)b[i]=a[(i+4*t)%36];best=min(best,b);}if(bank.insert(best).second){cout<<"{\"values\":[";for(int i=0;i<36;i++)cout<<(i?",":"")<<best[i];cout<<"],\"matches\":"<<hits<<"}\n"<<flush;}}
bool stop(){return limitp&&countp>=limitp;}
void large(){for(int m=3;m<=8;m++){int d=8-m;auto pat=patterns(m);for(int c=0;c<4;c++){vector<int> outside;for(int i=0;i<36;i++)if(i%4!=c)outside.push_back(i);vector<vector<int>> anchors;for(int half=0;half<(d?2:1);half++){vector<int>v(outside.begin()+(half?14:0),outside.begin()+(half?27:14));auto z=combs(v,d);anchors.insert(anchors.end(),z.begin(),z.end());}for(auto s:pat){int g[36],y[36];fill(g,g+36,1);for(int a:s)for(int i=0;i<36;i++)g[i]=mt[g[i]][sub(xs[i],xs[c+4*a])];for(int i=0;i<36;i++)y[i]=mt[sub(wordv[i],wordv[c])][iv[g[i]]];for(auto a:anchors){int r[36],l[36],bucket[p]={},touched[36],nt=0;interp(a,y,r,l);for(int i:outside)if(l[i]){int t=mt[sub(y[i],r[i])][iv[l[i]]];if(!bucket[t])touched[nt++]=t;bucket[t]++;}for(int z=0;z<nt;z++){int t=touched[z];if(bucket[t]>=4){int val[36];for(int i=0;i<36;i++)val[i]=add(wordv[c],mt[g[i]][add(r[i],mt[t][l[i]])]);record(val);}}countp++;if(stop())return;}}}cerr<<"m "<<m<<" pencils "<<countp<<" bank "<<bank.size()<<"\n";}}
int main(int argc,char**argv){if(argc>1)limitp=stoll(argv[1]);for(int a=0;a<p;a++)for(int b=0;b<p;b++)mt[a][b]=a*b%p;for(int a=1;a<p;a++)iv[a]=pw(a,p-2);int root=0;for(int a=2;a<p;a++)if(pw(a,36)==1&&pw(a,18)!=1&&pw(a,12)!=1){root=a;break;}for(int i=0;i<36;i++){xs[i]=pw(root,i);int z=sub(pw(xs[i],9),1);wordv[i]=mt[mt[z][z]][iv[2]];}auto start=chrono::steady_clock::now();large();cerr<<"DONE root="<<root<<" pencils="<<countp<<" orbits="<<bank.size()<<" seconds="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";}
