#include<bits/stdc++.h>
using namespace std;
using ll = long long;
void solve(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string s;
        cin>>s;
        int cnt=0;
        ll ans=0;
        map<char,int>m;
        for(int i=0;i<n;++i){
            m[s[i]]++;
            if(m[s[i]]==1) cnt++;
            ans+=cnt;
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