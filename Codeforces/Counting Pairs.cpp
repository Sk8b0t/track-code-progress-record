#include<bits/stdc++.h>
using namespace std;
using ll = long long;

ll logic(vector<ll>a,ll tar){
    ll cnt=0;
    int l=0,r=a.size()-1;
    while(l<r){
        if(a[l]+a[r]<=tar){
            cnt+=r-l;
            l++;
        }
        else r--;
    }
    return cnt;
}

void solve(){
    int t;
    cin>>t;
    int n,x,y;
    cin>>n>>x>>y;
    vector<ll>a(n);
    ll summ=0;
    for(auto &itm:a){
         cin>>itm;
         summ+=itm;
    }
    sort(a.begin(),a.end());
    ll L=summ-y;
    ll R=summ-x;
    cout<<logic(a,R)-logic(a,L-1);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}