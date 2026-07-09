#include<bits/stdc++.h>
using namespace std;
int longestValidParentheses(string s) {
    stack<int>st;
    stack<char>chk;
    unordered_map<char,int>m={{'(',-1},{')',1}};
    int cnt=0;
    vector<int>ind(s.size(),1);

   for(int i=0;i<s.size();++i){
    if(m[s[i]]<0) {
        st.push(i);
        chk.push(s[i]);
    }
    else{
        if(!st.empty() && (m[chk.top()] + m[s[i]] == 0)){
            ind[st.top()]=0;
            ind[i]=0;
            st.pop();
            chk.pop();
        }                    
    }
   }
   int l=0,r=0;
   int mx=0;
   while(r<ind.size()){
    if(ind[r]==0){
        mx=max(mx,r-l+1);
    }
    else l=r+1;
    ++r;
   }
   return mx;
   
}
int main(){
 string s ="(()";
 cout<<longestValidParentheses(s);

}