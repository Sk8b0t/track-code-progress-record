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
      map<ll,ll>m;
      for(auto &itm:a){
       cin>>itm;
       m[itm]++;
    }
      ll mx=0;
      for(auto itm:m){
         mx=max(mx,itm.second);
      }
      if(mx==n){
         cout<<0<<endl;
         continue;
      }
      ll cnt=0;
      for(int i=mx;i<n;i*=2){
         cnt++;
      }
      cout<<cnt+(n-mx)<<endl;


    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

#ifndef ONLINE_JUDGE
    freopen("inputf.in", "r", stdin);
    freopen("outputf.out", "w", stdout);
#endif

    solve();
    return 0;
        
}