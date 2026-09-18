#include <complex>
#include <vector>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdint>
#include <cfenv>
#include <limits>
using C=std::complex<double>;using U=uint64_t;
const U p=2130706433;
U pw(U a,U b){U r=1;for(;b;b>>=1,a=a*a%p)if(b&1)r=r*a%p;return r;}
int main(){std::cerr<<std::setprecision(17)<<"META "<<std::numeric_limits<double>::is_iec559<<" "<<(std::fegetround()==FE_TONEAREST)<<"\n";const double pi=std::acos(-1.);U omega=pw(3,(p-1)/256);U val[7][256];for(int ell=1;ell<=6;ell++)for(int j=1;j<=255;j++)val[ell][j]=pw(omega,U(ell)*j);
std::cout<<std::setprecision(17)<<"{\"p\":"<<p<<",\"omega\":"<<omega<<",\"coefficients\":[";bool comma=false;
for(int ell=0;ell<=6;ell++)for(int t=1;t<=(ell?8:1);t++){
 std::vector<C>d(137*256);d[0]=1;
 for(int j=1;j<=255;j++){
  double angle=ell?2*pi*double((U(t)*val[ell][j])%p)/double(p):0.;C ph(std::cos(angle),std::sin(angle));
  if(ell)std::cerr<<ell<<" "<<t<<" "<<j<<" "<<((U(t)*val[ell][j])%p)<<" "<<ph.real()<<" "<<ph.imag()<<"\n";
  for(int k=std::min(j,136);k>=1;k--)for(int h=0;h<256;h++)d[k*256+((h+j)&255)]+=ph*d[(k-1)*256+h];
 }
 if(comma)std::cout<<",";comma=true;std::cout<<"{\"direction\":"<<ell<<",\"harmonic\":"<<(ell?t:0)<<",\"values\":[";
 for(int h=0;h<256;h++){if(h)std::cout<<",";auto a=d[136*256+h];std::cout<<"["<<a.real()<<","<<a.imag()<<"]";}std::cout<<"]}";
}
std::cout<<"]}\n";}
