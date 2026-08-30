#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
	int t;
    cin>>t;
    while(t--){
    	int n;
    	if(n<11) cout<<n<<"\n";
    	else{
         int ans=(n/10);
    	 cout<<ans+9<<"\n";
    }

    }

}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	solve();
	return 0;
}