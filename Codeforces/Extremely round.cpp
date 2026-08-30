#include<bits/stdc++.h>
using namespace std;
using ll = long long;

bool chk(ll i){
	ll zero_cnt=0,dig_cnt=0;
	while(i){
		ll r=i%10;
		if(r==0) zero_cnt++;
		dig_cnt++;
		i=i/10;
	}
	return zero_cnt==dig_cnt-1;


}

void solve(){
    int t;
    cin>>t;
    vector<ll>A;
    for(ll i=1;i<=999999;++i){
    	if(chk(i)) A.push_back(i);
    }
    while(t--){
    	ll n;
    	cin>>n;
    	ll cnt=0;
    	for(int i=0;i<A.size();++i){
    		if(n>=A[i]) cnt++;
    		else break;
    	}
    	cout<<cnt<<endl;
    	
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