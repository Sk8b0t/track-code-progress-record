#include<bits/stdc++.h>
using namespace std;
using ll = long long;

bool chk(vector<int>&a,int ele){
    vector<int>b;
    for(int i=0;i<a.size();++i){
        if(a[i]!=ele) b.push_back(a[i]);
    }
    for(int i=0;i<b.size();++i){
        if(b[i]!=b[b.size()-1-i]){
            return false;
        }
    }
    return true ;
}

void solve(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int>a(n);
        for(auto &itm:a) cin>>itm;
        int cnt=0;
        for(int i=0;i<n;++i){
            if(a[i]!=a[n-1-i]){
                if(chk(a,a[i])||chk(a,a[n-1-i])) cout<<"YES"<<endl;
                else cout<<"NO"<<endl;
                cnt=0;
                break;
            }
            else cnt++;
        }
        if(cnt>0) cout<<"YES"<<endl;
    }

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}