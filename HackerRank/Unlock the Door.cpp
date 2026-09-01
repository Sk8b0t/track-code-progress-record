#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int M=1e9+7;
const int N=1e5+7;
int fact[N];

int binexp(int a,int b,int m){
	int res=1;
	while(b>0){
		if(b&1) res=(res*1LL*a)%m;
		a=(a*1LL*a)%m;
		b>>=1;
	}
	return res;
}

void solve(){
    int t;
    cin>>t;
    fact[0]=1;
    for(int i=1;i<N;++i){
    	fact[i]=(fact[i-1]*1LL*i)%M;
    }

    while(t--){
    	int n,k;
    	cin>>n>>k;
    	//kCn*n!
    	int ans=fact[k];
        ans=(ans*1LL*fact[n])%M;
    	int den=(fact[n]*1LL*fact[k-n])%M;
    	ans=(ans*1LL*binexp(den,M-2,M))%M;
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