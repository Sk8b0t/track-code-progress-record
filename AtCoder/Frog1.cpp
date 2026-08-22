#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int N=1e6+10;

int h[N];
int dp[N];

int func(int i){
    int cst=INT_MAX;
    if(i==0) return 0;
    if(dp[i]!=-1) return dp[i];
    
    cst=min(cst,func(i-1)+abs(h[i]-h[i-1]));
    if(i>1) cst=min(cst,func(i-2)+abs(h[i]-h[i-2]));
    return dp[i]=cst;

}

void solve(){
    int n;
    cin>>n;
    for(int i=0;i<n;++i){
        cin>>h[i];
    }
    cout<<func(n-1)<<endl;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    memset(dp,-1,sizeof(dp));
    solve();
    return 0;
}