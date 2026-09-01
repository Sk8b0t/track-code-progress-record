#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int M=1e9+7;

int binexp(int a,int b,int m){
	int res=1;
	while(b>0){
		if(b&1) res=(res*1LL*a)%m;
		a=(a*1LL*a)%M;
		b>>=1;
	}
	return res;
    
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout<<binexp(2,M-2,M);

}