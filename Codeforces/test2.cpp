#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
	int t;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		vector<int>a(n);
		for(auto &itm:a) cin>>itm;
		if(a[0]==1) cout<<"YES\n";
	    else cout<<"NO\n";
		
	}
    
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}