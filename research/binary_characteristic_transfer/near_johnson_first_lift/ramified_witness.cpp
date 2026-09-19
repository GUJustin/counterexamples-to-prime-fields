#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;using U=uint32_t;const int Q=1<<21,O=Q-1,C=421,R=2580,T=29,M=129;vector<U> ex(2*O),lg(Q);U mul(U a,U b){return a&&b?ex[lg[a]+lg[b]]:0;}
int main(){U x=1;for(int i=0;i<O;i++){ex[i]=x;lg[x]=i;x<<=1;if(x&Q)x^=Q|5;}for(int i=O;i<2*O;i++)ex[i]=ex[i-O];ifstream f("ramified_diagonal_matrix.bin",ios::binary);vector<vector<U>>basis(C),proof(C);vector<U>w;int at=-1;for(int i=0;i<R;i++){vector<U>a(C+1),v(R);f.read((char*)a.data(),4*(C+1));v[i]=1;bool stored=false;for(int j=C-1;j>=0;j--)if(a[j]){if(basis[j].empty()){U z=ex[O-lg[a[j]]];for(auto&u:a)u=mul(u,z);for(int k=0;k<=i;k++)v[k]=mul(v[k],z);basis[j]=a;proof[j]=v;stored=true;break;}U z=a[j];for(int k=0;k<=j;k++)a[k]^=mul(z,basis[j][k]);a[C]^=mul(z,basis[j][C]);for(int k=0;k<=i;k++)v[k]^=mul(z,proof[j][k]);}if(!stored&&a[C]){U z=ex[O-lg[a[C]]];for(auto&u:v)u=mul(u,z);w=v;at=i;break;}}
if(at<0)return 2;ifstream l("local_relations.bin",ios::binary);vector<U>orig(M*T);for(int i=0;i<R;i++){U bank;array<U,T>v;l.read((char*)&bank,4);l.read((char*)v.data(),4*T);for(int j=0;j<T;j++)orig[bank*T+j]^=mul(w[i],v[j]);}ofstream out("ramified_contradiction.bin",ios::binary);out.write((char*)orig.data(),4*orig.size());int count=0;for(auto a:orig)count+=a!=0;cout<<"{\"first_inconsistent_reduced_row\":"<<at<<",\"nonzero_original_equation_weights\":"<<count<<",\"right_hand_side\":1}\n";}
