#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
  int t;
  cin>>t;
  while(t--){
    int n;
    cin>>n;
    vector<ll>a(n);
    for(auto &itm:a) cin>>itm;
    set<ll>u(a.begin(),a.end());
    vector<ll>v(u.begin(),u.end());
    ll l=0;
    ll r=n-1;
    ll cnt=0,mx=0;
    for(int r=0;r<v.size();++r){
    while(v[r]-v[l]>n-1){
        l++;
    }
    mx=max(mx,r-l+1);
}
cout<<mx<<"\n";

    }

  }

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}