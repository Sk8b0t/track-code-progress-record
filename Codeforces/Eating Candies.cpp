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
        int l=0,r=n-1,mx=0;
        int s=a[l],s1=a[r];
        while(r>l){
            if(s==s1){
                mx=l+1+n-r;
                ++l;
                s+=a[l];
            }
            if(s1>s){
                ++l;
                s+=a[l];
            }
            else{
                --r;
                s1+=a[r];
            }
        }
        cout <<mx<<endl;   
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}