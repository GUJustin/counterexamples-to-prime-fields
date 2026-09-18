#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int q,r; vector<int>a;
void rec(int start){
 if((int)a.size()==r){
  unsigned mask=0;for(int x:a)mask|=1u<<x;
  for(int s=1;s<q;s++){unsigned t=0;for(int x:a)t|=1u<<((x+s)%q);if(t<mask)return;}
  vector<int>counts(q);for(int x:a)for(int y:a)counts[(x-y+q)%q]++;
  cout<<mask;for(int d=1;d<=r;d++)cout<<' '<<counts[d];cout<<'\n';return;
 }
 for(int x=start;x<=q-(r-(int)a.size());x++){a.push_back(x);rec(x+1);a.pop_back();}
}
int main(int argc,char**argv){q=stoi(argv[1]);r=(q-1)/2;rec(0);}
