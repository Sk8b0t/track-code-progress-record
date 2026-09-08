#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<ll>a(n);
        map<ll,ll>m;
        ll mn=INT_MAX;
        for(auto &itm:a){
            cin>>itm;
            m[itm]++;
            mn=min(mn,itm);
        }
        vector<ll>b;
        for(int i=0;i<m[mn];++i) b.push_back(mn);
        vector<ll>c;
        for(auto &itm:a){
            if(itm!=mn) c.push_back(itm);
        }
        if(c.size()>0){
        cout<<b.size()<<" "<<c.size()<<endl;
        for(auto &itm:b) cout<<itm<<" ";
        cout<<endl;
        for(auto &itm:c) cout<<itm<<" ";
        cout<<endl;
         }

     else cout<<-1<<endl;
 }

}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

#ifndef ONLINE_JUDGE
    freopen("inputf.in", "r", stdin);
    freopen("outputf.out", "w", stdout);
#endif

    solve();
    return 0;
}