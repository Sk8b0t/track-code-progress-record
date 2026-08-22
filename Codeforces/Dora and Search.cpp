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
        int r=n-1,l=0;
        int mn=1,mx=n;
        while(l<r){
            if(a[l]==mn){
                l++;
                mn++;
            }
            else if(a[l]==mx){
                l++;
                mx--;
            }
            else if(a[r]==mx){
                r--;
                mx--;
            }
            else if(a[r]==mn){
                r--;
                mn++;
            }
            else break;

        }
        if(r-l>1) cout<<l+1<<" "<<r+1<<endl;
        else cout<<-1<<endl;
    }

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}