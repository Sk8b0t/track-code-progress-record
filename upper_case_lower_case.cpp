#include<bits/stdc++.h>
using namespace std;
using ll = long long;

string printBinary(int n){
    string s;
    while(n>=1){
        s+=to_string(n%2);
        n=n>>1;
    }
    reverse(s.begin(),s.end());
    return s;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout<<printBinary(19)<<endl;
    for(char c='a';c<='d';c++){
        cout<<c<<" "<<printBinary(int(c))<<endl;
        cout<< char(c&(~(1<<5)))<<" "<<printBinary(int(c&(~(1<<5))))<<endl;
    }
    cout<<char('C'|' ')<<endl;
    cout<<char('c'&'_');
    return 0;
}