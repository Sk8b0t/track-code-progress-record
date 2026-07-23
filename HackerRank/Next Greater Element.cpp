#include <bits/stdc++.h>
using namespace std;
vector<int> NGE(vector<int>v){
    vector<int>indA(v.size());
    stack<int>st;
    for(int i=0;i<v.size();++i){
        while(!st.empty()&&v[i]>v[st.top()]){
            indA[st.top()]=i;
            st.pop();
        }
        st.push(i);
    }
    while(!st.empty()){
        indA[st.top()]=-1;
        st.pop();
    }
    return indA;
}
int main (){
    vector<int>v;
    int n;
    cin>>n;
    for(int i=0;i<n;++i){
        int ele;
        cin>>ele;
        v.push_back(ele);
    }

    auto index=NGE(v);
    for(int i=0;i<n;++i){
        if(index[i]<0) cout<<v[i]<<" "<<-1<<endl;
        else cout<<v[i]<<" "<<v[index[i]]<<endl;
    }


}