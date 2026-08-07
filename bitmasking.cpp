#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
   int t;
   cin>>t;
   vector<int>mask(n,0);
   for(int i=0;i<t;++i){
    int n;
    cin>>n;
    int msk=0;
    for(int i=0;i<n;++i){
        int days;
        cin>>days;
        msk=(msk|(1<<days));
    }
    mask[i]=msk;
   }
   int mx=0;
   for(int i=0;i<t;++i){
    for(int j=i+1;j<t;++j){
        int common=mask[i]&mask[j];
        mx=max(mx,__builtin_popcount(common)); 
    }
   }
   cout<<mx;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}