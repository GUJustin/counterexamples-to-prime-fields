#include <array>
#include <vector>
#include <set>
#include <iostream>
using namespace std;
int plusT[289][289],timesT[289][289],negT[289],inverse[289];
int add(int a,int b){return plusT[a][b];}int mul(int a,int b){return timesT[a][b];}int sub(int a,int b){return add(a,negT[b]);}
int power(int a,int n){int r=1;while(n){if(n&1)r=mul(r,a);a=mul(a,a);n>>=1;}return r;}
int eval(const vector<int>&a,int x){int r=0;for(int i=a.size()-1;i>=0;i--)r=add(mul(r,x),a[i]);return r;}
unsigned rotate(unsigned mask,int k){unsigned r=0;for(int i=0;i<24;i++)if(mask&(1u<<i))r|=1u<<(3*(i/3)+(i%3+k)%3);return r;}
int main(){
 for(int a=0;a<289;a++){int x=a%17,y=a/17;negT[a]=(17-x)%17+17*((17-y)%17);for(int b=0;b<289;b++){int z=b%17,t=b/17;plusT[a][b]=(x+z)%17+17*((y+t)%17);timesT[a][b]=(x*z+7*y*t)%17+17*((x*t+y*z)%17);}}
 for(int a=1;a<289;a++){int x=a%17,y=a/17,d=(x*x-7*y*y)%17;if(d<0)d+=17;int u=1;while(u*d%17!=1)u++;inverse[a]=x*u%17+17*((17-y)*u%17);}
 int omega=2;while(power(omega,3)!=1)omega++;omega=mul(omega,omega); // opposite primitive root from smallest choice
 int word[16];for(int &w:word)cin>>w;
 int X[48],W[48],diffInv[48][48];
 // Alternate base-fiber halves, not the source's first-eight/last-eight split.
 for(int h=0;h<2;h++)for(int j=0;j<8;j++){int base=2*j+h,t=power(base+1,11);for(int r=0;r<3;r++){int i=24*h+3*j+r;X[i]=mul(t,power(omega,r));W[i]=word[base];}}
 for(int i=0;i<48;i++)for(int j=0;j<48;j++)diffInv[i][j]=i==j?0:inverse[sub(X[i],X[j])];
 long long visited=0,pencils=0,descended=0;set<vector<int>>hits;
 for(int half=0;half<2;half++)for(unsigned mask=0;mask<(1u<<24);mask++){
  if(__builtin_popcount(mask)!=8)continue;visited++;
  if(rotate(mask,1)<mask||rotate(mask,2)<mask)continue;pencils++;
  vector<int> idx,dd;for(int i=23;i>=0;i--)if(mask&(1u<<i)){idx.push_back(24*half+i);dd.push_back(W[24*half+i]);}
  // Newton divided differences, then convert to monomial coefficients.
  for(int k=1;k<8;k++)for(int i=7;i>=k;i--)dd[i]=mul(sub(dd[i],dd[i-1]),diffInv[idx[i]][idx[i-k]]);
  vector<int> q{dd[7]};for(int k=6;k>=0;k--){vector<int>b(q.size()+1);for(int j=0;j<(int)q.size();j++){b[j]=sub(b[j],mul(X[idx[k]],q[j]));b[j+1]=add(b[j+1],q[j]);}b[0]=add(b[0],dd[k]);q=b;}
  vector<int> loc{1};for(int k:idx){vector<int>b(loc.size()+1);for(int j=0;j<(int)loc.size();j++){b[j]=sub(b[j],mul(X[k],loc[j]));b[j+1]=add(b[j+1],loc[j]);}loc=b;}
  vector<int> rest,ratios;
  for(int i=0;i<48;i++){if(i/24==half&&(mask&(1u<<(i%24))))continue;int den=eval(loc,X[i]);if(!den)abort();rest.push_back(i);ratios.push_back(mul(sub(W[i],eval(q,X[i])),inverse[den]));}
  // A concurrent set of eight among forty contains a reference among the first33.
  // For each reference, seven equal slopes identify that eight-line concurrence.
  for(int ref=0;ref<33;ref++){
   array<int,289> counts{};
   for(int j=0;j<40;j++)if(j!=ref){
    int slope=mul(sub(ratios[j],ratios[ref]),diffInv[rest[j]][rest[ref]]);
    if(++counts[slope]!=7)continue;
    int intercept=sub(ratios[ref],mul(slope,X[rest[ref]]));vector<int> c(10);bool down=true;
    for(int k=0;k<10;k++){c[k]=add(k<8?q[k]:0,add(k<9?mul(intercept,loc[k]):0,k>0?mul(slope,loc[k-1]):0));if(k%3&&c[k])down=false;}
    if(down){descended++;continue;}
    int actual=0;for(int i=0;i<48;i++)actual+=eval(c,X[i])==W[i];if(actual<16)abort();hits.insert(c);
   }
  }
 }
 cout<<"{\"pass_no_nondescended_hits\":"<<(hits.empty()?"true":"false")<<",\"subsets_visited\":"<<visited<<",\"pencils\":"<<pencils<<",\"descended_encounters\":"<<descended<<",\"non_descended_hits\":"<<hits.size()<<",\"symmetry\":\"C3 deck only; no Frobenius quotient\",\"halves\":\"alternating base fibers\"}\n";
}
