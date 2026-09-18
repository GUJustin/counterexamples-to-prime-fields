#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
const int q=841,p=29;
vector<int> ad(q*q),mu(q*q);int iv[q],ng[q];
inline int add(int a,int b){return ad[a*q+b];}inline int mul(int a,int b){return mu[a*q+b];}
int pw(int a,int n){int b=1;for(;n;n>>=1,a=mul(a,a))if(n&1)b=mul(a,b);return b;}
int nodes[28],words[28],row[28][10];long long tested=0,hits=0,points=0,unresolved=0;long long nullities[11]={};ofstream hout;
int eval(const array<int,10>& v,int x){int y=0;for(int i=7;i>=0;i--)y=add(mul(y,x),v[i]);return y;}
void check(array<int,10> v){points++;if(!v[8]&&!v[9])return;
 if(v[8]){int b=mul(ng[v[9]],iv[v[8]]);for(int x:nodes)if(x==b)return;if(!eval(v,b))return;}
 else if(!v[7])return;
 vector<int>s;for(int i=0;i<28;i++)if(eval(v,nodes[i])==mul(add(mul(v[8],nodes[i]),v[9]),words[i]))s.push_back(i);
 if(s.size()<14)return;hits++;
 hout<<"{\"coefficients\":[";for(int i=0;i<10;i++)hout<<(i?",":"")<<v[i];hout<<"],\"support\":[";for(int i=0;i<(int)s.size();i++)hout<<(i?",":"")<<s[i];hout<<"]}\n";hout.flush();
}
void run(vector<int>&sel){int a[14][10];for(int i=0;i<14;i++)copy(row[sel[i]],row[sel[i]]+10,a[i]);int rank=0;vector<int>piv;
 for(int j=0;j<10;j++){int z=rank;while(z<14&&!a[z][j])z++;if(z==14)continue;for(int k=0;k<10;k++)swap(a[z][k],a[rank][k]);int inv=iv[a[rank][j]];for(int k=j;k<10;k++)a[rank][k]=mul(a[rank][k],inv);
 for(int i=0;i<14;i++)if(i!=rank&&a[i][j]){int f=ng[a[i][j]];for(int k=j;k<10;k++)a[i][k]=add(a[i][k],mul(f,a[rank][k]));}piv.push_back(j);rank++;}
 tested++;nullities[10-rank]++;if(rank==10)return;vector<array<int,10>>bas;
 for(int j=0;j<10;j++)if(find(piv.begin(),piv.end(),j)==piv.end()){array<int,10>v={};v[j]=1;for(int i=0;i<rank;i++)v[piv[i]]=ng[a[i][j]];bas.push_back(v);}
 if(bas.size()==1)check(bas[0]);
 else if(bas.size()==2){check(bas[1]);for(int c=0;c<q;c++){auto v=bas[0];for(int j=0;j<10;j++)v[j]=add(v[j],mul(c,bas[1][j]));check(v);}}
 else{unresolved++;for(auto v:bas)check(v);}
}
int main(int argc,char**argv){for(int a=0;a<q;a++){ng[a]=((p-a%p)%p)+p*((p-a/p)%p);for(int b=0;b<q;b++){ad[a*q+b]=(a%p+b%p)%p+p*((a/p+b/p)%p);mu[a*q+b]=((a%p)*(b%p)+2*(a/p)*(b/p))%p+p*(((a%p)*(b/p)+(a/p)*(b%p))%p);}}
 for(int a=1;a<q;a++)iv[a]=pw(a,q-2);
 ifstream in(argv[1]);hout.open(argv[2]);int np;in>>np;for(int i=0;i<28;i++){in>>nodes[i]>>words[i];row[i][0]=1;for(int j=1;j<8;j++)row[i][j]=mul(row[i][j-1],nodes[i]);row[i][8]=ng[mul(nodes[i],words[i])];row[i][9]=ng[words[i]];}
 for(int t=0;t<np;t++){int f;in>>f;vector<int>F(f),E(f);for(int&i:F)in>>i;for(int&i:E)in>>i;vector<int>single,sel;
 for(int j=0;j<14;j++){if(find(F.begin(),F.end(),j)!=F.end()){sel.push_back(2*j);sel.push_back(2*j+1);}else if(find(E.begin(),E.end(),j)==E.end())single.push_back(j);}
 int fixed=sel.size();for(int mask=0;mask<(1<<((int)single.size()-1));mask++){sel.resize(fixed);sel.push_back(2*single[0]);for(int k=1;k<(int)single.size();k++)sel.push_back(2*single[k]+((mask>>(k-1))&1));run(sel);}
 }
 cout<<"{\"patterns\":"<<tested<<",\"hits\":"<<hits<<",\"projective_points_tested\":"<<points<<",\"higher_dimensional_unresolved\":"<<unresolved<<",\"nullities\":[";for(int i=0;i<=10;i++)cout<<(i?",":"")<<nullities[i];cout<<"]}\n";
}
