#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    int t;
    cin>>t;
    while(t--){
    int n,k;
    cin>>n>>k;
    vector<int>a(n);
    for(auto &itm:a) cin>>itm;
    if(k==1){
        int cnt=0;
        for(int i=0;i<n-1;++i){
            if(a[i+1]-a[i]<0){
                cnt++;
                break;
            }
        }
        if(cnt==0) cout<<"YES\n";
        else cout<<"NO\n";
    }
    else cout<<"YES\n";  
}
}



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}