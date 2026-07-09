#include<bits/stdc++.h>
using namespace std;
int main(){
    int N;
    cin>>N;
    map<int,multiset<string>>m;
    for(int i=0;i<N;++i){
        int n;
        string s;
        cin>>s>>n;
        m[n].insert(s);
    }
    auto item=--m.end();
    while(true){
        for(auto &wtf: (*item).second) cout<<wtf<<" "<<(*item).first<<endl;
        if(item==m.begin()) break;
        --item;
    }
}

