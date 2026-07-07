#include <bits/stdc++.h>
using namespace std;
void printVec(vector<int> v){
    for(int i=0;i<v.size();++i){
        cout<<v[i]<<" ";
    }
    cout<<endl;
}
int main(){
    vector<vector<int>> v;
    int n;
    cin>>n;
    for(int i=0;i<n;++i){
        v.push_back(vector<int>());
        int n1;
        cin>>n1;
        for(int j=0;j<n1;++j){
            int x;
            cin>>x;
            v[i].push_back(x);
        }

    }
    for(int i=0;i<v.size();++i){
        printVec(v[i]);
    }
    
}