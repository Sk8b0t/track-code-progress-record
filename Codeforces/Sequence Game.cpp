#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    int t;
    cin>>t;
    while(t--){
    int n;
    cin>>n;
    vector<ll>b(n);
    for(auto &itm:b) cin>>itm;
    vector<ll>a;
    a.push_back(b[0]);
    for(int i=1;i<n;++i){
        if(b[i-1]>b[i]){
            a.push_back(b[i]);
            a.push_back(b[i]);
        }
        else a.push_back(b[i]);

    }
    cout<<a.size()<<endl;
    for(auto &itm:a) cout<<itm<<" ";
        cout<<"\n";


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