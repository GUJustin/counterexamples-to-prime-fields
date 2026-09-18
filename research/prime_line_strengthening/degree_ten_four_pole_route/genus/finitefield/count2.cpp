#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;const int p=29,q=841;vector<int> mt(q*q),at(q*q);int ad(int a,int b){return at[a*q+b];}int mu(int a,int b){return mt[a*q+b];}int neg(int a){return (29-a%29)%29+29*((29-a/29)%29);}int pw(int a,int n){int z=1;for(;n;n>>=1,a=mu(a,a))if(n&1)z=mu(z,a);return z;}
struct Term{int k,l,c;};using Poly=vector<Term>;int choose[40][40];
int ev(const vector<int>&f,int y){int z=0;for(int j=(int)f.size()-1;j>=0;j--)z=ad(mu(z,y),f[j]);return z;}
int jet(const Poly&f,const vector<int>&xp,const vector<int>&yp,int a,int b){int z=0;for(auto t:f)if(t.k>=a&&t.l>=b)z=ad(z,mu(t.c*choose[t.k][a]%p*choose[t.l][b]%p,mu(xp[t.k-a],yp[t.l-b])));return z;}
void trim(vector<int>&f){while(!f.empty()&&!f.back())f.pop_back();}
bool sf(vector<int>f){trim(f);vector<int>g;for(int i=1;i<(int)f.size();i++)g.push_back(mu(i%p,f[i]));trim(g);while(!g.empty()){auto r=f;int iv=pw(g.back(),q-2);while(r.size()>=g.size()){int c=mu(r.back(),iv),j=r.size()-g.size();for(int i=0;i<(int)g.size();i++)r[i+j]=ad(r[i+j],neg(mu(c,g[i])));trim(r);}f=g;g=r;}return f.size()==1;}
int main(){for(int a=0;a<q;a++)for(int b=0;b<q;b++){at[a*q+b]=(a%p+b%p)%p+p*((a/p+b/p)%p);mt[a*q+b]=(a%p*(b%p)+2*(a/p)*(b/p))%p+p*((a%p*(b/p)+a/p*(b%p))%p);}for(int i=0;i<40;i++){choose[i][0]=choose[i][i]=1;for(int j=1;j<i;j++)choose[i][j]=(choose[i-1][j-1]+choose[i-1][j])%p;}
 array<Poly,3>base;for(auto&f:base){int n;cin>>n;while(n--){Term t;cin>>t.k>>t.l>>t.c;f.push_back(t);}}int n;cin>>n;vector<array<int,3>>pars(n);for(auto&v:pars)for(int&a:v)cin>>a;vector<int>known(n),smooth(n),unknown(n),ordinary(n);
 for(int ch=0;ch<4;ch++){array<Poly,3>fs=base;for(auto&f:fs)for(auto&t:f){int k=t.k,l=t.l;if(ch>=2)t.k=34-k-3*l;if(ch==1||ch==3)t.l=10-l;}
 for(int xi=0;xi<(ch<2?q:1);xi++){int x=xi;vector<int>xp(35,1);for(int i=1;i<35;i++)xp[i]=mu(xp[i-1],x);array<vector<int>,3>coeff;for(int b=0;b<3;b++){coeff[b].resize(11);for(auto t:fs[b])coeff[b][t.l]=ad(coeff[b][t.l],mu(t.c,xp[t.k]));}
 for(int yi=0;yi<((ch==0||ch==2)?q:1);yi++){int y=yi;array<int,3>vs;for(int b=0;b<3;b++)vs[b]=ev(coeff[b],y);vector<int>yp;for(int r=0;r<n;r++){int z=0;for(int b=0;b<3;b++)z=ad(z,mu(pars[r][b],vs[b]));if(z)continue;if(yp.empty()){yp.resize(11,1);for(int j=1;j<11;j++)yp[j]=mu(yp[j-1],y);}auto jj=[&](int a,int b){int o=0;for(int k=0;k<3;k++)o=ad(o,mu(pars[r][k],jet(fs[k],xp,yp,a,b)));return o;};if(jj(1,0)||jj(0,1)){known[r]++;smooth[r]++;continue;}vector<int>co;int m;for(m=2;m<=11;m++){co.assign(m+1,0);bool nz=false;for(int b=0;b<=m;b++){co[b]=jj(m-b,b);nz|=co[b]!=0;}if(nz)break;}if(m==12){unknown[r]++;continue;}int deg=m;while(deg>=0&&!co[deg])deg--;bool ord=(m-deg<=1)&&sf(co);if(!ord){unknown[r]++;vector<int>der;for(int j=1;j<(int)co.size();j++)der.push_back(mu(j%p,co[j]));int simple=(m-deg==1);for(int t=0;t<q;t++)simple+=ev(co,t)==0&&ev(der,t)!=0;known[r]+=simple;continue;}int nr=(m>deg);for(int t=0;t<q;t++)nr+=ev(co,t)==0;known[r]+=nr;ordinary[r]++;}}}}
 cout<<"[";for(int i=0;i<n;i++){if(i)cout<<",";cout<<"{\"parameters\":["<<pars[i][0]<<","<<pars[i][1]<<","<<pars[i][2]<<"],\"known\":"<<known[i]<<",\"smooth\":"<<smooth[i]<<",\"ordinary\":"<<ordinary[i]<<",\"unknown\":"<<unknown[i]<<"}";}cout<<"]\n";}
