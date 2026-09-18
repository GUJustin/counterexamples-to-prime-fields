#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <chrono>
using namespace std;
uint32_t rot(uint32_t m,int q,int d=1){return ((m<<d)&((1u<<q)-1))|(m>>(q-d));}
uint32_t canon(uint32_t m,int q){uint32_t ans=m;for(int j=1;j<q;j++){m=rot(m,q);ans=min(ans,m);}return ans;}
int main(int argc,char**argv){string dir=argc>1?argv[1]:".";for(int q:vector<int>{5,9,15,21}){
 auto start=chrono::steady_clock::now();int r=(q-1)/2;uint32_t full=(1u<<q)-1;map<uint64_t,vector<uint32_t>> profiles;long long subsets=0;
 for(uint32_t m=(1u<<r)-1;m<=full;){
  if(canon(m,q)==m){uint64_t key=0,power=1;for(int d=1;d<=r;d++){key+=power*__builtin_popcount(m&rot(m,q,d));power*=r+1;}profiles[key].push_back(m);subsets++;}
  uint32_t c=m&-m,t=m+c;if(t>full)break;m=(((t^m)>>2)/c)|t;
 }
 auto complement=[&](uint64_t key){uint64_t out=0,power=1;for(int d=0;d<r;d++){int a=key%(r+1);key/=r+1;out+=(r-1-a)*power;power*=r+1;}return out;};
 long long good=0,pairs=0,goodprofiles=0;vector<uint32_t>allowed;ofstream file(dir+"/profiles_q"+to_string(q)+".json");file<<"{\"q\":"<<q<<",\"r\":"<<r<<",\"base\":"<<r+1<<",\"profiles\":[";bool first=true;
 for(auto &item:profiles){auto target=profiles.find(complement(item.first));if(target==profiles.end())continue;goodprofiles++;good+=item.second.size();pairs+=(long long)item.second.size()*target->second.size();for(auto m:item.second)allowed.push_back(canon(full^m,q));
 if(!first)file<<",";first=false;file<<"{\"key\":"<<item.first<<",\"target_key\":"<<target->first<<",\"C_masks\":[";for(size_t i=0;i<item.second.size();i++)file<<(i?",":"")<<item.second[i];file<<"]}";
 }
 sort(allowed.begin(),allowed.end());file<<"],\"allowed_first_support_masks\":[";for(size_t i=0;i<allowed.size();i++)file<<(i?",":"")<<allowed[i];file<<"]}\n";
 cout<<"{\"q\":"<<q<<",\"canonical_subsets\":"<<subsets<<",\"distinct_profiles\":"<<profiles.size()<<",\"compatible_profiles\":"<<goodprofiles<<",\"compatible_first_supports\":"<<good<<",\"ordered_canonical_profile_pairs\":"<<pairs<<",\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"}"<<endl;
}}
