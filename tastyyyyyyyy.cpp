#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    int n;
    cin>>n;
    vector<int>a(n);
    for(auto &itm:a) cin>>itm;
    
    vector<int>pre(n+1,0);
    for(int i=1;i<=n;++i) 
      pre[i]=pre[i-1]+a[i-1];

    int q;
    cin>>q;
    while(q--){
        int x;
        cin>>x;
        int l=1,h=n,mid;
        while(l<=h){
            mid=(l+h)/2;
            if(pre[mid]>=x) h=mid-1;
            else l=mid+1;
        }
        cout<<max(h,l)<<endl;
    }

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}