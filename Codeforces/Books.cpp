#include<bits/stdc++.h>
using namespace std;
using ll = long long;
 
void solve(){
    int n,k;
    cin>>n>>k;
    vector<int>a(n);
    for(auto &itm:a) cin>>itm;
    int r=0,l=0,cnt=0,mx=0;
    ll sum=0;
    while(r<n){
        sum+=a[r];
        cnt++;
        while(sum>k){
            sum-=a[l];
            l++;
            cnt--;
        }
        mx=max(mx,cnt);
        r++;     
    }
    cout<<mx<<endl;
 
}
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    solve();
    return 0;
}