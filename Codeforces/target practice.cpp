#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    int t;
    cin>>t;
    while(t--){
    vector<string>a(10);
    for(auto &itm:a) cin>>itm;
    int sm=0;
    for(int i=0;i<10;++i){
        for(int j=0;j<10;++j){
            if(a[i][j]=='X') {
                int id=min(i,10-i-1);
                int jd=min(j,10-j-1);
                sm+=min(id,jd)+1;
        }
    }
}
    cout<<sm<<endl;

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