#include<bits/stdc++.h>
using namespace std;
int longestValidParentheses(string s) {
    unordered_map<char,int>m={{'(',-1},{')',1}};
    vector<int>ind(s.size(),1);
    stack<char>chk;
    stack<int>st;

    for(int i=0;i<s.size();++i){
        if(m[s[i]]<0){
            chk.push(s[i]);
            st.push(i);
        }
        else{
            if(!st.empty()&&(m[st.top()]+m[i]==0)){
                ind[st.top()]=0;
                ind[i]=0;
                st.pop();
                chk.pop();
            }
        }
    }
    vector<int>ans;
    int l=0,r=0,mx=0;
    while(r<s.size()){
        if(ind[r]==0) mx=max(mx,r-l+1);
        else l=r+1;
        ++r;

        }
        return mx;
    }

int main(){
    string s="(()))";
    cout<<longestValidParentheses(s)<<endl;
}

