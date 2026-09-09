#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    int n ;
    cin>>n;
    while(n--){
        string s,t;
        cin>>s>>t;
        map<int,int>m;
        string ans="";
        for(int i=0;i<t.size();++i) m[t[i]]++;
        for(int i=s.size()-1;i>=0;--i){
            if(m[s[i]]>0){
                m[s[i]]--;
                ans+=s[i];
            }
        }
        reverse(ans.begin(),ans.end());
        cout<<((ans==t)?"YES\n":"NO\n");
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