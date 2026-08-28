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
    	ll ans=0;
        for(int i=0;i<n;++i){
        	ans=__gcd(ans,abs(a[i]-a[n-i-1]));

        }
        cout<<ans<<endl;

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