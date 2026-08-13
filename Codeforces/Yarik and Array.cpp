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
    int mx=a[0],sum=a[0];
    for(int i=1;i<n;++i){
        if(abs(a[i])%2!=abs(a[i-1])%2)
           sum=max(sum+a[i],a[i]);
        else sum=a[i];
        mx=max(mx,sum);
    }
    cout<<mx<<endl;
   }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}