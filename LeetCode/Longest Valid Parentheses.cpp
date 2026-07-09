#include<bits/stdc++.h>
using namespace std;
int longestValidParentheses(string s) {
    stack<char> st;
    unordered_map<char,int>m={{'[',-3},{'{',-2},{'(',-1},{']',3},{'}',2},{')',1}};
    int cnt=0;
    for(char c:s){
        if(m[c]<0) st.push(c);
        else{
            if(!s.empty()|| m[st.top()]+m[c]==0) cnt+=1;
        }
    }
    return cnt*2;
}
int main(){
 string s = ")()())";
 cout<<longestValidParentheses(s);



}