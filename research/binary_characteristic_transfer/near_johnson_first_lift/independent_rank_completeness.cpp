#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using U=uint32_t;
static constexpr U Q=1u<<21, MOD=Q|5u, ORDER=Q-1;
std::vector<U> logarithm(Q,Q), exponent(2*ORDER);
U product(U a,U b){return a&&b?exponent[logarithm[a]+logarithm[b]]:0;}
U inverse(U a){assert(a);return exponent[ORDER-logarithm[a]];}
U slow_product(U a,U b){U result=0;while(b){if(b&1)result^=a;b>>=1;a<<=1;if(a&Q)a^=MOD;}return result;}
U read32(std::istream& in){unsigned char b[4];in.read((char*)b,4);assert(in);return U(b[0])|(U(b[1])<<8)|(U(b[2])<<16)|(U(b[3])<<24);}
int reversed_rank(std::vector<std::vector<U>> matrix,int columns){
  int rank=0, rows=matrix.size();
  for(int c=columns-1;c>=0;c--){
    int pivot=rows-1;while(pivot>=rank&&!matrix[pivot][c])--pivot;
    if(pivot<rank)continue;
    std::swap(matrix[pivot],matrix[rank]);
    U scale=inverse(matrix[rank][c]);
    for(int j=0;j<c;j++)matrix[rank][j]=product(matrix[rank][j],scale);
    matrix[rank][c]=1;
    for(int i=rank+1;i<rows;i++)if(matrix[i][c]){
      U factor=matrix[i][c];matrix[i][c]=0;
      for(int j=0;j<c;j++)matrix[i][j]^=product(factor,matrix[rank][j]);
    }
    ++rank;
  }
  return rank;
}
struct Bank {U z;std::vector<U> h;std::vector<int> support;};
int main(){
  U current=1;
  for(U i=0;i<ORDER;i++){
    assert(current&&current<Q&&logarithm[current]==Q);
    logarithm[current]=i;exponent[i]=current;
    current<<=1;if(current&Q)current^=MOD;
  }
  assert(current==1);
  for(U i=ORDER;i<2*ORDER;i++)exponent[i]=exponent[i-ORDER];
  for(U i=1;i<=256;i++){
    U a=(i*7919u)%Q,b=(i*104729u)%Q;
    assert(product(a,b)==slow_product(a,b));
  }
  std::ifstream fixture("fixture.txt");int N,K,M,T;fixture>>N>>K>>M>>T;
  assert(N==128&&K==8&&M==129&&T==29);
  std::vector<U>x(N),f(N),g(N);
  for(int i=0;i<N;i++)fixture>>x[i]>>f[i]>>g[i];
  std::vector<Bank> banks(M);
  for(auto& bank:banks){int a,b;fixture>>a>>b>>bank.z;bank.h.resize(K);bank.support.resize(T);
    for(auto& v:bank.h)fixture>>v;for(auto& v:bank.support)fixture>>v;assert(fixture);}
  const int G=3*N, count=M*(T-K-1);
  std::vector<std::vector<std::vector<U>>> local(M);
  std::vector<std::vector<U>> derivatives(M,std::vector<U>(T));
  int min_local=T,max_local=0;
  for(int bi=0;bi<M;bi++){
    auto& bank=banks[bi];local[bi].assign(T,std::vector<U>(K+1));
    for(int ri=0;ri<T;ri++){
      int i=bank.support[ri];assert(i>=0&&i<N);
      U power=1;
      for(int j=0;j<K;j++){local[bi][ri][j]=power;power=product(power,x[i]);}
      local[bi][ri][K]=g[i];
      U derivative=0;
      for(int j=1;j<K;j+=2)derivative^=product(bank.h[j],local[bi][ri][j-1]);
      derivatives[bi][ri]=derivative;
    }
    int rank=reversed_rank(local[bi],K+1);
    min_local=std::min(min_local,rank);max_local=std::max(max_local,rank);assert(rank==K+1);
  }
  std::ifstream reduced("reduced_matrix.bin",std::ios::binary),relations("local_relations.bin",std::ios::binary);
  std::vector<std::vector<U>> global(count,std::vector<U>(G));
  for(int row=0;row<count;row++){
    for(int c=0;c<G;c++){global[row][c]=read32(reduced);assert(global[row][c]<Q);}
    (void)read32(reduced); // RHS is irrelevant to tangent-kernel rank.
    U bi=read32(relations);assert(bi<(U)M);
    std::vector<U> expected(G),local_sum(K+1);
    for(int ri=0;ri<T;ri++){
      U weight=read32(relations);assert(weight<Q);
      int i=banks[bi].support[ri];
      expected[i]^=product(weight,derivatives[bi][ri]);
      expected[N+i]^=weight;
      expected[2*N+i]^=product(weight,banks[bi].z);
      for(int j=0;j<K+1;j++)local_sum[j]^=product(weight,local[bi][ri][j]);
    }
    assert(std::all_of(local_sum.begin(),local_sum.end(),[](U a){return a==0;}));
    assert(expected==global[row]);
  }
  assert(reduced.peek()==std::char_traits<char>::eof());
  assert(relations.peek()==std::char_traits<char>::eof());
  int global_rank=reversed_rank(global,G);
  assert(global_rank==347);
  int total_columns=G+M*(K+1), rank_lower_bound=global_rank+M*(K+1);
  const int expected_kernel_dimension=37;
  std::ifstream basis_input("tangent_basis.bin",std::ios::binary);
  std::vector<std::vector<U>> basis(expected_kernel_dimension,std::vector<U>(total_columns));
  for(auto& vector:basis)for(auto& value:vector){value=read32(basis_input);assert(value<Q);}
  assert(basis_input.peek()==std::char_traits<char>::eof());
  int basis_rank=reversed_rank(basis,total_columns);
  assert(basis_rank==expected_kernel_dimension);
  for(int bi=0;bi<M;bi++)for(int ri=0;ri<T;ri++){
    int i=banks[bi].support[ri],offset=G+bi*(K+1);
    for(const auto& vector:basis){
      U value=product(vector[i],derivatives[bi][ri])^vector[N+i]^product(vector[2*N+i],banks[bi].z);
      for(int j=0;j<K+1;j++)value^=product(vector[offset+j],local[bi][ri][j]);
      assert(value==0);
    }
  }
  assert(total_columns-rank_lower_bound==basis_rank);
  std::cout<<"{\"PASS\":true,\"local_rank_min\":"<<min_local
           <<",\"local_rank_max\":"<<max_local<<",\"verified_local_banks\":"<<M
           <<",\"original_relation_rows_reconstructed\":"<<count
           <<",\"reduced_coefficient_rank\":"<<global_rank
           <<",\"original_jacobian_rank_lower_bound\":"<<rank_lower_bound
           <<",\"original_columns\":"<<total_columns
           <<",\"kernel_dimension_upper_bound\":"<<total_columns-rank_lower_bound
           <<",\"saved_tangent_basis_rank\":"<<basis_rank
           <<",\"all_saved_vectors_in_original_kernel\":true"
           <<",\"original_kernel_complete\":true"
           <<",\"pivot_order\":\"reverse columns, bottom-first row selection\"}\n";
}
