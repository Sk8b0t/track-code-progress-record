#include <bits/stdc++.h>
using namespace std;
string isBalanced(string s) {
    stack<char>st;
    unordered_map<char,int>m={{'[',-1},{'{',-2},{'(',-3},{']',1},{'}',2},{')',3}};
    for(char c:s){
        if (m[c]<0) st.push(c);
        else{
            if(st.empty()) return "NO";
            if(m[st.top()]+m[c]!=0) return "NO";
            st.pop();
        }
    }
    if(st.empty()) return "YES";
    else return "NO";
}
int main(){
    int t;
    cin>>t;
    while(t--){
        string s;
        cin>>s;
        cout<<isBalanced(s)<<endl;
        
    }
}
