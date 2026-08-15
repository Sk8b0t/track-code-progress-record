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
        int ans=-1;
        for(int i=0;i<n;++i){
            if(a[i]!=i){
                if(ans==-1)
                   ans=a[i];
                else 
                    ans&=a[i];
            }
        }
        cout<<ans<<endl;

    }
    

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}