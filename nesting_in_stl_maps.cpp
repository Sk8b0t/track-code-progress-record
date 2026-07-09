#include <bits/stdc++.h>
using namespace std;
int main(){
    map<pair<string,string>,vector<int>> m;
    int n;
    cin>>n;
    for(int i=0;i<n;++i){
        string s,l;
        int n1;
        cin>>s>>l>>n1;
        for(int j=0;j<n1;++j){
            int x;
            cin>>x;
            m[{s,l}].push_back(x);
        }
            
        for(auto &pr: m){
            cout<<pr.first.first<<" "<<pr.first.second<<endl;
            for(auto &lst:pr.second) cout<<lst;
            cout<<"endl";
        }
    }
}