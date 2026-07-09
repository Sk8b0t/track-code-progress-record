#include <bits/stdc++.h>
using namespace std;
bool isValid(string s) {
    unordered_map<char,int>m={{'[',-3},{'{',-2},{'(',-1},{']',3},{'}',2},{')',1}};
    stack<char> st;
    for(char ch:s){
        if(m[ch]<0) st.push(ch);
        else{
            if(st.empty()|| m[st.top()]+m[ch]!=0) return false;
            st.pop();
        }   
    }
    if(st.empty()) return true;
    else return false;
}

int main(){
    string s="(]";
    cout<<isValid(s)<<endl;


}