#include<bits/stdc++.h>
using namespace std;
using ll = long long;

bool pred(ll mid,vector<ll>&a,ll c){
    ll sm=0;
    for(int i=0;i<a.size();++i){
        ll side=a[i]+(2*mid);
        if(side>1e9+4) return false;
        sm+=(side*side);
        if(sm>c) return false;
    }
    return sm<=c;
}

void solve(){
    int t;
    cin>>t;
    while(t--){
        ll n,c;
        cin>>n>>c;
        vector<ll>a(n);
        for(auto &itm:a) cin>>itm;
        ll l=1,h=1e9+4;
        while(h>=l){
            ll mid=(l+h)/2;
            if(pred(mid,a,c)) l=mid+1;
            else h=mid-1;
            
        }
        cout<<h<<endl;
    }

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}