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

int main(int argc,char**argv){assert(argc==4);int lo=stoi(argv[1]),hi=stoi(argv[2]);string dir=argv[3];
for(int m=lo;m<=hi;m++){
 g.clear();orig.clear();lev.clear();it.clear();
 I n=262144,w=131071,D=I(m)*181275;int Q=159,S=35;node();node();int ids[160][36];fill(&ids[0][0],&ids[0][0]+160*36,-1);vector<pair<int,int>>vars;I B=0;
 for(int j=0;j<=S;j++)for(int i=0;i+j<=Q;i++){I c=D-w*i-(w-1)*j;if(c<=0)continue;int id=node();ids[i][j]=id;vars.push_back({i,j});B+=c;edge(0,id,c);}
 for(auto[i,j]:vars)if(i){assert(ids[i-1][j]>=0);edge(ids[i][j],ids[i-1][j],B+1);}
 for(int q=0;q<=Q;q++)for(int ell=0;ell<m&&ell<=D-1-(w-1)*q;ell++){
 vector<int>a;for(int i=max(0,q-S);i<=min(q,ell);i++){assert(ids[i][q-i]>=0);a.push_back(ids[i][q-i]);}
 if(a.empty())continue;int z=node();for(int x:a)edge(x,z,n);edge(z,1,I(m-ell)*n);}
 I flow=0;while(bfs()){it.assign(g.size(),0);while(I f=dfs(0,B-flow+1))flow+=f;}
 vector<bool>reach(g.size());queue<int>qu;qu.push(0);reach[0]=1;while(!qu.empty()){int u=qu.front();qu.pop();for(auto&e:g[u])if(e.cap&&!reach[e.to]){reach[e.to]=1;qu.push(e.to);}}
 I cut=0;for(auto&o:orig){auto&e=g[o.u][o.pos];if(reach[o.u]&&!reach[e.to])cut+=o.cap;}assert(cut==flow);
 string stem=dir+"/m"+to_string(m);ofstream f(stem+".flowbin",ios::binary);int nonzero=0;
 for(uint32_t k=0;k<orig.size();k++){auto&o=orig[k];I v=o.cap-g[o.u][o.pos].cap;if(v){f.write((char*)&k,4);f.write((char*)&v,8);nonzero++;}}
 ofstream out(stem+".json");out<<"{\"m\":"<<m<<",\"D\":"<<D<<",\"nodes\":"<<g.size()<<",\"edges\":"<<orig.size()<<",\"nonzero_flows\":"<<nonzero<<",\"benefit_sum\":"<<B<<",\"flow\":"<<flow<<",\"maximum_slope\":"<<B-flow<<",\"source_side\":[";
 bool first=1;for(int i=0;i<reach.size();i++)if(reach[i]){if(!first)out<<",";first=0;out<<i;}out<<"],\"selected_support\":[";first=1;for(auto[i,j]:vars)if(reach[ids[i][j]]){if(!first)out<<",";first=0;out<<"["<<i<<","<<j<<"]";}out<<"]}\n";
 cout<<m<<" "<<B-flow<<" "<<g.size()<<" "<<orig.size()<<endl;
}}
