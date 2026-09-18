#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
constexpr int q=2187;
vector<uint16_t> addtab;array<int,q> negv,lg,invv,cb,nn;array<int,2*q> ex;
int add(int a,int b){return addtab[a*q+b];}int sub(int a,int b){return add(a,negv[b]);}
int mul(int a,int b){return (!a||!b)?0:ex[lg[a]+lg[b]];}
int power(int a,int k){return a?ex[(lg[a]*k)%(q-1)]:0;}
int timesx(int a){int ds[7];for(int i=0;i<7;i++){ds[i]=a%3;a/=3;}int r[7]={};for(int i=1;i<7;i++)r[i]=ds[i-1];r[0]=(r[0]+ds[6])%3;r[2]=(r[2]+2*ds[6])%3;int v=0;for(int i=6;i>=0;i--)v=3*v+r[i];return v;}
struct Rec{uint64_t key;array<uint16_t,5> loc;};vector<Rec> records;
int universal=0,impossible=0;long total=0;
void process(array<int,4> rows){
 int c[5]={1,0,0,0,0};int len=1;
 for(int x:rows){int z=0,y=x;for(int j=0;j<len;j++){z=add(z,mul(c[j],y));y=cb[y];}if(!z)abort();int zz=mul(z,z),nc[5]={};for(int j=0;j<len;j++){nc[j]=sub(nc[j],mul(zz,c[j]));nc[j+1]=add(nc[j+1],cb[c[j]]);}len++;copy(nc,nc+5,c);}
 total++;int E=c[0],C=c[1],B=c[2],A=c[3];if(c[4]!=1)abort();
 int u=sub(cb[C],mul(B,cb[A]));int k=add(sub(sub(nn[E],mul(nn[A],cb[C])),power(B,10)),mul(B,power(A,12)));
 if(!u&&!B){if(k)impossible++;else universal++;return;}
 int line;if(u)line=mul(B,invv[u])*q+mul(k,invv[u]);else line=q*q+mul(k,invv[B]);
 int z1=sub(cb[B],power(A,4));int z0=add(sub(sub(nn[C],mul(nn[A],cb[B])),mul(A,nn[B])),power(A,13));int slope,constant;
 if(B){slope=sub(z1,mul(A,mul(u,invv[B])));constant=sub(z0,mul(A,mul(k,invv[B])));}
 else{slope=A;constant=sub(z0,mul(z1,mul(k,invv[u])));}
 records.push_back({(uint64_t(line)<<32)|uint32_t(slope*q+constant),{uint16_t(E),uint16_t(C),uint16_t(B),uint16_t(A),1}});
}
int main(int argc,char**argv){auto start=chrono::steady_clock::now();lg.fill(-1);int x=1;for(int i=0;i<q-1;i++){if(lg[x]>=0){cerr<<"x not primitive\n";return 2;}ex[i]=x;lg[x]=i;x=timesx(x);int xx=x,yy=0,pp=1;for(int j=0;j<7;j++){yy+=((3-xx%3)%3)*pp;xx/=3;pp*=3;}x=yy;}if(x!=1)return 3;for(int i=q-1;i<2*q;i++)ex[i]=ex[i-(q-1)];
 addtab.resize(q*q);for(int a=0;a<q;a++){int aa=a,ds[7];for(int j=0;j<7;j++){ds[j]=aa%3;aa/=3;}int n=0;for(int j=6;j>=0;j--)n=3*n+(3-ds[j])%3;negv[a]=n;for(int b=0;b<q;b++){int bb=b,z=0,pw=1;for(int j=0;j<7;j++){z+=((ds[j]+bb%3)%3)*pw;bb/=3;pw*=3;}addtab[a*q+b]=z;}}
 for(int a=0;a<q;a++){invv[a]=a?ex[(q-1-lg[a])%(q-1)]:0;cb[a]=power(a,3);nn[a]=power(a,9);}records.reserve(1000000);int pw[7]={1,3,9,27,81,243,729};
 for(int a=0;a<4;a++)for(int b=a+1;b<5;b++)for(int c=b+1;c<6;c++)for(int d=c+1;d<7;d++){
 array<int,4> piv={a,b,c,d};vector<pair<int,int>>free;for(int i=0;i<4;i++)for(int j=piv[i]+1;j<7;j++)if(find(piv.begin(),piv.end(),j)==piv.end())free.push_back({i,j});int lim=1;for(auto _ :free)lim*=3;
 for(int code=0;code<lim;code++){int v=code;array<int,4>rows={pw[a],pw[b],pw[c],pw[d]};for(auto [i,j]:free){rows[i]+=pw[j]*(v%3);v/=3;}process(rows);}}
 sort(records.begin(),records.end(),[](auto&a,auto&b){return a.key<b.key;});map<int,int>hist;int maxlabels=0,lines=0;vector<size_t>best;
 for(size_t i=0;i<records.size();){size_t j=i;int labels=0;uint64_t last=~uint64_t(0);while(j<records.size()&&(records[j].key>>32)==(records[i].key>>32)){if(records[j].key!=last){labels++;last=records[j].key;}j++;}hist[labels]++;lines++;if(labels>maxlabels){maxlabels=labels;best.clear();}if(labels==maxlabels)best.push_back(i);i=j;}
 ofstream out(argc>1?argv[1]:"p3.json");out<<"{\n\"p\":3,\"field_modulus\":[2,0,1,0,0,0,0,1],\"subspaces\":"<<total<<",\"head_lines\":"<<lines<<",\"universal\":"<<universal<<",\"impossible\":"<<impossible<<",\"maximum_distinct_labels\":"<<maxlabels<<",\"label_histogram\":{";bool first=true;for(auto [k,v]:hist){if(!first)out<<",";first=false;out<<"\""<<k<<"\":"<<v;}out<<"},\"best_group_count\":"<<best.size()<<",\"best\":[";first=true;for(int ix=0;ix<min(3,int(best.size()));ix++){if(!first)out<<",";first=false;size_t i=best[ix],j=i;out<<"{\"line_id\":"<<(records[i].key>>32)<<",\"locators\":[";bool ff=true;while(j<records.size()&&(records[j].key>>32)==(records[i].key>>32)){if(!ff)out<<",";ff=false;out<<"[";for(int k=0;k<5;k++){if(k)out<<",";out<<records[j].loc[k];}out<<"]";j++;}out<<"]}";}out<<"],\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"}\n";
 cout<<"subspaces "<<total<<" lines "<<lines<<" maximum "<<maxlabels<<" best_groups "<<best.size()<<" universal "<<universal<<" impossible "<<impossible<<"\n";
}
