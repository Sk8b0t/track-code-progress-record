#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    int t;
    cin>>t;
    while(t--){
        ll n,q;
        cin>>n>>q;
        vector<ll>a(n);
        vector<ll>x(q);
        for(auto &itm:a) cin>>itm;
        for(auto &itm:x) cin>>itm;
        ll chk=31;
        for(int i=0;i<q;++i){
            if(x[i]>=chk) continue;
            for(int j=0;j<n;++j){
                if(a[j]%(1LL<<x[i])==0)a[j]+=(1LL<<(x[i]-1));
            }
            chk=x[i];
            }
        for(auto &itm:a) cout<<itm<<" ";
        cout<<"\n";
    }

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}