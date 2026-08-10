#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int logic(vector<int>&a,int tar){
    int l=0,r=0,mx=0,sum=0;
    while(r<a.size()){
        sum+=a[r];
        while(sum>tar){
            sum-=a[l];
            l++;
        }
        if(sum==tar) mx=max(mx,r-l+1);
        r++;
    }
    return mx;
}

void solve(){
    int t;
    cin>>t;
    while(t--){
        int n,s;
        cin>>n>>s;
        int tot_sum=0;
        vector<int>a(n);
        for(auto &itm:a){
            cin>>itm;
            tot_sum+=itm;
        }
        if(tot_sum<s) cout<<-1<<endl;
        else{
        int ans=logic(a,s);
        cout<<n-ans<<endl;
        }

    
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}