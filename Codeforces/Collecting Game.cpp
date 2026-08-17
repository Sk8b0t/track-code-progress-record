#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<pair<ll,int>>a(n);
        for(int i=0;i<n;++i){
            cin>>a[i].first;
            a[i].second=i;
        }
        sort(a.begin(),a.end());
        vector<ll>pre(n);
        pre[0]=a[0].first;
        for(int i=1;i<n;++i){
            pre[i]=pre[i-1]+a[i].first;
        }
        vector<ll>ans(n);
        for(int i=0;i<n;++i){
            int j=i;
            while(j<n){
                pair<ll,int>tar={pre[j]+1,INT_MIN};
                ll idx=lower_bound(a.begin(),a.end(),tar)-a.begin();
                idx--;
                if(j==idx)break;
                j=idx;
            }
            ans[a[i].second]=j;
        }
        for(auto &itm:ans) 
           cout<<itm<<" ";
        cout<<"\n";
    }

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}