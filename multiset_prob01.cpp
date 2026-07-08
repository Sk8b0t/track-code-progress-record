#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
    int n,k;
    cin>>n>>k;
    multiset<long long> bag;
    for(int i=0;i<n;++i){
        long long c;
        cin>>c;
        bag.insert(c);
    }
    long long cnt=0; 
    for(int i=0;i<k;++i){
        auto cnd=--bag.end();
        cnt+=*cnd;
        bag.erase(cnd);
        bag.insert(*cnd/2);
    }
    cout<<cnt<<endl;
}
}