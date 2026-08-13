#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    int t;
    cin>>t;
    while(t--){
        int n,k;
        cin>>n>>k;
        vector<ll>a(n);
        vector<ll>pre(n,0);
        for(auto &itm:a) cin>>itm;
        sort(a.begin(),a.end());
        pre[0]=a[0];
        for(int i=1;i<n;++i){
            pre[i]=pre[i-1]+a[i];
        }
        ll sum=0,mx=0;
        int l=0,r=0;
        for(int i=0;i<=k;++i){
            r=n-(k-i+1);
            l=2*i;
            sum=pre[r]-(l==0?0:pre[l-1]);
            mx=max(sum,mx);
        }
        cout<<mx<<endl;
    }

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}