#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    int t;
    cin>>t;
    while(t--){
        ll n,k;
        cin>>n>>k;
        vector<ll>a(n);
        vector<ll>h(n);
        for(auto &itm:a)cin>>itm;
        for(auto &itm:h)cin>>itm;
        ll l=0,r=0,mx=0,sm=0;
        while(r<n){
            if(r!=0 &&h[r-1]%h[r]!=0){
                l=r;
                sm=0;
            }
            sm+=a[r];
            while(sm>k){
                sm-=a[l];
                l++;
            }
            mx=max(mx,r-l+1);
            r++;
        }
        cout<<mx<<endl;

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