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
       int tot=0;
       bool chk=false;
       for(int i=0;i<n;++i){
          if(i+2<n &&s[i]=='.'&& s[i+1]=='.'&&s[i+2]=='.')
              chk=true;
         if(s[i]=='.') tot++;

       }
       if(chk) cout<<2<<endl;
       else cout<<tot<<endl;
}
}



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}