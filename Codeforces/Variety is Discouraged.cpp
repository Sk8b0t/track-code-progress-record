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
    map<int,int>m;
    for(int i=0;i<n;++i){
        cin>>a[i];
        m[a[i]]++;
        
    }
    int l=-1,r=-1,curr=0,mx=0;
    for(int i=0;i<n;++i){
        if(m[a[i]]==1) curr++;
        else curr=0;
        if(curr>mx){
            mx=curr;
            r=i;
            l=r-curr+1; 
        }
    }

    if(mx==0) cout<<0<<"\n";
    else cout<<l+1<<" "<<r+1<<"\n";
    
   }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}