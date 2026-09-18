#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int pw(int a,int b,int p){long long r=1;for(;b;b>>=1,a=(long long)a*a%p)if(b&1)r=r*a%p;return r;}
bool prime(int p){if(p<2)return false;for(int d=2;d*d<=p;d++)if(p%d==0)return false;return true;}
int main(){long long shapes=0,cosets=0,fullpass=0,deleted=0;int bestmissing=999999,bp=0,bL=0,bb=0;vector<int> hits;for(int p=3;p<=5000;p+=2)if(prime(p)){
 vector<int> fs;int v=p-1;for(int d=2;d*d<=v;d++)if(v%d==0){fs.push_back(d);while(v%d==0)v/=d;}if(v>1)fs.push_back(v);int gen=2;for(;;gen++){bool ok=true;for(int d:fs)if(pw(gen,(p-1)/d,p)==1)ok=false;if(ok)break;}
 for(int L=4;L<p;L++)if((p-1)%L==0){int m=(p-1)/L,s=L-1;if(m<2||2*s*s>=7*p||s*(s-1)<2*(p-1)||7*m<=2*s)continue;shapes++;
 vector<int> H;int z=1,step=pw(gen,m,p);for(int j=0;j<L;j++){H.push_back(z);z=(long long)z*step%p;}
 int b=1;for(int c=1;c<m;c++){b=(long long)b*gen%p;cosets++;vector<int> count(p,0);for(int i=0;i<L;i++)for(int j=i+1;j<L;j++){int q=(long long)((b-H[i]+p)%p)*((b-H[j]+p)%p)%p;count[q]++;}int missing=0;for(int y=1;y<p;y++)missing+=count[y]==0;if(missing<bestmissing){bestmissing=missing;bp=p;bL=L;bb=b;}if(missing)continue;fullpass++;
 for(int h:H){deleted++;vector<int> cur=count;int a=(b-h+p)%p;for(int x:H)if(x!=h)cur[(long long)a*((b-x+p)%p)%p]--;int miss=0;for(int y=1;y<p;y++)miss+=cur[y]==0;if(!miss){cout<<"HIT "<<p<<" "<<L<<" "<<m<<" "<<b<<" "<<h<<"\n";hits.push_back(p);}}
 }
 }
 }cout<<"COUNTS "<<shapes<<" "<<cosets<<" "<<fullpass<<" "<<deleted<<" "<<hits.size()<<"\n";cout<<"BEST "<<bestmissing<<" "<<bp<<" "<<bL<<" "<<bb<<"\n";}
