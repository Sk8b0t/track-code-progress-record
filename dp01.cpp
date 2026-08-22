#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int N=1e5+5;
int dp[N];

int fib(int n){
    if(n==0) return 0;
    if(n==1)return 1;
    if(dp[n]==-1) return dp[n];
    return dp[n]=fib(n-1)+fib(n-2);

}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    memset(dp,-1,sizeof(dp));
    cout<<fib(3)<<endl;
    
    

    return 0;
}