#include <bits/stdc++.h>
using namespace std;
const int N=10e5;
int hsh[N][26];
int main (){
    int t;
    cin>>t;
    while(t--){
        int n,q;
        cin>>n>>q;
        string s;
        cin>>s;
        for(int i=0;i<n;++i){
            hsh[i+1][s[i]-'a']++;
        }
        for(int i=0;i<26;++i){
            for(int j=1;j<=n;++j){
                hsh[j][i]+=hsh[j-1][i];
            }
        }
        while(q--){
            int l,r;
            cin>>l>>r;
            int chr_cnt=0,odd_cnt=0;
            for(int i=0;i<26;++i){
                chr_cnt=hsh[r][i]-hsh[l-1][i];
                if (chr_cnt%2!=0) odd_cnt++;
            }
            if(odd_cnt>1) cout<<"NO";
            else cout<<"YES";
    }
}
}