#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int M=1e9+7;

void solve(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<ll>a(n);
        vector<ll>b(n);
        for(auto &itm:a)cin>>itm;
        for(auto &itm:b)cin>>itm;
        sort(a.rbegin(),a.rend());
        sort(b.rbegin(),b.rend());
        int l=0,r=0;
        ll cnt=0;
        ll ans=1;
        while(r<n){
            if(l<n && b[r]<a[l]){
                cnt++;
                l++;
            }
            else{
                ans=(ans*cnt)%M;
                cnt--;
                r++;
            }
        }
        cout <<ans<<endl;

}
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}