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
            long long x;
            cin>>x;
            bag.insert(x);
        }
        long long cnt=0;
        for(int i=0;i<k;++i){
        auto m=--bag.end();
        cnt+=*m;
        bag.erase(m);
        bag.insert(*m/2);
        }
        cout<<cnt<<endl;
    }
}