#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    int n;
    cin>>n;
    vector<ll>a(n);
    for(auto &itm:a) cin>>itm;
    ll mn=INT_MAX;
    for(int i=0;i<n;++i){
        mn=min(mn,abs(a[i]));
    }
    cout<<mn<<endl;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

// #ifndef ONLINE_JUDGE
//     freopen("inputf.in", "r", stdin);
//     freopen("outputf.out", "w", stdout);
// #endif

    solve();
    return 0;
}