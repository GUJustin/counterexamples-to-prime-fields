#include <array>
#include <chrono>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
#include "input.hpp"
int A[289][289],M[289][289],N[289],I[289],X[48],W[48],perm[6][24];long long pencils=0,visited=0,limit=0,descending=0;bool stopped=false;set<vector<int>>hits;vector<int>S;
int add(int a,int b){return A[a][b];}int mul(int a,int b){return M[a][b];}int sub(int a,int b){return A[a][N[b]];}
int power(int a,int e){int r=1;while(e){if(e&1)r=mul(r,a);a=mul(a,a);e>>=1;}return r;}
int eval(const vector<int>&c,int x){int y=0;for(int j=c.size()-1;j>=0;j--)y=add(mul(y,x),c[j]);return y;}
bool canonical(unsigned mask){for(int g=1;g<6;g++){unsigned t=0;for(int i:S)t|=1u<<perm[g][i];if(t<mask)return false;}return true;}
int invdiff[48][48];unsigned short buckets[289*289];
void process(int half,unsigned mask){visited++;if(!canonical(mask))return;pencils++;
vector<int>loc{1},q(8,0);for(int i:S){int x=X[24*half+i];vector<int>b(loc.size()+1);for(int j=0;j<(int)loc.size();j++){b[j]=add(b[j],mul(N[x],loc[j]));b[j+1]=add(b[j+1],loc[j]);}loc=b;}
for(int i:S){int idx=24*half+i,x=X[idx];vector<int>b(8);b[7]=loc[8];for(int j=6;j>=0;j--)b[j]=add(loc[j+1],mul(x,b[j+1]));int den=eval(b,x);if(!den)abort();int t=mul(W[idx],I[den]);for(int j=0;j<8;j++)q[j]=add(q[j],mul(t,b[j]));}
vector<int> ids,ts,touched;
for(int i=0;i<48;i++){if(i/24==half&&(mask&(1u<<(i%24))))continue;int den=eval(loc,X[i]);if(!den)abort();ids.push_back(i);ts.push_back(mul(sub(W[i],eval(q,X[i])),I[den]));}
for(int i=0;i<40;i++)for(int j=i+1;j<40;j++){
 int slope=mul(sub(ts[i],ts[j]),invdiff[ids[i]][ids[j]]);int intercept=sub(ts[i],mul(slope,X[ids[i]]));int key=289*slope+intercept;
 if(!buckets[key])touched.push_back(key);
 if(++buckets[key]!=28)continue;
 vector<int>c(10);bool desc=true;
 for(int k=0;k<10;k++){c[k]=add(k<8?q[k]:0,add(k<9?mul(intercept,loc[k]):0,k?mul(slope,loc[k-1]):0));if(k%3&&c[k])desc=false;}
 int agreement=0;for(int k=0;k<48;k++)agreement+=eval(c,X[k])==W[k];if(agreement<16)abort();
 if(desc){descending++;continue;}hits.insert(c);
}
for(int key:touched)buckets[key]=0;
if(limit&&pencils>=limit)stopped=true;}
void choose(int start,int left,int half,unsigned mask){if(stopped)return;if(!left){process(half,mask);return;}for(int i=start;i<=24-left;i++){S.push_back(i);choose(i+1,left-1,half,mask|(1u<<i));S.pop_back();if(stopped)return;}}
int main(int argc,char**argv){if(argc>1)limit=atoll(argv[1]);auto st=chrono::steady_clock::now();for(int a=0;a<289;a++){int x=a%17,y=a/17;N[a]=(17-x)%17+17*((17-y)%17);for(int b=0;b<289;b++){int z=b%17,t=b/17;A[a][b]=(x+z)%17+17*((y+t)%17);M[a][b]=(x*z+7*y*t)%17+17*((x*t+y*z)%17);}}for(int a=1;a<289;a++){for(int b=1;b<289;b++)if(M[a][b]==1)I[a]=b;if(!I[a])abort();}int zeta=59;if(power(zeta,3)!=1||zeta==1)abort();for(int i=0;i<16;i++){int t=power(i+1,11);for(int r=0;r<3;r++){X[3*i+r]=mul(t,power(zeta,r));W[3*i+r]=baseword[i];if(power(X[3*i+r],3)!=i+1)abort();}}int g=0;for(int a:{1,2})for(int b=0;b<3;b++){for(int i=0;i<24;i++)perm[g][i]=3*(i/3)+(a*(i%3)+b)%3;g++;}for(int i=0;i<48;i++)for(int j=0;j<48;j++)if(i!=j)invdiff[i][j]=I[sub(X[i],X[j])];for(int half=0;half<2;half++)choose(0,8,half,0);
cout<<"{\"field\":\"F17(theta),theta^2=7\",\"zeta\":59,\"target\":16,\"pencils\":"<<pencils<<",\"subsets_visited\":"<<visited<<",\"complete\":"<<(stopped?"false":"true")<<",\"descended_encounters\":"<<descending<<",\"hits\":[";int hi=0;for(const auto&c:hits){if(hi++)cout<<",";cout<<"{\"coefficients\":[";for(int j=0;j<10;j++){if(j)cout<<",";cout<<c[j];}cout<<"],\"support\":[";bool first=true;for(int i=0;i<48;i++)if(eval(c,X[i])==W[i]){if(!first)cout<<",";cout<<i;first=false;}cout<<"]}";}cout<<"],\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<"}\n";}
