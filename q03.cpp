#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    map<int,multiset<string>>m;
    for(int i=0;i<n;++i){
        int x;
        string s;
        cin>>s>>x;
        m[-1*x].insert(s);
    }
    for(auto &a:m){
        for(auto &b: a.second) cout<<b<<" "<<a.first*-1<<endl;
    }
}