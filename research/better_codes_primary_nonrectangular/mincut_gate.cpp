#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;using I=int64_t;
struct Edge{int to,rev;I cap;};struct Orig{int u,pos;I cap;};vector<vector<Edge>>g;vector<Orig>orig;vector<int>lev,it;
int node(){g.emplace_back();return g.size()-1;}void edge(int u,int v,I c){orig.push_back({u,(int)g[u].size(),c});g[u].push_back({v,(int)g[v].size(),c});g[v].push_back({u,(int)g[u].size()-1,0});}
bool bfs(){lev.assign(g.size(),-1);queue<int>q;q.push(0);lev[0]=0;while(!q.empty()){int u=q.front();q.pop();for(auto&e:g[u])if(e.cap&&lev[e.to]<0){lev[e.to]=lev[u]+1;q.push(e.to);}}return lev[1]>=0;}
I dfs(int u,I f){if(u==1)return f;for(int &k=it[u];k<(int)g[u].size();k++){auto&e=g[u][k];if(e.cap&&lev[e.to]==lev[u]+1){I a=dfs(e.to,min(f,e.cap));if(a){e.cap-=a;g[e.to][e.rev].cap+=a;return a;}}}return 0;}
int main(int argc,char**argv){assert(argc==6||argc==7);I n=262144,w=131071;int m=stoi(argv[2]),Q=stoi(argv[4]),S=stoi(argv[5]);I D=argc==7?stoll(argv[6]):181275LL*m,L=stoll(argv[3]);assert(D>(m-1)+(w-1)*Q);node();node();vector<vector<int>> ids(Q+1,vector<int>(S+1,-1));vector<pair<int,int>>vars;I B=0;for(int j=0;j<=S;j++)for(int i=0;i+j<=Q;i++){int id=node();ids[i][j]=id;vars.push_back({i,j});I c=(L<0?1:L-i-j+1)*(D-w*i-(w-1)*j);assert(c>0);B+=c;edge(0,id,c);}for(auto [i,j]:vars)if(i)edge(ids[i][j],ids[i-1][j],B+1);
for(int q=0;q<=Q;q++)for(int ell=0;ell<m;ell++){vector<int>a;for(int i=max(0,q-S);i<=min(q,ell);i++)a.push_back(ids[i][q-i]);if(a.empty())continue;int z=node();I K=n*(L<0?1:L-q+1);for(int x:a)edge(x,z,K);edge(z,1,(m-ell)*K);}
I flow=0;while(bfs()){it.assign(g.size(),0);while(I f=dfs(0,B-flow+1))flow+=f;}vector<bool>reach(g.size());queue<int>qu;qu.push(0);reach[0]=true;while(!qu.empty()){int u=qu.front();qu.pop();for(auto&e:g[u])if(e.cap&&!reach[e.to]){reach[e.to]=true;qu.push(e.to);}}
I cut=0;for(auto&o:orig){auto&e=g[o.u][o.pos];if(reach[o.u]&&!reach[e.to])cut+=o.cap;}assert(cut==flow);ofstream f(string(argv[1])+".flow");for(int k=0;k<(int)orig.size();k++){auto&o=orig[k];I v=o.cap-g[o.u][o.pos].cap;if(v)f<<k<<" "<<v<<"\n";}ofstream out(string(argv[1])+".json");out<<"{\"D\":"<<D<<",\"m\":"<<m<<",\"L\":"<<L<<",\"Q\":"<<Q<<",\"S\":"<<S<<",\"nodes\":"<<g.size()<<",\"edges\":"<<orig.size()<<",\"benefit_sum\":"<<B<<",\"flow\":"<<flow<<",\"maximum_surplus\":"<<B-flow<<",\"source_side\":[";bool first=true;for(int i=0;i<(int)reach.size();i++)if(reach[i]){if(!first)out<<",";first=false;out<<i;}out<<"],\"selected_support\":[";first=true;for(auto [i,j]:vars)if(reach[ids[i][j]]){if(!first)out<<",";first=false;out<<"["<<i<<","<<j<<"]";}out<<"]}\n";cout<<"max surplus "<<B-flow<<" nodes "<<g.size()<<" edges "<<orig.size()<<"\n";}
