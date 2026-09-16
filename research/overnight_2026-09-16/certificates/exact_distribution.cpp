// Exact conditional distribution of sum binom(a,2), with reachability pruning.
// Counts fit uint64_t: every intermediate count is at most binom(64,32).
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <string>
#include <utility>
#include <vector>

struct Histogram { int low = 0; std::vector<uint64_t> counts; };
using Key = std::pair<int,int>;
using Rows = std::map<Key,Histogram>;

void accumulate(Histogram &dst, const Histogram &src, int shift) {
    int low=src.low+shift, high=low+int(src.counts.size());
    if (dst.counts.empty()) { dst.low=low; dst.counts=src.counts; return; }
    int old_high=dst.low+int(dst.counts.size());
    if (low<dst.low) {
        dst.counts.insert(dst.counts.begin(),dst.low-low,0);
        dst.low=low;
    }
    if (high>old_high) dst.counts.resize(high-dst.low,0);
    for (size_t j=0;j<src.counts.size();++j) {
        auto &v=dst.counts[low-dst.low+j];
        assert(std::numeric_limits<uint64_t>::max()-v>=src.counts[j]);
        v+=src.counts[j];
    }
}

int main(int argc,char **argv) {
    assert(argc==5);
    int n=std::stoi(argv[1]),t=std::stoi(argv[2]),q=std::stoi(argv[3]);
    assert(1<=n && n<=64 && 0<=t && t<=n && q>=0);
    Rows rows; rows[{0,0}]={0,{1}};
    size_t peak_states=1, peak_cells=1;
    for (int a=n-1;a>=0;--a) {
        Rows next;
        for (const auto &[key,hist]: rows) for (int take=0;take<=1;++take) {
            int size=key.first+take,total=key.second+take*a,need=t-size;
            if (need<0 || need>a) continue;
            int minimum=need*(need-1)/2,maximum=need*(2*a-need-1)/2;
            if (total+minimum>q || total+maximum<q) continue;
            accumulate(next[{size,total}],hist,take*a*(a-1)/2);
        }
        rows=std::move(next);
        size_t cells=0;
        for (const auto &[key,hist]:rows) cells+=hist.counts.size();
        peak_states=std::max(peak_states,rows.size());
        peak_cells=std::max(peak_cells,cells);
        if (n==64) std::cerr << "remaining=" << a << " states=" << rows.size()
                           << " cells=" << cells << '\n';
    }
    std::ofstream out(argv[4]); assert(out);
    out << "y,count\n";
    auto it=rows.find({t,q});
    if (it!=rows.end()) {
        const auto &h=it->second;
        for (size_t j=0;j<h.counts.size();++j)
            if (h.counts[j]) out << h.low+j << ',' << h.counts[j] << '\n';
    }
    assert(out.good());
    std::cerr << "peak_states=" << peak_states << " peak_cells=" << peak_cells << '\n';
}
