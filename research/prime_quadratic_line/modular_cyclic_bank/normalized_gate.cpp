#include <algorithm>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;using I=long long;
int pw(int a,int e,int p){int z=1;while(e){if(e&1)z=(I)z*a%p;a=(I)a*a%p;e>>=1;}return z;}
int primitive(int p){for(int g=2;;g++){bool ok=true;for(int d=1;d<p-1;d++)if((p-1)%d==0&&pw(g,d,p)==1){ok=false;break;}if(ok)return g;}}
void histout(const vector<I>&h){cout<<"{";bool f=true;for(int j=0;j<(int)h.size();j++)if(h[j]){if(!f)cout<<",";f=false;cout<<"\""<<j<<"\":"<<h[j];}cout<<"}";}
int top(const vector<I>&h,int below){for(int j=min(below,(int)h.size()-1);j>=0;j--)if(h[j])return j;return -1;}
int main(){auto start=chrono::steady_clock::now();
 for(int p:{17,97,193}){
  int g=primitive(p);
  for(int n=8;n<p;n++)if((p-1)%n==0){
   int omega=pw(g,(p-1)/n,p);vector<int>x(n);x[0]=1;for(int j=1;j<n;j++)x[j]=(I)x[j-1]*omega%p;
   const int rows=p*p;vector<uint8_t>values((size_t)rows*n),all3(rows);vector<int>c0(rows),c1(rows),c2(rows);
   for(int a=0;a<p;a++)for(int b=0;b<p;b++){
    int row=a*p+b,c=(1-a-b+2*p)%p;c0[row]=c;c1[row]=b;c2[row]=a;all3[row]=(a&&b&&c);
    for(int j=0;j<n;j++)values[(size_t)row*n+j]=((I)a*x[j]*x[j]+b*x[j]+c)%p;
   }
   vector<uint8_t>w(n,1);
   for(int m=1;m<n;m++){
    for(int j=0;j<n;j++)w[j]=(I)w[j]*x[j]%p;if(m<=2)continue;
    vector<I>hn(n+1),hf(n+1);int seed=-1,fseed=-1,best=-1,fbest=-1;
    for(int row=0;row<rows;row++){
     const uint8_t*v=values.data()+(size_t)row*n;int a=0;
     for(int j=0;j<n;j++)a+=v[j]==w[j];
     hn[a]++;if(a>best){best=a;seed=row;}if(all3[row]){hf[a]++;if(a>fbest){fbest=a;fseed=row;}}
    }
    if(hn[0])return 2;
    vector<I>h(n+1),f(n+1);I sum=0,fsum=0;
    for(int a=1;a<=n;a++){if(n*hn[a]%a||n*hf[a]%a)return 3;h[a]=n*hn[a]/a;f[a]=n*hf[a]/a;sum+=h[a];fsum+=f[a];}
    h[0]=(I)p*p*p-sum;f[0]=(I)(p-1)*(p-1)*(p-1)-fsum;
    I j1=0,j2=0,j3=0;for(int a=0;a<=n;a++){j1+=a*h[a];j2+=(I)a*(a-1)*h[a];j3+=(I)a*(a-1)*(a-2)*h[a];}
    if(h[0]<0||f[0]<0||j1!=(I)n*p*p||j2!=(I)n*(n-1)*p||j3!=(I)n*(n-1)*(n-2))return 4;
    int A=top(h,n),B=top(h,A-1),FA=top(f,n),FB=top(f,FA-1),outside=0;
    for(int a=0;a<=n;a++)if(h[a]-(a==FA?f[a]:0)>0)outside=a;
    cout<<"{\"p\":"<<p<<",\"n\":"<<n<<",\"m\":"<<m<<",\"primitive_root\":"<<g<<",\"domain_generator\":"<<omega<<",\"A\":"<<A<<",\"L\":"<<h[A]<<",\"B\":"<<B<<",\"gap\":"<<A-B<<",\"remaining_coordinates\":"<<p-n<<",\"seed\":["<<c0[seed]<<","<<c1[seed]<<","<<c2[seed]<<"],\"histogram\":";histout(h);
    cout<<",\"full_coefficients\":{\"A\":"<<FA<<",\"L\":"<<f[FA]<<",\"B_within\":"<<FB<<",\"outside_bank_max\":"<<outside<<",\"seed\":["<<c0[fseed]<<","<<c1[fseed]<<","<<c2[fseed]<<"],\"histogram\":";histout(f);
    cout<<"},\"moment_checks\":true,\"elapsed_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"}\n";cout.flush();
   }
  }
 }
}
