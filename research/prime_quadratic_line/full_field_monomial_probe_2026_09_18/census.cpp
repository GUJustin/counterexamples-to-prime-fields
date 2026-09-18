#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>

using namespace std;

static int power(int x, int e, int p) {
    int result = 1;
    for (; e; e >>= 1, x = x*x % p) if (e & 1) result = result*x % p;
    return result;
}

static int threshold(int p, int numerator, int denominator) {
    int a = 0;
    while (int64_t(a)*a*denominator*denominator < int64_t(numerator)*numerator*p) ++a;
    return a;
}

static void print_histogram(const vector<int64_t>& hist) {
    cout << '{';
    bool first = true;
    for (int a = 0; a < int(hist.size()); ++a) if (hist[a]) {
        if (!first) cout << ',';
        first = false;
        cout << '"' << a << "\":" << hist[a];
    }
    cout << '}';
}

int main(int argc, char** argv) {
    const auto started = chrono::steady_clock::now();
    for (int arg = 1; arg < argc; ++arg) {
        const int p = atoi(argv[arg]);
        if (p != 31 && p != 43 && p != 61 && p != 101) throw runtime_error("unapproved prime");
        for (int d = 2; d*d <= p; ++d) if (p % d == 0) throw runtime_error("not prime");
        vector<int> x2(p), word(p), counts(p);
        for (int x = 0; x < p; ++x) x2[x] = x*x % p;
        for (int e = 3; e <= p - 1; ++e) {
            for (int x = 0; x < p; ++x) word[x] = power(x, e, p);
            vector<int64_t> hist(p+1), full_hist(p+1);
            for (int a = 0; a < p; ++a) for (int b = 0; b < p; ++b) {
                fill(counts.begin(), counts.end(), 0);
                for (int x = 0; x < p; ++x) {
                    int c = (word[x] - a*x2[x] - b*x) % p;
                    if (c < 0) c += p;
                    ++counts[c];
                }
                for (int c = 0; c < p; ++c) {
                    ++hist[counts[c]];
                    if (a && b && c) ++full_hist[counts[c]];
                }
            }
            int64_t m0=0,m1=0,m2=0,m3=0;
            for (int a = 0; a <= p; ++a) {
                m0 += hist[a]; m1 += a*hist[a];
                m2 += int64_t(a)*(a-1)/2*hist[a];
                m3 += int64_t(a)*(a-1)*(a-2)/6*hist[a];
            }
            if (m0 != int64_t(p)*p*p || m1 != int64_t(p)*p*p ||
                m2 != int64_t(p)*(p-1)/2*p || m3 != int64_t(p)*(p-1)*(p-2)/6)
                throw runtime_error("interpolation moment failure");
            int maximum = p, full_maximum = p;
            while (!hist[maximum]) --maximum;
            while (!full_hist[full_maximum]) --full_maximum;
            cout << "{\"p\":" << p << ",\"n\":" << p << ",\"e\":" << e
                 << ",\"histogram\":";
            print_histogram(hist);
            cout << ",\"full_coefficient_histogram\":";
            print_histogram(full_hist);
            cout << ",\"maximum\":" << maximum << ",\"maximizer_count\":" << hist[maximum]
                 << ",\"full_coefficient_maximum\":" << full_maximum
                 << ",\"full_coefficient_maximizer_count\":" << full_hist[full_maximum]
                 << ",\"threshold_profiles\":[";
            const array<pair<int,int>,3> constants = {{{1,2},{1,1},{13,10}}};
            bool first = true;
            for (auto [num, den] : constants) {
                const int A = threshold(p,num,den);
                int64_t L=0, LF=0;
                for (int a=A; a<=p; ++a) {L+=hist[a]; LF+=full_hist[a];}
                if (!first) cout << ',';
                first = false;
                cout << "{\"c_numerator\":" << num << ",\"c_denominator\":" << den
                     << ",\"A\":" << A << ",\"list_size\":" << L
                     << ",\"full_coefficient_list_size\":" << LF << '}';
            }
            cout << "],\"interpolation_moments_verified\":true,\"elapsed_seconds\":"
                 << chrono::duration<double>(chrono::steady_clock::now()-started).count() << "}\n";
        }
    }
}
