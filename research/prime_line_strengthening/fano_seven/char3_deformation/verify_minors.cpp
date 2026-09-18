#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
struct F{array<int,18>a{};bool zero()const{for(int x:a)if(x)return false;return true;}};
const int g[18]={1,2,1,0,2,2,1,2,0,0,2,1,2,1,0,1,0,0};
F decode(uint32_t x){F a;for(int i=0;i<18;i++){a.a[i]=x%3;x/=3;}return a;}
uint32_t encode(F x){uint32_t z=0;for(int i=17;i>=0;i--)z=z*3+x.a[i];return z;}
F sub(F x,F y){for(int i=0;i<18;i++)x.a[i]=(x.a[i]+3-y.a[i])%3;return x;}
F mul(const F&x,const F&y){int c[35]={};for(int i=0;i<18;i++)if(x.a[i])for(int j=0;j<18;j++)c[i+j]+=x.a[i]*y.a[j];for(int k=34;k>=18;k--){int v=c[k]%3;if(v)for(int j=0;j<18;j++)c[k-18+j]+=g[j]*(3-v);}F z;for(int i=0;i<18;i++)z.a[i]=c[i]%3;return z;}
F pw(F x,uint32_t n){F v=decode(1);for(;n;n>>=1,x=mul(x,x))if(n&1)v=mul(v,x);return v;}
int main(){int cases;cin>>cases;cout<<"[";for(int t=0;t<cases;t++){int mask,n;cin>>mask>>n;vector<vector<F>>a(n,vector<F>(n));for(auto&r:a)for(auto&x:r){uint32_t z;cin>>z;x=decode(z);}F det=decode(1);for(int k=0;k<n;k++){int j=k;while(j<n&&a[j][k].zero())j++;assert(j<n);if(j!=k){swap(a[j],a[k]);det=mul(det,decode(2));}F pivot=a[k][k];det=mul(det,pivot);F iv=pw(pivot,387420487);assert(encode(mul(iv,pivot))==1);for(int c=k+1;c<n;c++)a[k][c]=mul(a[k][c],iv);for(int r=k+1;r<n;r++)if(!a[r][k].zero()){F factor=a[r][k];for(int c=k+1;c<n;c++)a[r][c]=sub(a[r][c],mul(factor,a[k][c]));}}assert(!det.zero());if(t)cout<<",";cout<<"{\"triple_mask\":"<<mask<<",\"minor_size\":"<<n<<",\"determinant_univariate_encoding\":"<<encode(det)<<"}";}cout<<"]\n";}
