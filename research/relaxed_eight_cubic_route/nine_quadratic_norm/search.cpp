#include <algorithm>
#include <array>
#include <chrono>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
#include "input.hpp"
int A[289][289],M[289][289],N[289],I[289];
int add(int a,int b){return A[a][b];}int mul(int a,int b){return M[a][b];}int sub(int a,int b){return add(a,N[b]);}
using V=vector<int>;using Mat=vector<V>;
struct Sol{bool ok;V v;Mat b;};
Sol solve(Mat a,int d){int r=0;V piv;for(int c=0;c<d;c++){int k=r;while(k<(int)a.size()&&!a[k][c])k++;if(k==(int)a.size())continue;swap(a[k],a[r]);int iv=I[a[r][c]];for(int j=c;j<=d;j++)a[r][j]=mul(a[r][j],iv);for(int i=0;i<(int)a.size();i++)if(i!=r&&a[i][c]){int f=a[i][c];for(int j=c;j<=d;j++)a[i][j]=sub(a[i][j],mul(f,a[r][j]));}piv.push_back(c);r++;}for(int i=r;i<(int)a.size();i++)if(a[i][d])return {false,{},{}};V v(d);for(int i=0;i<r;i++)v[piv[i]]=a[i][d];Mat b;for(int c=0;c<d;c++)if(find(piv.begin(),piv.end(),c)==piv.end()){V z(d);z[c]=1;for(int i=0;i<r;i++)z[piv[i]]=N[a[i][c]];b.push_back(z);}return {true,v,b};}
void trim(V&f){while(f.size()>1&&!f.back())f.pop_back();}bool zero(V f){trim(f);return f.size()==1&&!f[0];}
V rem(V a,const V&b){trim(a);while(!zero(a)&&a.size()>=b.size()){int d=a.size()-b.size(),t=mul(a.back(),I[b.back()]);for(int j=0;j<(int)b.size();j++)a[d+j]=sub(a[d+j],mul(t,b[j]));trim(a);}return a;}
V gcd(V a,V b){while(!zero(b)){V c=rem(a,b);a=b;b=c;}int iv=I[a.back()];for(int&x:a)x=mul(x,iv);return a;}
V quot(V a,const V&b){V q(max(1,(int)a.size()-(int)b.size()+1));while(!zero(a)&&a.size()>=b.size()){int d=a.size()-b.size(),t=mul(a.back(),I[b.back()]);q[d]=t;for(int j=0;j<(int)b.size();j++)a[d+j]=sub(a[d+j],mul(t,b[j]));trim(a);}if(!zero(a))abort();trim(q);return q;}
int odddegree(V f){trim(f);if(zero(f))return 0;int out=(8-(int)f.size()+1)%2;V df(max(1,(int)f.size()-1));for(int j=1;j<(int)f.size();j++)df[j-1]=mul(j,f[j]);trim(df);V c=gcd(f,df),w=quot(f,c);int i=1;while(w.size()>1){V y=gcd(w,c),z=quot(w,y);if(i%2)out+=z.size()-1;w=y;c=quot(c,y);i++;}return out;}
V norm[18];Mat full[18];set<V> seen;vector<V> accepted;long long unresolved[4]={},systems[4]={},consistent[4]={};vector<array<int,3>> dims;
void consider(const Sol&s,int f){if(!s.ok)return;consistent[f]++;if(!s.b.empty()){unresolved[f]++;return;}if(!seen.insert(s.v).second)return;V E(5),J(9);for(int i=0;i<5;i++)E[i]=mul(N[s.v[i]],9);for(int i=0;i<5;i++)for(int j=0;j<5;j++)J[i+j]=add(J[i+j],mul(E[i],E[j]));for(int i=0;i<9;i++)J[i]=sub(J[i],s.v[5+i]);if(odddegree(J)<=2)accepted.push_back(s.v);}
Mat restricted[18];Sol base;V subset;int currentf;
void choosefull(int pos,int remain,Mat rows){if(!remain){systems[currentf]++;Sol z=solve(rows,base.b.size());if(!z.ok)return;Sol result{true,base.v,{}};for(int k=0;k<(int)base.b.size();k++)for(int j=0;j<14;j++)result.v[j]=add(result.v[j],mul(z.v[k],base.b[k][j]));for(auto&b:z.b){V v(14);for(int k=0;k<(int)base.b.size();k++)for(int j=0;j<14;j++)v[j]=add(v[j],mul(b[k],base.b[k][j]));result.b.push_back(v);}consider(result,currentf);return;}for(int i=pos;i<=(int)subset.size()-remain;i++){Mat next=rows;for(auto&r:restricted[subset[i]])next.push_back(r);choosefull(i+1,remain-1,next);}}
void subsearch(int pos,int remain){if(!remain){Mat rows;for(int i:subset)rows.push_back(norm[i]);base=solve(rows,14);if(!base.ok)return;if(!currentf){systems[0]++;consider(base,0);return;}for(int i:subset){restricted[i].clear();for(auto&r:full[i]){V row(base.b.size()+1);row.back()=r[14];for(int j=0;j<14;j++)row.back()=sub(row.back(),mul(r[j],base.v[j]));for(int k=0;k<(int)base.b.size();k++)for(int j=0;j<14;j++)row[k]=add(row[k],mul(r[j],base.b[k][j]));restricted[i].push_back(row);}}choosefull(0,currentf,{});return;}for(int i=pos;i<=18-remain;i++){subset.push_back(i);subsearch(i+1,remain-1);subset.pop_back();}}
int main(){auto start=chrono::steady_clock::now();for(int a=0;a<289;a++){int x=a%17,y=a/17;N[a]=(17-x)%17+17*((17-y)%17);for(int b=0;b<289;b++){int z=b%17,t=b/17;A[a][b]=(x+z)%17+17*((y+t)%17);M[a][b]=(x*z+7*y*t)%17+17*((x*t+y*z)%17);}}for(int a=1;a<289;a++)for(int b=1;b<289;b++)if(M[a][b]==1)I[a]=b;for(int i=0;i<18;i++){V pw(9,1);for(int j=1;j<9;j++)pw[j]=mul(pw[j-1],nodes[i]);V row(15);for(int j=0;j<5;j++)row[j]=mul(words[i],pw[j]);for(int j=0;j<9;j++)row[5+j]=pw[j];row[14]=N[mul(words[i],words[i])];norm[i]=row;V r(15),t(15);for(int j=0;j<5;j++)r[j]=pw[j];r[14]=N[mul(2,words[i])];for(int j=1;j<5;j++)t[j]=mul(mul(j,words[i]),pw[j-1]);for(int j=1;j<9;j++)t[5+j]=mul(j,pw[j-1]);full[i]={r,t};}
for(currentf=0;currentf<=3;currentf++){subsearch(0,15-currentf);cerr<<"f="<<currentf<<" consistent="<<consistent[currentf]<<" unresolved="<<unresolved[currentf]<<" norms="<<seen.size()<<" accepted="<<accepted.size()<<endl;}
cout<<"{\"field\":\"F17(theta),theta^2=7\",\"cases\":[";for(int f=0;f<4;f++){if(f)cout<<",";cout<<"{\"full_fibers\":"<<f<<",\"systems\":"<<systems[f]<<",\"consistent\":"<<consistent[f]<<",\"unresolved\":"<<unresolved[f]<<"}";}cout<<"],\"norms_tested\":"<<seen.size()<<",\"accepted\":[";for(int i=0;i<(int)accepted.size();i++){if(i)cout<<",";cout<<"[";for(int j=0;j<14;j++){if(j)cout<<",";cout<<accepted[i][j];}cout<<"]";}cout<<"],\"all_norms\":[";int ni=0;for(const auto&v:seen){if(ni++)cout<<",";cout<<"[";for(int j=0;j<14;j++){if(j)cout<<",";cout<<v[j];}cout<<"]";}cout<<"],\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"}\n";}
