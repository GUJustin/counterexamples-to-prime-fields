#include <array>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;
int plusT[289][289],timesT[289][289],minusT[289],invT[289];
int add(int a,int b){return plusT[a][b];} int mul(int a,int b){return timesT[a][b];} int sub(int a,int b){return add(a,minusT[b]);}
using Row=array<int,15>;using Vec=array<int,14>;
struct Space {bool ok=true;Vec point{};vector<Vec> directions;};
// Forward echelon elimination, then back-substitution for particular and free vectors.
Space linear(vector<Row> a,int n){
 int rank=0;vector<int> pivot;
 for(int col=0;col<n;col++){
  int r=rank;while(r<(int)a.size()&&!a[r][col])r++;
  if(r==(int)a.size())continue;swap(a[r],a[rank]);int iv=invT[a[rank][col]];
  for(int j=col;j<=n;j++)a[rank][j]=mul(a[rank][j],iv);
  for(int i=rank+1;i<(int)a.size();i++){int factor=a[i][col];if(!factor)continue;for(int j=col;j<=n;j++)a[i][j]=sub(a[i][j],mul(factor,a[rank][j]));}
  pivot.push_back(col);rank++;
 }
 for(int i=rank;i<(int)a.size();i++)if(a[i][n]){Space s;s.ok=false;return s;}
 Space s;
 for(int r=rank-1;r>=0;r--){int c=pivot[r],v=a[r][n];for(int j=c+1;j<n;j++)v=sub(v,mul(a[r][j],s.point[j]));s.point[c]=v;}
 for(int f=0;f<n;f++)if(find(pivot.begin(),pivot.end(),f)==pivot.end()){
  Vec v{};v[f]=1;
  for(int r=rank-1;r>=0;r--){int c=pivot[r];for(int j=c+1;j<n;j++)v[c]=sub(v[c],mul(a[r][j],v[j]));}
  s.directions.push_back(v);
 }
 return s;
}
Row normR[18],derR[18][2];set<Vec> all;long long systems[4]{},consistent[4]{},families[4]{},bases[4]{};
void visit(const Space& b,const vector<int>& selected,int f){
 int dim=b.directions.size();array<array<Row,2>,18> restricted{};
 for(int j:selected)for(int e=0;e<2;e++){
  const Row&r=derR[j][e];Row &rr=restricted[j][e];rr[dim]=r[14];
  for(int k=0;k<14;k++)rr[dim]=sub(rr[dim],mul(r[k],b.point[k]));
  for(int l=0;l<dim;l++)for(int k=0;k<14;k++)rr[l]=add(rr[l],mul(r[k],b.directions[l][k]));
 }
 auto check=[&](const vector<int>& full){
  systems[f]++;vector<Row> rows;for(int j:full)for(int e=0;e<2;e++)rows.push_back(restricted[j][e]);
  Space a=linear(rows,dim);if(!a.ok)return;consistent[f]++;
  if(!a.directions.empty()){families[f]++;return;}
  Vec v=b.point;for(int l=0;l<dim;l++)for(int k=0;k<14;k++)v[k]=add(v[k],mul(a.point[l],b.directions[l][k]));
  // Canonical B0..B4,C0..C8 output from reversed C/B input.
  Vec canonical{};for(int j=0;j<5;j++)canonical[j]=v[13-j];for(int j=0;j<9;j++)canonical[5+j]=v[8-j];all.insert(canonical);
 };
 if(f==0){check({});return;}
 for(int a=0;a<(int)selected.size();a++){
  if(f==1){check({selected[a]});continue;}
  for(int c=a+1;c<(int)selected.size();c++){
   if(f==2){check({selected[a],selected[c]});continue;}
   for(int d=c+1;d<(int)selected.size();d++)check({selected[a],selected[c],selected[d]});
  }
 }
}
int main(){
 for(int a=0;a<289;a++){
  int x=a%17,y=a/17;minusT[a]=(17-x)%17+17*((17-y)%17);
  for(int b=0;b<289;b++){int z=b%17,t=b/17;plusT[a][b]=(x+z)%17+17*((y+t)%17);timesT[a][b]=(x*z+7*y*t)%17+17*((x*t+y*z)%17);}
 }
 for(int a=1;a<289;a++){int x=a%17,y=a/17;int n=(x*x-7*y*y)%17;if(n<0)n+=17;int iv=1;while(n*iv%17!=1)iv++;invT[a]=x*iv%17+17*((17-y)*iv%17);}
 for(int i=0;i<18;i++){
  int x,w;cin>>x>>w;array<int,9> pw{};pw[0]=1;for(int k=1;k<9;k++)pw[k]=mul(pw[k-1],x);
  for(int k=0;k<9;k++)normR[i][8-k]=pw[k];for(int k=0;k<5;k++)normR[i][13-k]=mul(w,pw[k]);normR[i][14]=minusT[mul(w,w)];
  for(int k=0;k<5;k++)derR[i][0][13-k]=pw[k];derR[i][0][14]=minusT[mul(2,w)];
  for(int k=1;k<9;k++)derR[i][1][8-k]=mul(k,pw[k-1]);for(int k=1;k<5;k++)derR[i][1][13-k]=mul(k,mul(w,pw[k-1]));
 }
 // Independent bit-mask enumeration of every base subset; no recursive search.
 for(unsigned mask=0;mask<(1u<<18);mask++){
  int size=__builtin_popcount(mask),f=15-size;if(f<0||f>3)continue;bases[f]++;
  vector<int> sel;vector<Row> rows;for(int j=17;j>=0;j--)if(mask&(1u<<j)){sel.push_back(j);rows.push_back(normR[j]);}
  Space b=linear(rows,14);if(b.ok)visit(b,sel,f);
 }
 cout<<"{\"cases\":[";for(int f=0;f<4;f++){if(f)cout<<",";cout<<"{\"f\":"<<f<<",\"base_subsets\":"<<bases[f]<<",\"systems\":"<<systems[f]<<",\"consistent\":"<<consistent[f]<<",\"families\":"<<families[f]<<"}";}cout<<"],\"all_norms\":[";bool first=true;for(auto v:all){if(!first)cout<<",";first=false;cout<<"[";for(int j=0;j<14;j++){if(j)cout<<",";cout<<v[j];}cout<<"]";}cout<<"]}\n";
}
