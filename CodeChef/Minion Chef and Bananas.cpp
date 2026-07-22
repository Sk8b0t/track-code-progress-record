#include<bits/stdc++.h>
using namespace std;
using ll = long long;

bool pred(ll k,ll h,vector<ll>&a){
    ll tot=0;
    for(auto &itm:a){
         tot+=(itm+k-1)/k;
         if(tot>h) return false;
    }
    return tot<=h;
}

void solve(){
  ll n,h;
  cin>>n>>h;
  vector<ll>a(n);
  for(auto &itm:a)cin>>itm;
  ll lo=1,hi=*max_element(a.begin(),a.end()),mid;
  while(lo<=hi){
    mid=(hi+lo)/2;
    if(pred(mid,h,a)) hi=mid-1;
    else lo=mid+1;
  }
  cout<<lo<<"\n";

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--){
     solve();
    }
}