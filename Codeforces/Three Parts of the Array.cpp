#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    int n;
    cin>>n;
    vector<int>a(n);
    for(auto &itm:a) cin>>itm;
    ll sl=0,sr=0;
    int l=0,r=n-1;
    ll mx=0;
    while(r>=l){
        if(sl>sr){
            sr+=a[r];
            r--;
        }
        else{
            sl+=a[l];
            l++;
        }
        if(sl==sr){
            mx=max(mx,sl);
        }
    }
    cout<<mx<<endl;

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}