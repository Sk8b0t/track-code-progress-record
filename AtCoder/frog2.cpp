#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int N=1e5+10;

int h[N];
int dp[N];
int k;

int func(int i){
    if(i==0) return 0;
    if(dp[i]!=-1) return dp[i];
    int cst=INT_MAX;
    for(int j=1;j<=k;++j){
        if(i>=j)
          cst=min(cst,func(i-j)+abs(h[i-j]-h[i]));
    } 
    return dp[i]=cst;
}

void solve(){
    
    int n;
    cin>>n>>k;
    for(int i=0;i<n;++i) cin>>h[i];
    cout<<func(n-1)<<endl;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    memset(dp,-1,sizeof(dp));
    solve();
    return 0;
}