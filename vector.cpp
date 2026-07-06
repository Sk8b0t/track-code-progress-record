#include <bits/stdc++.h>
using namespace std;
void printVec(vector<int> &v){
    cout<<"Size:"<<v.size()<<endl;
    for(int i=0;i<v.size();++i){
        cout<<v[i]<<" ";
    }
    cout<<endl;
}
int main(){
    vector<int> v(5,10);
    printVec(v);
    v.push_back(12);
    printVec(v);
    v.pop_back();
    printVec(v);
}