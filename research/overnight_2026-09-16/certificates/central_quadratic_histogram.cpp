#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <numeric>
#include <string>
#include <vector>

// Exact subset DP in centered coordinates. States that cannot reach the
// prescribed first sum with the remaining cardinality are discarded.
int main(int argc,char** argv) {
    assert(argc==5 || argc==6);
    int n=std::stoi(argv[1]),t=std::stoi(argv[2]);
    std::string order=argv[3],output=argv[4];
    assert(n>1 && t>0 && t<=n/2);
    int first=(argc==6)?std::stoi(argv[5]):t*(n-1)/2;
    bool even=n%2==0;
    int unit=even?2:1,maximum_coordinate=even?n-1:(n-1)/2;
    int target=even?2*first-t*(n-1):first-t*((n-1)/2);
    int yoffset;
    if(even){int numerator=(n-2)*(4*first-t*n);assert(numerator%8==0);yoffset=numerator/8;}
    else {int center=(n-1)/2;yoffset=center*target+t*center*(center-1)/2;}
    auto second=[even](int u){return even?(u*u-1)/8:u*(u-1)/2;};
    __uint128_t bound=1;
    for(int i=1;i<=t;i++) bound=bound*(n-i+1)/i;
    assert(bound<=std::numeric_limits<uint64_t>::max());
    std::vector<int> items;
    if(order=="paired") {
        if(!even)items.push_back(0);
        for(int j=1;j<=maximum_coordinate;j+=unit){items.push_back(-j);items.push_back(j);}
    }
    else {assert(order=="linear");for(int j=-maximum_coordinate;j<=maximum_coordinate;j+=unit)items.push_back(j);}
    assert(int(items.size())==n);
    std::vector<int> allv;
    for(int u:items)allv.push_back(second(u));
    std::sort(allv.rbegin(),allv.rend());
    const int vmax=std::accumulate(allv.begin(),allv.begin()+t,0);
    std::vector<int> stride(t+1,1);
    for(int k=1;k<=t;k++)stride[k]=stride[k-1]+allv[k-1];
    std::vector<int> lower(t+1),upper(t+1);
    std::vector<std::vector<uint64_t>> dp(t+1);
    size_t bytes=0;
    for(int k=0;k<=t;k++) {
        lower[k]=std::max(-k*maximum_coordinate,target-(t-k)*maximum_coordinate);
        upper[k]=std::min(k*maximum_coordinate,target+(t-k)*maximum_coordinate);
        assert(lower[k]<=upper[k] && (upper[k]-lower[k])%unit==0);
        size_t cells=size_t((upper[k]-lower[k])/unit+1)*stride[k];
        bytes+=cells*sizeof(uint64_t);dp[k].resize(cells);
    }
    std::cerr<<"allocated_bytes="<<bytes<<" vmax="<<vmax<<"\n";
    dp[0][0]=1;
    std::vector<int> seen_u,seen_v;
    for(int u:items) {
        int v=second(u),seen=seen_u.size();
        std::sort(seen_u.begin(),seen_u.end());std::sort(seen_v.begin(),seen_v.end());
        for(int k=std::min(t,seen+1);k>=1;k--) {
            int old=k-1;
            int qlo=std::accumulate(seen_u.begin(),seen_u.begin()+old,0);
            int qhi=std::accumulate(seen_u.end()-old,seen_u.end(),0);
            qlo=std::max(qlo,lower[old]);qhi=std::min(qhi,upper[old]);
            int vlo=std::accumulate(seen_v.begin(),seen_v.begin()+old,0);
            int vhi=std::accumulate(seen_v.end()-old,seen_v.end(),0);
            vhi=std::min(vhi,stride[k]-1-v);
            if(vlo>vhi)continue;
            for(int q=qlo;q<=qhi;q+=unit) {
                int next=q+u;if(next < lower[k] || next>upper[k])continue;
                assert((q-lower[old])%unit==0 && (next-lower[k])%unit==0);
                const uint64_t* src=dp[old].data()+size_t((q-lower[old])/unit)*stride[old];
                uint64_t* dst=dp[k].data()+size_t((next-lower[k])/unit)*stride[k]+v;
                for(int j=vlo;j<=vhi;j++)dst[j]+=src[j];
            }
        }
        seen_u.push_back(u);seen_v.push_back(v);
        if(seen_u.size()%10==0)std::cerr<<"processed="<<seen_u.size()<<"\n";
    }
    std::ofstream out(output);assert(out);
    out<<"v,count\n";
    uint64_t total=0,maximum=0;int argmax=-1;
    for(int v=0;v<=vmax;v++) {
        uint64_t value=dp[t][v];out<<v<<","<<value<<"\n";total+=value;
        if(value>maximum){maximum=value;argmax=v;}
    }
    std::cout<<"{\"n\":"<<n<<",\"t\":"<<t<<",\"q\":"<<first<<",\"Y_offset\":"<<yoffset<<",\"total\":"<<total
             <<",\"maximum\":"<<maximum<<",\"argmax_v\":"<<argmax
             <<",\"vmax\":"<<vmax<<",\"allocated_bytes\":"<<bytes<<"}\n";
}
