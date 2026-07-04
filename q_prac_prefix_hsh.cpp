#include <bits/stdc++.h>
using namespace std;
const int N=10e5+10;
int hsh[26][N];
int main(){
    int t;
    cin>>t;
    while(t--){
        int n,q;
        cin>>n>>q;
        for(int i=0;i<26;++i){
            for(int j=0;j<=n;++j){
               hsh[i][j]=0;
            }
        }
        string s;
        cin>>s;
        for(int i=0;i<n;++i){
            hsh[s[i]-'a'][i+1]++;
        }
        for(int i=0;i<26;++i){
            for(int j=1;j<=n;++j){
                hsh[i][j]+=hsh[i][j-1];
            }
        }
        while(q--){
            int l,r;
            cin>>l>>r;
            int chr_cnt=0,odd_cnt=0;
            for(int i=0;i<26;++i){
                chr_cnt=hsh[i][r]-hsh[i][l-1];
                if(chr_cnt%2!=0) odd_cnt++;
            }
            if(odd_cnt>1) cout<<"NO"<<endl;
            else cout<<"YES"<<endl;
        }

        }
    }

