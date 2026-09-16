// Exhaust all rational quotient pencils from two complete fibers.
// The selected domains are small; memory is linear in the subset count.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using std::vector;

int power(int a,int e,int p){int r=1;for(;e;e>>=1,a=a*a%p)if(e&1)r=r*a%p;return r;}
struct Subset{uint64_t mask;vector<int> coefficients,values,inverses;};

void run(int p,int n,int B,bool expect_classified){
  assert(n<63 && (p-1)%n==0 && n%B==0);
  int root=0;
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
    for(int x:domain){int v=0;for(auto it=item.coefficients.rbegin();it!=item.coefficients.rend();++it)v=(v*x+*it)%p;
      item.values.push_back(v);item.inverses.push_back(inverse[v]);}
    subsets.push_back(std::move(item));
  };
  generate(generate,0,0);
  uint64_t examined=0,balanced=0,cyclic=0,dihedral=0,other=0;
  vector<int> counts(p),touched;vector<int> first_other;
  for(size_t i=0;i<subsets.size();++i)for(size_t j=i+1;j<subsets.size();++j){
    const auto &a=subsets[i],&b=subsets[j];if(a.mask&b.mask)continue;++examined;
    touched.clear();bool good=true;
    for(int x=0;x<n;++x){
      if(!a.values[x] || !b.values[x])continue;
      int label=a.values[x]*b.inverses[x]%p;
      if(!counts[label])touched.push_back(label);
      if(++counts[label]>B){good=false;break;}
    }
    if(good)for(int label:touched)if(counts[label]!=B){good=false;break;}
    for(int label:touched)counts[label]=0;
    if(!good)continue;++balanced;
    bool is_cyclic=true;
    for(int r=1;r<B;++r)if(a.coefficients[r] || b.coefficients[r])is_cyclic=false;
    bool is_dihedral=false;
    if(B==4){
      int c=a.coefficients[0];
      is_dihedral=c && c==b.coefficients[0] && !a.coefficients[1] && !a.coefficients[3]
                  && !b.coefficients[1] && !b.coefficients[3]
                  && a.coefficients[2]!=b.coefficients[2]
                  && n%4==0 && power(c,n/4,p)==p-1;
    }
    if(is_cyclic)++cyclic;
    else if(is_dihedral)++dihedral;
    else{++other;if(first_other.empty()){
      first_other=a.coefficients;first_other.insert(first_other.end(),b.coefficients.begin(),b.coefficients.end());}}
  }
  const int images=n/B;
  assert(cyclic==uint64_t(images)*(images-1)/2);
  if(B==4)assert(dihedral==uint64_t(n/4)*images*(images-1)/2);
  if(expect_classified)assert(!other);else assert(other);
  std::cout<<"{\"p\":"<<p<<",\"n\":"<<n<<",\"B\":"<<B
           <<",\"subsets\":"<<subsets.size()<<",\"disjoint_pairs_checked\":"<<examined
           <<",\"balanced_pairs\":"<<balanced<<",\"cyclic_pairs\":"<<cyclic
           <<",\"dihedral_pairs\":"<<dihedral<<",\"other_pairs\":"<<other
           <<",\"satisfies_candidate_hypotheses\":"<<(expect_classified?"true":"false")
           <<",\"first_other_coefficient_pair\":[";
  for(size_t i=0;i<first_other.size();++i)std::cout<<(i?",":"")<<first_other[i];
  std::cout<<"]}"<<std::endl;
}

int main(){
  run(13,6,3,false);
  run(97,8,4,false);
  run(109,18,3,true);
  run(193,24,3,true);
  run(193,24,4,true);
}
