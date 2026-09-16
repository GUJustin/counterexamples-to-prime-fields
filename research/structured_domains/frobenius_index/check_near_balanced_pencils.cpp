// Exhaust rational pencils represented by two full fibers on small subgroups.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using std::vector;

int power(int a,int e,int p){int r=1;for(;e;e>>=1,a=a*a%p)if(e&1)r=r*a%p;return r;}
int value(const vector<int>& a,int x,int p){int r=0;for(auto it=a.rbegin();it!=a.rend();++it)r=(r*x+*it)%p;return r;}
struct Subset{uint64_t mask;vector<int> coefficients,values;};

int torus_decks(const vector<int>& A,const vector<int>& V,const vector<int>& domain,int p){
  const int B=int(A.size())-1;assert(p>2*B+1);int count=0;
  for(int zeta:domain)for(int inversion=0;inversion<2;++inversion){
    bool good=true;
    for(int x=1;x<=2*B+1;++x){
      int y=zeta*(inversion?power(x,p-2,p):x)%p;
      if((value(A,x,p)*value(V,y,p)-value(A,y,p)*value(V,x,p))%p){good=false;break;}
    }
    if(good)++count;
  }
  assert(count<=B);return count;
}

void run(int p,int n,int B,uint64_t expected_qualifying){
  assert(n<63 && (p-1)%n==0 && n>=2*B);
  const int ell=(p-1)/n;int root=0;
  for(int a=2;a<p && !root;++a){
    int candidate=power(a,(p-1)/n,p);bool exact=power(candidate,n,p)==1;
    for(int d=1;d<n;++d)if(n%d==0 && power(candidate,d,p)==1)exact=false;
    if(exact)root=candidate;
  }
  assert(root);vector<int> domain(n,1),inverse(p);
  for(int i=1;i<n;++i)domain[i]=domain[i-1]*root%p;
  for(int a=1;a<p;++a)inverse[a]=power(a,p-2,p);
  vector<Subset> subsets;vector<int> selection(B);
  auto generate=[&](auto&& self,int begin,int depth)->void{
    if(depth<B){for(int i=begin;i<=n-(B-depth);++i){selection[depth]=i;self(self,i+1,depth+1);}return;}
    Subset item;item.mask=0;item.coefficients={1};
    for(int i:selection){
      item.mask|=uint64_t(1)<<i;vector<int> next(item.coefficients.size()+1);
      for(size_t j=0;j<item.coefficients.size();++j){
        next[j]=(next[j]+p-domain[i]*item.coefficients[j]%p)%p;
        next[j+1]=(next[j+1]+item.coefficients[j])%p;
      }
      item.coefficients=next;
    }
    for(int x:domain)item.values.push_back(value(item.coefficients,x,p));
    subsets.push_back(std::move(item));
  };
  generate(generate,0,0);
  uint64_t examined=0,qualifying=0,positive_defect=0,balanced_non_torus=0;
  vector<uint64_t> histogram(n+1,0),qualifying_defects(n+1,0);
  vector<int> counts(p),touched;int max_covered=0;
  for(size_t i=0;i<subsets.size();++i)for(size_t j=i+1;j<subsets.size();++j){
    const auto& A=subsets[i];const auto& V=subsets[j];
    if(A.mask&V.mask)continue;++examined;touched.clear();
    for(int x=0;x<n;++x){
      if(!A.values[x] || !V.values[x])continue;
      int label=A.values[x]*inverse[V.values[x]]%p;
      if(!counts[label])touched.push_back(label);
      ++counts[label];assert(counts[label]<=B);
    }
    int covered=2*B;
    for(int label:touched){if(counts[label]==B)covered+=B;counts[label]=0;}
    assert(covered<=n);++histogram[covered];max_covered=std::max(max_covered,covered);
    int c=n-covered;
    bool hypotheses=ell>=6 && n>6*(B-1+c);
    if(hypotheses || !c){
      int decks=torus_decks(A.coefficients,V.coefficients,domain,p);
      if(hypotheses){
        ++qualifying;++qualifying_defects[c];positive_defect+=c>0;
        assert(decks==B);
        if(2*c<B){assert(n%B==0);assert(c==0);}
      }
      if(!c && decks<B)++balanced_non_torus;
    }
  }
  assert(qualifying==expected_qualifying);
  if(ell<6 || n<=6*(B-1))assert(balanced_non_torus>0);
  std::cout<<"{\"p\":"<<p<<",\"n\":"<<n<<",\"B\":"<<B<<",\"index\":"<<ell
           <<",\"disjoint_pairs_checked\":"<<examined<<",\"maximum_complete_coverage\":"<<max_covered
           <<",\"qualifying_pencils\":"<<qualifying<<",\"positive_defect_qualifying\":"<<positive_defect
           <<",\"balanced_non_torus_negative_controls\":"<<balanced_non_torus<<",\"coverage_histogram\":{";
  bool first=true;for(int k=0;k<=n;++k)if(histogram[k]){std::cout<<(first?"":",")<<"\""<<k<<"\":"<<histogram[k];first=false;}
  std::cout<<"},\"qualifying_defect_histogram\":{";first=true;
  for(int k=0;k<=n;++k)if(qualifying_defects[k]){std::cout<<(first?"":",")<<"\""<<k<<"\":"<<qualifying_defects[k];first=false;}
  std::cout<<"}}"<<std::endl;
}

int main(){
  run(151,25,3,0);
  run(163,27,2,2106);
  run(13,6,3,0);
  run(97,8,4,0);
}
