#include <bits/stdc++.h>
using namespace std;

void solve() {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int cnt=0;
        vector<int>a(n);
        for(auto &itm:a){
            cin>>itm;
            if(itm==1) cnt++;

        }
        if((n-1)/2<cnt) cout<<"Bessie\n";
        else cout<<"Elsie\n";
    }

    
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();

  
}