#include<bits/stdc++.h>
using namespace std;
vector<int> nextGreaterElement(vector<int>&v1,vector<int>&v){
    vector<int>ind(v.size());
    stack<int> st;

    for(int i=0;i<v.size();++i){
        while(!st.empty()&&v[i]>v[st.top()]){
            ind[st.top()]=i;
            st.pop();
        }
        st.push(i);
    }
    while(!st.empty()){
        ind[st.top()]=-1;
        st.pop();
    }

    map<int,int>m;
    for(int i=0;i<v.size();++i){
        if(ind[i]<0) m[v[i]]=-1;
        else m[v[i]]=v[ind[i]];
    }
    vector<int>ans;
    for(auto &item: v1) ans.push_back(m[item]);
    return ans;

}
int main(){
    vector<int>nums1={4,1,2};
    vector<int>nums2={1,3,4,2};
    auto x =nextGreaterElement(nums1,nums2);
    for(auto &i:x) cout<<i<<" ";

}